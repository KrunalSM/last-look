# ePrivacy Directive 2002/58/EC
- source-id: eprivacy
- walk: targeted
- url: https://eur-lex.europa.eu/eli/dir/2002/58/oj/eng
- read-on: 2026-11-03

Targeted walk: only the articles the checks rely on. Read on three EUR-Lex texts, fetched from the EU Publications Office because EUR-Lex refuses scripted requests: the original Directive (above); Directive 2009/136/EC, which replaced Art. 5(3) and Art. 13 (https://eur-lex.europa.eu/eli/dir/2009/136/oj/eng); and the consolidated text of 19.12.2009 (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02002L0058-20091219), which says it has no legal effect. This replaces the Wikipedia summary the seed rule used.

The Directive binds Member States; apps meet it through national laws. Start dates are the transposition deadlines: 31 October 2003 (2002/58/EC Art. 17(1)) and 25 May 2011 (2009/136/EC Art. 4(1)).

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| Art. 5(1) | Confidentiality of communications | Doesn't concern apps | - | 2026-11-03 | Aimed at listening to or intercepting network communications. |
| Art. 5(3) | Storing or reading information on a user's device: consent unless strictly necessary | Covered | trackers-before-consent, session-replay-consent | 2026-11-03 | As replaced by 2009/136/EC Art. 2(5). |
| Art. 13(1)-(2) | Marketing email: prior consent, or similar products to own customers with a way to refuse | Partly covered | marketing-email-footer | 2026-11-03 | The check finds a missing opt-out and ignored opt-out flags; whether consent was given is outside the code. |
| Art. 13(4) | No disguised sender; a valid address for opting out | Partly covered | marketing-email-footer | 2026-11-03 | Only the opt-out link; a disguised sender is not checked. |
| Art. 17 | Transposition deadline, 31 October 2003 | Doesn't concern apps | - | 2026-11-03 | Gives the Art. 13 start date. |
| 2009/136/EC Art. 4 | Transposition deadline, 25 May 2011 | Doesn't concern apps | - | 2026-11-03 | Gives the Art. 5(3) start date. |
