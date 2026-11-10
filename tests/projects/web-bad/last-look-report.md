# last-look report

Generated 2026-08-14.

## Notice
This is a first pass, not legal advice.

## Project summary
Web app. Users in India and the EU.

## What probably applies
- India (DPDP) and EU (GDPR) privacy rules.

## Rule findings

### No age check at sign-up
```
Check: age-handling
Location: src/app/signup/page.tsx:42
Evidence: Confirmed in code
Why: Sign-up asks no date of birth, so under-13 users are not screened out.
Applies to: US
Strength: Law
Severity: High
Priority: Now
Fix: Add an age gate before the account is created.
Rule started: 2000-04-21
Status: In force
Verified on: 2026-08-14
Source: https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa
```

## Good practice findings
None.

## Check on your own
None.

## Data map
Email address, password hash.

## New rules found (unverified)
None.

## Not checked or skipped
Live site: not tested.

## Looked at, nothing found
None.

## Details for Later findings
None.

## Notice again
This is a first pass, not legal advice.
