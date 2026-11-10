# Apple Human Interface Guidelines: Privacy
- source-id: apple-hig
- walk: targeted
- url: https://developer.apple.com/design/human-interface-guidelines/privacy
- read-on: 2026-11-03

Read through the page's own data file (https://developer.apple.com/tutorials/data/design/human-interface-guidelines/privacy.json), because the page renders with scripts. Page change log: last change 21 June 2023. Only the Privacy page was walked.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| Best practices | Ask only for data a feature needs; be transparent; process on device | Partly covered | forced-login-or-permissions | 2026-11-03 | Transparency and on-device processing are not checked. |
| Requesting permission | Ask when a feature needs it; avoid asking at launch | Covered | permission-at-launch | 2026-11-03 |  |
| Requesting permission (purpose strings) | Brief, specific purpose string saying how and why | Covered | permission-purpose-strings | 2026-11-03 |  |
| Pre-alert screens, windows, or views | One button that opens the alert, no "Allow" wording, no cancel | Not done yet | - |  | Custom screens before the system alert are not checked yet. |
| Tracking requests | System alert before tracking; no incentives; no withheld features | Partly covered | forced-login-or-permissions, tracking-without-att | 2026-11-03 | Misleading custom screens around the alert are not checked. |
| Location button | Lightweight location sharing for one action | Not done yet | - |  |  |
| Protecting data | Keychain, no plain-text passwords, passkeys, two-factor sign-in | Not done yet | - |  |  |
| Platform considerations | macOS and visionOS notes | Not done yet | - |  |  |
