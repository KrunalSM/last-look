"""Lint a last-look skill tree: checks/<area>.md, rules/*.md, coverage/*.md.

Stdlib only. Maintainer tooling: users of the skill never run this.
Usage: python3 tests/tools/lint_content.py [--release]
"""
import argparse
import json
import re
from datetime import date
from pathlib import Path

from content import (
    AREAS, FULL_WALK_SOURCES, SEVERITIES, STATUSES, STRENGTHS,
    parse_checks, parse_coverage, parse_rules, parse_rules_summary,
)

# Pinned test-case check ids (fixtures depend on them) and their areas.
TEST_CASE_IDS = {
    "terms-acceptance-record": "consent-records", "terms-change-notice": "consent-records",
    "prechecked-consent": "consent-records", "privacy-policy-missing": "privacy-notices",
    "account-deletion-missing": "user-rights", "google-fonts-remote": "third-party-data",
    "trackers-before-consent": "tracking-ads", "session-replay-consent": "tracking-ads",
    "secrets-in-client": "exposure", "open-database-rules": "exposure",
    "prod-logging-personal-data": "exposure", "age-handling": "children",
    "dark-pattern-urgency": "dark-patterns", "renewal-terms-checkout": "money",
    "marketing-email-footer": "communication", "uploads-takedown-process": "user-content",
    "grievance-officer-missing": "business-details", "permission-at-launch": "platforms",
    "permission-purpose-strings": "platforms", "ai-data-disclosure": "ai",
    "store-data-disclosure": "platforms",
}

CHECK_FIELDS = ("title", "area", "needs", "severity", "evidence-default", "look-for",
                "why", "fix", "exceptions", "elsewhere")
RULE_FIELDS = ("check", "source-id", "applies-to", "strength", "reference", "rule-started",
               "status", "verified-on", "source", "secondary")
COVERAGE_FIELDS = ("source-id", "walk", "url", "read-on")

STORE_SOURCES = ("apple-review-guidelines", "google-play-policy")
INDIA_SOURCES = tuple(s for s in FULL_WALK_SOURCES if s not in STORE_SOURCES)
STALE_DAYS_STORE, STALE_DAYS_LAW = 92, 183

_URL = re.compile(r"https?://\S+")
# Every run loads whole check and rule files, so long fields cost every user; caps keep them short.
CHECK_CAPS = {"why": 250, "fix": 400, "exceptions": 600}
LOOK_FOR_CAP, REFERENCE_CAP = 300, 400
_SENTENCE_BREAK = re.compile(r"[.!?]\s+[A-Z]")
_RULE_STATUS = re.compile(r"In force|Coming (\d{4}-\d{2}-\d{2})")


def _date(s: str) -> date | None:
    try:
        return date.fromisoformat(s) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s) else None
    except ValueError:
        return None


_EXPECTED_KEYS = {"planted", "must_not_confirm", "clean", "secrets", "needs_browser"}


def _expected_problem(e) -> str | None:
    """Why `e` is not a valid fixture expected.json (the shape score.py reads), or None."""
    if not isinstance(e, dict) or e.keys() != _EXPECTED_KEYS:
        return f"must be an object with exactly these keys: {sorted(_EXPECTED_KEYS)}"
    if not all(isinstance(e[k], list) and all(isinstance(x, str) for x in e[k]) for k in ("must_not_confirm", "secrets")):
        return "must_not_confirm and secrets must be lists of strings"
    if not all(isinstance(e[k], bool) for k in ("clean", "needs_browser")):
        return "clean and needs_browser must be true or false"
    if not isinstance(e["planted"], list):
        return "planted must be a list"
    for p in e["planted"]:
        ok = (isinstance(p, dict) and {"check", "file", "line"} <= p.keys() <= {"check", "file", "line", "evidence"}
              and isinstance(p["check"], str) and isinstance(p["file"], (str, type(None)))
              and (p["line"] is None or (isinstance(p["line"], int) and not isinstance(p["line"], bool)))
              and p.get("evidence", "confirm") in ("confirm", "maybe"))
        if not ok:
            return f"bad planted item {p!r}"
    return None


