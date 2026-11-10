# Coverage map

This is the index of the coverage map. Each source gets one file, `coverage/<source-id>.md`, with one row per section of that source. A source that only one or a few rules cite has no file: it is listed at the end as not walked.

Statuses: `Covered` means a check finds the mistake; `Partly covered` means a check finds part of it; `Can't tell from code` means the item is grouped into a check that reports `Maybe: check on your own`; `Doesn't concern apps` means the section has nothing a developer could get wrong in an app or site; `Not done yet` means nobody has decided the section yet.

| Source | File | Walk |
|---|---|---|
| DPDP Act 2023 and Rules 2025 | `coverage/dpdp.md` | full |
| IT Rules 2021 (intermediaries) | `coverage/it-rules-2021.md` | full |
| CERT-In Directions 2022 | `coverage/cert-in-2022.md` | full |
| Consumer Protection (E-Commerce) Rules 2020 | `coverage/ecommerce-rules-2020.md` | full |
| Dark Patterns Guidelines 2023 | `coverage/dark-patterns-2023.md` | full |
| Apple App Review Guidelines | `coverage/apple-review-guidelines.md` | full |
| Google Play Developer Program Policy | `coverage/google-play-policy.md` | full |
| General Data Protection Regulation | `coverage/gdpr.md` | targeted |
| ePrivacy Directive 2002/58/EC | `coverage/eprivacy.md` | targeted |
| UK GDPR and PECR | `coverage/uk-gdpr-pecr.md` | targeted |
| European Accessibility Act | `coverage/eaa.md` | targeted |
| COPPA Rule | `coverage/coppa.md` | targeted |
| CAN-SPAM Act | `coverage/can-spam.md` | targeted |
| California Invasion of Privacy Act (CIPA) | `coverage/cipa.md` | targeted |
| California auto-renewal law | `coverage/ca-auto-renewal.md` | targeted |
| California Consumer Privacy Act (CCPA) | `coverage/ccpa.md` | targeted |
| DMCA s.512 | `coverage/dmca.md` | targeted |
| RBI E-mandate Framework 2026 (recurring payments) | `coverage/rbi-recurring-payments.md` | targeted |
| Apple Human Interface Guidelines: Privacy | `coverage/apple-hig.md` | targeted |
| Android developer docs: permissions and security risks | `coverage/android-docs.md` | targeted |
| OWASP: Top 10, API Security Top 10, MASVS and cheat sheets | `coverage/owasp.md` | targeted |
| WCAG 2.2 | `coverage/wcag.md` | targeted |
| Open-source licence texts (GNU GPL FAQ, AGPL) | `coverage/oss-licences.md` | targeted |
| RBI (Digital Lending) Directions 2025 (`rbi-digital-lending`) | - | single rule, not walked |
| FIU-IND AML and CFT Guidelines for VDA service providers (`fiu-ind-vda`) | - | single rule, not walked |
| Medical devices notified as drugs, S.O. 648(E) of 2020 (`medical-devices-india`) | - | single rule, not walked |
| California Online Privacy Protection Act, Bus. & Prof. Code s.22575 (`caloppa`) | - | one section (two records), not walked |
| FTC staff post on changing terms, February 2024 (`ftc-act`) | - | single rule, not walked |
| LG München I ruling on Google Fonts, 20 January 2022 (`lg-muenchen-2022`) | - | single rule, not walked |
| Information Technology Act 2000, s.10A (`it-act-2000`) | - | single rule, not walked |
| Apple App Privacy details in App Store Connect (`apple-app-privacy`) | - | single rule, not walked |
| Apple developer docs on logging (`apple-docs`) | - | single rule, not walked |
| Vendor docs for Stripe, Supabase and Firebase (`vendor-docs`) | - | seed rules, not walked |

A targeted walk covers only the sections the checks rely on, so the whole source counts as partly covered; its other sections are absent or `Not done yet`.

The skill never loads this file or `coverage/` during a run. A report states coverage from each rules file's `coverage-summary` line.
