# CERT-In Directions 2022 under s.70B(6) of the IT Act
- source-id: cert-in-2022
- walk: full
- url: https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- read-on: 2026-11-03

Directions No. 20(3)/2022-CERT-In of 28 April 2022, read with the official FAQs and the one extension notice. All three texts are on cert-in.org.in and are the only documents listed on CERT-In's page for these Directions (https://www.cert-in.org.in/Directions70B.jsp, "Last Updated On November 03, 2026"); no amendment was found.

FAQs, dated May 2022 in the document (released 18 May 2022 per law-firm summaries, secondary): https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf. The FAQ says it is not a legal document and changes nothing in the Directions; where it reads them down (logs stored abroad, Q35), the rules state both.
Extension of 27 June 2022 (MSMEs, and validated names and addresses under (v)(a) and (f), both from 25 September 2022): https://www.cert-in.org.in/PDF/CERT-In_directions_extension_MSMEs_and_validation_27.06.2022.pdf

Start date. The Directions become effective "after 60 days" from issue on 28 April 2022; neither they nor FAQ Q44 give the day. Counting 60 days gives 27 June 2022, the date law-firm and policy-tracker summaries give (secondary: https://digitalpolicyalert.org/event/4676-entry-into-force-with-grace-period-of-cert-ins-information-security-practices-directive-including-cybersecurity-measures). Reading it as 60 full days that must pass first gives 28 June 2022, and the extension notice, dated 27 June 2022, still says the Directions are "to become effective". Rules use 2022-06-27 with secondary: yes.

Courts. SnTHostings challenged directions (iv) and (v) in the Delhi High Court and was allowed to withdraw the petition on 14 March 2024 (secondary: https://www.internetfreedom.in/snthostings-withdraw-petition-legality-of-2022-directions/). No other challenge was found.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| Preamble | CERT-In's appointment and functions (s.70B(1), (4)), CERT-In Rules 2013, power to direct (s.70B(6)), reasons | Doesn't concern apps | - | 2026-11-03 | Recitals. Who is bound is set in each direction. |
| (i) | Sync all ICT system clocks with NIC or NPL NTP servers, or ones traceable to them | Can't tell from code | breach-readiness | 2026-11-03 | Custom time sources in server config are noted. The direction lets multi-region setups use another accurate source that does not deviate from NIC and NPL; FAQ Q40 extends that to any organisation. |
| (ii) | Report Annexure I incidents to CERT-In within 6 hours of noticing | Can't tell from code | breach-readiness | 2026-11-03 | Reporting happens outside the code; the incident plan is a check-on-your-own item. Email, phone and fax are given. |
| (iii) | Act, inform or assist when CERT-In orders, in the format and time set; name a Point of Contact | Can't tell from code | breach-readiness | 2026-11-03 | Applies to service providers, intermediaries, data centres, body corporate and government bodies. |
| (iv) | Enable logs of all ICT systems, keep them 180 days within India, give them to CERT-In | Partly covered | log-retention-too-short, breach-readiness | 2026-11-03 | Retention set too short, and logging off for a whole server or service, are checked in config. No retention set, logs held only abroad, audit logging off and handing logs over are check-on-your-own items. FAQ Q35 lets copies sit abroad; Q36 says Indian jurisdiction. |
| (v) | Data centres, VPS, cloud and VPN providers: keep 7 kinds of customer details for 5 years after the registration ends | Can't tell from code | provider-customer-records | 2026-11-03 | (a) and (f) from 25 Sep 2022 (extension). Company VPNs for staff are out (FAQ Q34). The sign-up schema can show missing fields, but not validation or retention. |
| (vi) | Virtual asset service providers, exchanges and custodian wallets: KYC and transaction records for 5 years | Can't tell from code | provider-customer-records | 2026-11-03 | Records must let each transaction be rebuilt. |
| Closing para, terms | Terms take their meaning from the IT Act and the CERT-In Rules 2013 | Doesn't concern apps | - | 2026-11-03 | Definitions. |
| Closing para, furnishing | Furnish the details CERT-In calls for after an incident; non-compliance may be punished under s.70B(7) | Can't tell from code | breach-readiness | 2026-11-03 | s.70B(7), quoted in the FAQ introduction: up to one year, a fine up to one lakh rupees, or both. |
| Closing para, start | Effective after 60 days from issue | Doesn't concern apps | - | 2026-11-03 | 27 or 28 June 2022; see the header. |
| Annexure I | 20 types of cyber security incidents to report | Can't tell from code | breach-readiness | 2026-11-03 | Includes data breach, data leak, unauthorised access, website defacement or injected code, malware, DoS, phishing, malicious and fake mobile apps, and attacks on apps, payments, cloud and AI systems. Refers to r.12(1)(a) of the CERT-In Rules 2013. |
| Annexure II | Point of Contact details, sent to info@cert-in.org.in and kept current | Can't tell from code | breach-readiness | 2026-11-03 | |
| Annexure III | KYC documents for virtual asset providers | Can't tell from code | provider-customer-records | 2026-11-03 | Documents accepted under RBI KYC Directions 2016, the SEBI circular of 24 Apr 2020 or DoT self-KYC of 21 Sep 2021; RBI due diligence for business customers. |
| Extension, MSMEs | Directions effective for MSMEs from 25 Sep 2022 | Doesn't concern apps | - | 2026-11-03 | Date change only, now past; in the rules' references. MSMEs as classified by S.O. 1702(E) of 1 June 2020. |
| Extension, (v)(a) and (f) | Validated names, addresses and contact numbers by hosting and VPN providers from 25 Sep 2022 | Can't tell from code | provider-customer-records | 2026-11-03 | Date change only, now past. |
| FAQ intro, Q1-Q6 | Background, CERT-In's role, meaning of cyber security incident | Doesn't concern apps | - | 2026-11-03 | Q3 defines a cyber security incident as a real or suspected adverse event. |
| FAQ Q7, Q11, Q25-Q29 | Who the Directions bind | Doesn't concern apps | - | 2026-11-03 | Scope only, used in the checks' exceptions and the rules' applies-to: organisations of any kind, Indian or foreign, for cyber incidents (Q26-Q28). Individual citizens are not covered (Q7), but a sole proprietorship is a body corporate (Q25). |
| FAQ Q8, Q22 | IT Act overrides other laws; reporting overrides confidentiality clauses in contracts | Doesn't concern apps | - | 2026-11-03 | |
| FAQ Q9-Q10, Q12-Q14, Q24, Q30, Q31 | Reporting: incident types, intermediaries, method, who reports, the 6-hour clock, partial reports, data on a third party's systems | Can't tell from code | breach-readiness | 2026-11-03 | Q13 and Q31: every entity that notices must report, including when its data sits on a third party's systems; the duty cannot be passed on by contract. Q10: intermediaries should also report serious incidents not listed. Q30: send what is known within 6 hours, and it names the incidents for the 6-hour clock: severe ones (such as DoS, intrusion, ransomware) on public information infrastructure, data breaches or leaks, large-scale or frequent intrusions, and incidents affecting human safety. |
| FAQ Q15 | Reporting a vulnerability on its own is voluntary | Doesn't concern apps | - | 2026-11-03 | |
| FAQ Q16-Q21 | Disclosure, chain of custody, aims, privacy, benefits | Doesn't concern apps | - | 2026-11-03 | Q20: no standing requests for data. |
| FAQ Q23 | Penalties for non-compliance | Doesn't concern apps | - | 2026-11-03 | s.70B(7); to be used reasonably, for deliberate non-compliance. |
| FAQ Q32 | Confidentiality of customer data, and personal data of foreign data subjects in logs | Doesn't concern apps | - | 2026-11-03 | No new duty: existing confidentiality duties stay unchanged. Personal data in logs is handled by prod-logging-personal-data under other rules. |
| FAQ Q33-Q34 | Ownership pattern of customers; company VPNs are out | Can't tell from code | provider-customer-records | 2026-11-03 | |
| FAQ Q35-Q38 | Logs: storage abroad, foreign providers, kinds of logs, who may ask | Partly covered | log-retention-too-short, breach-readiness | 2026-11-03 | Q35 allows copies abroad if produced in reasonable time; Q36 says services for users in India keep logs in Indian jurisdiction. Q37: successful and failed events. Q38: a CERT-In officer of Deputy Secretary rank or above. |
| FAQ Q39-Q43 | Clock sync: why, other sources, cloud time, NIC and NPL server names | Can't tell from code | breach-readiness | 2026-11-03 | IST not required, but record the time zone (Q40); cloud-native time is fine (Q42). |
| FAQ Q44 | Start: 60 days after issue | Doesn't concern apps | - | 2026-11-03 | |
| FAQ Annexure I | Explanation of each incident type | Can't tell from code | breach-readiness | 2026-11-03 | |
