"""Parsers and pinned constants for last-look content files (checks, rules, coverage).

Stdlib only. Maintainer tooling: users of the skill never run this.
"""
import re
from pathlib import Path

AREAS = (
    "consent-records", "privacy-notices", "user-rights", "retention-breach", "cross-border",
    "third-party-data", "tracking-ads", "exposure", "children", "accessibility",
    "dark-patterns", "money", "communication", "user-content", "licences", "ai",
    "platforms", "business-details", "regulated-fields",
)
STRENGTHS = ("Law", "Court or regulator", "Store rule", "Good practice")
SEVERITIES = ("Critical", "High", "Medium", "Low")
STATUSES = ("Covered", "Partly covered", "Can't tell from code", "Doesn't concern apps", "Not done yet")
EVIDENCE_VALUES = (
    "Confirmed in code", "Confirmed on live site", "Maybe: check on your own",
    "Not tested", "Skipped", "Nothing found",
)
FULL_WALK_SOURCES = (
    "dpdp", "it-rules-2021", "cert-in-2022", "ecommerce-rules-2020",
    "dark-patterns-2023", "apple-review-guidelines", "google-play-policy",
)

COVERAGE_COLUMNS = ("Section", "Topic", "Status", "Checks", "Verified on", "Note")

_FIELD = re.compile(r"^- ([\w-]+):[ \t]*(.*?)\s*$")
_ITEM = re.compile(r"^[ \t]+- (.*?)\s*$")


def _blocks(path: Path) -> list[dict]:
    """Split a file into `## id` blocks; lines before the first heading are ignored.

    Each block is a dict with "id" plus its fields. A field whose value is empty and
    is followed by indented `  - item` lines becomes a list.
    """
    blocks: list[dict] = []
    block: dict | None = None
    last_key = None
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            block = {"id": line[3:].strip()}
            blocks.append(block)
            last_key = None
        elif block is None or not line.strip():
            continue
        elif m := _FIELD.match(line):
            last_key = m[1]
            if last_key in block:
                raise ValueError(f"{path}:{n}: duplicate key {last_key!r} in {block['id']}")
            block[last_key] = m[2]
        elif (m := _ITEM.match(line)) and last_key:
            if block[last_key] == "":
                block[last_key] = []
            if not isinstance(block[last_key], list):
                raise ValueError(f"{path}:{n}: list item under non-list key {last_key!r}")
            block[last_key].append(m[1])
        else:
            raise ValueError(f"{path}:{n}: cannot read line: {line!r}")
    return blocks


def parse_checks(path: Path) -> dict[str, dict]:
    checks: dict[str, dict] = {}
    for b in _blocks(path):
        if b["id"] in checks:
            raise ValueError(f"{path}: duplicate check id {b['id']!r}")
        checks[b["id"]] = b
    return checks


def parse_rules(path: Path) -> list[dict]:
    return _blocks(path)


def parse_rules_summary(path: Path) -> str | None:
    """The `- coverage-summary:` value from the lines above the first `## ` block."""
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            break
        if (m := _FIELD.match(line)) and m[1] == "coverage-summary":
            return m[2]
    return None


def parse_coverage(path: Path) -> dict:
    meta: dict[str, str] = {}
    rows: list[dict] = []
    header_seen = False
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not header_seen:
                if tuple(cells) != COVERAGE_COLUMNS:
                    raise ValueError(f"{path}:{n}: expected columns {COVERAGE_COLUMNS}, got {tuple(cells)}")
                header_seen = True
            elif set(line) <= set("|-: "):
                continue  # separator row
            elif len(cells) != len(COVERAGE_COLUMNS):
                raise ValueError(f"{path}:{n}: expected {len(COVERAGE_COLUMNS)} cells, got {len(cells)}")
            else:
                section, topic, status, checks, verified_on, note = cells
                rows.append({
                    "section": section, "topic": topic, "status": status,
                    "checks": [] if checks == "-" else [c.strip() for c in checks.split(",")],
                    "verified_on": verified_on, "note": note,
                })
        elif not header_seen and (m := _FIELD.match(line)):
            meta[m[1]] = m[2]
    return {"meta": meta, "rows": rows}
