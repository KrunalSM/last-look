"""Score AI-agent runs of last-look against fixture projects with planted mistakes.

Stdlib only. Maintainer tooling: users of the skill never run this.
Usage: python3 tests/tools/score.py [--results tests/results] [--fixtures tests/projects] [--markdown]
Results: <results>/<fixture>/<mode>/run-<n>/last-look-report.md; expectations: <fixtures>/<fixture>/expected.json.
A planted item may set "evidence": "maybe" (default "confirm") when it can only be expected as a Maybe item.
In a needs_browser fixture a planted item is found only by a finding with Evidence "Confirmed on live site".
A results folder named `a+b` is a combined run of fixtures a and b. Prints JSON (or Markdown); always exits 0.
"""
import argparse
import json
import posixpath
import shutil
import tempfile
from collections import Counter
from pathlib import Path

from check_report import MAYBE, MAYBE_LIMIT, check_report, parse_location, parse_report

ROOT = Path(__file__).resolve().parents[2]
MODES = ("skill", "baseline", "web", "browser")  # only skill (and browser for needs_browser fixtures) decide `pass`
REPORT = "last-look-report.md"
LINE_SLACK, FOUND_RATE_MIN, CLEAN_OTHER_MAX = 3, 0.9, 2
CRITICAL_HIGH = ("Critical", "High")
LIVE_SITE = "Confirmed on live site"


def _matches(item: dict, check: str, location: str) -> bool:
    if item["check"] != check:
        return False
    if item["file"] is None:
        return True
    parsed = parse_location(location)
    if parsed is None or posixpath.normpath(parsed[0]) != posixpath.normpath(item["file"]):
        return False
    _, first, last = parsed
    return item["line"] is None or (first is not None and first - LINE_SLACK <= item["line"] <= last + LINE_SLACK)


def _expected(fixtures: Path, name: str) -> dict:
    """Expectations for a fixture; `a+b` is the union of a and b with planted files prefixed `a/`, `b/`."""
    parts = name.split("+")
    out = {"planted": [], "must_not_confirm": [], "clean": False, "secrets": [], "needs_browser": False}
    for part in parts:
        e = json.loads((fixtures / part / "expected.json").read_text(encoding="utf-8"))
        prefix = f"{part}/" if len(parts) > 1 else ""
        out["planted"] += [{"check": p["check"], "file": prefix + p["file"] if p["file"] else None, "line": p["line"],
                            "evidence": p.get("evidence", "confirm")} for p in e["planted"]]
        if bad := [p["evidence"] for p in out["planted"] if p["evidence"] not in ("confirm", "maybe")]:
            raise ValueError(f"{part}/expected.json: planted evidence must be 'confirm' or 'maybe', got {bad[0]!r}")
        out["must_not_confirm"] += e["must_not_confirm"]
        out["secrets"] += e["secrets"]
        if len(parts) == 1:
            out["clean"], out["needs_browser"] = e["clean"], e["needs_browser"]
    return out


def _worst_run(items: list[dict]) -> int:
    return max(Counter(i["run"] for i in items).values(), default=0)


