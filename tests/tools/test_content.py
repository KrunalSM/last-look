import tempfile
import unittest
from pathlib import Path

from content import (
    AREAS,
    EVIDENCE_VALUES,
    FULL_WALK_SOURCES,
    SEVERITIES,
    STATUSES,
    STRENGTHS,
    parse_checks,
    parse_coverage,
    parse_rules,
    parse_rules_summary,
)

FIX = Path(__file__).parent / "fixtures"


class ParserTests(unittest.TestCase):
    def test_parse_checks_reads_block(self):
        c = parse_checks(FIX / "checks.md")["terms-acceptance-record"]
        self.assertEqual(c["severity"], "High")
        self.assertEqual(c["look-for"][0], "code: sign-up or checkout handler stores no terms version or acceptance timestamp")
        self.assertEqual(len(c["look-for"]), 3)
        self.assertEqual(c["why"], "Without a record you can't show what a user agreed to.")

    def test_parse_checks_reads_all_blocks(self):
        self.assertEqual(sorted(parse_checks(FIX / "checks.md")), ["privacy-policy-missing", "terms-acceptance-record"])

    def test_parse_checks_keeps_pipes_and_urls_in_values(self):
        c = parse_checks(FIX / "checks.md")["privacy-policy-missing"]
        self.assertEqual(c["elsewhere"], "EU | GDPR Art. 13 expects an equivalent notice | https://example.org/gdpr")

    def test_parse_checks_rejects_duplicate_id(self):
        with self.assertRaises(ValueError):
            parse_checks(FIX / "dup_checks.md")

    def test_parse_rules_reads_fields(self):
        r = parse_rules(FIX / "rules.md")[0]
        self.assertEqual((r["check"], r["strength"], r["secondary"]), ("terms-acceptance-record", "Law", "no"))
        self.assertEqual(r["id"], "dpdp-s6-consent-record")
        self.assertEqual(r["status"], "Coming 2027-05-13")

    def test_parse_rules_ignores_header_before_first_block(self):
        rules = parse_rules(FIX / "rules.md")
        self.assertEqual([r["id"] for r in rules], ["dpdp-s6-consent-record", "good-practice-privacy-link"])

    def test_parse_rules_summary(self):
        self.assertTrue(parse_rules_summary(FIX / "rules.md").startswith("DPDP, IT Rules"))
        self.assertIsNone(parse_rules_summary(FIX / "checks.md"))

    def test_parse_coverage_reads_meta_and_rows(self):
        cov = parse_coverage(FIX / "coverage.md")
        self.assertEqual(cov["meta"]["walk"], "full")
        self.assertEqual(cov["meta"]["source-id"], "dpdp")
        self.assertEqual(cov["rows"][0]["checks"], ["terms-acceptance-record"])
        self.assertEqual(
            cov["rows"][0],
            {"section": "s.6", "topic": "Consent and withdrawal", "status": "Covered",
             "checks": ["terms-acceptance-record"], "verified_on": "2026-11-03", "note": ""},
        )

    def test_parse_coverage_dash_means_no_checks(self):
        self.assertEqual(parse_coverage(FIX / "coverage.md")["rows"][1]["checks"], [])

    def test_parse_coverage_splits_comma_checks(self):
        row = parse_coverage(FIX / "coverage.md")["rows"][2]
        self.assertEqual(row["checks"], ["privacy-policy-missing", "terms-change-notice"])
        self.assertEqual(row["note"], "Two checks")

    def test_parse_rejects_malformed_input(self):
        bad = {
            "dup key": ("## a\n- title: x\n- title: y\n", parse_checks),
            "stray prose": ("## a\n- title: x\nsome prose\n", parse_checks),
            "item under scalar": ("## a\n- title: x\n  - item\n", parse_checks),
            "short table row": ("| Section | Topic | Status | Checks | Verified on | Note |\n|---|---|---|---|---|---|\n| s.1 | T |\n", parse_coverage),
            "wrong columns": ("| A | B |\n|---|---|\n", parse_coverage),
        }
        with tempfile.TemporaryDirectory() as d:
            for name, (text, parse) in bad.items():
                f = Path(d) / "x.md"
                f.write_text(text, encoding="utf-8")
                with self.subTest(name), self.assertRaises(ValueError):
                    parse(f)


class ConstantTests(unittest.TestCase):
    def test_pinned_values(self):
        self.assertEqual(len(AREAS), 19)
        self.assertEqual(STRENGTHS, ("Law", "Court or regulator", "Store rule", "Good practice"))
        self.assertEqual(SEVERITIES, ("Critical", "High", "Medium", "Low"))
        self.assertEqual(STATUSES, ("Covered", "Partly covered", "Can't tell from code", "Doesn't concern apps", "Not done yet"))
        self.assertEqual(len(EVIDENCE_VALUES), 6)
        self.assertEqual(len(FULL_WALK_SOURCES), 7)


if __name__ == "__main__":
    unittest.main()
