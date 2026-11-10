# General Data Protection Regulation (EU) 2016/679
- source-id: gdpr
- walk: targeted
- url: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- read-on: 2026-11-03

Targeted walk: only the articles the checks rely on, plus articles read along the way. The text was read from the Official Journal copy (OJ L 119, 4.5.2016) that the EU Publications Office serves at http://publications.europa.eu/resource/celex/32016R0679, because EUR-Lex refuses scripted requests; the EUR-Lex page above opens in a browser.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| Recital 32 | Silence, pre-ticked boxes or inactivity are not consent | Covered | prechecked-consent | 2026-11-03 | |
| Art. 4(11) | Definition of consent: a clear affirmative act | Covered | prechecked-consent | 2026-11-03 | Read with Art. 7 and Recital 32. |
| Art. 7(1) | Be able to show that consent was given | Covered | consent-record-missing | 2026-11-03 | |
| Art. 7(2) | Consent request set apart from other matters | Partly covered | prechecked-consent | 2026-11-03 | Only the bundled-checkbox pattern. |
| Art. 7(3) | Withdraw at any time, as easily as consent was given | Covered | consent-withdrawal-missing | 2026-11-03 | |
| Art. 7(4) | Service made conditional on unneeded consent | Not done yet | - | | Read; not mapped. |
| Art. 8 | Child's consent to online services (16, or 13 to 16 by national law) | Not done yet | - | | Read; age-handling has no GDPR rule yet. |
| Art. 12 | Clear information, help with rights, answer within one month | Partly covered | data-rights-request-missing | 2026-11-03 | Answer times are outside the code. |
| Art. 13(1)-(2) | Information when data is collected | Partly covered | privacy-policy-missing, privacy-notice-incomplete, ai-data-disclosure | 2026-11-04 | Missing policy, an incomplete notice and AI recipients; the timing "at collection" is not checked. |
| Art. 13(3) | Notice before data is used for a new purpose | Partly covered | terms-change-notice | 2026-11-03 | The check finds terms that change with no notice step; the new purpose itself is not checked. |
| Art. 15 | Right of access | Partly covered | data-rights-request-missing | 2026-11-03 | Only whether a way to ask is published. |
| Art. 16 | Right to correction | Partly covered | data-rights-request-missing | 2026-11-03 | Only whether a way to ask is published. |
| Art. 17 | Right to erasure | Covered | account-deletion-missing | 2026-11-03 | A web email route may be enough; see the check's exceptions. |
| Art. 28 | Processor contracts | Not done yet | - | | cross-border-transfers (outside services) has India wording only. |
| Art. 32 | Security of processing | Partly covered | open-database-rules | 2026-11-03 | Only open database rules. |
| Art. 33-34 | Breach notice to the authority and to people | Not done yet | - | | breach-readiness has India wording only. |
| Art. 44-49 | Transfers outside the EU | Not done yet | - | | cross-border-transfers has India wording only. |
| Art. 99 | Entry into force; applies from 25 May 2018 | Doesn't concern apps | - | 2026-11-03 | Gives the start date the rules use. |