def lint(root: Path, release: bool = False, today: date | None = None) -> list[str]:
    """Return one error string per problem; an empty list means clean."""
    root, today = Path(root), today or date.today()
    errors: list[str] = []

    def err(path: Path, who: str, msg: str) -> None:
        errors.append(f"{path.relative_to(root).as_posix()}: {who + ': ' if who else ''}{msg}")

    def load(parse, path: Path):
        try:
            return parse(path)
        except UnicodeDecodeError as e:
            err(path, "", f"not valid UTF-8 (byte {e.start})")
        except ValueError as e:
            errors.append(str(e))

    def fields(path, who, block, names):
        for k in names:
            if block.get(k) in (None, "", []):
                err(path, who, f"missing field: {k}")
            elif isinstance(block[k], list) and k != "look-for":
                err(path, who, f"{k} must be a single value, not a list")
                block[k] = ""  # keeps later checks from crashing on a list
        for k in sorted(block.keys() - set(names) - {"id"}):
            err(path, who, f"unknown field: {k}")

    def enum(path, who, block, key, allowed, label=None):
        if block.get(key) not in allowed:
            err(path, who, f"invalid {label or key} {block.get(key)!r}")

    def date_field(path, who, name, value, past=True):
        d = _date(value)
        if d is None:
            err(path, who, f"invalid {name} date {value!r}")
        elif past and d > today:
            err(path, who, f"{name} in the future: {value}")
        return d

    checks: dict[str, dict] = {}
    ids_in_area: dict[str, set] = {}
    for path in sorted((root / "checks").glob("*.md")):
        for cid, c in (load(parse_checks, path) or {}).items():
            if cid in checks:
                err(path, cid, "duplicate check id")
            checks.setdefault(cid, c)
            ids_in_area.setdefault(path.stem, set()).add(cid)
            fields(path, cid, c, CHECK_FIELDS)
            if c.get("area") not in AREAS:
                err(path, cid, f"unknown area {c.get('area')!r}")
            elif c["area"] != path.stem:
                err(path, cid, f"area does not match file: {c['area']!r}")
            enum(path, cid, c, "severity", SEVERITIES)
            enum(path, cid, c, "evidence-default", ("confirm", "maybe"))
            if c.get("look-for") and not isinstance(c["look-for"], list):
                err(path, cid, "look-for must be a list of items")
            for key, cap in CHECK_CAPS.items():
                if isinstance(c.get(key), str) and len(c[key]) > cap:
                    err(path, cid, f"{key} too long: {len(c[key])} characters (max {cap})")
            if isinstance(c.get("why"), str) and _SENTENCE_BREAK.search(c["why"]):
                err(path, cid, "why must be one sentence")
            for n, item in enumerate(c["look-for"] if isinstance(c.get("look-for"), list) else [], 1):
                if len(item) > LOOK_FOR_CAP:
                    err(path, cid, f"look-for item {n} too long: {len(item)} characters (max {LOOK_FOR_CAP})")
            parts = c.get("elsewhere", "").split(" | ")
            if c.get("elsewhere") != "none" and not (len(parts) == 3 and _URL.fullmatch(parts[2])):
                err(path, cid, "invalid elsewhere (use none or '<region> | <one line> | <url>')")
    for cid, area in TEST_CASE_IDS.items():
        if cid not in checks:
            errors.append(f"missing test-case check: {cid}")
        elif checks[cid].get("area") != area:
            errors.append(f"test-case check in wrong area: {cid} should be in {area}")

    for path in sorted((root / "tests" / "projects").glob("*/expected.json")):
        name = path.parent.name
        try:
            exp = json.loads(path.read_text(encoding="utf-8"))
            problem = _expected_problem(exp)
        except (ValueError, OSError) as e:  # bad JSON, bad UTF-8 (both ValueError), unreadable file
            exp, problem = None, str(e)
        if problem:
            errors.append(f"bad expected.json in fixture {name}: {problem}")
            continue
        used = [p["check"] for p in exp["planted"]] + exp["must_not_confirm"]
        errors += [f"unknown check id in fixture {name}: {cid}" for cid in used if cid not in checks]
        folder = path.parent.resolve()
        for p in exp["planted"]:
            if p["file"] is None:
                continue
            target = (folder / p["file"]).resolve()
            if not target.is_relative_to(folder) or not target.is_file():
                errors.append(f"planted file missing in fixture {name}: {p['file']}")
            elif p["line"] is not None and not 1 <= p["line"] <= len(target.read_bytes().splitlines()):
                errors.append(f"planted line out of range in fixture {name}: {p['file']}:{p['line']}")

    rules: list[dict] = []
    for path in sorted((root / "rules").glob("*.md")):
        parsed = load(parse_rules, path)
        if parsed is None:
            continue
        if not parse_rules_summary(path):
            err(path, "", "missing coverage summary")
        for r in parsed:
            rules.append(r)
            who, strength = r["id"], r.get("strength")
            fields(path, who, r, RULE_FIELDS)
            if r.get("check") not in checks:
                err(path, who, f"unknown check {r.get('check')!r}")
            enum(path, who, r, "strength", STRENGTHS)
            enum(path, who, r, "secondary", ("yes", "no"))
            if isinstance(r.get("reference"), str) and len(r["reference"]) > REFERENCE_CAP:
                err(path, who, f"reference too long: {len(r['reference'])} characters (max {REFERENCE_CAP})")
            m = _RULE_STATUS.fullmatch(r.get("status", ""))
            if not m or (m[1] and not _date(m[1])):
                err(path, who, f"invalid status {r.get('status')!r}")
            elif m[1] and _date(m[1]) <= today:
                err(path, who, f"status Coming {m[1]} has passed: change it to In force")
            started = r.get("rule-started", "")
            if strength == "Good practice":
                if started != "n/a":
                    err(path, who, "rule-started must be n/a for Good practice")
            elif started == "n/a":
                err(path, who, "rule-started must be a date, n/a is only for Good practice")
            else:
                # "before DATE": in force no later than DATE, when the start day is unconfirmed.
                date_field(path, who, "rule-started", started.removeprefix("before "), past=False)
            verified = date_field(path, who, "verified-on", r.get("verified-on", ""))
            if not _URL.fullmatch(r.get("source", "")):
                err(path, who, "source is not a URL")
            limit = STALE_DAYS_STORE if r.get("source-id") in STORE_SOURCES or strength == "Store rule" else (
                STALE_DAYS_LAW if strength in ("Law", "Court or regulator") else None)
            if release and verified and limit and (today - verified).days > limit:
                err(path, who, f"stale: verified-on {verified} is over {limit} days old")

    sources_with_coverage: set[str] = set()
    for path in sorted((root / "coverage").glob("*.md")):
        cov = load(parse_coverage, path)
        if not cov:
            continue
        meta = cov["meta"]
        sources_with_coverage.add(meta.get("source-id"))
        fields(path, "", meta, COVERAGE_FIELDS)
        if meta.get("source-id") != path.stem:
            err(path, "", "source-id does not match file name")
        enum(path, "", meta, "walk", ("full", "targeted"))
        if not _URL.fullmatch(meta.get("url", "")):
            err(path, "", "url is not a URL")
        date_field(path, "", "read-on", meta.get("read-on", ""))
        if release and meta.get("source-id") in FULL_WALK_SOURCES and not cov["rows"]:
            errors.append(f"no coverage rows: {meta['source-id']}")
        for row in cov["rows"]:
            who = f"row {row['section']}"
            enum(path, who, row, "status", STATUSES, "coverage status")
            for cid in row["checks"]:
                if not cid:
                    err(path, who, "empty checks cell (use - for none)")
                elif cid not in checks:
                    err(path, who, f"unknown check {cid!r}")
            if row["verified_on"] or row["status"] != "Not done yet":
                date_field(path, who, "verified-on", row["verified_on"])
            if release and row["status"] == "Not done yet" and meta.get("source-id") in FULL_WALK_SOURCES:
                err(path, who, "coverage not complete: Not done yet")

    if release:
        for source in FULL_WALK_SOURCES:
            if source not in sources_with_coverage:
                errors.append(f"missing coverage file: {source}")
        verified_checks = {r.get("check") for r in rules if r.get("verified-on")}
        verified_sources = {r.get("source-id") for r in rules if r.get("verified-on")}
        for area in AREAS:
            if not ids_in_area.get(area, set()) & verified_checks:
                errors.append(f"no verified check in area: {area}")
        for source in INDIA_SOURCES:
            if source not in verified_sources:
                errors.append(f"no verified check for source: {source}")
    return errors


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--release", action="store_true", help="also enforce release rules")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    a = ap.parse_args(argv)
    errors = lint(a.root, a.release)
    for e in errors:
        print(e)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
