# California Invasion of Privacy Act, Penal Code s.630-638.55
- source-id: cipa
- walk: targeted
- url: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=631
- read-on: 2026-11-03

Targeted walk: only the sections the checks rely on. Read on leginfo.legislature.ca.gov in a browser (scripted requests get 403): s.631, s.637.2 and SB 690 as chaptered (https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB690). This replaces the california.public.law copy the seed rule used.

SB 690 (Caballero), Chapter 976, Statutes of 2026, approved by the Governor and filed on 30 September 2026. It amends only s.637.2: a new subdivision (d) lets only the Attorney General sue a private actor for a s.638.51 violation (pen registers and trap and trace devices) that arises from a website or app, and applies that retroactively to pending claims in actions commenced within two years before its operative date. The bill states no operative date and has no urgency clause, so it takes effect on 1 January 2027 (Cal. Const. art. IV, s.8(c)(1): 1 January after 90 days from enactment).

s.631 and s.637.2. SB 690 does not touch s.631. For s.631 claims, s.637.2(a) still allows a private action for the greater of $5,000 per violation or three times actual damages, with no need to show actual damages (s.637.2(c)). Current s.631 text: Stats. 2022, ch. 27, effective 1 January 2023; current s.637.2 text until SB 690 takes effect: Stats. 2016, ch. 855, effective 1 January 2017. Whether session replay reads communications "in transit" is for the courts, which are split.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| s.631(a) | Reading a communication in transit without all parties' consent | Partly covered | session-replay-consent | 2026-11-03 | Session replay only; a risk, not a settled ban. |
| s.637.2 | Private civil claim, $5,000 per violation or 3x damages | Partly covered | session-replay-consent | 2026-11-03 | Cited with s.631. SB 690's subdivision (d) applies only to s.638.51. |
| s.638.51 | Pen register or trap and trace device without a court order | Not done yet | - | | Tracker claims under this section: from 1 January 2027 only the Attorney General may bring them for websites and apps (SB 690). No rule added. |
