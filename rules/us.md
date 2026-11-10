# United States
- coverage-summary: targeted walks read on 2026-11-03: COPPA Rule as amended in 2025, CAN-SPAM Act, California Penal Code s.631 and s.637.2 (with SB 690 of 2026), California auto-renewal law (Bus. & Prof. Code 17600-17606), CCPA (with its opt-out preference signal rule) and DMCA s.512; only the sections the checks rely on are covered. CalOPPA s.22575 and the FTC terms-change post: single rules.

## coppa-age-handling
- check: age-handling
- source-id: coppa
- applies-to: US
- strength: Law
- reference: COPPA Rule, 16 CFR Part 312; FTC FAQ A.2 (child-directed services, or actual knowledge of under-13 users), A.12 (no duty to ask visitors' age), B.2 (civil penalties up to $53,088 per violation, a maximum). Dates from 90 FR 16918, not the FAQ: Rule in force 21 April 2000; amended Rule effective 23 June 2025, compliance by 22 April 2026
- rule-started: 2000-04-21
- status: In force
- verified-on: 2026-11-03
- source: https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- secondary: yes

## can-spam-marketing-email-footer
- check: marketing-email-footer
- source-id: can-spam
- applies-to: US
- strength: Law
- reference: CAN-SPAM Act, 15 U.S.C. 7704(a)(3)-(5): a working opt-out, honoured within 10 business days, a clear opt-out notice and a valid postal address; transactional or relationship messages are not commercial (7702(2)(B), another page). FTC guide: up to $53,088 per email, a maximum (16 CFR 1.98(d)); no 2026 adjustment (91 FR 58446). In force 1 January 2004
- rule-started: 2004-01-01
- status: In force
- verified-on: 2026-11-03
- source: https://www.govinfo.gov/content/pkg/USCODE-2024-title15/html/USCODE-2024-title15-chap103-sec7704.htm
- secondary: yes

## cipa-session-replay-consent
- check: session-replay-consent
- source-id: cipa
- applies-to: US (California)
- strength: Law
- reference: Cal. Penal Code s.631 (reading a communication in transit without all parties' consent); s.637.2 (civil claim: greater of $5,000 per violation or 3x damages). SB 690 (Stats. 2026, ch. 976; in effect 1 January 2027, Cal. Const. art. IV s.8(c)) leaves s.631 and that claim unchanged; it limits only pen-register claims (s.638.51). Courts are split on replay. s.631 text effective 1 January 2023
- rule-started: before 2023-01-01
- status: In force
- verified-on: 2026-11-03
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=631
- secondary: no

## ca-bpc-17602-renewal-terms-checkout
- check: renewal-terms-checkout
- source-id: ca-auto-renewal
- applies-to: US (California)
- strength: Law
- reference: Cal. Bus. & Prof. Code s.17602, for goods or services: renewal terms clear and conspicuous near the consent request, express consent, an acknowledgment, cancelling online if bought online, notice of price changes 7-30 days ahead; text for contracts from 1 July 2025 (s.17602(j)). s.17603 makes unconsented goods or products a gift; it does not name services
- rule-started: 2025-07-01
- status: In force
- verified-on: 2026-11-03
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17602
- secondary: no

## ccpa-1798-100-privacy-policy-missing
- check: privacy-policy-missing
- source-id: ccpa
- applies-to: US (California, businesses over a CCPA threshold)
- strength: Law
- reference: Cal. Civ. Code s.1798.100(a): at or before collection, tell consumers the categories of data, purposes, whether it is sold or shared, and how long it is kept. Only businesses in s.1798.140(d): revenue over $26,625,000 (2025-26 figure, cppa.ca.gov; adjusted 1 January 2027), or buying, selling or sharing data of 100,000 consumers or households, or half of revenue from that. Operative 1 January 2023
- rule-started: 2023-01-01
- status: In force
- verified-on: 2026-11-03
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.100
- secondary: yes

## ccpa-1798-130-privacy-notice-incomplete
- check: privacy-notice-incomplete
- source-id: ccpa
- applies-to: US (California, businesses over a CCPA threshold)
- strength: Law
- reference: Cal. Civ. Code s.1798.130(a)(5): the online privacy policy must describe consumer rights and two or more request methods, and list categories of data collected in the past 12 months, sources, purposes, third-party recipients, and what was sold, shared or disclosed (or none), updated every 12 months. Thresholds: see ccpa-1798-100-privacy-policy-missing. Text as amended effective 1 January 2026
- rule-started: before 2026-01-01
- status: In force
- verified-on: 2026-11-04
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.130
- secondary: yes

## ccpa-1798-130-data-rights-request-missing
- check: data-rights-request-missing
- source-id: ccpa
- applies-to: US (California, businesses over a CCPA threshold)
- strength: Law
- reference: Cal. Civ. Code s.1798.130(a)(1): two or more ways to ask to know, delete or correct, with a toll-free number; an online-only business with a direct relationship needs only an email address, plus its website if it has one. Answer within 45 days. Thresholds as in s.1798.140(d), revenue figure on cppa.ca.gov. Current text effective 1 January 2026; start day not on the page
- rule-started: before 2026-01-01
- status: In force
- verified-on: 2026-11-03
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.130
- secondary: yes

## ccpa-1798-135-opt-out-signal-ignored
- check: opt-out-signal-ignored
- source-id: ccpa
- applies-to: US (California, businesses over a CCPA threshold that sell or share personal information, as with ad or retargeting tags)
- strength: Law
- reference: Cal. Civ. Code s.1798.120 (opt out of sale or sharing), s.1798.140(ah) (sharing: for cross-context behavioural ads), s.1798.135(a)-(b): a "Do Not Sell or Share My Personal Information" link, or honour opt-out preference signals; CCPA Regs s.7025 (cppa.ca.gov): treat a valid signal, such as an HTTP header, as an opt-out. Thresholds and regs on other pages. s.1798.135 text effective 1 January 2025
- rule-started: before 2025-01-01
- status: In force
- verified-on: 2026-11-03
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.135
- secondary: yes

## caloppa-22575-privacy-policy-missing
- check: privacy-policy-missing
- source-id: caloppa
- applies-to: US (California): operators of commercial websites or online services that collect personal information from California residents; no revenue threshold
- strength: Law
- reference: Cal. Bus. & Prof. Code s.22575 (CalOPPA): post a privacy policy conspicuously, naming the data collected and who it is shared with, how changes are notified, its effective date, its response to Do Not Track signals if it tracks users across sites, and whether others do. A violation arises only if it is not posted within 30 days of notice. Current text effective 1 January 2014
- rule-started: before 2014-01-01
- status: In force
- verified-on: 2026-11-03
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22575
- secondary: no

## caloppa-22575-privacy-notice-incomplete
- check: privacy-notice-incomplete
- source-id: caloppa
- applies-to: US (California): operators of commercial websites or online services that collect personal information from California residents; no revenue threshold
- strength: Law
- reference: Cal. Bus. & Prof. Code s.22575(b) (CalOPPA): the posted policy must name the categories of data collected and of third parties it is shared with, any process to review and change data, how material changes are notified, its effective date, its response to Do Not Track signals if it tracks users across sites, and whether others may do so. Current text effective 1 January 2014
- rule-started: before 2014-01-01
- status: In force
- verified-on: 2026-11-04
- source: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22575
- secondary: no

## dmca-512-uploads-takedown-process
- check: uploads-takedown-process
- source-id: dmca
- applies-to: US
- strength: Law
- reference: 17 U.S.C. 512(c)(2): the safe harbour for user-stored content needs an agent listed on the site and with the Copyright Office ($6, lapses after 3 years unless renewed: 37 CFR 201.3, 201.38). The risk is losing it: statutory damages up to $150,000 per work need willful infringement (s.504(c)) and timely registration (s.412). In force 28 October 1998
- rule-started: 1998-10-28
- status: In force
- verified-on: 2026-11-03
- source: https://www.govinfo.gov/content/pkg/USCODE-2024-title17/html/USCODE-2024-title17-chap5-sec512.htm
- secondary: no

## ftc-terms-change-notice
- check: terms-change-notice
- source-id: ftc-act
- applies-to: US
- strength: Court or regulator
- reference: FTC staff post, 13 February 2024: quietly making data practices more permissive through a retroactive change to terms or privacy policy could be unfair or deceptive (FTC Act s.5; Gateway Learning 2004, 1Health 2023)
- rule-started: 2024-02-13
- status: In force
- verified-on: 2026-11-03
- source: https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/02/ai-other-companies-quietly-changing-your-terms-service-could-be-unfair-or-deceptive
- secondary: no
