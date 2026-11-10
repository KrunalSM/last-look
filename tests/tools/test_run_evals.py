import contextlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from run_evals import build_command, build_prompt, main, prepare_workdir

FAKE_AGENT = """import os, sys
if os.environ.get("FAKE_BAD"):
    sys.stdout.buffer.write(b"bad \\xff\\xfe bytes\\n")
    sys.stdout.flush()
if not os.environ.get("FAKE_NOWRITE"):
    open("last-look-report.md", "w").write(f"cwd={os.getcwd()}\\nargv={' '.join(sys.argv[1:])}\\nstdin={sys.stdin.read()}")
print("fake stdout")
sys.exit(int(os.environ.get("FAKE_RC", "0")))
"""


def flag(cmd, name):
    return cmd[cmd.index(name) + 1]


class CommandTests(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ)
        patcher.start()
        self.addCleanup(patcher.stop)
        os.environ.pop("LAST_LOOK_AGENT_CMD", None)

    def test_skill_mode_disallows_web_tools(self):
        cmd = build_command("skill")
        self.assertEqual(flag(cmd, "--allowedTools"), "Skill,Read,Grep,Glob,Write")
        self.assertEqual(flag(cmd, "--disallowedTools"), "WebSearch,WebFetch")
        self.assertEqual(cmd[:4], ["claude", "-p", "--permission-mode", "acceptEdits"])

    def test_tools_flag_limits_available_tools(self):
        # --allowedTools only pre-approves; --tools removes every other built-in tool (Bash, Task, Edit...).
        self.assertEqual(flag(build_command("skill"), "--tools"), "Skill,Read,Grep,Glob,Write")
        self.assertEqual(flag(build_command("web"), "--tools"), "Skill,Read,Grep,Glob,Write,WebSearch,WebFetch")
        for mode in ("skill", "web"):
            cmd = build_command(mode)
            self.assertEqual(flag(cmd, "--tools"), flag(cmd, "--allowedTools"))
            self.assertEqual(cmd[-2], "--tools")  # variadic flag last, so it swallows nothing

    def test_default_command_isolates_user_config(self):
        cmd = build_command("skill")
        self.assertEqual(flag(cmd, "--setting-sources"), "project")
        self.assertIn("--strict-mcp-config", cmd)
        self.assertIn("--no-session-persistence", cmd)
        self.assertNotIn("--bare", cmd)  # --bare needs an API key, so OAuth logins can't use it
        for mode in ("baseline", "web"):
            self.assertEqual(build_command(mode)[:cmd.index("--allowedTools")], cmd[:cmd.index("--allowedTools")])

    def test_web_mode_allows_web_tools(self):
        cmd = build_command("web")
        self.assertEqual(flag(cmd, "--allowedTools"), "Skill,Read,Grep,Glob,Write,WebSearch,WebFetch")
        self.assertNotIn("--disallowedTools", cmd)

    def test_baseline_uses_skill_mode_flags(self):
        self.assertEqual(build_command("baseline"), build_command("skill"))

    def test_unknown_mode_rejected(self):
        for mode in ("browser", "nope"):
            with self.assertRaises(ValueError):
                build_command(mode)

    def test_agent_cmd_env_override(self):
        os.environ["LAST_LOOK_AGENT_CMD"] = "fake-agent --flag 'two words'"
        self.assertEqual(build_command("skill")[:3], ["fake-agent", "--flag", "two words"])

    def test_prompt_includes_answers_verbatim(self):
        answers = "Q1: yes\n  * odd   spacing & 'quotes' ₹\n"
        self.assertIn(answers, build_prompt(answers, "skill"))
        self.assertIn(answers, build_prompt(answers, "baseline"))
        self.assertIn("last-look skill", build_prompt(answers, "skill"))
        self.assertNotIn("last-look skill", build_prompt(answers, "baseline"))
        self.assertEqual(build_prompt(answers, "web"), build_prompt(answers, "skill"))
        self.assertEqual(build_prompt("A", "skill"),
                         "Use the last-look skill on this project. Answers to its questions: A. Write the report and stop.")
        self.assertEqual(build_prompt("A", "baseline"),
                         "Check this project for legal, app store and good-practice mistakes. Answers: A. "
                         "Write the findings to last-look-report.md and stop.")


class WorkdirTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.fixtures, self.skill, self.tmp = root / "fixtures", root / "skill", root / "work"
        self.tmp.mkdir()
        for name in ("a", "b"):
            (self.fixtures / name / "src").mkdir(parents=True)
            (self.fixtures / name / "src" / "x.ts").write_text(name)
            (self.fixtures / name / "answers.md").write_text(f"answers {name}\n")
            (self.fixtures / name / "expected.json").write_text("{}")
            (self.fixtures / name / "src" / "expected.json").write_text("project's own")
        for rel in ("SKILL.md", "checks/c.md", "rules/r.md", "references/f.md",
                    "tests/t.py", "coverage/c.md", ".superpowers/p.md", "README.md"):
            (self.skill / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.skill / rel).write_text(rel)

    def test_single_fixture_at_root_without_answer_key(self):
        work = prepare_workdir(self.fixtures, ["a"], "skill", self.skill, self.tmp)
        self.assertEqual((work / "src" / "x.ts").read_text(), "a")
        self.assertFalse((work / "expected.json").exists())
        self.assertFalse((work / "answers.md").exists())
        self.assertTrue((work / "src" / "expected.json").exists())  # only the top-level key is dropped

    def test_site_folder_is_not_for_agent(self):
        (self.fixtures / "a" / "site").mkdir()
        (self.fixtures / "a" / "site" / "index.html").write_text("<html>")
        (self.fixtures / "a" / "src" / "site").mkdir()
        (self.fixtures / "a" / "src" / "site" / "keep.ts").write_text("project's own")
        (self.fixtures / "b" / "site").mkdir()
        (self.fixtures / "b" / "site" / "index.html").write_text("<html>")
        work = prepare_workdir(self.fixtures, ["a"], "skill", self.skill, self.tmp)
        self.assertFalse((work / "site").exists())
        self.assertTrue((work / "src" / "site" / "keep.ts").exists())  # only the top-level folder is dropped
        combined = prepare_workdir(self.fixtures, ["a", "b"], "skill", self.skill, self.tmp / "both")
        self.assertFalse((combined / "a" / "site").exists())
        self.assertFalse((combined / "b" / "site").exists())
        self.assertTrue((combined / "a" / "src" / "x.ts").exists())

    def test_skill_mode_copies_only_skill_parts(self):
        work = prepare_workdir(self.fixtures, ["a"], "skill", self.skill, self.tmp)
        dest = work / ".claude" / "skills" / "last-look"
        self.assertEqual(sorted(p.name for p in dest.iterdir()), ["SKILL.md", "checks", "references", "rules"])
        self.assertTrue((dest / "rules" / "r.md").is_file())

    def test_baseline_has_no_skill_folder(self):
        work = prepare_workdir(self.fixtures, ["a"], "baseline", self.skill, self.tmp)
        self.assertFalse((work / ".claude").exists())

    def test_skill_modes_need_skill_md(self):
        (self.skill / "SKILL.md").unlink()
        for mode in ("skill", "web"):
            with self.assertRaisesRegex(FileNotFoundError, "SKILL.md"):
                prepare_workdir(self.fixtures, ["a"], mode, self.skill, self.tmp)
        prepare_workdir(self.fixtures, ["a"], "baseline", self.skill, self.tmp)  # baseline never needs it

    def test_combine_puts_each_fixture_in_subfolder(self):
        work = prepare_workdir(self.fixtures, ["a", "b"], "skill", self.skill, self.tmp)
        self.assertEqual((work / "a" / "src" / "x.ts").read_text(), "a")
        self.assertEqual((work / "b" / "src" / "x.ts").read_text(), "b")
        self.assertFalse((work / "src").exists())
        for name in ("a", "b"):
            self.assertFalse((work / name / "expected.json").exists())
            self.assertFalse((work / name / "answers.md").exists())
        self.assertTrue((work / ".claude" / "skills" / "last-look" / "SKILL.md").is_file())


