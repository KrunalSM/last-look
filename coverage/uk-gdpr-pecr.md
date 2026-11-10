# UK GDPR and the Privacy and Electronic Communications Regulations 2003
- source-id: uk-gdpr-pecr
- walk: targeted
- url: https://www.legislation.gov.uk/uksi/2003/2426/contents
- read-on: 2026-11-03

Targeted walk: only the provisions the checks rely on. Read on legislation.gov.uk in a browser (scripted requests get a bot challenge): PECR reg. 6, Sch. A1, reg. 22 and reg. 23; UK GDPR Art. 13 (https://www.legislation.gov.uk/eur/2016/679/article/13); Data (Use and Access) Act 2025 s.112 (https://www.legislation.gov.uk/ukpga/2025/18/section/112). Commencement stages from GOV.UK (https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement, last updated 12 October 2026).

Data (Use and Access) Act 2025 and cookies. s.112(2) substituted PECR reg. 6 and Sch. 12 (via s.112(4)) inserted Sch. A1, both in force 5 February 2026 (S.I. 2026/82, reg. 2(w) and 2(z13)); legislation.gov.uk lists no outstanding effects. Sch. A1 keeps consent as the rule and adds exceptions: transmission (para 3), strictly necessary, with examples such as security, fraud, faults, login and saved choices (para 4), statistics to improve one's own service or site (para 5), where the data is shared only with someone helping to make those improvements (para 5(1)(c)) and the exemption does not reach data the device emits by itself (para 5(2)), and appearance or functions (para 6), both only with clear information and a free, simple way to object, and emergency location (para 7). Consent may be given through browser settings (para 2(3)). s.114 added a charity soft opt-in to reg. 22, also from 5 February 2026. From 30 September 2026 the Information Commission replaced the Information Commissioner (S.I. 2026/1015, per the Art. 13 page).

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| PECR reg. 6 | No storing or reading of device data except under Sch. A1 | Covered | trackers-before-consent | 2026-11-03 | Text from 5 February 2026. |
| PECR Sch. A1 para 2 | Consent with clear and full information | Covered | trackers-before-consent | 2026-11-03 | |
| PECR Sch. A1 paras 3-4 | Transmission and strictly necessary storage | Covered | trackers-before-consent | 2026-11-03 | In the check's exceptions. |
| PECR Sch. A1 paras 5-6 | Statistics and appearance, with an easy free objection | Partly covered | trackers-before-consent | 2026-11-03 | The check reports these as Maybe; the conditions (sharing only with helpers, no data the device emits itself, objection offered) are in the rule and can't be cleared from code. |
| PECR Sch. A1 para 7 | Location for emergency help | Doesn't concern apps | - | 2026-11-03 | Only for emergency services' contact. |
| PECR reg. 22 | Marketing email: prior consent or soft opt-in | Partly covered | marketing-email-footer | 2026-11-03 | The check finds a missing opt-out; whether consent was given is outside the code. Charity soft opt-in (reg. 22(3A)) from 5 February 2026. |
| PECR reg. 23 | No hidden sender; a valid address for opting out | Partly covered | marketing-email-footer | 2026-11-03 | Only the opt-out link; a hidden sender is not checked. |
| UK GDPR Art. 13 | Information when data is collected | Partly covered | privacy-policy-missing, privacy-notice-incomplete | 2026-11-04 | Missing policy and an incomplete notice; Art. 13(2)(ca) adds complaints to the controller from 19 June 2026. |
