import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from score import main, render_markdown, score
from test_check_report import block, make

CHECK = "terms-acceptance-record"
LIVE = "Confirmed on live site"


class ScoreTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.results, self.fixtures, self.skill = root / "results", root / "fixtures", root / "skill"
        (self.skill / "rules").mkdir(parents=True)
        (self.skill / "rules" / "x.md").write_text(
            "# x.md\n- coverage-summary: x.\n\n## r-dpdp\n- check: c\n- source: https://example.org/dpdp\n")

    def fixture(self, name, planted=(), **over):
        d = self.fixtures / name
        (d / "src").mkdir(parents=True)
        (d / "src" / "x.ts").write_text("".join(f"line {i}\n" for i in range(1, 21)))
        expected = {"planted": [{"check": CHECK, "file": "src/x.ts", "line": 3, **p} for p in planted],
                    "must_not_confirm": [], "clean": False, "secrets": [], "needs_browser": False, **over}
        (d / "expected.json").write_text(json.dumps(expected))

    def run_report(self, name, mode, n, *blocks, **bodies):
        d = self.results / name / mode / f"run-{n}"
        d.mkdir(parents=True)
        (d / "last-look-report.md").write_text(make({"Rule findings": "".join(blocks), **bodies}))

    def score(self):
        return score(self.results, self.fixtures, self.skill)

    def mode(self, name, mode="skill"):
        return self.score()["fixtures"][name][mode]

    def test_match_needs_same_check_and_file(self):
        cases = [  # (planted override, finding override, found)
            ({}, {}, True),
            ({}, {"Location": "src/x.ts:6"}, True),
            ({}, {"Location": "src/x.ts:7"}, False),
            ({}, {"Location": "src/x.ts"}, False),
            ({}, {"Location": "src/x.ts:1-2"}, True),
            ({}, {"Location": "src/x.ts:9-12"}, False),
            ({}, {"Location": "`./src/x.ts:3` (in the signup form)"}, True),
            ({}, {"Check": "other-check"}, False),
            ({}, {"Location": "src/y.ts:3"}, False),
            ({"line": None}, {"Location": "src/x.ts"}, True),
            ({"line": None}, {"Location": "src/x.ts:15"}, True),
            ({"line": None}, {"Location": "src/y.ts"}, False),
            ({"file": None, "line": None}, {"Location": "README.md"}, True),
            ({"file": None, "line": None}, {"Check": "other-check"}, False),
        ]
        for i, (planted, over, _) in enumerate(cases):
            self.fixture(f"c{i}", [planted])
            self.run_report(f"c{i}", "skill", 1, block(over=over))
        fixtures = self.score()["fixtures"]
        for i, (planted, over, found) in enumerate(cases):
            with self.subTest(planted=planted, finding=over):
                self.assertEqual(len(fixtures[f"c{i}"]["skill"]["found"]), int(found))

    def test_found_needs_two_of_three_runs(self):
        for name, hits in (("one", 1), ("two", 2)):
            self.fixture(name, [{}])
            for n in (1, 2, 3):
                self.run_report(name, "skill", n, *([block()] if n <= hits else []))
        self.assertEqual(self.mode("one")["missed"], [{"check": CHECK, "file": "src/x.ts", "line": 3, "evidence": "confirm"}])
        self.assertEqual(self.mode("one")["found"], [])
        self.assertEqual(len(self.mode("two")["found"]), 1)
        self.assertEqual(self.mode("two")["missed"], [])

    def test_overall_pass_needs_90_percent(self):
        for found, expected in ((10, True), (9, True), (8, False)):
            shutil.rmtree(self.results, ignore_errors=True)
            shutil.rmtree(self.fixtures, ignore_errors=True)
            self.fixture("p", [{"check": f"check-{i}"} for i in range(10)])
            self.run_report("p", "skill", 1, *[block(over={"Check": f"check-{i}"}) for i in range(found)])
            overall = self.score()["overall"]
            with self.subTest(found=found):
                self.assertEqual((overall["found"], overall["planted"]), (found, 10))
                self.assertEqual(overall["found_rate"], found / 10)
                self.assertEqual(overall["pass"], expected, overall)

    def test_clean_fixture_fails_on_critical_high_false_confirm(self):
        for severity in ("Critical", "High"):
            shutil.rmtree(self.results, ignore_errors=True)
            shutil.rmtree(self.fixtures, ignore_errors=True)
            self.fixture("clean", clean=True)
            self.run_report("clean", "skill", 1, block(over={"Severity": severity}))
            with self.subTest(severity):
                self.assertEqual(self.mode("clean")["false_confirmed"]["critical_high"], 1)
                self.assertFalse(self.score()["overall"]["pass"])

    def test_clean_fixture_allows_two_other_false_confirms(self):
        for count, expected in ((2, True), (3, False)):
            shutil.rmtree(self.results, ignore_errors=True)
            shutil.rmtree(self.fixtures, ignore_errors=True)
            self.fixture("clean", clean=True)
            self.run_report("clean", "skill", 1, *[block(f"Finding {i}", {"Severity": "Medium"}) for i in range(count)])
            with self.subTest(count):
                fc = self.mode("clean")["false_confirmed"]
                self.assertEqual((fc["critical_high"], fc["other"]), (0, count))
                self.assertEqual(self.score()["overall"]["pass"], expected)

    def test_false_confirms_on_other_fixtures_do_not_fail_pass(self):
        self.fixture("bad", [{}])
        self.run_report("bad", "skill", 1, block(), block("Extra", {"Check": "x-1", "Severity": "High"}))
        self.assertEqual(self.mode("bad")["false_confirmed"]["critical_high"], 1)
        self.assertTrue(self.score()["overall"]["pass"])

    def test_must_not_confirm_hit_fails(self):
        self.fixture("general", must_not_confirm=["age-handling"])
        self.run_report("general", "skill", 1, block("Age", {"Check": "age-handling"}))
        hits = self.mode("general")["must_not_confirm_hits"]
        self.assertEqual([(h["run"], h["check"]) for h in hits], [("run-1", "age-handling")])
        self.assertFalse(self.score()["overall"]["pass"])

    def test_must_not_confirm_ignores_maybe(self):
        self.fixture("general", must_not_confirm=["age-handling"])
        self.run_report("general", "skill", 1, **{"Check on your own": block(
            "Age", {"Check": "age-handling", "Evidence": "Maybe: check on your own", "Severity": "Low"})})
        self.assertEqual(self.mode("general")["must_not_confirm_hits"], [])
        self.assertTrue(self.score()["overall"]["pass"])

    def test_maybe_items_do_not_count_as_false_alarms(self):
        self.fixture("clean", clean=True)
        maybes = "".join(block(f"Maybe {i}", {"Evidence": "Maybe: check on your own", "Severity": "High"})
                         for i in range(3))
        self.run_report("clean", "skill", 1, **{"Check on your own": maybes})
        m = self.mode("clean")
        self.assertEqual((m["false_confirmed"]["critical_high"], m["false_confirmed"]["other"]), (0, 0))
        self.assertEqual(m["maybe_max"], 3)
        self.assertTrue(self.score()["overall"]["pass"])

    def test_maybe_max_over_fifteen_fails(self):
        self.fixture("clean", clean=True)
        maybes = "".join(block(f"Maybe {i}", {"Evidence": "Maybe: check on your own"}) for i in range(16))
        self.run_report("clean", "skill", 1, **{"Check on your own": maybes})
        self.assertEqual(self.mode("clean")["maybe_max"], 16)
        self.assertFalse(self.score()["overall"]["pass"])

    def test_checker_error_fails_pass(self):
        self.fixture("bad", [{}])
        self.run_report("bad", "skill", 1, block(), block("Made up", {"Location": "src/nope.ts:1"}))
        errors = self.mode("bad")["checker_errors"]
        self.assertEqual(len(errors), 1)
        self.assertIn("run-1: invented location", errors[0])
        self.assertFalse(self.score()["overall"]["pass"])

    def test_checker_gets_fixture_secrets(self):
        self.fixture("bad", [{}], secrets=["sk_live_FAKE1"])
        self.run_report("bad", "skill", 1, block(over={"Why": "Key sk_live_FAKE1 is in the repo."}))
        errors = self.mode("bad")["checker_errors"]
        self.assertTrue(any("secret echoed" in e for e in errors), errors)
        self.assertFalse(any("sk_live_FAKE1" in e for e in errors))

    def test_missing_report_is_checker_error(self):
        self.fixture("bad", [{}])
        (self.results / "bad" / "skill" / "run-1").mkdir(parents=True)
        self.assertIn("run-1: no last-look-report.md", self.mode("bad")["checker_errors"])
        self.assertFalse(self.score()["overall"]["pass"])

    def test_fixture_without_skill_runs_fails_pass(self):
        self.fixture("never-run", [{}])
        overall = self.score()["overall"]
        self.assertEqual((overall["found"], overall["planted"], overall["pass"]), (0, 1, False))

    def test_later_bullet_counts_as_found(self):
        self.fixture("later", [{}])
        bullet = f"- Terms not saved ({CHECK}) at `src/x.ts:4`: No record of consent. Fix: Save it.\n"
        self.run_report("later", "skill", 1, bullet)
        self.assertEqual(len(self.mode("later")["found"]), 1)

    def test_unconfirmed_block_at_planted_location_is_not_found(self):
        self.fixture("maybe", [{}])
        self.run_report("maybe", "skill", 1, **{"Check on your own": block(
            over={"Evidence": "Maybe: check on your own", "Severity": "Low"})})
        self.assertEqual(len(self.mode("maybe")["missed"]), 1)

    def test_maybe_planted_item_matches_maybe_block(self):
        maybe = {"Evidence": "Maybe: check on your own", "Severity": "Low"}
        cases = [  # (planted override, section, finding override, found)
            ({"evidence": "maybe", "line": None}, "Check on your own", maybe, True),
            ({"evidence": "maybe"}, "Check on your own", {**maybe, "Location": "src/x.ts:5"}, True),
            ({"evidence": "maybe"}, "Check on your own", {**maybe, "Location": "src/x.ts:9"}, False),
            ({"evidence": "maybe"}, "Check on your own", {**maybe, "Check": "other-check"}, False),
            ({"evidence": "maybe"}, "Rule findings", {}, True),  # Confirmed also satisfies a maybe item
            ({"evidence": "maybe"}, "Rule findings", {"Evidence": "Not tested"}, False),
            ({"evidence": "maybe"}, "Rule findings", {"Evidence": "Nothing found"}, False),
            ({"evidence": "confirm"}, "Check on your own", maybe, False),
            ({}, "Check on your own", maybe, False),
        ]
        for i, (planted, section, over, _) in enumerate(cases):
            self.fixture(f"m{i}", [planted])
            self.run_report(f"m{i}", "skill", 1, **{section: block(over=over)})
        fixtures = self.score()["fixtures"]
        for i, (planted, section, over, found) in enumerate(cases):
            with self.subTest(planted=planted, section=section, finding=over):
                m = fixtures[f"m{i}"]["skill"]
                self.assertEqual(len(m["found"]), int(found))
                self.assertEqual((m["false_confirmed"]["critical_high"], m["false_confirmed"]["other"]), (0, 0))

    def test_maybe_planted_item_found_by_later_bullet(self):
        self.fixture("later", [{"evidence": "maybe", "line": None}])
        self.run_report("later", "skill", 1, f"- Store form ({CHECK}) at `src/x.ts`: Cannot tell. Fix: Check it.\n")
        self.assertEqual(len(self.mode("later")["found"]), 1)

    def test_unknown_planted_evidence_is_an_error(self):
        self.fixture("typo", [{"evidence": "Maybe"}])
        with self.assertRaises(ValueError):
            self.score()

    def test_needs_browser_items_count_only_in_browser_mode(self):
        self.fixture("live", [{"file": None, "line": None}], needs_browser=True)
        self.run_report("live", "skill", 1, block("Skill sees it", {"Location": "src/x.ts"}))
        self.run_report("live", "browser", 1, block("Browser sees it", {"Location": "src/x.ts", "Evidence": LIVE}))
        fx = self.score()["fixtures"]["live"]
        self.assertEqual((fx["skill"]["planted"], fx["skill"]["found"], fx["skill"]["missed"]), (0, [], []))
        self.assertEqual((fx["browser"]["planted"], len(fx["browser"]["found"])), (1, 1))
        self.assertTrue(self.score()["overall"]["pass"])

    def test_needs_browser_item_needs_live_site_evidence(self):
        cases = [  # (section, finding override, found)
            ("Rule findings", {"Evidence": LIVE}, True),
            ("Details for Later findings", {"Evidence": LIVE}, True),
            ("Rule findings", {"Evidence": "Confirmed in code"}, False),
            ("Rule findings", {"Evidence": "Maybe: check on your own", "Severity": "Low"}, False),
            ("Rule findings", {"Evidence": "Not tested"}, False),
            ("Rule findings", {"Evidence": LIVE, "Check": "other-check"}, False),
        ]
        for i, (_, _, _) in enumerate(cases):
            self.fixture(f"b{i}", [{"file": None, "line": None}], needs_browser=True)
        for i, (section, over, _) in enumerate(cases):
            self.run_report(f"b{i}", "browser", 1, **{section: block(over={"Location": "http://localhost:8765/", **over})})
        fixtures = self.score()["fixtures"]
        for i, (section, over, found) in enumerate(cases):
            with self.subTest(section=section, finding=over):
                self.assertEqual(len(fixtures[f"b{i}"]["browser"]["found"]), int(found))

    def test_needs_browser_item_not_found_by_code_evidence_or_later_bullet(self):
        self.fixture("live", [{"file": None, "line": None}], needs_browser=True)
        self.run_report("live", "browser", 1, block(over={"Location": "index.html:31"}),
                        f"- Terms not saved ({CHECK}) at `index.html:31`: Cannot tell. Fix: Check it.\n")
        m = self.mode("live", "browser")
        self.assertEqual((len(m["found"]), len(m["missed"])), (0, 1))
        self.assertEqual((m["false_confirmed"]["critical_high"], m["false_confirmed"]["other"]), (0, 0))  # right check, just no credit
        self.assertFalse(self.score()["overall"]["pass"])

    def test_live_site_evidence_still_finds_ordinary_planted_item(self):
        self.fixture("plain", [{}])
        self.run_report("plain", "skill", 1, block(over={"Evidence": LIVE}))
        self.assertEqual(len(self.mode("plain")["found"]), 1)

    def test_needs_browser_missed_in_browser_mode_fails(self):
        self.fixture("live", [{"file": None, "line": None}], needs_browser=True)
        self.run_report("live", "skill", 1, block("Skill sees it"))
        self.assertFalse(self.score()["overall"]["pass"])  # no browser runs at all
        self.run_report("live", "browser", 1)
        overall = self.score()["overall"]
        self.assertEqual((overall["found"], overall["planted"], overall["pass"]), (0, 1, False))

    def test_baseline_and_web_never_affect_pass(self):
        self.fixture("bad", [{}], must_not_confirm=["age-handling"], clean=True)
        self.run_report("bad", "skill", 1, block())  # planted match: not a false alarm
        bad = block("Bad", {"Check": "age-handling", "Severity": "High", "Location": "src/nope.ts:1"})
        self.run_report("bad", "baseline", 1, bad)
        self.run_report("bad", "web", 1, bad)
        fx = self.score()["fixtures"]["bad"]
        for mode in ("baseline", "web"):
            self.assertEqual(len(fx[mode]["missed"]), 1)
            self.assertTrue(fx[mode]["checker_errors"] and fx[mode]["must_not_confirm_hits"])
            self.assertEqual(fx[mode]["false_confirmed"]["critical_high"], 1)
        self.assertTrue(self.score()["overall"]["pass"], self.score()["overall"])

    def test_combined_fixture_unions_expectations(self):
        self.fixture("a", [{}])
        self.fixture("b", [{"check": "other-check"}], must_not_confirm=["age-handling"], clean=True)
        self.run_report("a+b", "skill", 1, block("A", {"Location": "a/src/x.ts:3"}),
                        block("B", {"Check": "other-check", "Location": "b/src/x.ts:4"}))
        m = self.mode("a+b")
        self.assertEqual([p["file"] for p in m["found"]], ["a/src/x.ts", "b/src/x.ts"])
        self.assertEqual((m["missed"], m["checker_errors"], m["must_not_confirm_hits"]), ([], [], []))
        self.run_report("a+b", "baseline", 1, block("A", {"Check": "age-handling", "Location": "b/src/x.ts:3"}))
        self.assertEqual(len(self.mode("a+b", "baseline")["must_not_confirm_hits"]), 1)
        self.run_report("a", "skill", 1, block("A"))
        o = self.score()["overall"]
        self.assertEqual((o["found"], o["planted"], o["single_found"], o["single_planted"]), (3, 4, 1, 2))
        self.assertIn("counts combined folders again; 1/2 in single-project folders", render_markdown(self.score()))

    def test_render_markdown_lists_misses(self):
        self.fixture("bad", [{}, {"check": "other-check", "line": None}])
        self.run_report("bad", "skill", 1, block("Wrong", {"Check": "x-1", "Severity": "High"}))
        self.run_report("bad", "baseline", 1, block())
        md = render_markdown(self.score())
        self.assertIn("## bad", md)
        self.assertIn("Misses", md)
        self.assertIn("skill: `other-check` at `src/x.ts`", md)
        self.assertIn("skill: `terms-acceptance-record` at `src/x.ts:3`", md)
        self.assertIn("False alarms", md)
        self.assertIn("`x-1` at `src/x.ts:3` (High)", md)
        self.assertIn("## Skill versus baseline", md)
        self.assertIn("Pass: **no**", md)

    def test_cli_prints_json_or_markdown_and_exits_zero(self):
        self.fixture("bad", [{}])
        self.run_report("bad", "skill", 1)
        args = ["--results", str(self.results), "--fixtures", str(self.fixtures)]
        for extra, check in (([], lambda out: json.loads(out)["overall"]["pass"] is False),
                             (["--markdown"], lambda out: out.startswith("# last-look"))):
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                self.assertEqual(main(args + extra), 0)
            self.assertTrue(check(buf.getvalue()), buf.getvalue())


if __name__ == "__main__":
    unittest.main()