class MainTests(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ)
        patcher.start()
        self.addCleanup(patcher.stop)
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.results, self.projects = root / "results", root / "projects"
        for name in ("a", "b"):
            (self.projects / name).mkdir(parents=True)
            (self.projects / name / "app.txt").write_text(name)
            (self.projects / name / "answers.md").write_text(f"answers for {name}\n")
        (root / "fake.py").write_text(FAKE_AGENT)
        self.skill = root / "skill"
        self.skill.mkdir()
        (self.skill / "SKILL.md").write_text("skill")
        os.environ["LAST_LOOK_AGENT_CMD"] = f"{sys.executable} {root / 'fake.py'}"

    def run_main(self, *args, **kw):
        argv = ["--results", str(self.results), "--projects", str(self.projects), *args]
        kw.setdefault("skill", self.skill)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return main(argv, **kw)

    def test_bad_fixture_names_rejected_before_anything_is_deleted(self):
        stale = self.results / "a" / "skill" / "run-1"
        stale.mkdir(parents=True)
        for bad in ("../a", "../projects/a", "./a", "a/b", "a\\b", "a,..", "a,", ".", ""):
            with self.assertRaises(SystemExit, msg=bad):
                self.run_main("--fixtures", bad, "--mode", "skill")
            self.assertTrue(stale.is_dir(), bad)

    def test_missing_skill_rejected_before_anything_is_deleted(self):
        stale = self.results / "a" / "skill" / "run-1"
        stale.mkdir(parents=True)
        (self.skill / "SKILL.md").unlink()
        with self.assertRaises(SystemExit):
            self.run_main("--fixtures", "a", "--mode", "skill")
        self.assertTrue(stale.is_dir())

    def test_only_run_directories_are_removed(self):
        out = self.results / "a" / "skill"
        out.mkdir(parents=True)
        (out / "run-notes.txt").write_text("keep")
        self.run_main("--fixtures", "a", "--mode", "skill")
        self.assertEqual((out / "run-notes.txt").read_text(), "keep")

    def test_undecodable_output_is_logged_not_fatal(self):
        os.environ["FAKE_BAD"] = "1"
        self.run_main("--fixtures", "a", "--mode", "skill")
        log = (self.results / "a" / "skill" / "run-1" / "agent.log").read_text(encoding="utf-8")
        self.assertIn("bad", log)
        self.assertIn("fake stdout", log)

    def test_missing_agent_binary_is_logged_per_run_and_continues(self):
        os.environ["LAST_LOOK_AGENT_CMD"] = "/nonexistent/last-look-agent"
        self.assertEqual(self.run_main("--fixtures", "a", "--mode", "skill", "--runs", "2"), 0)
        for n in (1, 2):
            log = (self.results / "a" / "skill" / f"run-{n}" / "agent.log").read_text()
            self.assertIn("nonexistent", log)
            self.assertFalse((self.results / "a" / "skill" / f"run-{n}" / "last-look-report.md").exists())

    def test_end_to_end_writes_runs_and_cleans_up(self):
        self.results.joinpath("a", "skill", "run-9").mkdir(parents=True)
        self.results.joinpath("a", "baseline", "run-1").mkdir(parents=True)
        self.assertEqual(self.run_main("--fixtures", "a", "--mode", "skill", "--runs", "2"), 0)
        out = self.results / "a" / "skill"
        self.assertEqual(sorted(p.name for p in out.iterdir()), ["run-1", "run-2"])  # stale run-9 gone
        self.assertTrue((self.results / "a" / "baseline" / "run-1").is_dir())  # other mode untouched
        report = (out / "run-2" / "last-look-report.md").read_text()
        self.assertIn("answers for a", report.split("stdin=", 1)[1])  # prompt arrives on stdin
        self.assertIn("--disallowedTools WebSearch,WebFetch", report)
        work = Path(report.split("cwd=", 1)[1].splitlines()[0])
        self.assertFalse(work.exists())
        self.assertNotEqual(work.resolve(), Path.cwd().resolve())
        log = (out / "run-1" / "agent.log").read_text()
        self.assertIn("0", log.splitlines()[0])
        self.assertIn("fake stdout", log)

    def test_combined_run_stored_under_joined_name(self):
        self.run_main("--fixtures", "a,b", "--mode", "web")
        report = (self.results / "a+b" / "web" / "run-1" / "last-look-report.md").read_text()
        self.assertIn("## a\nanswers for a", report)
        self.assertIn("## b\nanswers for b", report)

    def test_unchanged_stale_report_is_not_saved(self):
        stale = "# old report from an earlier run\n"
        (self.projects / "a" / "last-look-report.md").write_text(stale)
        os.environ["FAKE_NOWRITE"] = "1"
        self.run_main("--fixtures", "a", "--mode", "skill")
        run = self.results / "a" / "skill" / "run-1"
        self.assertFalse((run / "last-look-report.md").exists())
        self.assertIn("report unchanged from fixture", (run / "agent.log").read_text())
        self.assertEqual((self.projects / "a" / "last-look-report.md").read_text(), stale)  # fixture untouched

    def test_rewritten_stale_report_is_saved(self):
        (self.projects / "a" / "last-look-report.md").write_text("# old report\n")
        self.run_main("--fixtures", "a", "--mode", "skill")
        run = self.results / "a" / "skill" / "run-1"
        self.assertIn("answers for a", (run / "last-look-report.md").read_text())
        self.assertNotIn("unchanged", (run / "agent.log").read_text())

    def test_combined_run_ignores_per_fixture_stale_reports(self):
        for name in ("a", "b"):
            (self.projects / name / "last-look-report.md").write_text(f"# old report {name}\n")
        os.environ["FAKE_NOWRITE"] = "1"
        self.run_main("--fixtures", "a,b", "--mode", "skill")
        run = self.results / "a+b" / "skill" / "run-1"
        self.assertFalse((run / "last-look-report.md").exists())  # no root report: nothing to save
        self.assertNotIn("unchanged", (run / "agent.log").read_text())
        os.environ.pop("FAKE_NOWRITE")
        self.run_main("--fixtures", "a,b", "--mode", "skill")
        self.assertIn("## a\nanswers for a", (run / "last-look-report.md").read_text())

    def test_failed_and_timed_out_runs_still_log_and_continue(self):
        os.environ["FAKE_RC"] = "3"
        self.run_main("--fixtures", "a", "--mode", "baseline", "--runs", "2")
        for n in (1, 2):
            log = (self.results / "a" / "baseline" / f"run-{n}" / "agent.log").read_text()
            self.assertIn("3", log.splitlines()[0])

        calls = []

        def fake_run(cmd, **kw):
            calls.append(kw)
            if len(calls) == 1:
                raise subprocess.TimeoutExpired(cmd, kw["timeout"], output=b"partial out", stderr=None)
            return subprocess.CompletedProcess(cmd, 0, "ok", "")

        self.run_main("--fixtures", "a", "--mode", "skill", "--runs", "2", run=fake_run)
        self.assertEqual({c["timeout"] for c in calls}, {1200})
        self.assertEqual({(c["encoding"], c["errors"]) for c in calls}, {("utf-8", "replace")})
        out = self.results / "a" / "skill"
        self.assertIn("timeout", (out / "run-1" / "agent.log").read_text())
        self.assertIn("partial out", (out / "run-1" / "agent.log").read_text())
        self.assertFalse((out / "run-1" / "last-look-report.md").exists())
        self.assertIn("ok", (out / "run-2" / "agent.log").read_text())


if __name__ == "__main__":
    unittest.main()
