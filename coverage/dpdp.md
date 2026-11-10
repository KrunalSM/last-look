# DPDP Act 2023 and Rules 2025
- source-id: dpdp
- walk: full
- url: https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- read-on: 2026-11-03

All three texts are official Gazette copies on meity.gov.in, read on 2026-11-03.

Act: https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf (Digital Personal Data Protection Act, 2023, No. 22 of 2023)
Rules: https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf (Digital Personal Data Protection Rules, 2025, G.S.R. 846(E))
Commencement: https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf (G.S.R. 843(E))

Start dates. Both notifications are dated 13 November 2025 in the Gazette. G.S.R. 843(E) brings the Act in by stages: s.1(2), s.2, s.18 to s.26, s.35, s.38 to s.43, s.44(1) and (3) on publication (2025-11-13); s.6(9) and s.27(1)(d) one year later (2026-11-13); everything else, including all duties of businesses, eighteen months later (2027-05-13). Rule 1 of the Rules sets the same stages for the Rules. The notices give periods, not calendar days; the dates here count the months from the Gazette date, the earliest plausible reading. Every DPDP rule's reference carries the doubt note: 13 or 14 May 2027: Gazette dated 13 Nov 2025, uploaded and signed 14 Nov. Some secondary sources say 12 or 14 May 2027; the press office says the Rules were notified on 14 November 2025, the date in the e-Gazette copy numbers and digital signatures.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| s.1 | Short title and commencement | Doesn't concern apps | - | 2026-11-03 | Start dates come from G.S.R. 843(E): see the header. |
| s.2 | Definitions | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. A child is anyone under 18 (s.2(f)), as used by age-handling. |
| s.3 | Where the Act applies | Doesn't concern apps | - | 2026-11-03 | Scope, used when working out what applies: processing in India, or abroad when offering goods or services to people in India. Personal or domestic use, and data the person made public, are out. |
| s.4 | Grounds: consent or a legitimate use | Partly covered | trackers-before-consent, session-replay-consent | 2026-11-03 | Checked for analytics, ads and replay, the usual consent-based processing in apps. |
| s.5(1) | Notice with or before a consent request | Covered | privacy-policy-missing, privacy-notice-incomplete | 2026-11-03 | Contents set by r.3. |
| s.5(2) | Notice to users who consented before the start date | Can't tell from code | privacy-notice-delivery | 2026-11-03 | Whether the notice is sent can't be seen in code. |
| s.5(3) | Notice in English or an Eighth Schedule language | Can't tell from code | privacy-notice-delivery | 2026-11-03 | Translations can be seen; which languages users need can't. |
| s.6(1) | Valid consent, limited to the data needed | Partly covered | prechecked-consent, trackers-before-consent, session-replay-consent | 2026-11-03 | Pre-ticked and bundled boxes and consent before tracking are checked. Asking for more data than the purpose needs is not checked yet. |
| s.6(2) | Consent terms that break the law are invalid | Doesn't concern apps | - | 2026-11-03 | States a legal effect, not a duty. |
| s.6(3) | Consent request: plain language, language option, contact | Partly covered | privacy-notice-delivery, privacy-contact-missing | 2026-11-03 | Contact is checked in code; the language option is a check-on-your-own item. |
| s.6(4) | Withdraw consent as easily as it was given | Covered | consent-withdrawal-missing | 2026-11-03 |  |
| s.6(5) | Effects of withdrawal | Doesn't concern apps | - | 2026-11-03 | States a legal effect; reflected in the consent-withdrawal-missing exceptions. |
| s.6(6) | Stop processing after withdrawal, processors too | Covered | consent-withdrawal-missing, cross-border-transfers | 2026-11-03 | Processors' side is a check-on-your-own item. |
| s.6(7) | Consent through a Consent Manager | Doesn't concern apps | - | 2026-11-03 | A route the user may choose; nothing for an app to get wrong in code. |
| s.6(8) | Consent Manager accountability | Doesn't concern apps | - | 2026-11-03 | Duties of registered Consent Managers only (First Schedule Part B). |
| s.6(9) | Consent Manager registration | Doesn't concern apps | - | 2026-11-03 | From 2026-11-13 under G.S.R. 843(E)(b) (13 or 14 Nov 2026: Gazette dated 13 Nov 2025, uploaded and signed 14 Nov). Concerns only companies registering as Consent Managers. |
| s.6(10) | Proving notice and consent | Covered | consent-record-missing | 2026-11-03 | Consent kept only in the browser is a check-on-your-own item. Terms of service acceptance is not covered by this section. |
| s.7 | Certain legitimate uses | Partly covered | trackers-before-consent | 2026-11-03 | Analytics and ads are not listed uses. Clauses (b) to (i) are state, legal, court, emergency, disaster and employment uses. |
| s.8(1) | Business responsible, including for its processors | Can't tell from code | cross-border-transfers | 2026-11-03 |  |
| s.8(2) | Processors only under a valid contract | Can't tell from code | cross-border-transfers | 2026-11-03 |  |
| s.8(3) | Accurate data where it drives decisions or is shared | Partly covered | data-rights-request-missing | 2026-11-03 | The correction route is checked; accuracy itself can't be seen in code. |
| s.8(4) | Technical and organisational measures | Can't tell from code | breach-readiness | 2026-11-03 | General duty; its specific parts are mapped in their own rows. |
| s.8(5) | Reasonable security safeguards | Partly covered | open-database-rules, secrets-in-client, prod-logging-personal-data, breach-readiness | 2026-11-03 | Minimum safeguards listed in r.6(1); rules cite r.6. |
| s.8(6) | Breach intimation to the Board and users | Can't tell from code | breach-readiness | 2026-11-03 | Manner set by r.7. |
| s.8(7) | Erase on withdrawal or when the purpose ends, processors too | Partly covered | consent-withdrawal-missing, retention-periods-unset, cross-border-transfers | 2026-11-03 |  |
| s.8(8) | When a purpose counts as no longer served | Can't tell from code | retention-periods-unset | 2026-11-03 | Periods set in r.8 and the Third Schedule. |
| s.8(9) | Publish a contact for questions about processing | Covered | privacy-contact-missing | 2026-11-03 | Manner set by r.9. |
| s.8(10) | Grievance redressal mechanism | Covered | grievance-officer-missing | 2026-11-03 | Response period in r.14(3). |
| s.8(11) | Meaning of not approaching the business | Doesn't concern apps | - | 2026-11-03 | Clarifies s.8(8); used by retention-periods-unset. |
| s.9(1) | Verifiable consent of a parent or lawful guardian | Covered | age-handling, parental-consent-unverified | 2026-11-03 | Manner set by r.10 and r.11. |
| s.9(2) | No processing harmful to a child's well-being | Partly covered | age-handling | 2026-11-03 | Only ads and tracking for children are checked. |
| s.9(3) | No tracking, monitoring or targeted ads for children | Covered | age-handling | 2026-11-03 |  |
| s.9(4) | Exempt classes and purposes for children | Doesn't concern apps | - | 2026-11-03 | Exemptions listed in r.12 and the Fourth Schedule; reflected in the parental-consent-unverified exceptions. |
| s.9(5) | Government may set a higher exempt age | Doesn't concern apps | - | 2026-11-03 | Government power for notified businesses. |
| s.10 | Significant Data Fiduciary duties | Can't tell from code | significant-data-fiduciary | 2026-11-03 | Only for businesses the Government notifies. |
| s.11 | Right to access information about personal data | Partly covered | data-rights-request-missing | 2026-11-03 | The published way to ask is checked; what a reply contains can't be seen in code. |
| s.12 | Right to correction and erasure | Covered | account-deletion-missing, data-rights-request-missing | 2026-11-03 |  |
| s.13 | Right of grievance redressal | Covered | grievance-officer-missing | 2026-11-03 | Response period in r.14(3). |
| s.14 | Right to nominate | Partly covered | data-rights-request-missing | 2026-11-03 | The fix names nomination; the process can't be seen in code. |
| s.15 | Duties of users | Doesn't concern apps | - | 2026-11-03 | Duties of the people whose data it is, not of the service. |
| s.16 | Transfer of personal data outside India | Can't tell from code | cross-border-transfers | 2026-11-03 | Depends on Government notifications and other laws. |
| s.17 | Exemptions | Doesn't concern apps | - | 2026-11-03 | Exemptions (legal claims, courts, offences, contracts for people outside India, mergers, loan defaults, notified state bodies, research, notified businesses). They decide whether duties apply; nothing to find in code. The s.17(1)(d) carve-out (people outside India, under a contract with a foreign party) and the s.17(3) notified-business exemption are written into the exceptions of the checks they affect. |
| s.18 | Board established | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.19 | Board composition and members | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.20 | Members' pay and term | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.21 | Members' disqualifications | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.22 | Resignation and vacancies | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.23 | Board proceedings | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.24 | Board officers and staff | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.25 | Members and staff are public servants | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.26 | Chairperson's powers | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.27 | Board's powers and functions | Doesn't concern apps | - | 2026-11-03 | s.27(1)(d) from 2026-11-13 (13 or 14 Nov 2026: Gazette dated 13 Nov 2025, uploaded and signed 14 Nov); the rest from 2027-05-13. |
| s.28 | Board's procedure | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. |
| s.29 | Appeal to the Appellate Tribunal | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. |
| s.30 | Tribunal orders executable as decrees | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. |
| s.31 | Mediation | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. |
| s.32 | Voluntary undertaking | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. |
| s.33 | Penalties | Doesn't concern apps | - | 2026-11-03 | The Board weighs gravity, duration, gain, mitigation and impact; Schedule amounts are maximums. From 2027-05-13. |
| s.34 | Penalties go to the Consolidated Fund | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. |
| s.35 | Protection for action in good faith | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.36 | Government may call for information | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13; procedure in r.23. |
| s.37 | Blocking after repeated penalties | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. Government and intermediary duty. |
| s.38 | Relation to other laws | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.39 | Civil courts barred | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.40 | Power to make rules | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.41 | Laying rules before Parliament | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.42 | Power to amend the Schedule | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.43 | Removing difficulties | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| s.44 | Amendments to other Acts | Doesn't concern apps | - | 2026-11-03 | s.44(1) and (3) in force 2025-11-13; s.44(2), which removes IT Act s.43A, from 2027-05-13. |
| Schedule item 1 | Maximum penalty: security safeguards (s.8(5)) | Doesn't concern apps | - | 2026-11-03 | Up to 250 crore rupees, a maximum. |
| Schedule item 2 | Maximum penalty: breach intimation (s.8(6)) | Doesn't concern apps | - | 2026-11-03 | Up to 200 crore rupees, a maximum. |
| Schedule item 3 | Maximum penalty: children (s.9) | Doesn't concern apps | - | 2026-11-03 | Up to 200 crore rupees, a maximum. |
| Schedule item 4 | Maximum penalty: Significant Data Fiduciary (s.10) | Doesn't concern apps | - | 2026-11-03 | Up to 150 crore rupees, a maximum. |
| Schedule item 5 | Maximum penalty: users' duties (s.15) | Doesn't concern apps | - | 2026-11-03 | Up to 10,000 rupees, a maximum; applies to users. |
| Schedule item 6 | Maximum penalty: breaking a voluntary undertaking | Doesn't concern apps | - | 2026-11-03 | Up to the amount for the original breach. |
| Schedule item 7 | Maximum penalty: any other breach | Doesn't concern apps | - | 2026-11-03 | Up to 50 crore rupees, a maximum. |
| r.1 | Short title and commencement | Doesn't concern apps | - | 2026-11-03 | r.1, r.2 and r.17 to r.21 in force 2025-11-13; r.4 from 2026-11-13 (13 or 14 Nov 2026: Gazette dated 13 Nov 2025, uploaded and signed 14 Nov); r.3, r.5 to r.16, r.22 and r.23 from 2027-05-13 (13 or 14 May 2027: Gazette dated 13 Nov 2025, uploaded and signed 14 Nov). |
| r.2 | Definitions | Doesn't concern apps | - | 2026-11-03 | A user account includes profiles, handles, email address and mobile number. |
| r.3 | What the notice must contain | Covered | privacy-notice-incomplete | 2026-11-03 |  |
| r.4 | Consent Manager registration and duties | Doesn't concern apps | - | 2026-11-03 | From 2026-11-13 (13 or 14 Nov 2026: Gazette dated 13 Nov 2025, uploaded and signed 14 Nov). Concerns only companies registering as Consent Managers. |
| r.5 | State processing for subsidies, benefits and licences | Doesn't concern apps | - | 2026-11-03 | State bodies only. |
| r.6 | Reasonable security safeguards | Partly covered | open-database-rules, secrets-in-client, prod-logging-personal-data, log-retention-too-short, breach-readiness, cross-border-transfers | 2026-11-03 | Access control, masking and log retention are checked in code; encryption at rest, monitoring, backups and contracts are check-on-your-own items. |
| r.7 | Breach intimation to users and the Board | Can't tell from code | breach-readiness | 2026-11-03 |  |
| r.8(1) | Erasure after the Third Schedule period | Can't tell from code | retention-periods-unset | 2026-11-03 | Large platforms only. |
| r.8(2) | Warning 48 hours before erasure | Can't tell from code | retention-periods-unset | 2026-11-03 | Large platforms only. |
| r.8(3) | Keep processing logs for at least one year | Partly covered | log-retention-too-short | 2026-11-03 | Checked only where the repo sets a retention period. |
| r.9 | Publish a contact for questions about processing | Covered | privacy-contact-missing | 2026-11-03 | Including it in every reply to a rights request can't be seen in code. |
| r.10 | Verifiable consent of a parent | Covered | parental-consent-unverified | 2026-11-03 |  |
| r.11 | Consent of the guardian of a person with disability | Covered | parental-consent-unverified | 2026-11-03 |  |
| r.12 | Children exemptions | Doesn't concern apps | - | 2026-11-03 | Exemptions listed in the Fourth Schedule; reflected in the parental-consent-unverified exceptions. |
| r.13 | Significant Data Fiduciary duties | Can't tell from code | significant-data-fiduciary, cross-border-transfers | 2026-11-03 | r.13(4) local storage of listed data is grouped with cross-border-transfers. |
| r.14 | Publishing how to use rights and the grievance period | Covered | data-rights-request-missing, grievance-officer-missing | 2026-11-03 |  |
| r.15 | Transfer outside India | Can't tell from code | cross-border-transfers | 2026-11-03 | Depends on Government orders. |
| r.16 | Research, archiving and statistics exemption | Doesn't concern apps | - | 2026-11-03 | Exemption. |
| r.17 | Appointing the Chairperson and Members | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| r.18 | Members' pay and terms | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| r.19 | Board meetings and inquiry time | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| r.20 | Board as a digital office | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| r.21 | Board officers and staff | Doesn't concern apps | - | 2026-11-03 | In force 2025-11-13. |
| r.22 | Appeal to the Appellate Tribunal | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. |
| r.23 | Government calls for information | Doesn't concern apps | - | 2026-11-03 | From 2027-05-13. The Government may tell a business not to disclose the request. |
| First Schedule Part A | Consent Manager registration conditions | Doesn't concern apps | - | 2026-11-03 | Consent Managers only. |
| First Schedule Part B | Consent Manager obligations | Doesn't concern apps | - | 2026-11-03 | Consent Managers only. |
| Second Schedule | Standards for State processing and research | Doesn't concern apps | - | 2026-11-03 | State bodies and research only. |
| Third Schedule | Erasure periods for large platforms | Can't tell from code | retention-periods-unset | 2026-11-03 | E-commerce and social media platforms with 2 crore or more registered users in India, online gaming with 50 lakh or more: 3 years. A seller on a marketplace is not an e-commerce entity here. |
| Fourth Schedule Part A | Exempt classes for children's data | Doesn't concern apps | - | 2026-11-03 | Health services, schools, crèches and child transport; reflected in the parental-consent-unverified exceptions. |
| Fourth Schedule Part B | Exempt purposes for children's data | Doesn't concern apps | - | 2026-11-03 | Includes an email-only account, real-time location for safety and blocking harmful content; reflected in the parental-consent-unverified exceptions. |
| Fifth Schedule | Members' terms of service | Doesn't concern apps | - | 2026-11-03 | Board only. |
| Sixth Schedule | Board staff terms of service | Doesn't concern apps | - | 2026-11-03 | Board only. |
| Seventh Schedule | Purposes for Government information requests | Doesn't concern apps | - | 2026-11-03 | Lists the purposes behind r.8(3) and r.23. |