def _score_mode(run_dirs: list[Path], exp: dict, project: Path, skill: Path, scored: bool) -> dict:
    planted, secrets = exp["planted"], exp["secrets"]
    hits, false, forbidden, errors, maybe_max = [0] * len(planted), [], [], [], 0

    def scrub(s: str) -> str:
        for secret in filter(None, secrets):
            s = s.replace(secret, "[secret]")
        return s

    for run in run_dirs:
        report = run / REPORT
        if not report.is_file():
            errors.append(f"{run.name}: no {REPORT}")
            continue
        errors += [f"{run.name}: {e}" for e in check_report(report, project, skill, secrets)]
        parsed = parse_report(report.read_text(encoding="utf-8"))
        maybe_max = max(maybe_max, parsed["maybe_count"])
        def blocks(keep) -> list[dict]:
            return [{"run": run.name, "check": f.get("Check", "").replace("`", "").strip(),
                     "location": scrub(f.get("Location", "")), "severity": f.get("Severity", ""),
                     "evidence": f.get("Evidence", "")}
                    for f in parsed["findings"] if keep(f.get("Evidence", ""))]

        # Confirmed blocks and Later bullets find any planted item; Maybe blocks find only items planted as "maybe".
        # Not tested, Skipped and Nothing found never find anything. In a needs_browser fixture only
        # "Confirmed on live site" blocks find a planted item (not code evidence, Later bullets or Maybe).
        confirmed, maybes = blocks(lambda e: e.startswith("Confirmed")), blocks(lambda e: e == MAYBE)
        # A needs_browser fixture's tracker is invisible in code: only live-site evidence finds it (bullets carry none).
        live_only = exp["needs_browser"]
        seen = [(c["check"], c["location"]) for c in confirmed if not live_only or c["evidence"] == LIVE_SITE]
        seen += [] if live_only else [(b["check"], b["location"]) for b in parsed["later_bullets"]]
        seen_maybe = [(c["check"], c["location"]) for c in maybes]
        for i, p in enumerate(planted):
            hits[i] += any(_matches(p, c, loc) for c, loc in seen + (seen_maybe if p["evidence"] == "maybe" and not live_only else []))
        false += [c for c in confirmed if not any(_matches(p, c["check"], c["location"]) for p in planted)]
        forbidden += [c for c in confirmed if c["check"] in exp["must_not_confirm"]]

    need = max(1, -(-2 * len(run_dirs) // 3))  # ceil(2/3 of runs), at least one run
    found = [p for p, h in zip(planted, hits) if h >= need] if scored else []
    return {
        "runs": len(run_dirs), "planted": len(planted) if scored else 0,
        "found": found, "missed": [p for p in planted if p not in found] if scored else [],
        # Counts are the worst single run: the bar is per report. `items` lists every one.
        "false_confirmed": {
            "critical_high": _worst_run([i for i in false if i["severity"] in CRITICAL_HIGH]),
            "other": _worst_run([i for i in false if i["severity"] not in CRITICAL_HIGH]), "items": false},
        "must_not_confirm_hits": forbidden, "maybe_max": maybe_max, "checker_errors": errors,
    }


def _run_dirs(results: Path, name: str, mode: str) -> list[Path]:
    return sorted(d for d in (results / name / mode).glob("run-*") if d.is_dir())


def score(results, fixtures, skill=None) -> dict:
    results, fixtures, skill = Path(results), Path(fixtures), Path(skill) if skill else ROOT
    ran = {d.name for d in results.iterdir() if d.is_dir()} if results.is_dir() else set()
    names = sorted(ran | {p.parent.name for p in fixtures.glob("*/expected.json")})  # an unrun fixture must fail the gate
    summary: dict = {"fixtures": {}}
    reasons: list[str] = []
    found_n = planted_n = maybe_max = single_found = single_planted = 0
    for name in names:
        exp = _expected(fixtures, name)
        deciding = ("skill", "browser") if exp["needs_browser"] else ("skill",)
        scored_mode = deciding[-1]  # the mode whose planted items decide `pass`
        with tempfile.TemporaryDirectory() as tmp:
            project = fixtures / name
            if "+" in name:  # copies, not symlinks: check_report rejects paths that resolve outside the project
                project = Path(tmp) / name
                for part in name.split("+"):
                    shutil.copytree(fixtures / part, project / part)
            modes = {m: _score_mode(_run_dirs(results, name, m), exp, project, skill, m == "browser" or not exp["needs_browser"])
                     for m in MODES if m in deciding or _run_dirs(results, name, m)}
        summary["fixtures"][name] = modes
        for mode in deciding:
            m, who = modes[mode], f"{name}/{mode}"
            maybe_max = max(maybe_max, m["maybe_max"])
            if not m["runs"]:
                reasons.append(f"{who}: no runs")
            if m["checker_errors"]:
                reasons.append(f"{who}: {len(m['checker_errors'])} checker error(s)")
            if m["must_not_confirm_hits"]:
                reasons.append(f"{who}: must-not-confirm hit ({', '.join(sorted({h['check'] for h in m['must_not_confirm_hits']}))})")
            fc = m["false_confirmed"]
            if exp["clean"] and fc["critical_high"]:
                reasons.append(f"{who}: false Confirmed at Critical/High on a clean fixture")
            if exp["clean"] and fc["other"] > CLEAN_OTHER_MAX:
                reasons.append(f"{who}: {fc['other']} false Confirmed on a clean fixture (limit {CLEAN_OTHER_MAX})")
        planted_n += modes[scored_mode]["planted"]
        found_n += len(modes[scored_mode]["found"])
        if "+" not in name:  # a combined folder re-plants its parts' mistakes
            single_planted += modes[scored_mode]["planted"]
            single_found += len(modes[scored_mode]["found"])
    if not names:
        reasons.append("no fixtures scored")
    if found_n < FOUND_RATE_MIN * planted_n:
        reasons.append(f"found {found_n} of {planted_n} planted mistakes (need {FOUND_RATE_MIN:.0%})")
    if maybe_max > MAYBE_LIMIT:
        reasons.append(f"a report has {maybe_max} Maybe items (limit {MAYBE_LIMIT})")
    summary["overall"] = {"found": found_n, "planted": planted_n, "found_rate": found_n / planted_n if planted_n else 1.0,
                          "maybe_max": maybe_max, "single_found": single_found, "single_planted": single_planted,
                          "pass": not reasons, "reasons": reasons}
    return summary


def _where(p: dict) -> str:
    if p["file"] is None:
        return f"`{p['check']}`"
    return f"`{p['check']}` at `{p['file']}{'' if p['line'] is None else ':' + str(p['line'])}`"


def _found(m: dict | None) -> str:
    return f"{len(m['found'])}/{m['planted']}" if m and m["planted"] else "n/a"


def _false(m: dict | None) -> str:
    return f"{m['false_confirmed']['critical_high']}/{m['false_confirmed']['other']}" if m and m["runs"] else "n/a"


def render_markdown(summary: dict) -> str:
    o = summary["overall"]
    out = ["# last-look eval results", "",
           f"Pass: **{'yes' if o['pass'] else 'no'}**. Planted mistakes found: {o['found']}/{o['planted']} "
           f"({o['found_rate']:.0%})"
           + (f", which counts combined folders again; {o['single_found']}/{o['single_planted']} in single-project folders"
              if o["single_planted"] != o["planted"] else "")
           + f". Most Maybe items in one report: {o['maybe_max']}."]
    out += ["", *[f"- {r}" for r in o["reasons"]]] if o["reasons"] else []
    for name, modes in summary["fixtures"].items():
        out += ["", f"## {name}", "",
                "| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |",
                "|---|---|---|---|---|---|---|"]
        out += [f"| {mode} | {m['runs']} | {_found(m)} | {_false(m)} | {len(m['must_not_confirm_hits'])} "
                f"| {m['maybe_max']} | {len(m['checker_errors'])} |" for mode, m in modes.items()]
        for title, lines in (
            ("Misses", [f"- {mode}: {_where(p)}" for mode, m in modes.items() for p in m["missed"]]),
            ("False alarms", [f"- {mode} {i['run']}: `{i['check']}` at `{i['location']}` ({i['severity']})"
                              for mode, m in modes.items() for i in m["false_confirmed"]["items"]]),
            ("Must-not-confirm hits", [f"- {mode} {i['run']}: `{i['check']}` at `{i['location']}`"
                                       for mode, m in modes.items() for i in m["must_not_confirm_hits"]]),
            ("Checker errors", [f"- {mode} {e}" for mode, m in modes.items() for e in m["checker_errors"]]),
        ):
            if lines:
                out += ["", f"{title}:", *lines]
    out += ["", "## Skill versus baseline", "",
            "| Fixture | Skill found | Baseline found | Skill false Confirmed | Baseline false Confirmed |", "|---|---|---|---|---|"]
    for name, modes in summary["fixtures"].items():
        s, b = modes.get("skill"), modes.get("baseline")
        sf = _found(modes.get("browser")) if s and not s["planted"] else _found(s)
        out.append(f"| {name} | {sf} | {_found(b)} | {_false(s)} | {_false(b)} |")
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--results", type=Path, default=ROOT / "tests" / "results")
    ap.add_argument("--fixtures", type=Path, default=ROOT / "tests" / "projects")
    ap.add_argument("--markdown", action="store_true", help="print a README-ready table instead of JSON")
    a = ap.parse_args(argv)
    summary = score(a.results, a.fixtures)
    print(render_markdown(summary) if a.markdown else json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
