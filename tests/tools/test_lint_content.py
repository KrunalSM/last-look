import contextlib
import io
import json
import shutil
import tempfile
import unittest
from datetime import date
from pathlib import Path

from content import AREAS, FULL_WALK_SOURCES
from lint_content import TEST_CASE_IDS, lint, main

TODAY = date(2026, 11, 3)
INDIA = ("dpdp", "it-rules-2021", "cert-in-2022", "ecommerce-rules-2020", "dark-patterns-2023")


def check_block(cid, area):
    return f"""## {cid}
- title: Title of {cid}
- area: {area}
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code: something
  - site: none
  - ask: none
- why: Because.
- fix: Fix it.
- exceptions: none
- elsewhere: none

"""


def rule_block(rid, check, source, strength="Law"):
    started = "n/a" if strength == "Good practice" else "2025-01-01"
    return f"""## {rid}
- check: {check}
- source-id: {source}
- applies-to: India
- strength: {strength}
- reference: Ref
- rule-started: {started}
- status: In force
- verified-on: 2026-10-01
- source: https://example.org/{source}
- secondary: no

"""


def coverage_file(source, walk, row):
    return f"""# {source}
- source-id: {source}
- walk: {walk}
- url: https://example.org/{source}
- read-on: 2026-10-01

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
{row}
"""


def clean_tree(root):
    """A skill tree that lints clean, in release mode too."""
    by_area = {}
    for cid, area in TEST_CASE_IDS.items():
        by_area.setdefault(area, []).append(cid)
    for area in AREAS:
        by_area.setdefault(area, [f"extra-{area}"])
    (root / "checks").mkdir()
    for area, ids in by_area.items():
        (root / "checks" / f"{area}.md").write_text("".join(check_block(c, area) for c in ids))
    all_ids = [c for ids in by_area.values() for c in ids]

    def rules(name, title, blocks):
        (root / "rules").mkdir(exist_ok=True)
        (root / "rules" / name).write_text(f"# {title}\n- coverage-summary: Everything.\n\n" + "".join(blocks))

    rules("india.md", "India", [rule_block(f"r-{c}", c, INDIA[i % 5]) for i, c in enumerate(all_ids)])
    rules("apple.md", "Apple", [rule_block("r-apple", "terms-acceptance-record", "apple-review-guidelines", "Store rule")])
    rules("google-play.md", "Google", [rule_block("r-google", "terms-acceptance-record", "google-play-policy", "Store rule")])
    rules("good-practice.md", "Practice", [rule_block("r-gp", "privacy-policy-missing", "good-practice", "Good practice")])
    (root / "coverage").mkdir()
    covered = "| s.1 | Topic | Covered | terms-acceptance-record | 2026-10-01 | |"
    for s in FULL_WALK_SOURCES:
        (root / "coverage" / f"{s}.md").write_text(coverage_file(s, "full", covered))
    # targeted sources may keep Not done yet rows at release
    (root / "coverage" / "rbi.md").write_text(coverage_file("rbi", "targeted", "| s.1 | Payments | Not done yet | - | | |"))


def setf(root, rel, block, key, value):
    """Set (or with None, delete) a `- key:` line inside one `## block`."""
    out, inside = [], False
    for line in (root / rel).read_text().splitlines():
        if line.startswith("## "):
            inside = line == f"## {block}"
        if inside and line.startswith(f"- {key}:"):
            if value is None:
                continue
            line = f"- {key}: {value}"
        out.append(line)
    (root / rel).write_text("\n".join(out) + "\n")


def sub(root, rel, old, new):
    text = (root / rel).read_text()
    assert old in text, (rel, old)
    (root / rel).write_text(text.replace(old, new))


class LintTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        clean_tree(self.root)

    def errors(self, **kw):
        return lint(self.root, today=TODAY, **kw)

    def assertError(self, text, **kw):
        errs = self.errors(**kw)
        self.assertTrue(any(text in e for e in errs), f"{text!r} not in {errs}")

    def test_clean_tree_passes(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(self.errors(release=True), [])

    def test_unknown_area_in_check(self):
        setf(self.root, "checks/consent-records.md", "terms-acceptance-record", "area", "nonsense")
        self.assertError("unknown area")

    def test_check_area_must_match_file_name(self):
        setf(self.root, "checks/consent-records.md", "terms-acceptance-record", "area", "money")
        self.assertError("area does not match file")

    def test_pinned_check_in_wrong_area(self):
        setf(self.root, "checks/consent-records.md", "terms-acceptance-record", "area", "money")
        self.assertError("test-case check in wrong area")

    def test_missing_and_unknown_check_fields(self):
        setf(self.root, "checks/consent-records.md", "terms-acceptance-record", "why", None)
        sub(self.root, "checks/consent-records.md", "- fix:", "- bogus: x\n- fix:")
        self.assertError("missing field: why")
        self.assertError("unknown field: bogus")

    def test_empty_look_for_counts_as_missing(self):
        sub(self.root, "checks/consent-records.md", "- look-for:\n  - code: something\n  - site: none\n  - ask: none\n", "- look-for:\n")
        self.assertError("missing field: look-for")

    def test_bad_enums_on_checks(self):
        setf(self.root, "checks/money.md", "renewal-terms-checkout", "evidence-default", "sure")
        setf(self.root, "checks/money.md", "renewal-terms-checkout", "elsewhere", "EU only")
        self.assertError("invalid evidence-default")
        self.assertError("invalid elsewhere")

    def test_list_where_single_value_expected(self):
        sub(self.root, "rules/apple.md", "- source: https://example.org/apple-review-guidelines", "- source:\n  - https://example.org/a")
        sub(self.root, "checks/money.md", "- elsewhere: none", "- elsewhere:\n  - x")
        self.assertError("source must be a single value")
        self.assertError("elsewhere must be a single value")

    def test_duplicate_check_id_across_files(self):
        with open(self.root / "checks" / "money.md", "a") as f:
            f.write(check_block("terms-acceptance-record", "money"))
        self.assertError("duplicate check id")

    def test_rule_points_to_missing_check(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "check", "nope")
        self.assertError("unknown check")

    def test_bad_strength_severity_status(self):
        setf(self.root, "checks/money.md", "renewal-terms-checkout", "severity", "Huge")
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "strength", "Vibes")
        setf(self.root, "rules/india.md", "r-terms-change-notice", "status", "Maybe later")
        self.assertError("invalid severity")
        self.assertError("invalid strength")
        self.assertError("invalid status")

    def test_rule_started_na_only_for_good_practice(self):
        with self.subTest("good practice with a date"):
            setf(self.root, "rules/good-practice.md", "r-gp", "rule-started", "2025-01-01")
            self.assertError("rule-started must be n/a")
        with self.subTest("law with n/a"):
            setf(self.root, "rules/india.md", "r-terms-acceptance-record", "rule-started", "n/a")
            self.assertError("rule-started must be a date")
        with self.subTest("bad date"):
            setf(self.root, "rules/india.md", "r-terms-change-notice", "rule-started", "soon")
            self.assertError("invalid rule-started date")

    def test_field_length_caps(self):
        caps = [("rules/india.md", "r-terms-acceptance-record", "reference", 400),
                ("checks/money.md", "renewal-terms-checkout", "why", 250),
                ("checks/money.md", "renewal-terms-checkout", "fix", 400),
                ("checks/money.md", "renewal-terms-checkout", "exceptions", 600)]
        for rel, block, key, cap in caps:
            with self.subTest(key):
                setf(self.root, rel, block, key, "x" * cap)
                self.assertEqual(self.errors(), [])
                setf(self.root, rel, block, key, "x" * (cap + 1))
                self.assertError(f"{rel}: {block}: {key} too long: {cap + 1} characters (max {cap})")
                setf(self.root, rel, block, key, "Short.")

    def test_look_for_item_cap(self):
        sub(self.root, "checks/money.md", "  - code: something", "  - code: " + "y" * 294)
        self.assertEqual(self.errors(), [])
        sub(self.root, "checks/money.md", "  - code: " + "y" * 294, "  - code: " + "y" * 295)
        self.assertError("checks/money.md: renewal-terms-checkout: look-for item 1 too long: 301 characters (max 300)")

    def test_why_is_one_sentence(self):
        setf(self.root, "checks/money.md", "renewal-terms-checkout", "why", "Users lose money. Stores reject it.")
        self.assertError("renewal-terms-checkout: why must be one sentence")
        setf(self.root, "checks/money.md", "renewal-terms-checkout", "why", "Under DPDP s.17(1)(d) and the U.S. rule, users lose money.")
        self.assertEqual(self.errors(), [])

    def test_rule_started_before_date(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "rule-started", "before 2026-10-16")
        self.assertEqual(self.errors(), [])
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "rule-started", "before soon")
        self.assertError("invalid rule-started date")
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "rule-started", "2025-01-01")
        setf(self.root, "rules/good-practice.md", "r-gp", "rule-started", "before 2026-10-16")
        self.assertError("rule-started must be n/a")

    def test_verified_on_future_date(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "verified-on", "2026-12-01")
        sub(self.root, "coverage/dpdp.md", "| 2026-10-01 |", "| 2026-12-01 |")
        errs = self.errors()
        self.assertTrue(any("r-terms-acceptance-record" in e and "verified-on in the future" in e for e in errs), errs)
        self.assertTrue(any("coverage/dpdp.md" in e and "verified-on in the future" in e for e in errs), errs)

    def test_verified_on_today_is_fine(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "verified-on", "2026-11-03")
        self.assertEqual(self.errors(), [])

    def test_bad_verified_on_date(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "verified-on", "yesterday")
        self.assertError("invalid verified-on date")

    def test_source_must_be_url(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "source", "dpdp act")
        self.assertError("source is not a URL")

    def test_rules_file_has_coverage_summary(self):
        sub(self.root, "rules/apple.md", "- coverage-summary: Everything.\n", "")
        self.assertError("missing coverage summary")

    def test_coverage_checks_must_exist(self):
        sub(self.root, "coverage/dpdp.md", "| terms-acceptance-record |", "| nope |")
        self.assertError("unknown check")

    def test_coverage_empty_checks_cell(self):
        sub(self.root, "coverage/dpdp.md", "| terms-acceptance-record |", "|  |")
        self.assertError("empty checks cell")

    def test_coverage_status_values(self):
        sub(self.root, "coverage/dpdp.md", "| Covered |", "| Mostly |")
        self.assertError("invalid coverage status")

    def test_coverage_file_must_match_source_id(self):
        sub(self.root, "coverage/dpdp.md", "- source-id: dpdp", "- source-id: other")
        self.assertError("source-id does not match file")

    def test_pinned_test_case_ids_present(self):
        for cid, area in TEST_CASE_IDS.items():
            with self.subTest(cid):
                path = self.root / "checks" / f"{area}.md"
                original = path.read_text()
                path.write_text(original.replace(f"## {cid}\n", "## renamed\n"))
                self.assertError(f"missing test-case check: {cid}")
                path.write_text(original)

    def test_missing_directories_do_not_crash(self):
        for d in ("checks", "rules", "coverage"):
            shutil.rmtree(self.root / d)
        errs = self.errors()
        self.assertEqual(len(errs), len(TEST_CASE_IDS))
        self.assertTrue(all("missing test-case check" in e for e in errs))

    def test_parse_error_becomes_lint_error(self):
        with open(self.root / "rules" / "india.md", "a") as f:
            f.write("garbage line\n")
        self.assertError("cannot read line")

    def test_release_blocks_not_done_yet(self):
        sub(self.root, "coverage/dpdp.md", "| Covered |", "| Not done yet |")
        self.assertError("not complete", release=True)
        self.assertEqual([e for e in self.errors() if "not complete" in e], [])

    def test_release_requires_check_per_area(self):
        (self.root / "checks" / "accessibility.md").unlink()
        sub(self.root, "rules/india.md", "- check: extra-accessibility", "- check: terms-acceptance-record")
        self.assertError("no verified check in area: accessibility", release=True)
        self.assertEqual([e for e in self.errors() if "no verified check" in e], [])

    def test_release_requires_coverage_file_per_full_walk_source(self):
        with self.subTest("file deleted"):
            (self.root / "coverage" / "dpdp.md").unlink()
            self.assertError("missing coverage file: dpdp", release=True)
            self.assertEqual([e for e in self.errors() if "missing coverage file" in e], [])
        with self.subTest("meta source-id names another source"):
            sub(self.root, "coverage/cert-in-2022.md", "- source-id: cert-in-2022", "- source-id: other")
            self.assertError("missing coverage file: cert-in-2022", release=True)
        with self.subTest("every full-walk source reported"):
            shutil.rmtree(self.root / "coverage")
            missing = [e for e in self.errors(release=True) if "missing coverage file" in e]
            self.assertEqual(len(missing), len(FULL_WALK_SOURCES))

    def test_release_requires_coverage_rows(self):
        sub(self.root, "coverage/dpdp.md", "| s.1 | Topic | Covered | terms-acceptance-record | 2026-10-01 | |\n", "")
        self.assertError("no coverage rows: dpdp", release=True)
        self.assertEqual([e for e in self.errors() if "no coverage rows" in e], [])
        # a targeted source may stay empty
        (self.root / "coverage" / "rbi.md").write_text(coverage_file("rbi", "targeted", ""))
        self.assertEqual([e for e in self.errors(release=True) if "rbi" in e], [])

    def fixture(self, name, data, files=None):
        path = self.root / "tests" / "projects" / name / "expected.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data if isinstance(data, str) else json.dumps(data))
        for rel, text in (files or {}).items():
            (path.parent / rel).parent.mkdir(parents=True, exist_ok=True)
            (path.parent / rel).write_text(text)

    def test_fixture_ids_must_be_defined_checks(self):
        # Pinned ids and any other check defined under checks/ are fine; anything else is not.
        good = {"planted": [{"check": "google-fonts-remote", "file": "a.html", "line": 3},
                            {"check": "extra-accessibility", "file": "a.html", "line": 1},
                            {"check": "store-data-disclosure", "file": None, "line": None, "evidence": "maybe"}],
                "must_not_confirm": ["age-handling", "extra-licences"], "clean": False, "secrets": [], "needs_browser": False}
        self.fixture("ok", good, {"a.html": "1\n2\n3\n"})
        self.assertEqual(self.errors(), [])
        self.fixture("bad-planted", {**good, "planted": [{"check": "nope-planted", "file": None, "line": None}]})
        self.fixture("bad-not-confirm", {**good, "must_not_confirm": ["nope-confirm"]})
        self.assertError("unknown check id in fixture bad-planted: nope-planted")
        self.assertError("unknown check id in fixture bad-not-confirm: nope-confirm")
        self.assertEqual([e for e in self.errors() if "fixture ok" in e], [])

    def test_fixture_expected_json_shape(self):
        good = {"planted": [], "must_not_confirm": [], "clean": True, "secrets": [], "needs_browser": False}
        item = {"check": "age-handling", "file": None, "line": None}
        bad = {
            "not-json": "{oops",
            "not-object": [],
            "missing-key": {k: v for k, v in good.items() if k != "secrets"},
            "extra-key": {**good, "extra": 1},
            "planted-not-list": {**good, "planted": {}},
            "item-no-check": {**good, "planted": [{"file": None, "line": None}]},
            "item-bad-line": {**good, "planted": [{**item, "line": "3"}]},
            "item-bad-file": {**good, "planted": [{**item, "file": 7}]},
            "item-bad-evidence": {**good, "planted": [{**item, "evidence": "sure"}]},
            "clean-not-bool": {**good, "clean": "yes"},
            "secrets-not-strings": {**good, "secrets": [1]},
        }
        for name, data in bad.items():
            self.fixture(name, data)
        self.fixture("ok", good)
        errs = self.errors()
        for name in bad:
            with self.subTest(name):
                self.assertTrue(any(f"bad expected.json in fixture {name}" in e for e in errs), errs)
        self.assertFalse(any("fixture ok" in e for e in errs), errs)

    def test_fixture_planted_file_must_exist(self):
        def exp(file):
            return {"planted": [{"check": "age-handling", "file": file, "line": None}],
                    "must_not_confirm": [], "clean": False, "secrets": [], "needs_browser": False}
        self.fixture("ok", exp("src/a.ts"), {"src/a.ts": "x\n"})
        self.fixture("gone", exp("src/gone.ts"))
        self.fixture("dir", exp("src"), {"src/a.ts": "x\n"})
        self.fixture("escape", exp("../ok/src/a.ts"))
        self.fixture("no-file", exp(None))
        errs = self.errors()
        self.assertIn("planted file missing in fixture gone: src/gone.ts", errs)
        self.assertIn("planted file missing in fixture dir: src", errs)
        self.assertIn("planted file missing in fixture escape: ../ok/src/a.ts", errs)
        self.assertEqual([e for e in errs if "fixture ok" in e or "fixture no-file" in e], [])

    def test_fixture_planted_line_in_range(self):
        def exp(line):
            return {"planted": [{"check": "age-handling", "file": "a.ts", "line": line}],
                    "must_not_confirm": [], "clean": False, "secrets": [], "needs_browser": False}
        files = {"a.ts": "one\ntwo\nthree\n"}  # 3 lines, with a trailing newline
        for name, line in (("first", 1), ("last", 3), ("none", None), ("past", 4), ("zero", 0), ("negative", -1)):
            self.fixture(name, exp(line), files)
        errs = self.errors()
        self.assertIn("planted line out of range in fixture past: a.ts:4", errs)
        self.assertIn("planted line out of range in fixture zero: a.ts:0", errs)
        self.assertIn("planted line out of range in fixture negative: a.ts:-1", errs)
        self.assertEqual([e for e in errs if "out of range" in e and any(f"fixture {n}:" in e for n in ("first", "last", "none"))], [])
        self.assertEqual(len([e for e in errs if "out of range" in e]), 3)

    def test_non_utf8_file_names_the_path(self):
        for rel in ("checks/consent-records.md", "rules/india.md", "coverage/dpdp.md"):
            with self.subTest(rel):
                path = self.root / rel
                original = path.read_bytes()
                path.write_bytes(b"\xff\xfe## x\n")
                errs = self.errors()
                path.write_bytes(original)
                self.assertTrue(any(rel in e and "UTF-8" in e for e in errs), errs)

    def test_release_requires_india_source_check(self):
        sub(self.root, "rules/india.md", "source-id: cert-in-2022", "source-id: dpdp")
        self.assertError("no verified check for source: cert-in-2022", release=True)

    def test_release_warns_stale_law_and_store(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "verified-on", "2026-04-01")
        setf(self.root, "rules/apple.md", "r-apple", "verified-on", "2026-07-01")
        errs = self.errors(release=True)
        self.assertTrue(any("r-terms-acceptance-record" in e and "stale" in e for e in errs), errs)
        self.assertTrue(any("r-apple" in e and "stale" in e for e in errs), errs)
        self.assertEqual([e for e in self.errors() if "stale" in e], [])

    def test_stale_thresholds(self):
        for d, stale in (("2026-05-04", False), ("2026-05-03", True)):
            with self.subTest(f"law {d}"):
                setf(self.root, "rules/india.md", "r-terms-acceptance-record", "verified-on", d)
                self.assertEqual(any("stale" in e for e in self.errors(release=True)), stale)
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "verified-on", "2026-10-01")
        for d, stale in (("2026-08-03", False), ("2026-08-02", True)):
            with self.subTest(f"store {d}"):
                setf(self.root, "rules/google-play.md", "r-google", "verified-on", d)
                self.assertEqual(any("stale" in e for e in self.errors(release=True)), stale)

    def test_passed_coming_status(self):
        for d, passed in (("2026-11-03", True), ("2026-11-04", False)):
            with self.subTest(d):
                setf(self.root, "rules/india.md", "r-terms-acceptance-record", "status", f"Coming {d}")
                self.assertEqual(any("has passed" in e for e in self.errors()), passed)

    def test_store_rule_strength_goes_stale_like_store_sources(self):
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "strength", "Store rule")
        setf(self.root, "rules/india.md", "r-terms-acceptance-record", "verified-on", "2026-08-02")
        self.assertTrue(any("r-terms-acceptance-record" in e and "stale" in e for e in self.errors(release=True)))

    def test_cli_exit_codes(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(["--root", str(self.root)]), 0)
        self.assertEqual(out.getvalue(), "")
        setf(self.root, "checks/money.md", "renewal-terms-checkout", "severity", "Huge")
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(["--root", str(self.root)]), 1)
        self.assertIn("invalid severity", out.getvalue())


if __name__ == "__main__":
    unittest.main()
