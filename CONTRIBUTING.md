# Contributing

last-look is written in Markdown. People who use the skill never run code, so every change you make lives in `SKILL.md`, `checks/`, `rules/`, `references/` or `coverage/`. Scripts in `tests/` are for maintainers only.

Thank you for helping. A wrong rule misleads everyone who runs the skill, so this guide asks for care more than speed.

## How the content fits together

| Folder or file | What it holds |
|---|---|
| `checks/<area>.md` | One block per mistake: how to find it in code or on a site, why it matters, how to fix it, and when it does not apply. One file per area. |
| `rules/<file>.md` | One block per rule: which law, store rule or good practice asks for a check, with its strength, dates and source link. One file per country, region or store. |
| `coverage/<source-id>.md` | The coverage map for one source: one row per section, with what was decided for it. |
| `COVERAGE.md` | The index of coverage files. |
| `references/check-format.md` | The exact format of checks and rules. Read it before you write either. |
| `references/report-format.md` | The report layout the skill follows. |

The formats for checks and rules are in [`references/check-format.md`](references/check-format.md). The coverage file format is described under [Walking a source](#walking-a-source) below.

**One check per mistake.** A missing delete-account button is one check, however many laws or stores ask for it. Each law or store gets its own rule record that points at that check. Adding a country means adding rule records, plus checks only for mistakes that exist nowhere else.

## Rules for the content

- **Summarise and link.** Never copy long legal or guideline text. Short quoted phrases are fine.
- **Official sources first.** Set `secondary: yes` on the rule if the source is not the official text (a law firm summary, a mirror of the text), or if a value that decides whether, when or to whom the rule applies (`rule-started`, a `Coming` date, a threshold or scope limit) is not on the `source` page. Then `reference` names where that value comes from. A penalty or fee amount may stay `no` when `reference` names its official source.
- **Never invent.** No made-up URLs, section numbers or dates. If a source does not give the start day of a rule, use `before YYYY-MM-DD` with the date of the version you read, and say so in `reference`.
- **State the scope.** A rule that only covers some businesses, users or features must say so in the check's `exceptions` and the rule's `applies-to`, so it is never read as universal.
- **Keep look-for lines general.** Describe patterns, never the names, files or paths of the test projects in `tests/projects/`.
- **Good practice has a limit.** A good-practice check is added only if it affects privacy, security, store approval or user trust.
- **Never rename a check id.** Reports and tests depend on them. Change a title or wording instead.
- **Write your own words.** Do not copy text or structure from other compliance skills or tools. You may read them to find gaps.
- **Keep source copies out of git.** Save them under `.sources/<source-id>/`, which is gitignored.
- **Keep fields short.** The skill loads whole check and rule files on every run. The linter caps `why` at 250 characters and one sentence, `fix` at 400, `exceptions` at 600, each `look-for` item at 300 and a rule's `reference` at 400. Put each piece of advice in one check and point to it from others; leave duty lists to the source link.

## Walking a source

A walk turns a legal or policy source into checks, rule records and a coverage map, section by section. A full walk gives every section a final status. A targeted walk covers only the sections that checks rely on.

1. **Get the source.** Fetch the official text and save it under `.sources/<source-id>/`. Record its URL and the date you read it in the coverage file header. If the official site cannot be reached, use the best copy you can find, label it secondary in the header and in the rules, and say which copy you used.
2. **List the sections.** Create `coverage/<source-id>.md` with this header and table, and add one row per section with status `Not done yet`. Use the source's own numbering. For a full walk, list every section, rule, schedule and numbered item. You may split a long section into its sub-sections when they need different decisions.

   ```markdown
   # <Source name>
   - source-id: <source-id>
   - walk: full
   - url: https://<official text>
   - read-on: YYYY-MM-DD

   | Section | Topic | Status | Checks | Verified on | Note |
   |---|---|---|---|---|---|
   | s.6(4) | Withdrawing consent | Not done yet | - | | |
   ```

   Only these four header keys are allowed. Put any extra links on plain lines (not starting with `- `) under the header. Cells cannot contain the `|` character. In the Checks cell write `-` for none, or check ids separated by commas. Write Verified on as `YYYY-MM-DD` for every row you decide; it may stay empty only while the status is `Not done yet`.
3. **Decide each section.** For each row, ask what a developer could get wrong in an app or site, then give it one status:
   - `Covered`: a check finds the mistake. `Partly covered`: a check finds part of it. Name the check ids. Reuse an existing check if the mistake is already there; otherwise add a check to the right area file. Then add a rule record whose `check` points at it.
   - `Can't tell from code`: the evidence lives outside the project (contracts, store forms, a plan on paper). Group these by topic into one check with `evidence-default: maybe`, so the skill raises a "check on your own" item. Do not make one check per section.
   - `Doesn't concern apps`: sections about government, a regulator, appeals, definitions, exemptions and the like. Write a short reason in the Note.
   - Fill in `Verified on` for every row you decide. A full walk leaves no row at `Not done yet`.
4. **Write well.** Follow [Rules for the content](#rules-for-the-content). Keep each area file about one subject.
5. **Verify with a fresh pass.** See [Two-pass verification](#two-pass-verification).
6. **Update the summary.** Change the `- coverage-summary:` line at the top of the rules file so it says how far this source is covered. Reports quote that line.
7. **Run the linter and unit tests.** Both must pass, and a full walk must have zero `Not done yet` rows. See [Commands](#commands).
8. **Run a smoke eval.** Run the skill once on the `web-bad` test project and check the report, so new checks do not break it. If the source matters to mobile apps, also run `android-bad` or `ios-bad`. For an app store source, run both.
9. **Commit.** One commit per source, with the message `content: <source> walk`. Commit only skill files, coverage files and this guide, never `.sources/` or `tests/results/`.

## Two-pass verification

"Verified" means the source text was read, the claim matches it, and the date is recorded. One pass is never enough.

1. The writer walks the source and writes the checks, rules and coverage rows.
2. A second, independent reader opens the source copy and each new or changed check and rule. They do not see the writer's notes or reasoning. For each item they answer `agree` or `disagree: <why>`, checking that the claim, the section number, the dates and the scope match the source.
3. The writer fixes each disagreement, and the second reader checks those items again.

When the tool you use has subagents, the second reader can be a fresh subagent that is given only the source and the items. Otherwise ask another person.

Before a release, a maintainer checks a random sample of 10 rules against their sources. If one is wrong, it is fixed, every rule from that source is verified again, and 10 more are checked.

## Adding a check

1. Search `checks/` for the mistake first. If a check already finds it, add a rule to that check instead.
2. Pick the area file in `checks/` that fits. The 19 area ids are fixed: each one is a file name in `checks/`, and `area` must match it.
3. Add a `## <check-id>` block with every field in the format. Use a new kebab-case id.
4. Fill `look-for` with concrete patterns, by platform where it matters, plus what to observe on a live site and any question to ask the user.
5. Write `exceptions` carefully: they are how the skill avoids false alarms.
6. Add at least one rule record for the check. A check with no rule cannot be cited in a report.

## Adding a rule

1. Open the rules file for the country, region or store. Add a `## <rule-id>` block in the format from `references/check-format.md`.
2. Point `check` at an existing check id.
3. Use the official text as `source`. Set `rule-started`, `status`, `verified-on` and `secondary` as the format says. Only `Good practice` rules may use `rule-started: n/a`.
4. If the rule comes from a walked source, add or update its coverage row.

## Adding a source

1. Choose a short `source-id` in kebab-case, such as `gdpr` or `cert-in-2022`.
2. Walk it as described above, as a full or targeted walk.
3. Add the source to the table in `COVERAGE.md`.

## Adding a country

1. Create `rules/<country>.md` with a `# <Country>` title and a `- coverage-summary:` line.
2. Walk that country's main sources. Most mistakes already have checks; add rule records for them. Add new checks only for mistakes that exist only there.
3. Add the rules file to the table in step 4 of `SKILL.md`, so the skill loads it when the country is in scope.

## Searching for new rules (for maintainers)

Laws and store rules change. This routine finds changes. Nothing is published without a person's review.

1. Ask an AI tool with web search to look at the official sources of each walked source for changes since its `read-on` date: amendments, new notifications, new versions of store guidelines. Queries contain legal topics only, never project code or details.
2. For each change found, re-read the changed sections in the official text and walk them again with the procedure above.
3. The tool proposes edits to checks, rule records and coverage rows, each with its source link.
4. A person reviews the proposal, runs the second-reader check, the linter and the tests, and merges it.

Rules past their verification age (6 months for law, 3 months for store rules) are the first to re-check.

## Commands

All commands run from the repo root with Python 3.10 or later and no extra packages.

    python3 tests/tools/lint_content.py            # check the content format
    python3 tests/tools/lint_content.py --release  # also the release rules: complete full walks, no stale dates
    python3 -m unittest discover -s tests/tools    # unit tests for the maintainer scripts

Evals run the skill with an AI agent on the test projects and score the reports:

    export LAST_LOOK_AGENT_CMD='claude -p --permission-mode acceptEdits --setting-sources project --strict-mcp-config --no-session-persistence --model sonnet'
    python3 tests/tools/run_evals.py --fixtures web-bad --mode skill --runs 1
    python3 tests/tools/check_report.py tests/results/web-bad/skill/run-1/last-look-report.md \
        --project tests/projects/web-bad --skill . --secret sk_test_FAKE0000000000000000
    python3 tests/tools/score.py --markdown

[`tests/README.md`](tests/README.md) explains the eval modes, the checker, the scorer, cost and timing.
