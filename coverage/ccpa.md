# California Consumer Privacy Act, Civil Code s.1798.100-1798.199.100, and CCPA Regulations
- source-id: ccpa
- walk: targeted
- url: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.100
- read-on: 2026-11-03

Targeted walk: only the sections the checks rely on, plus ones read along the way. Statute read in the CalPrivacy (CPPA) copy "effective 01/01/2026" (https://cppa.ca.gov/pdf/20260101_ccpa_statute.pdf) and checked for the cited sections on leginfo in a browser; regulations read in the CPPA copy effective 1 January 2026 (https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf, which the regulations page labels "CCPA Regulations").

Thresholds (s.1798.140(d)). A for-profit business doing business in California is covered if it meets one of: annual gross revenue over $25,000,000 as adjusted, which CalPrivacy set at $26,625,000 from 1 January 2025 (https://cppa.ca.gov/regulations/cpi_adjustment.html, "Current" on 2026-11-03; adjusted every odd-numbered year under s.1798.199.95(d), so the next change is due 1 January 2027); buying, selling or sharing personal information of 100,000 or more consumers or households; or half or more of revenue from selling or sharing it. Fines from the same page: up to $2,663 per violation or $7,988 per intentional violation or one involving consumers known to be under 16.

Opt-out of sale or sharing. s.1798.120 gives the right to opt out of sale or sharing ("sharing" means for cross-context behavioural advertising, s.1798.140(ah)). s.1798.135(a) needs a "Do Not Sell or Share My Personal Information" link (and a "Limit the Use of My Sensitive Personal Information" link, or one combined link); under s.1798.135(b) a business may instead honour an opt-out preference signal. Regulation s.7025 makes a business that sells or shares treat a valid signal, in a commonly used format "such as an HTTP header field or JavaScript object", as an opt-out for that browser or device. The regulations do not name Global Privacy Control; the check looks for it (`navigator.globalPrivacyControl`, `Sec-GPC`) as the common signal. The check opt-out-signal-ignored covers web pages with third-party ad or retargeting tags only, confirms only when both the signal handling and the link are missing, and asks the threshold question.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| s.1798.100(a) | Notice at or before collection: categories, purposes, sale or sharing, retention | Partly covered | privacy-policy-missing | 2026-11-03 | Missing notice only. |
| s.1798.105 | Right to delete | Not done yet | - | | The text sets no in-app deletion duty; request routes are the s.1798.130 row. |
| s.1798.106 | Right to correct | Partly covered | data-rights-request-missing | 2026-11-03 | |
| s.1798.110 | Right to know | Partly covered | data-rights-request-missing | 2026-11-03 | |
| s.1798.120 | Right to opt out of sale or sharing | Partly covered | opt-out-signal-ignored | 2026-11-03 | Ad and retargeting tags on websites only. |
| s.1798.130(a)(1)-(2) | Two or more request methods (email for online-only businesses), answer within 45 days | Partly covered | data-rights-request-missing | 2026-11-03 | Only whether request methods are published; the 45 days are outside the code. |
| s.1798.130(a)(5) | Privacy policy contents, updated every 12 months | Partly covered | privacy-notice-incomplete | 2026-11-04 | Contents only; the 12-month update is not checked. |
| s.1798.135 | Do Not Sell or Share link, or honour opt-out preference signals | Partly covered | opt-out-signal-ignored | 2026-11-03 | The "Limit the Use of My Sensitive Personal Information" link is not checked. |
| s.1798.140(d) | Definition of business and thresholds | Doesn't concern apps | - | 2026-11-03 | Scope, stated in the rules. |
| s.1798.199.95(d) | Inflation adjustment of thresholds every odd year | Doesn't concern apps | - | 2026-11-03 | |
| s.1798.140(ah) | Definition of sharing: for cross-context behavioural advertising | Doesn't concern apps | - | 2026-11-03 | Definition; why the check is limited to ad tags. |
| Regs s.7025 | Opt-out preference signals | Partly covered | opt-out-signal-ignored | 2026-11-03 | Web signal handling only; profiles and offline data are outside the code. |
