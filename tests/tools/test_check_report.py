import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from check_report import SECTIONS, check_report, main, parse_location, parse_report

SECRET = "sk_live_FAKEFAKE1234"

DEFAULT = {
    "Check": "terms-acceptance-record", "Location": "src/x.ts:3", "Evidence": "Confirmed in code",
    "Why": "No record of what the user agreed to.", "Applies to": "India", "Strength": "Law",
    "Severity": "High", "Priority": "Now", "Fix": "Save terms_version and accepted_at.",
    "Rule started": "2027-05-13", "Status": "Coming 2027-05-13", "Verified on": "2026-11-03",
    "Source": "https://example.org/dpdp",
}


def block(title="Terms acceptance not saved", over=None):
    """A finding: heading plus fenced field lines. In `over`, None drops a field."""
    fields = {**DEFAULT, **(over or {})}
    lines = [f"{k}: {v}" for k, v in fields.items() if v is not None]
    return f"### {title}\n```\n" + "\n".join(lines) + "\n```\n"


BODIES = {
    "Notice": "This lists commonly expected items. It is not legal advice.",
    "Project summary": "A small web app.",
    "What probably applies": "India.",
    "Rule findings": block(),
    "Good practice findings": "None.",
    "Check on your own": "None.",
    "Data map": "None.",
    "New rules found (unverified)": "None.",
    "Not checked or skipped": "- Critic pass: 1 re-checked, 0 removed",
    "Looked at, nothing found": "- privacy-policy-missing: nothing found (searched: footer links)\n",
    "Details for Later findings": "None.",
    "Notice again": "Same notice.",
}


def make(bodies=None, order=SECTIONS):
    b = {**BODIES, **(bodies or {})}
    return "# Last-look report\n\n" + "".join(f"## {s}\n\n{b[s]}\n" for s in order)


class CheckReportTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.project, self.skill = root / "project", root / "skill"
        (self.project / "src").mkdir(parents=True)
        (self.project / "src" / "x.ts").write_text("".join(f"line {i}\n" for i in range(1, 11)))
        (self.project / "README.md").write_text("hi\n")
        (self.skill / "rules").mkdir(parents=True)
        for name, url in (("india.md", "dpdp"), ("apple.md", "apple")):
            (self.skill / "rules" / name).write_text(
                f"# {name}\n- coverage-summary: x.\n\n## r-{url}\n- check: c\n- source: https://example.org/{url}\n")

    def errors(self, text, secrets=()):
        report = self.project.parent / "report.md"
        report.write_text(text)
        return check_report(report, self.project, self.skill, list(secrets))

    def assertHas(self, errors, needle):
        self.assertTrue(any(needle in e for e in errors), (needle, errors))

    def test_clean_report_passes(self):
        self.assertEqual(self.errors(make()), [])

    def test_sections_present_in_order(self):
        self.assertHas(self.errors(make(order=[s for s in SECTIONS if s != "Data map"])), "section order")
        swapped = list(SECTIONS)
        swapped[3], swapped[4] = swapped[4], swapped[3]
        self.assertHas(self.errors(make(order=swapped)), "section order")

    def test_banned_wording(self):
        for phrase in ("You are compliant", "you are breaking the law", "Approved", "everything is followed", "It is SAFE."):
            with self.subTest(phrase):
                self.assertHas(self.errors(make({"Project summary": phrase})), "banned wording")

    def test_banned_wording_exceptions(self):
        for ok in ("DMCA safe harbour", "the safe harbor rule", "unsafe code and safety", "the `safe-check` id", "disapproved"):
            with self.subTest(ok):
                self.assertEqual(self.errors(make({"Project summary": ok})), [])

    def test_banned_wording_inside_finding(self):
        text = make({"Rule findings": block(over={"Why": "It is safe to skip."})})
        self.assertHas(self.errors(text), "banned wording")

    def test_now_and_soon_need_all_fields(self):
        self.assertHas(self.errors(make({"Rule findings": block(over={"Verified on": None})})), "missing field")
        self.assertHas(self.errors(make({"Rule findings": block(over={"Fix": ""})})), "missing field")

    def test_later_details_block_needs_all_fields(self):
        later = block("Later thing", {"Priority": "Later", "Source": None})
        self.assertHas(self.errors(make({"Details for Later findings": later})), "missing field")

    def test_field_order(self):
        text = make({"Rule findings": "### T\n```\nLocation: src/x.ts:3\nCheck: c\n```\n"})
        self.assertHas(self.errors(text), "field order")

    def test_values_are_pinned(self):
        for field, bad in (("Evidence", "Probably"), ("Strength", "Strong"), ("Severity", "Huge"),
                           ("Priority", "Never"), ("Evidence", "Maybe"), ("Strength", "Lawful"),
                           ("Strength", "Law ; Bogus"), ("Severity", "High (ish)")):
            with self.subTest(f"{field}={bad}"):
                self.assertHas(self.errors(make({"Rule findings": block(over={field: bad})})), "invalid")

    def test_values_with_pinned_start_pass(self):
        over = {"Strength": "Court or regulator (one German ruling)",
                "Priority": "Later for this project (India-only users)"}
        self.assertEqual(self.errors(make({"Rule findings": block(over=over)})), [])

    def test_rule_metadata_formats(self):
        for field, bad in (("Rule started", "soon"), ("Status", "Active"), ("Verified on", "yesterday")):
            with self.subTest(field):
                self.assertHas(self.errors(make({"Rule findings": block(over={field: bad})})), "invalid")
        over = {"Strength": "Good practice", "Rule started": "n/a", "Status": "In force"}
        self.assertEqual(self.errors(make({"Rule findings": block(over=over)})), [])

    def test_rule_started_before_date(self):
        for ok in ("before 2026-10-16", "2027-05-13 ; before 2026-10-16"):
            with self.subTest(ok):
                over = {"Rule started": ok}
                if " ; " in ok:
                    over.update({"Strength": "Law ; Store rule", "Status": "Coming 2027-05-13 ; In force",
                                 "Verified on": "2026-11-03 ; 2026-11-03",
                                 "Source": "https://example.org/dpdp ; https://example.org/dpdp"})
                self.assertEqual(self.errors(make({"Rule findings": block(over=over)})), [])
        for bad in ("before soon", "2027-05-13 ; before soon"):
            with self.subTest(bad):
                self.assertHas(self.errors(make({"Rule findings": block(over={"Rule started": bad})})),
                               "invalid Rule started")

    def test_several_rules_on_one_finding(self):
        over = {"Strength": "Law ; Store rule", "Rule started": "2027-05-13 ; 2025-01-01",
                "Status": "Coming 2027-05-13 ; In force", "Verified on": "2026-11-03 ; 2026-10-01",
                "Source": "https://example.org/dpdp ; https://example.org/apple"}
        self.assertEqual(self.errors(make({"Rule findings": block(over=over)})), [])
        over["Status"] = "Coming 2027-05-13 ; Nope"
        self.assertHas(self.errors(make({"Rule findings": block(over=over)})), "invalid")
        over["Status"] = "Coming 2027-05-13 ; In force"
        over["Source"] = "https://example.org/dpdp ; https://example.org/nope"
        self.assertHas(self.errors(make({"Rule findings": block(over=over)})), "unknown source")

    def test_location_file_exists_and_line_in_range(self):
        for loc in ("src/x.ts:99", "src/x.ts:0", "src/nope.ts:1", "src/nope.ts", "../x.ts", "/etc/passwd"):
            with self.subTest(loc):
                self.assertHas(self.errors(make({"Rule findings": block(over={"Location": loc})})), "invented location")

    def test_location_forms_that_pass(self):
        for loc in ("src/x.ts:10", "src/x.ts:1", "README.md", "https://example.com/pricing", "http://example.com"):
            with self.subTest(loc):
                self.assertEqual(self.errors(make({"Rule findings": block(over={"Location": loc})})), [])

    def test_finding_without_location(self):
        self.assertHas(self.errors(make({"Rule findings": block(over={"Location": ""})})), "no location")

    def test_flags_report_citing_itself(self):
        for loc in ("last-look-report.md", "last-look-report.md:4", "docs/last-look-report.md"):
            with self.subTest(loc):
                self.assertHas(self.errors(make({"Rule findings": block(over={"Location": loc})})), "cites its own report")

    def test_source_must_exist_in_skill(self):
        text = make({"Rule findings": block(over={"Source": "https://example.org/made-up"})})
        self.assertHas(self.errors(text), "unknown source")

    def test_new_rules_exempt_from_source(self):
        text = make({"New rules found (unverified)": block("New rule", {"Source": "https://example.org/made-up"})})
        self.assertEqual(self.errors(text), [])

    def test_maybe_limit(self):
        def maybes(n):
            return "".join(block(f"Maybe {i}", {"Evidence": "Maybe: check on your own"}) for i in range(n))
        self.assertEqual(self.errors(make({"Check on your own": maybes(15)})), [])
        self.assertHas(self.errors(make({"Check on your own": maybes(16)})), "too many Maybe items")

    def test_new_rules_may_say_not_verified(self):
        over = {"Evidence": "Maybe: check on your own", "Rule started": "not verified",
                "Status": "not verified", "Verified on": "not verified", "Source": "https://example.org/found"}
        self.assertEqual(self.errors(make({"New rules found (unverified)": block("New rule", over)})), [])
        # A stated value still passes, and one value in three can be not verified.
        mixed = {**over, "Rule started": "2026-02-25", "Status": "In force"}
        self.assertEqual(self.errors(make({"New rules found (unverified)": block("New rule", mixed)})), [])

    def test_new_rules_other_values_still_pinned(self):
        for field, bad in (("Rule started", "unknown"), ("Status", "Active"), ("Verified on", "not verified yet"),
                           ("Strength", "not verified")):
            with self.subTest(field):
                text = make({"New rules found (unverified)": block("New rule", {field: bad})})
                self.assertHas(self.errors(text), f"invalid {field}")

    def test_not_verified_is_an_error_outside_new_rules(self):
        for section in ("Rule findings", "Good practice findings", "Check on your own", "Details for Later findings"):
            for field in ("Rule started", "Status", "Verified on"):
                with self.subTest(f"{section}/{field}"):
                    text = make({section: block("Thing", {field: "not verified"})})
                    self.assertHas(self.errors(text), f"invalid {field}")

    def test_new_rules_blocks_do_not_count_toward_maybe_limit(self):
        def maybes(n):
            return "".join(block(f"Maybe {i}", {"Evidence": "Maybe: check on your own"}) for i in range(n))
        text = make({"Check on your own": maybes(15), "New rules found (unverified)": maybes(3)})
        self.assertEqual(self.errors(text), [])
        self.assertEqual(parse_report(text)["maybe_count"], 15)
        over = make({"Check on your own": maybes(16), "New rules found (unverified)": maybes(3)})
        self.assertHas(self.errors(over), "16 (limit 15)")

    def test_nothing_found_names_search(self):
        text = make({"Looked at, nothing found":
                     "- privacy-policy-missing: nothing found\n- age-handling: nothing found (searched: signup)\n\n3 checks, none found."})
        errors = self.errors(text)
        self.assertEqual(len(errors), 1)
        self.assertHas(errors, "nothing found without search")

    def test_flags_echoed_secret(self):
        text = make({"Project summary": f"Key is {SECRET}."})
        errors = self.errors(text, [SECRET])
        self.assertHas(errors, "secret echoed")
        self.assertFalse(any(SECRET in e for e in errors))

    def test_secret_never_printed_in_other_errors(self):
        text = make({"Rule findings": block(over={"Location": f"src/{SECRET}.ts"})})
        errors = self.errors(text, [SECRET])
        self.assertHas(errors, "invented location")
        self.assertFalse(any(SECRET in e for e in errors))

    def test_later_bullets_are_parsed_and_located(self):
        bullet = "- Footer link missing (privacy-policy-missing) at src/x.ts:2: No policy link. Fix: Add one."
        parsed = parse_report(make({"Rule findings": bullet}))
        self.assertEqual(parsed["later_bullets"], [{
            "title": "Footer link missing", "check": "privacy-policy-missing",
            "location": "src/x.ts:2", "why": "No policy link.", "fix": "Add one."}])
        self.assertEqual(self.errors(make({"Rule findings": bullet})), [])
        bad = bullet.replace("src/x.ts:2", "src/x.ts:99")
        self.assertHas(self.errors(make({"Rule findings": bad})), "invented location")
        self.assertHas(self.errors(make({"Rule findings": bullet.replace("src/x.ts:2", "")})), "no location")

    def test_parse_report_shape(self):
        text = make({"Check on your own": block("M", {"Evidence": "Maybe: check on your own"})})
        parsed = parse_report(text)
        self.assertEqual(parsed["sections"], list(SECTIONS))
        self.assertEqual([f["section"] for f in parsed["findings"]], ["Rule findings", "Check on your own"])
        self.assertEqual(parsed["findings"][0]["Check"], "terms-acceptance-record")
        self.assertEqual(parsed["findings"][0]["Verified on"], "2026-11-03")
        self.assertEqual(parsed["findings"][1]["Evidence"], "Maybe: check on your own")
        self.assertEqual(parsed["maybe_count"], 1)
        self.assertEqual(parsed["nothing_found"], ["- privacy-policy-missing: nothing found (searched: footer links)"])

    def test_critic_pass_line_required(self):
        self.assertHas(self.errors(make({"Not checked or skipped": "None."})), "missing critic pass line")
        moved = make({"Not checked or skipped": "None.", "Data map": "- Critic pass: 1 re-checked, 0 removed"})
        self.assertHas(self.errors(moved), "missing critic pass line")
        self.assertHas(self.errors(make({"Not checked or skipped": "- Critic pass: done"})), "missing critic pass line")
        for ok in ("- **Critic pass:** 12 re-checked, 2 removed.", "Critic pass: `0 re-checked, 0 removed`"):
            with self.subTest(ok):
                self.assertEqual(self.errors(make({"Not checked or skipped": ok})), [])
        self.assertTrue(parse_report(make())["critic_pass"])

    # --- fix round 1 ---

    def test_source_url_punctuation_is_not_part_of_url(self):
        (self.skill / "rules" / "slash.md").write_text("# s\n- coverage-summary: x.\n\n## r\n- source: https://example.org/slash/\n")
        for source in ("DPDP Act (https://example.org/dpdp)", "[DPDP](https://example.org/dpdp)",
                       "https://example.org/dpdp.", "https://example.org/dpdp/", "https://example.org/dpdp#s6",
                       "<https://example.org/dpdp>", "https://example.org/dpdp,", "https://example.org/slash"):
            with self.subTest(source):
                self.assertEqual(self.errors(make({"Rule findings": block(over={"Source": source})})), [])
        for source in ("https://example.org/dpdpx", "(https://example.org/made-up)"):
            with self.subTest(source):
                self.assertHas(self.errors(make({"Rule findings": block(over={"Source": source})})), "unknown source")

    def test_location_accepts_notes_ranges_backticks_and_folders(self):
        for loc in ("src/x.ts:3 (signup handler)", "src/x.ts:2-5", "`src/x.ts:3`", "`src/x.ts:2-5` (note)",
                    "src", ".", "https://example.com/p (live page)"):
            with self.subTest(loc):
                self.assertEqual(self.errors(make({"Rule findings": block(over={"Location": loc})})), [])
        for loc in ("src/x.ts:5-99", "src/x.ts:9-2", "src/x.ts:11", "src:3", "src/nope.ts:3 (note)"):
            with self.subTest(loc):
                self.assertHas(self.errors(make({"Rule findings": block(over={"Location": loc})})), "invented location")
        self.assertHas(self.errors(make({"Rule findings": block(over={"Location": "`last-look-report.md:3` (stale)"})})),
                       "cites its own report")
        for empty in ("``", ":"):
            with self.subTest(empty):
                self.assertHas(self.errors(make({"Rule findings": block(over={"Location": empty})})), "no location")

    def test_h3_outside_finding_sections_is_not_a_finding(self):
        text = make({"Project summary": "### Stack\n\nNext.js", "Data map": "### Personal data\n\n- emails",
                     "Not checked or skipped": "### Skipped\n\n- live site\n- Critic pass: 1 re-checked, 0 removed"})
        self.assertEqual(self.errors(text), [])
        self.assertEqual([f["section"] for f in parse_report(text)["findings"]], ["Rule findings"])
        for section in ("Good practice findings", "Check on your own", "New rules found (unverified)", "Details for Later findings"):
            with self.subTest(section):
                self.assertHas(self.errors(make({section: "### Bare"})), "missing field")

    def test_banned_wording_across_line_wraps(self):
        self.assertHas(self.errors(make({"Project summary": "Overall you are\ncompliant."})), "banned wording")
        self.assertEqual(self.errors(make({"Project summary": "The DMCA safe\nharbor rule."})), [])

    def test_secret_not_leaked_through_repr(self):
        secret = "ab'c\\d"
        errors = self.errors(make({"Rule findings": block(f"t {secret} t", {"Verified on": None, "Location": f"src/{secret}.ts"})}),
                             [secret])
        self.assertHas(errors, "missing field")
        self.assertHas(errors, "invented location")
        for e in errors:
            self.assertNotIn("ab'c", e)
            self.assertNotIn("c\\d", e)
            self.assertNotIn("c\\\\d", e)

    def test_later_bullet_variants_are_checked(self):
        variants = {
            "backticks": "- Footer link (`privacy-policy-missing`) at `src/x.ts:99`: No link. Fix: Add one.",
            "bold": "- **Footer link** (privacy-policy-missing) at src/x.ts:99: No link. Fix: Add one.",
            "lowercase fix": "- Footer link (privacy-policy-missing) at src/x.ts:99: No link. fix: Add one.",
            "wrapped fix": "- Footer link (privacy-policy-missing) at src/x.ts:99: No link.\n  Fix: Add one.",
        }
        for name, bullet in variants.items():
            with self.subTest(name):
                self.assertHas(self.errors(make({"Rule findings": bullet})), "invented location")
                self.assertEqual(len(parse_report(make({"Rule findings": bullet}))["later_bullets"]), 1)
                self.assertEqual(self.errors(make({"Rule findings": bullet.replace("99", "2")})), [])
        self.assertEqual(parse_report(make({"Rule findings": variants["bold"]}))["later_bullets"][0]["title"], "Footer link")
        for bad in ("- Footer link (privacy-policy-missing) at src/x.ts:2 no colon here",
                    "- Footer link (privacy-policy-missing) at src/x.ts:2: No fix text given"):
            with self.subTest(bad):
                self.assertHas(self.errors(make({"Rule findings": bad})), "unparsed Later bullet")

    def test_prose_bullets_are_not_later_bullets(self):
        text = make({"Project summary": "- Payments (Razorpay) at checkout\n- Build (open-source) at launch",
                     "Not checked or skipped": "- Live site (skipped) at start\n- Critic pass: 1 re-checked, 0 removed"})
        self.assertEqual(self.errors(text), [])

    def test_nothing_found_bullet_may_wrap(self):
        text = make({"Looked at, nothing found": "- age-handling: nothing found\n  (searched: signup form)\n"})
        self.assertEqual(self.errors(text), [])

    def test_strength_and_priority_allow_trailing_text(self):
        for field, ok in (("Strength", "Law - DPDP"), ("Strength", "Law, DPDP s.6"), ("Strength", "Court or regulator (A ; B)"),
                          ("Priority", "Now."), ("Priority", "Now, before launch")):
            with self.subTest(f"{field}={ok}"):
                self.assertEqual(self.errors(make({"Rule findings": block(over={field: ok})})), [])
        for field, bad in (("Strength", "Lawful"), ("Priority", "Nowhere"), ("Priority", "Laterally")):
            with self.subTest(f"{field}={bad}"):
                self.assertHas(self.errors(make({"Rule findings": block(over={field: bad})})), "invalid")
        over = {"Strength": "Law (a ; b) ; Store rule", "Rule started": "2027-05-13 ; 2025-01-01"}
        self.assertEqual(self.errors(make({"Rule findings": block(over=over)})), [])

    def test_cli(self):
        report = self.project.parent / "report.md"
        argv = [str(report), "--project", str(self.project), "--skill", str(self.skill)]
        report.write_text(make())
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(argv), 0)
        self.assertEqual(out.getvalue(), "")
        report.write_text(make({"Project summary": f"{SECRET} is approved"}))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(main(argv + ["--secret", SECRET]), 1)
        self.assertIn("secret echoed", out.getvalue())
        self.assertIn("banned wording", out.getvalue())
        self.assertNotIn(SECRET, out.getvalue())

    def test_parse_location(self):
        for loc, expected in (
            ("src/x.ts:3", ("src/x.ts", 3, 3)),
            ("`src/x.ts:3-7` (the form)", ("src/x.ts", 3, 7)),
            ("src/x.ts, and more", ("src/x.ts", None, None)),
            ("./src/x.ts:", ("./src/x.ts", None, None)),
            ("https://example.org/a", None),
            ("`https://example.org/a` live", None),
            ("", None),
            (" , ", None),
        ):
            with self.subTest(loc):
                self.assertEqual(parse_location(loc), expected)


if __name__ == "__main__":
    unittest.main()
