# last-look

A first-pass check for common legal, app store and good-practice mistakes in apps, websites and digital services. Not legal advice.

> **Notice.** This is an automated first pass for common mistakes. It is not legal advice and it can never confirm compliance. A clean report means only that these checks found nothing; it does not mean the project follows any law or store rule. For decisions that matter, ask a qualified lawyer.

## What it does

last-look is an agent skill: plain Markdown instructions that an AI coding agent follows. There is no code to run. Point your agent at a project folder, a live URL or both, and it:

1. Looks at the project and asks only what it could not tell: where the business is based, which countries you want users in, which app stores, whether children use it, and whether you sell or share data. "I don't know" is a valid answer and is reported as an open risk.
2. Works out which rule sets probably apply, and loads only the checks the project needs.
3. Runs the checks, then a second pass that removes findings with no location or evidence.
4. Searches the web for newer rules if the agent has a web tool. These results go in their own "unverified" section.
5. Writes `last-look-report.md` to the project folder.

Each finding gives:

- the location, as `file:line` where possible
- how sure it is: confirmed in code, confirmed on the live site, or `Maybe: check on your own`
- why it matters, severity and priority
- a fix where one is possible
- the rule behind it, with its strength (law, court or regulator, store rule, or good practice), when the rule started, its status, when it was last checked against the source, and a source link

Good-practice findings sit in their own section, so they never look like law.

Options: say "rules only" to leave out the good-practice section, and "no search" to skip the web search for newer rules.

## Install

**Claude Code plugin:**

```
/plugin marketplace add KrunalSM/last-look
/plugin install last-look@last-look
```

A plugin lives outside your projects, so its `tests/` folder needs no action.

**Copy by hand.** Copy this folder, without `tests/`, to the place your agent reads skills from. If you use `git clone` or copy the whole repo, delete `tests/` from the installed copy: the test projects hold planted mistakes and fake keys.

- **Claude Code, for all your projects:** `~/.claude/skills/last-look/`
- **Claude Code, for one project:** `.claude/skills/last-look/` inside that project
- **Other agents:** any place the agent reads skills from, or ask it to read `SKILL.md` and follow it

Then ask, for example: "Use last-look on this project." For a live site, give the URL; a browser tool lets the agent check what loads before consent.

## What it covers

There are 93 checks in 19 areas (`checks/`) and 248 rule records (`rules/`).

| Rules file | Records | How deep |
|---|---|---|
| India (`rules/india.md`) | 97 | DPDP Act and Rules, IT Rules 2021, CERT-In Directions 2022, E-Commerce Rules 2020 and Dark Patterns Guidelines 2023 fully walked; RBI recurring-payment rules targeted; three more sources with one rule each |
| Google Play (`rules/google-play.md`) | 48 | Developer Program Policy fully walked |
| Apple (`rules/apple.md`) | 36 | App Review Guidelines fully walked |
| Good practice (`rules/good-practice.md`) | 31 | Targeted: Apple and Android privacy docs, OWASP, WCAG 2.2, open-source licences |
| EU and UK (`rules/eu-uk.md`) | 24 | Targeted: GDPR, ePrivacy, UK GDPR and PECR, European Accessibility Act |
| US (`rules/us.md`) | 12 | Targeted: COPPA, CAN-SPAM, CCPA, CIPA, California auto-renewal law, DMCA; CalOPPA (one section, s.22575) and one FTC post are added one at a time |

A full walk means every section of the source has a recorded decision. A targeted walk covers only the sections the checks rely on. [`COVERAGE.md`](COVERAGE.md) lists each source and links its section-by-section coverage file. Countries with no rules file get the common checks and web search results, and the report says no list exists yet.

## Limits

- It reads code and, with a browser tool, one live site. It can't see app store consoles, ad or analytics settings, contracts, server setup or what staff do. Those come out as `Maybe: check on your own`.
- It is not a security scanner. The report points to dedicated security tools.
- Health, finance, gambling and similar fields are flagged as needing extra rules, not checked in depth.
- Rules change. Each record shows when it was last checked against its source, and the report lists records past their check date.
- The agent can make mistakes. Re-read each cited line before acting on it.
- Most testing used Claude Code with Sonnet. One run each on the test projects with agy (Gemini 3.8 Flash) and Grok Build (grok-4.7) gave matching results, apart from one `Maybe` in place of a `Confirmed`. Weaker models can still cite a file or source that doesn't exist, so check each one. Other agents and models are untested.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for adding a check, a source or a country, and for the maintainer routine.

## Support and privacy

