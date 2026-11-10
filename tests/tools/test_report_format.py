"""The example report in references/report-format.md must pass check_report, using the real rules/*.md."""
import tempfile
import unittest
from pathlib import Path

from check_report import MAYBE, check_report, parse_location, parse_report

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "references" / "report-format.md"
START, END = "<!-- example-report:start -->", "<!-- example-report:end -->"


def example() -> str:
    text = DOC.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise AssertionError(f"{DOC} has no example between {START} and {END}")
    return text.split(START, 1)[1].split(END, 1)[0]


def build_project(text: str, project: Path) -> None:
    """Create every file the example cites, long enough for its highest cited line."""
    parsed = parse_report(text)
    lines: dict[str, int] = {}
    for loc in [f.get("Location", "") for f in parsed["findings"]] + [b["location"] for b in parsed["later_bullets"]]:
        if parsed_loc := parse_location(loc):
            path, _, last = parsed_loc
            lines[path] = max(lines.get(path, 1), last or 1)
    for path, count in lines.items():
        target = project / path
        if path.endswith("/"):
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("x\n" * count, encoding="utf-8")


class ExampleReport(unittest.TestCase):
    def test_example_passes_checker(self):
        text = example()
        with tempfile.TemporaryDirectory() as tmp:
            report, project = Path(tmp) / "report.md", Path(tmp) / "project"
            project.mkdir()
            report.write_text(text, encoding="utf-8")
            build_project(text, project)
            self.assertEqual(check_report(report, project, ROOT), [])

    def test_example_shows_each_kind_of_entry(self):
        parsed = parse_report(example())
        blocks = parsed["findings"]
        self.assertTrue(any(f.get("Priority", "").startswith("Now") for f in blocks), "no Now finding")
        self.assertTrue(parsed["later_bullets"], "no Later bullet")
        details = {f["title"] for f in blocks if f["section"] == "Details for Later findings"}
        for b in parsed["later_bullets"]:
            self.assertIn(b["title"], details, "Later bullet without its Details block")
        self.assertTrue(any(f.get("Evidence") == MAYBE for f in blocks), "no Maybe item")
        self.assertTrue(parsed["nothing_found"], "no nothing-found line")


if __name__ == "__main__":
    unittest.main()
