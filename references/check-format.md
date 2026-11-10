# Check and rule format

Every value sits on one `- key: value` line. A list value has the key with nothing after the colon, then indented `  - item` lines.

## Checks: `checks/<area>.md`

One file per area. The file starts with `# <Area title>`. Each check is one `## <check-id>` block:

```markdown
## terms-acceptance-record
- title: Terms acceptance not saved with version and time
- area: consent-records
- needs: accounts
- severity: High
- evidence-default: confirm
- look-for:
  - code: sign-up or checkout handler stores no terms version or acceptance timestamp
  - site: sign-up form has a terms checkbox
  - ask: none
- why: Without a record you can't show what a user agreed to.
- fix: Save terms_version and accepted_at with the user at acceptance.
- exceptions: none
- elsewhere: none
```

| Field | Meaning |
|---|---|
| `## <check-id>` | Stable id in kebab-case. Reports cite it in the `Check:` line. Never rename an id. |
| `title` | Short name of the mistake. Use it as the finding title. |
| `area` | One of the 19 area ids. Must match the file name. |
| `needs` | The feature the check depends on, such as `accounts`, `payments`, `email`, `database`, `user content`, `AI services`, `mobile app` or `iOS app`. `none` means it always runs. If the project lacks the feature, report the check as `Skipped`. |
| `severity` | `Critical`, `High`, `Medium` or `Low`: how serious the mistake is if a rule applies. |
| `evidence-default` | `confirm`: the code or site can show the mistake. `maybe`: the evidence lives outside the project (store forms, contracts, other systems), so report `Maybe: check on your own`. |
| `look-for` | What to search for. `code` items give patterns, by platform when it matters. `site` items say what to observe on a live site. `ask` items give a question for the user, or `none`; it is asked in the one question round, and if it stays unanswered and the code does not settle it, the check is reported as `Maybe: check on your own`. |
| `why` | One plain sentence on why it matters. |
| `fix` | An exact change where possible, otherwise steps. |
| `exceptions` | When the check does not apply, or must not be confirmed. Always read it before confirming. |
| `elsewhere` | `none`, or `<region> \| <one line> \| <url>`: a risk in another region, shown at `Later` with "may matter later". The URL is the `source` of a rule in `rules/*.md`; cite that rule's fields. |

**Length caps.** The skill loads whole files on every run, so the linter caps fields: `why` at most 250 characters and one sentence, `fix` 400, `exceptions` 600, and each `look-for` item 300. Leave long duty lists to the rule's source link, and point to another check ("see grievance-officer-missing") instead of repeating its advice.

## Rules: `rules/<file>.md`

A rules file starts with a title and one summary line. The summary says how far coverage goes, so a report can state it without loading the coverage map:

```markdown
# India
- coverage-summary: seed rules only, not yet walked
```

Then one `## <rule-id>` block per rule:

```markdown
## dpdp-s6-consent-record-missing
- check: consent-record-missing
- source-id: dpdp
- applies-to: India
- strength: Law
- reference: DPDP Act 2023, s.6(10)
- rule-started: 2027-05-13
- status: Coming 2027-05-13
- verified-on: 2026-11-03
- source: https://...
- secondary: yes
```

| Field | Meaning |
|---|---|
| `check` | The check id this rule supports. One check can have many rules. |
| `source-id` | The source it comes from, such as `dpdp`, `gdpr` or `apple-review-guidelines`. |
| `applies-to` | Who it covers: a country or region, a store, or `Everywhere`. Copy it to the finding's `Applies to:` line. |
| `strength` | `Law`, `Court or regulator`, `Store rule` or `Good practice`. |
| `reference` | Section or article, with any note a reader needs (dates in doubt, penalties as maximums). |
| `rule-started` | One of three forms. `YYYY-MM-DD`: the date the rule took effect, as a source confirms it. `before YYYY-MM-DD`: in force no later than this date, used when no source gives the start day; the date is the version or page date actually read, and `reference` says so. `n/a`: only for `Good practice`. Never guess a day. Reports copy the value as written. |
| `status` | `In force`, or `Coming YYYY-MM-DD`. |
| `verified-on` | When the source was last read and checked against this rule. |
| `source` | The URL to cite in the finding's `Source:` line. |
| `secondary` | `yes` if the source is not the official text, or if a value that decides whether, when or to whom the rule applies (`rule-started`, a `Coming` date, a threshold or scope limit) is not on the `source` page. Then `reference` names where that value comes from. A penalty or fee amount may stay `no` when `reference` names its official source. |

The linter caps `reference` at 400 characters. Give the section numbers, dates and doubt notes; leave the duty text to the source.

A report may cite only `source` URLs from these files, except in "New rules found (unverified)".