Report a wrong rule or a false finding at https://github.com/KrunalSM/last-look/issues. last-look itself collects nothing and sends nothing anywhere: it is text your agent reads. Your agent's own terms cover what it sends.

Privacy policy: https://github.com/KrunalSM/last-look#support-and-privacy

## Licence

MIT. See [`LICENSE`](LICENSE).

## Test results

These results come from small made-up test projects in `tests/projects/`, each with mistakes planted on purpose. They show how often the skill finds those mistakes and how often it raises things that were not planted. They say nothing about whether any real project is compliant, and the skill never claims that. The raw reports are not published; [`tests/README.md`](tests/README.md) shows how to run them again, at about $0.40 to $1.50 per run.

How the runs were done:

- Runs used Claude Code 2.1.316 in headless mode with Sonnet (`claude-sonnet-5-5`) on 4 November 2026. Each run started in a fresh temp folder holding only the test project and the skill, with personal settings, skills and MCP servers kept out. The agent had no shell, no subagents and no web tools, except in `web` mode.
- `skill` mode: 3 runs for each project, except 1 run for `site-js-only` (no browser) and 1 for the combined `web-bad` plus `android-bad` folder. `web` mode: `web-bad`, 1 run, with web search allowed. All `skill` and `web` runs used the final skill text, apart from later wording fixes (answers that conflict with the project, the skill's own folder, unverified search results, the join and wording rules, who counts as an India intermediary, rules whose scope turns on a fact, observe-only live-site steps, `Coming` dates that have passed, more folders to skip, a fact check before writing, and settings that switch code off), which were smoke-tested as described below.
- The `browser` run (`site-js-only` served on localhost, done by hand in Claude Code with the built-in browser) used the same text.
- `baseline` mode: the same agent with no skill, asked to check the project and write its findings to the same file, 1 run each, from 3 November. It does not depend on the skill text.
- A planted mistake counts as found when a finding with the same check id names the same file (within 3 lines when a line is planted) in at least 2 of 3 runs, or in the only run. A "false Confirmed" is any `Confirmed` finding that matches no planted mistake. On the bad projects these are real gaps that were not planted, or a planted mistake cited at another file (see below).
- Cost at list price: about $65 for every eval run made while testing and reworking, including runs that were replaced; $18.58 for the runs scored below, not counting the browser run. A skill run took 1 to 6 minutes and cost $0.42 to $1.45.
- Smoke test of the later wording fixes: 1 run each with Sonnet on the final skill text, kept outside `tests/results`, so the scores below do not include them, and their cost is not in the figures above. `clean-web` in `skill` mode: 0 checker errors, 0 false `Confirmed` findings, 10 Maybe items. `web-bad` in `web` mode: 0 checker errors, 24 of 24 planted mistakes found, and 6 `Confirmed` findings that match no planted mistake (all Medium, all among the real gaps listed below). Its 2 "New rules found (unverified)" blocks followed the new field rules: Maybe evidence, `not verified` for rule started, status and verified on, and an existing check id. A second smoke test, after the intermediary and scope lines: `web-bad` in `skill` mode found 24 of 24 planted mistakes with 0 checker errors and 8 Medium `Confirmed` findings that match no planted mistake, all among the real gaps listed below; `clean-web` in `skill` mode had 0 checker errors, 0 false `Confirmed` findings and 12 Maybe items. A third, after the live-site, `Coming` date and skip-list fixes: `web-bad` found 24 of 24 with 0 checker errors and the same 8 Medium unplanted gaps; `clean-web` had 0 checker errors, 0 false `Confirmed` findings and 11 Maybe items. A fourth, after the fact check and the rule for code switched off by a setting: `web-bad` found 24 of 24 with 0 checker errors and 7 of the same Medium unplanted gaps; `clean-web` had 0 checker errors, 0 false `Confirmed` findings and 12 Maybe items. No run went over 15 Maybe items, so the new overflow line was not exercised, and no browser run was repeated. One run each says nothing about the other fixtures.

Changed expectations and test-project fixes:

- `kids-bad` `age-handling` is now expected as `Maybe: check on your own`. A children's site loads AdSense with no child age tag in code, but the age setting can also sit outside the code (Search Console for AdSense, or the AdMob and Ad Manager consoles), so the code alone can't confirm it.
- `clean-web`'s privacy page now names the company running the service, gives a legal basis for each use, lists the rights to restrict, object and move data, says the gallery is public, and lists content reports and the two essential cookies. These were real gaps once GDPR Art. 13 was checked for an incomplete notice.
- `android-bad` now has its missing privacy policy planted (no link or URL anywhere in the app), and `ios-bad`, `expo-bad` and `android-bad` have the real gaps that earlier runs kept finding.

What the numbers do and don't show:

- Baseline "found" is near zero mostly because the scorer matches the skill's check ids and report layout, which a baseline report doesn't use. A keyword scan suggests the baseline reports mention most planted topics in prose. What they lack is the fixed layout, exact locations, sources from the rule files, evidence levels and the wording limits: the `ios-bad` and `kids-bad` baseline reports used words the skill bans ("safe", "approved"), though not as compliance claims.
- Unplanted `Confirmed` findings on the bad projects were checked by hand. They are real gaps in those projects:
  - `android-bad`: no privacy contact, consent withdrawal, data request or grievance route.
  - `web-bad`: no privacy contact, consent withdrawal, consent record, data request, refund information, business details, content rules or prior price.
  - `kids-bad`: an ad script with no consent, no account deletion, no way to withdraw consent and a one-line privacy page.
  - `ios-bad`: no privacy contact, data request or grievance route.
  - `expo-bad`: camera and notification permissions asked for but never used.
  - One `web-bad` run cited the planted missing terms record on the sign-up form instead of the server route.
- The browser run's three unplanted findings, an incomplete privacy notice, no privacy contact (a general email is shown but not labelled for privacy questions) and no grievance route, are possibly real gaps in that page; the privacy contact one is borderline.
- `clean-web` had no false `Confirmed` findings. `age-handling` was not confirmed on `web-bad` or `clean-web`.
- Most Maybe items in one report: 14, under the limit of 15. The count leaves out the blocks under "New rules found (unverified)", which are all Maybe and sit outside the limit; the `web` row counted 2 of them in the first scoring (12, now 10).
- Published misses: none. Two checks needed one rework each to reach 2 of 3 runs: `privacy-policy-missing` on an iOS app with no screens, and `age-handling` on a children's site with an ad script.

### last-look eval results

Pass: **yes**. Planted mistakes found: 73/73 (100%), which counts combined folders again; 42/42 in single-project folders. Most Maybe items in one report: 14.

#### android-bad

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 3 | 7/7 | 0/4 | 0 | 10 | 0 |
| baseline | 1 | 0/7 | 0/0 | 0 | 0 | 2 |

Misses:
- baseline: `permission-at-launch` at `app/src/main/java/example/fitbuddy/MainActivity.kt:16`
- baseline: `prod-logging-personal-data` at `app/src/main/java/example/fitbuddy/AuthRepository.kt:9`
- baseline: `account-deletion-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt`
- baseline: `store-data-disclosure`
- baseline: `prechecked-consent` at `app/src/main/res/layout/activity_main.xml:16`
- baseline: `target-api-too-low` at `app/build.gradle.kts:12`
- baseline: `privacy-policy-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt`

False alarms:
- skill run-1: `consent-withdrawal-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt (no switch to withdraw marketing or analytics consent)` (Medium)
- skill run-1: `grievance-officer-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt (no grievance contact or response time)` (Medium)
- skill run-1: `privacy-contact-missing` at `app/src/main/res/layout/activity_main.xml (sign-up consent shows no privacy contact)` (Medium)
- skill run-1: `data-rights-request-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt (no access or correction option)` (Medium)
- skill run-2: `consent-withdrawal-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt:12 (no marketing opt-out toggle)` (Medium)
- skill run-2: `data-rights-request-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt (no data request option)` (Medium)
- skill run-2: `grievance-officer-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt (no grievance contact)` (Medium)
- skill run-2: `privacy-contact-missing` at `app/src/main/res/layout/activity_main.xml (consent request shows no privacy contact)` (Medium)
- skill run-3: `consent-withdrawal-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt:12-16 (no marketing preference toggle)` (Medium)
- skill run-3: `data-rights-request-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt:12-16 (no way to request data access or correction)` (Medium)
- skill run-3: `privacy-contact-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt (no privacy contact in settings or on the sign-up screen)` (Medium)
- skill run-3: `grievance-officer-missing` at `app/src/main/java/example/fitbuddy/SettingsActivity.kt (no grievance route or response time)` (Medium)

Checker errors:
- baseline run-1: section order: expected Notice | Project summary | What probably applies | Rule findings | Good practice findings | Check on your own | Data map | New rules found (unverified) | Not checked or skipped | Looked at, nothing found | Details for Later findings | Notice again; found none
- baseline run-1: missing critic pass line: expected 'Critic pass: N re-checked, M removed' under Not checked or skipped

#### clean-web

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 3 | n/a | 0/0 | 0 | 12 | 0 |
| baseline | 1 | n/a | 0/0 | 0 | 0 | 2 |

Checker errors:
- baseline run-1: section order: expected Notice | Project summary | What probably applies | Rule findings | Good practice findings | Check on your own | Data map | New rules found (unverified) | Not checked or skipped | Looked at, nothing found | Details for Later findings | Notice again; found none
- baseline run-1: missing critic pass line: expected 'Critic pass: N re-checked, M removed' under Not checked or skipped

#### expo-bad

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 3 | 3/3 | 0/1 | 0 | 7 | 0 |
| baseline | 1 | 0/3 | 0/0 | 0 | 0 | 2 |

Misses:
- baseline: `permission-at-launch` at `App.tsx:13`
- baseline: `prod-logging-personal-data` at `App.tsx:17`
- baseline: `privacy-policy-missing` at `App.tsx`

False alarms:
- skill run-3: `forced-login-or-permissions` at `App.tsx:12 (camera and notification permissions requested, but no code uses the camera or sends a notification)` (Medium)

Checker errors:
- baseline run-1: section order: expected Notice | Project summary | What probably applies | Rule findings | Good practice findings | Check on your own | Data map | New rules found (unverified) | Not checked or skipped | Looked at, nothing found | Details for Later findings | Notice again; found none
- baseline run-1: missing critic pass line: expected 'Critic pass: N re-checked, M removed' under Not checked or skipped

#### ios-bad

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 3 | 5/5 | 0/3 | 0 | 10 | 0 |
| baseline | 1 | 0/5 | 0/0 | 0 | 0 | 3 |

Misses:
- baseline: `permission-purpose-strings` at `FitBuddy/Info.plist:12`
- baseline: `permission-at-launch` at `FitBuddy/AppDelegate.swift:13`
- baseline: `prod-logging-personal-data` at `FitBuddy/AuthService.swift:11`
- baseline: `store-data-disclosure`
- baseline: `privacy-policy-missing` at `FitBuddy/Info.plist`

False alarms:
- skill run-3: `grievance-officer-missing` at `FitBuddy/Info.plist (no grievance contact or response time found in any app file)` (Medium)
- skill run-3: `data-rights-request-missing` at `FitBuddy/Info.plist (no data request route found in any app file)` (Medium)
- skill run-3: `privacy-contact-missing` at `FitBuddy/Info.plist (no privacy contact found in any app file)` (Medium)

Checker errors:
- baseline run-1: section order: expected Notice | Project summary | What probably applies | Rule findings | Good practice findings | Check on your own | Data map | New rules found (unverified) | Not checked or skipped | Looked at, nothing found | Details for Later findings | Notice again; found none
- baseline run-1: banned wording: line 96: 'safe'
- baseline run-1: missing critic pass line: expected 'Critic pass: N re-checked, M removed' under Not checked or skipped

#### kids-bad

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 3 | 2/2 | 2/2 | 0 | 8 | 0 |
| baseline | 1 | 0/2 | 0/0 | 0 | 0 | 4 |

Misses:
- baseline: `age-handling` at `src/app/layout.tsx:8`
- baseline: `parental-consent-unverified` at `src/app/api/signup/route.ts:11`

False alarms:
- skill run-1: `trackers-before-consent` at `src/app/layout.tsx:8` (High)
- skill run-1: `privacy-notice-incomplete` at `src/app/privacy/page.tsx:5` (Medium)
- skill run-1: `account-deletion-missing` at `src/app (no delete route, page or privacy-page instruction)` (High)
- skill run-2: `trackers-before-consent` at `src/app/layout.tsx:8` (High)
- skill run-2: `account-deletion-missing` at `src/app (no delete route, button or page for the child profile)` (High)
- skill run-2: `privacy-notice-incomplete` at `src/app/privacy/page.tsx:5` (Medium)
- skill run-2: `consent-withdrawal-missing` at `src/app/privacy/page.tsx (no way to withdraw consent given at sign-up)` (Medium)
- skill run-3: `trackers-before-consent` at `src/app/layout.tsx:8` (High)
- skill run-3: `privacy-notice-incomplete` at `src/app/privacy/page.tsx:5` (Medium)
- skill run-3: `consent-withdrawal-missing` at `src/app/privacy/page.tsx (no way to withdraw consent)` (Medium)

Checker errors:
- baseline run-1: section order: expected Notice | Project summary | What probably applies | Rule findings | Good practice findings | Check on your own | Data map | New rules found (unverified) | Not checked or skipped | Looked at, nothing found | Details for Later findings | Notice again; found none
- baseline run-1: banned wording: line 17: 'approved'
- baseline run-1: banned wording: line 78: 'safe'
- baseline run-1: missing critic pass line: expected 'Critic pass: N re-checked, M removed' under Not checked or skipped

#### site-js-only

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 1 | n/a | 0/0 | 0 | 4 | 0 |
| baseline | 1 | n/a | 0/0 | 0 | 0 | 2 |
| browser | 1 | 1/1 | 0/3 | 0 | 3 | 0 |

False alarms:
- browser run-1: `privacy-notice-incomplete` at `http://localhost:8765/ (privacy policy section, #privacy)` (Medium)
- browser run-1: `privacy-contact-missing` at `http://localhost:8765/ (privacy policy section, #privacy, names no contact for personal data questions)` (Medium)
- browser run-1: `grievance-officer-missing` at `http://localhost:8765/ (privacy policy section, #privacy, no way to raise a complaint about personal data and no reply time)` (Medium)

Checker errors:
- baseline run-1: section order: expected Notice | Project summary | What probably applies | Rule findings | Good practice findings | Check on your own | Data map | New rules found (unverified) | Not checked or skipped | Looked at, nothing found | Details for Later findings | Notice again; found none
- baseline run-1: missing critic pass line: expected 'Critic pass: N re-checked, M removed' under Not checked or skipped

#### web-bad

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 3 | 24/24 | 1/8 | 0 | 11 | 0 |
| baseline | 1 | 1/24 | 6/7 | 0 | 0 | 62 |
| web | 1 | 24/24 | 0/8 | 0 | 10 | 0 |

Misses:
- baseline: `google-fonts-remote` at `src/app/layout.tsx:9`
- baseline: `terms-acceptance-record` at `src/app/api/signup/route.ts:11`
- baseline: `terms-change-notice` at `src/app/terms/page.tsx`
- baseline: `prechecked-consent` at `src/app/signup/page.tsx:11`
- baseline: `trackers-before-consent` at `src/app/layout.tsx:12`
- baseline: `session-replay-consent` at `src/components/Replay.tsx:7`
- baseline: `open-database-rules` at `supabase/migrations/0001_init.sql:9`
- baseline: `prod-logging-personal-data` at `src/app/api/signup/route.ts:18`
- baseline: `privacy-policy-missing` at `src/app/layout.tsx`
- baseline: `account-deletion-missing` at `src/app/settings/page.tsx`
- baseline: `dark-pattern-urgency` at `src/components/OfferTimer.tsx:6`
- baseline: `renewal-terms-checkout` at `src/app/checkout/page.tsx`
- baseline: `marketing-email-footer` at `src/emails/weekly-offers.html`
- baseline: `uploads-takedown-process` at `src/app/api/upload/route.ts`
- baseline: `grievance-officer-missing`
- baseline: `ai-data-disclosure` at `src/app/api/chat/route.ts:5`
- baseline: `image-alt-missing` at `src/app/flashcards/page.tsx:13`
- baseline: `unauthenticated-data-route` at `src/app/api/profile/route.ts:7`
- baseline: `rate-limit-missing` at `src/app/api/chat/route.ts:5`
- baseline: `open-source-licence-terms` at `src/lib/scheduler.ts:2`
- baseline: `regulated-field-present` at `src/app/api/paylater/route.ts:6`
- baseline: `cross-border-transfers` at `vercel.json:2`
- baseline: `retention-periods-unset` at `supabase/migrations/0001_init.sql`

False alarms:
- skill run-1: `consent-record-missing` at `src/app/api/signup/route.ts:14` (Medium)
- skill run-1: `consent-withdrawal-missing` at `src/app/settings/page.tsx (no marketing toggle)` (Medium)
- skill run-1: `data-rights-request-missing` at `src/app/settings/page.tsx (no data request option)` (Medium)
- skill run-1: `user-content-rules-missing` at `src/app/terms/page.tsx:6` (Medium)
- skill run-1: `privacy-contact-missing` at `src/app/layout.tsx:21 (footer has no privacy contact; the sign-up form shows none either)` (Medium)
- skill run-1: `business-identity-missing` at `src/app/layout.tsx:21 (footer shows no legal name, address or customer care contact)` (Medium)
- skill run-1: `return-refund-policy-missing` at `src/app/checkout/page.tsx (no refund or returns information near the pay button or in the footer)` (Medium)
- skill run-1: `discount-prior-price-missing` at `src/emails/weekly-offers.html:5` (Medium)
- skill run-2: `consent-withdrawal-missing` at `src/app/settings/page.tsx (no marketing opt-out)` (Medium)
- skill run-2: `data-rights-request-missing` at `src/app/settings/page.tsx (no data request option)` (Medium)
- skill run-2: `discount-prior-price-missing` at `src/emails/weekly-offers.html:5` (Medium)
- skill run-2: `return-refund-policy-missing` at `src/app/checkout/page.tsx (no refund or cancellation terms near the pay button)` (Medium)
- skill run-2: `business-identity-missing` at `src/app/layout.tsx:21 (footer shows no legal name, address or customer care contact)` (Medium)
- skill run-2: `privacy-contact-missing` at `src/app/layout.tsx:21 (footer has no privacy contact)` (Medium)
- skill run-2: `user-content-rules-missing` at `src/app/terms/page.tsx:6` (Medium)
- skill run-2: `terms-acceptance-record` at `src/app/signup/page.tsx:8 (required checkbox only; the server route src/app/api/signup/route.ts saves no terms version or time)` (High)
- skill run-3: `consent-record-missing` at `src/app/api/signup/route.ts:14` (Medium)
- skill run-3: `privacy-contact-missing` at `src/app/layout.tsx:22 (footer has no privacy contact)` (Medium)
- skill run-3: `business-identity-missing` at `src/app/layout.tsx:22 (footer shows only a Terms link)` (Medium)
- skill run-3: `data-rights-request-missing` at `src/app/settings/page.tsx (no data request or correction option)` (Medium)
- skill run-3: `consent-withdrawal-missing` at `src/app/settings/page.tsx (no marketing or tracking choice)` (Medium)
- skill run-3: `return-refund-policy-missing` at `src/app/checkout/page.tsx (no refund or cancellation information near the pay button)` (Medium)
- skill run-3: `user-content-rules-missing` at `src/app/terms/page.tsx:6` (Medium)
- skill run-3: `discount-prior-price-missing` at `src/emails/weekly-offers.html:5` (Medium)
- baseline run-1: `consent-before-tracking` at `src/app/layout.tsx:12-19, src/components/Replay.tsx:7, package.json (logrocket)` (High)
- baseline run-1: `privacy-notice` at `src/app/layout.tsx:21-23 (footer has only "Terms")` (High)
- baseline run-1: `marketing-consent` at `src/app/signup/page.tsx:11 (defaultChecked)` (High)
- baseline run-1: `marketing-email-requirements` at `src/emails/weekly-offers.html` (Medium)
- baseline run-1: `access-control` at `src/app/api/profile/route.ts:5-8, supabase/migrations/0001_init.sql:9, src/lib/db.ts:3` (High)
- baseline run-1: `dark-patterns` at `src/components/OfferTimer.tsx:5-8, src/app/checkout/page.tsx:23` (High)
- baseline run-1: `sensitive-financial-data` at `src/app/api/paylater/route.ts:6-15, src/app/checkout/page.tsx:26-31` (High)
- baseline run-1: `data-subject-rights` at `src/app/settings/page.tsx` (Medium)
- baseline run-1: `international-transfers` at `vercel.json (iad1), src/app/api/chat/route.ts:5, src/app/layout.tsx:9-12, src/components/Replay.tsx` (Medium)
- baseline run-1: `terms-content` at `src/app/terms/page.tsx` (Medium)
- baseline run-1: `open-source-licence` at `src/lib/scheduler.ts:1-3` (Medium)
- baseline run-1: `user-generated-content` at `src/app/api/upload/route.ts:6-10` (Medium)
- baseline run-1: `ai-transparency` at `src/app/chat/page.tsx, src/app/api/chat/route.ts` (Medium)
- web run-1: `consent-withdrawal-missing` at `src/app/settings/page.tsx (no marketing opt-out)` (Medium)
- web run-1: `consent-record-missing` at `src/app/api/signup/route.ts:14` (Medium)
- web run-1: `data-rights-request-missing` at `src/app/settings/page.tsx (no data request option)` (Medium)
- web run-1: `privacy-contact-missing` at `src/app/layout.tsx:21 (footer has no privacy contact)` (Medium)
- web run-1: `business-identity-missing` at `src/app/layout.tsx:21 (footer shows no legal name, address or customer care contact)` (Medium)
- web run-1: `user-content-rules-missing` at `src/app/terms/page.tsx:6` (Medium)
- web run-1: `discount-prior-price-missing` at `src/emails/weekly-offers.html:5` (Medium)
- web run-1: `return-refund-policy-missing` at `src/app/checkout/page.tsx (no refund or cancellation terms near the pay button)` (Medium)

Checker errors:
- baseline run-1: missing field: '1. Trackers and session replay load with no consent': Rule started
- baseline run-1: missing field: '1. Trackers and session replay load with no consent': Status
- baseline run-1: missing field: '1. Trackers and session replay load with no consent': Verified on
- baseline run-1: unknown source: '1. Trackers and session replay load with no consent': GDPR Art. 6 and 7; ePrivacy Directive Art. 5(3); DPDP Act 2023 s.4-6
- baseline run-1: missing field: '2. No privacy policy or notice': Rule started
- baseline run-1: missing field: '2. No privacy policy or notice': Status
- baseline run-1: missing field: '2. No privacy policy or notice': Verified on
- baseline run-1: unknown source: '2. No privacy policy or notice': GDPR Art. 12-14; DPDP Act 2023 s.5
- baseline run-1: missing field: '3. Marketing email box is pre-ticked': Rule started
- baseline run-1: missing field: '3. Marketing email box is pre-ticked': Status
- baseline run-1: missing field: '3. Marketing email box is pre-ticked': Verified on
- baseline run-1: unknown source: '3. Marketing email box is pre-ticked': GDPR Art. 4(11), 7; ePrivacy Directive Art. 13; Planet49 (CJEU C-673/17)
- baseline run-1: missing field: '4. Offer email has no unsubscribe link or sender details': Rule started
- baseline run-1: missing field: '4. Offer email has no unsubscribe link or sender details': Status
- baseline run-1: missing field: '4. Offer email has no unsubscribe link or sender details': Verified on
- baseline run-1: unknown source: '4. Offer email has no unsubscribe link or sender details': ePrivacy Directive Art. 13; e-Commerce Directive Art. 6
- baseline run-1: missing field: "5. Anyone can read any member's profile (and RLS is off)": Rule started
- baseline run-1: missing field: "5. Anyone can read any member's profile (and RLS is off)": Status
- baseline run-1: missing field: "5. Anyone can read any member's profile (and RLS is off)": Verified on
- baseline run-1: unknown source: "5. Anyone can read any member's profile (and RLS is off)": GDPR Art. 5(1)(f) and 32; DPDP Act 2023 s.8(5)
- baseline run-1: missing field: '6. Stripe secret key is written into browser code': Rule started
- baseline run-1: missing field: '6. Stripe secret key is written into browser code': Status
- baseline run-1: missing field: '6. Stripe secret key is written into browser code': Verified on
- baseline run-1: unknown source: '6. Stripe secret key is written into browser code': Stripe key-handling guidance
- baseline run-1: missing field: '7. Fake urgency on the checkout page': Rule started
- baseline run-1: missing field: '7. Fake urgency on the checkout page': Status
- baseline run-1: missing field: '7. Fake urgency on the checkout page': Verified on
- baseline run-1: unknown source: '7. Fake urgency on the checkout page': India Guidelines for Prevention and Regulation of Dark Patterns 2023 (CCPA); Consumer Protection Act 2019; EU Unfair Commercial Practices Directive
- baseline run-1: missing field: '8. PAN and income sent to a lender with no notice or consent': Rule started
- baseline run-1: missing field: '8. PAN and income sent to a lender with no notice or consent': Status
- baseline run-1: missing field: '8. PAN and income sent to a lender with no notice or consent': Verified on
- baseline run-1: unknown source: '8. PAN and income sent to a lender with no notice or consent': DPDP Act 2023 s.5-6, 8; RBI Digital Lending Directions
- baseline run-1: missing field: '9. Account data cannot be deleted or exported': Rule started
- baseline run-1: missing field: '9. Account data cannot be deleted or exported': Status
- baseline run-1: missing field: '9. Account data cannot be deleted or exported': Verified on
- baseline run-1: unknown source: '9. Account data cannot be deleted or exported': GDPR Art. 15-21; DPDP Act 2023 s.11-14
- baseline run-1: missing field: '10. Personal data goes to US-based vendors with no transfer basis': Rule started
- baseline run-1: missing field: '10. Personal data goes to US-based vendors with no transfer basis': Status
- baseline run-1: missing field: '10. Personal data goes to US-based vendors with no transfer basis': Verified on
- baseline run-1: unknown source: '10. Personal data goes to US-based vendors with no transfer basis': GDPR Chapter V; DPDP Act 2023 s.16
- baseline run-1: missing field: '11. Terms are thin and some clauses are unfair to consumers': Rule started
- baseline run-1: missing field: '11. Terms are thin and some clauses are unfair to consumers': Status
- baseline run-1: missing field: '11. Terms are thin and some clauses are unfair to consumers': Verified on
- baseline run-1: unknown source: '11. Terms are thin and some clauses are unfair to consumers': EU Unfair Contract Terms Directive 93/13; Consumer Rights Directive 2011/83; India Consumer Protection (E-Commerce) Rules 2020
- baseline run-1: missing field: '12. Copied AGPL code in a network service': Rule started
- baseline run-1: missing field: '12. Copied AGPL code in a network service': Status
- baseline run-1: missing field: '12. Copied AGPL code in a network service': Verified on
- baseline run-1: invalid Evidence: '12. Copied AGPL code in a network service': Confirmed in code (header). Whether it triggers obligations needs a lawyer.
- baseline run-1: invalid Priority: '12. Copied AGPL code in a network service': Before launch
- baseline run-1: unknown source: '12. Copied AGPL code in a network service': GNU AGPL-3.0, section 13
- baseline run-1: missing field: '13. User-uploaded images are public, unchecked and unmoderated': Rule started
- baseline run-1: missing field: '13. User-uploaded images are public, unchecked and unmoderated': Status
- baseline run-1: missing field: '13. User-uploaded images are public, unchecked and unmoderated': Verified on
- baseline run-1: unknown source: '13. User-uploaded images are public, unchecked and unmoderated': EU Digital Services Act Art. 16; India IT Rules 2021 (intermediary duties)
- baseline run-1: missing field: '14. AI chat partner is not disclosed and its use of data is not explained': Rule started
- baseline run-1: missing field: '14. AI chat partner is not disclosed and its use of data is not explained': Status
- baseline run-1: missing field: '14. AI chat partner is not disclosed and its use of data is not explained': Verified on
- baseline run-1: unknown source: '14. AI chat partner is not disclosed and its use of data is not explained': EU AI Act Art. 50 (confirm the application date)
- baseline run-1: missing critic pass line: expected 'Critic pass: N re-checked, M removed' under Not checked or skipped
- baseline run-1: nothing found without search: - Password storage uses bcrypt (cost 10), which is fine.
- baseline run-1: nothing found without search: - The Terms checkbox is required at sign-up and not pre-ticked.
- baseline run-1: nothing found without search: - No third-party advertising SDKs, no location or camera access, and no data selling in the code.

#### web-bad+android-bad

| Mode | Runs | Found | False Confirmed (Critical/High / other) | Must-not-confirm hits | Maybe max | Checker errors |
|---|---|---|---|---|---|---|
| skill | 1 | 31/31 | 0/11 | 0 | 14 | 0 |

False alarms:
- skill run-1: `consent-record-missing` at `web-bad/src/app/api/signup/route.ts:14` (Medium)
- skill run-1: `data-rights-request-missing` at `web-bad/src/app/settings/page.tsx (no data request or correction option)` (Medium)
- skill run-1: `privacy-contact-missing` at `web-bad/src/app/layout.tsx:21 (footer and sign-up form show no privacy contact)` (Medium)
- skill run-1: `consent-withdrawal-missing` at `web-bad/src/app/settings/page.tsx (no marketing toggle)` (Medium)
- skill run-1: `discount-prior-price-missing` at `web-bad/src/emails/weekly-offers.html:5` (Medium)
- skill run-1: `return-refund-policy-missing` at `web-bad/src/app/checkout/page.tsx (no refund, cancellation or payment information near the pay button)` (Medium)
- skill run-1: `business-identity-missing` at `web-bad/src/app/layout.tsx:21 (footer shows only a Terms link)` (Medium)
- skill run-1: `user-content-rules-missing` at `web-bad/src/app/terms/page.tsx:6` (Medium)
- skill run-1: `data-rights-request-missing` at `android-bad/app/src/main/java/example/fitbuddy/SettingsActivity.kt:12 (no data request or correction option)` (Medium)
- skill run-1: `privacy-contact-missing` at `android-bad/app/src/main/java/example/fitbuddy/SettingsActivity.kt:12 (no privacy contact)` (Medium)
- skill run-1: `consent-withdrawal-missing` at `android-bad/app/src/main/java/example/fitbuddy/SettingsActivity.kt:12 (no marketing switch)` (Medium)

#### Skill versus baseline

| Fixture | Skill found | Baseline found | Skill false Confirmed | Baseline false Confirmed |
|---|---|---|---|---|
| android-bad | 7/7 | 0/7 | 0/4 | 0/0 |
| clean-web | n/a | n/a | 0/0 | 0/0 |
| expo-bad | 3/3 | 0/3 | 0/1 | 0/0 |
| ios-bad | 5/5 | 0/5 | 0/3 | 0/0 |
| kids-bad | 2/2 | 0/2 | 2/2 | 0/0 |
| site-js-only | 1/1 | n/a | 0/0 | 0/0 |
| web-bad | 24/24 | 1/24 | 1/8 | 6/7 |
| web-bad+android-bad | 31/31 | n/a | 0/11 | n/a |

