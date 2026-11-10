# Tests

Maintainer tooling only. Users of the skill never run anything here. Everything is Python 3.10+ standard library.

## Unit tests and content lint

    python3 -m unittest discover -s tests/tools
    python3 tests/tools/lint_content.py
    python3 tests/tools/lint_content.py --release

All three must pass (exit 0) before a release. The first two must pass before every commit. `--release` adds the release rules: complete full walks, no stale dates, a verified check in every area.

## Running evals

`tests/tools/run_evals.py` copies a fixture from `tests/projects/` and the skill into a throwaway temp dir, runs a headless agent there with the prompt on stdin, and saves `tests/results/<fixture>/<mode>/run-<n>/last-look-report.md` and `agent.log`. A new call for the same fixture and mode replaces its earlier runs. `tests/results/` is gitignored.

Run evals on Sonnet. Set the agent command for every run:

    export LAST_LOOK_AGENT_CMD='claude -p --permission-mode acceptEdits --setting-sources project --strict-mcp-config --no-session-persistence --model sonnet'
    python3 tests/tools/run_evals.py --fixtures web-bad --mode skill --runs 1

- Modes: `skill` (skill installed, no web), `baseline` (no skill, no web), `web` (skill installed, web allowed). `--fixtures a,b` runs several fixtures as one project.
- `--setting-sources project --strict-mcp-config` keeps personal settings, skills, hooks and MCP servers out of the run.
- To keep the full transcript in `agent.log` (tool calls, the skills list, cost and duration), append `--output-format stream-json --verbose` to the command. Without it, `agent.log` holds only the agent's last message.
- The runner adds the tool flags itself. `--tools` sets the only tools the agent has: `Skill,Read,Grep,Glob,Write` in `skill` and `baseline` modes, plus `WebSearch,WebFetch` in `web` mode. So the agent has no shell, subagents or Edit. `--allowedTools` pre-approves the same list, and `--disallowedTools WebSearch,WebFetch` keeps the web tools out of the no-web modes.
- One run at a time. The runner's per-run timeout is 20 minutes.
- For the time and cost of the scored runs, see the Test results section of the root README.

## Checking and scoring

Check one report for format, banned wording, invented locations, unknown sources and echoed secrets (the fake secrets are in each fixture's `expected.json`):

    python3 tests/tools/check_report.py tests/results/web-bad/skill/run-1/last-look-report.md \
        --project tests/projects/web-bad --skill . --secret sk_test_FAKE0000000000000000

Score every saved run against the fixtures' `expected.json`:

    python3 tests/tools/score.py --markdown

Overall `pass` needs runs for every fixture, so it stays false until all have `skill` runs. Read the per-fixture rows: found/planted, false `Confirmed` (Critical or High / other), must-not-confirm hits, most Maybe items and checker errors.

## Browser run

The `site-js-only` fixture is served from its `site/` folder, which the runner never copies into the agent's work dir. Start the server from the repo root, then give the agent a browser and the URL `http://localhost:8765/`:

    python3 -m http.server 8765 --directory tests/projects/site-js-only/site
