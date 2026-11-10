"""Run headless agent sessions of last-look on fixture projects and save the reports for score.py.

Stdlib only. Maintainer tooling: users of the skill never run this.
Usage: python3 tests/tools/run_evals.py --fixtures web-bad[,android-bad] --mode skill --runs 3
           [--results tests/results] [--projects tests/projects]
Modes: skill (skill installed, no web), baseline (no skill, no web), web (skill installed, web allowed).
Each run happens in a throwaway temp dir, never in this repo, and lands in
<results>/<fixtures joined by +>/<mode>/run-<n>/ as last-look-report.md (if written) and agent.log.
The agent command is env LAST_LOOK_AGENT_CMD (default: DEFAULT_CMD, claude -p with project-only
settings and no user MCP servers); the prompt goes to its stdin. Browser-mode runs are done by hand.
"""
import argparse
import os
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODES = ("skill", "baseline", "web")
REPORT = "last-look-report.md"
SKILL_PARTS = ("SKILL.md", "checks", "rules", "references")
# The answer key, and a fixture's served `site/` folder (the agent gets only its URL), never reach the agent.
NOT_FOR_AGENT = ("expected.json", "answers.md", "site")
# Project settings only, no user MCP servers, nothing persisted. Not --bare: it needs an API key, not OAuth.
DEFAULT_CMD = ("claude -p --permission-mode acceptEdits --setting-sources project"
               " --strict-mcp-config --no-session-persistence")
TOOLS = "Skill,Read,Grep,Glob,Write"
TIMEOUT = 1200

PROMPTS = {
    "skill": "Use the last-look skill on this project. Answers to its questions: {}. Write the report and stop.",
    "baseline": "Check this project for legal, app store and good-practice mistakes. Answers: {}. "
                "Write the findings to last-look-report.md and stop.",
}
PROMPTS["web"] = PROMPTS["skill"]


def build_command(mode: str) -> list[str]:
    if mode not in MODES:
        raise ValueError(f"mode must be one of {MODES}, got {mode!r}")
    cmd = shlex.split(os.environ.get("LAST_LOOK_AGENT_CMD") or DEFAULT_CMD)
    # --allowedTools only pre-approves; --tools removes every other built-in (Bash, Task, Edit...). Kept last: it is variadic.
    if mode == "web":
        tools = TOOLS + ",WebSearch,WebFetch"
        return cmd + ["--allowedTools", tools, "--tools", tools]
    return cmd + ["--allowedTools", TOOLS, "--disallowedTools", "WebSearch,WebFetch", "--tools", TOOLS]


def build_prompt(answers: str, mode: str) -> str:
    return PROMPTS[mode].format(answers)


def _require_skill(skill: Path, mode: str) -> None:
    """A skill or web run without SKILL.md would silently be a baseline run."""
    if mode != "baseline" and not (skill / "SKILL.md").is_file():
        raise FileNotFoundError(f"{skill / 'SKILL.md'} not found: {mode} mode needs the skill")


def prepare_workdir(fixtures: Path, names: list[str], mode: str, skill: Path, tmp: Path) -> Path:
    """Fill the empty dir `tmp` with the fixture(s) and, unless baseline, the skill; returns `tmp`."""
    _require_skill(skill, mode)
    for name in names:
        src = fixtures / name
        shutil.copytree(src, tmp / name if len(names) > 1 else tmp, dirs_exist_ok=True,
                        ignore=lambda d, _: NOT_FOR_AGENT if Path(d) == src else ())  # top level only
    if mode != "baseline":
        dest = tmp / ".claude" / "skills" / "last-look"
        dest.mkdir(parents=True, exist_ok=True)
        for part in SKILL_PARTS:
            src = skill / part
            if src.is_dir():
                shutil.copytree(src, dest / part)
            elif src.is_file():
                shutil.copy2(src, dest / part)
    return tmp


def _text(value) -> str:
    return value.decode(errors="replace") if isinstance(value, bytes) else value or ""


def _log(status: str, stdout, stderr) -> str:
    return f"returncode: {status}\n--- stdout ---\n{_text(stdout)}\n--- stderr ---\n{_text(stderr)}\n"


def main(argv=None, run=subprocess.run, skill: Path = ROOT) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fixtures", required=True, help="fixture name, or a,b to run several in one project")
    ap.add_argument("--mode", choices=MODES, required=True)
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--results", type=Path, default=ROOT / "tests" / "results")
    ap.add_argument("--projects", type=Path, default=ROOT / "tests" / "projects")
    a = ap.parse_args(argv)
    if a.runs < 1:
        ap.error("--runs must be at least 1")
    names = a.fixtures.split(",")
    if bad := [n for n in names if n in ("", ".") or ".." in n or "/" in n or "\\" in n]:
        ap.error(f"fixture names must be bare folder names, got {bad[0]!r}")
    try:
        _require_skill(skill, a.mode)
    except FileNotFoundError as e:
        ap.error(str(e))
    if missing := [n for n in names if not (a.projects / n / "answers.md").is_file()]:
        ap.error(f"no answers.md in fixture(s): {', '.join(missing)}")
    texts = [(a.projects / n / "answers.md").read_text(encoding="utf-8") for n in names]
    answers = texts[0] if len(names) == 1 else "\n\n".join(f"## {n}\n{t}" for n, t in zip(names, texts))
    prompt, cmd = build_prompt(answers, a.mode), build_command(a.mode)
    out = a.results / "+".join(names) / a.mode
    for old in out.glob("run-*"):
        if old.is_dir():
            shutil.rmtree(old)
    for n in range(1, a.runs + 1):
        work = Path(tempfile.mkdtemp(prefix="last-look-eval-"))
        try:
            prepare_workdir(a.projects, names, a.mode, skill, work)
            # A single fixture may ship an old report; a combined work dir has no root report.
            stale = (work / REPORT).read_bytes() if (work / REPORT).is_file() else None
            try:
                p = run(cmd, input=prompt, cwd=work, capture_output=True, encoding="utf-8", errors="replace",
                        timeout=TIMEOUT)
                log = _log(str(p.returncode), p.stdout, p.stderr)
            except subprocess.TimeoutExpired as e:
                log = _log(f"timeout after {TIMEOUT}s", e.stdout, e.stderr)
            except OSError as e:  # e.g. agent binary missing: log it, try the next run
                log = _log(f"not started: {e}", "", "")
            report = work / REPORT
            saved = report.is_file() and report.read_bytes() != stale
            if report.is_file() and not saved:
                log += "report unchanged from fixture\n"  # the agent wrote nothing: do not score the old report
            dest = out / f"run-{n}"
            dest.mkdir(parents=True)
            (dest / "agent.log").write_text(log, encoding="utf-8")
            if saved:
                shutil.copy2(report, dest / REPORT)
            print(f"{dest}: {log.splitlines()[0]}; report {'saved' if (dest / REPORT).exists() else 'MISSING'}")
        finally:
            shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
