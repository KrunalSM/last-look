# Android developer docs: permissions and security risks
- source-id: android-docs
- walk: targeted
- url: https://developer.android.com/training/permissions/requesting
- read-on: 2026-11-03

Pages read, with their "Last updated" dates: Request runtime permissions (2026-10-28); App permissions best practices, https://developer.android.com/training/permissions/usage-notes (2026-10-28); Log info disclosure, https://developer.android.com/privacy-and-security/risks/log-info-disclosure (2024-09-24); Cleartext communications, https://developer.android.com/privacy-and-security/risks/cleartext-communications (2026-10-23); Hardcoded cryptographic secrets, https://developer.android.com/privacy-and-security/risks/hardcoded-cryptographic-secrets (2024-09-24).

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| Request runtime permissions: Basic principles | Ask in context, when the user starts the feature | Covered | permission-at-launch | 2026-11-03 |  |
| Request runtime permissions: Basic principles | Don't block the user; degrade gracefully when denied | Covered | forced-login-or-permissions | 2026-11-03 |  |
| Request runtime permissions: Workflow | Rationale UI and request flow | Not done yet | - |  |  |
| App permissions best practices: Increased situational context | Prompt only when a feature needs it; not every permission at startup | Covered | permission-at-launch | 2026-11-03 | Same advice as the basic principles, whose rule is cited. |
| App permissions best practices: Know the libraries you're working with | SDKs that add permissions | Not done yet | - |  |  |
| App permissions best practices: Limit background access to location | Background location only for core features | Not done yet | - |  |  |
| Security risks: Log info disclosure | No credentials or personal data in logcat; strip logs in release | Covered | prod-logging-personal-data | 2026-11-03 |  |
| Security risks: Cleartext communications | Encrypted channels; network security config | Covered | cleartext-traffic | 2026-11-03 |  |
| Security risks: Hardcoded cryptographic secrets | Keys in Keystore or KeyChain, not in code or strings.xml | Not done yet | - |  | secrets-in-client finds API keys, not hardcoded crypto keys. |
