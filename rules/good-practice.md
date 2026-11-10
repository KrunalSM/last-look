# Good practice
- coverage-summary: targeted walks of Apple Human Interface Guidelines (Privacy), Android developer docs (permissions, security risks), OWASP (Top 10:2025, API Security Top 10 2023, MASVS, cheat sheets) and WCAG 2.2 (accessibility basics); open-source licence texts (GNU GPL FAQ, AGPL) targeted for copyleft source duties; vendor docs as seed rules.

## android-permissions-in-context
- check: permission-at-launch
- source-id: android-docs
- applies-to: Android apps
- strength: Good practice
- reference: Android developer docs, Request runtime permissions: ask in context, when the user starts the feature that needs it
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.android.com/training/permissions/requesting
- secondary: no

## apple-hig-permissions-in-context
- check: permission-at-launch
- source-id: apple-hig
- applies-to: iOS apps
- strength: Good practice
- reference: Apple Human Interface Guidelines, Privacy: wait until people use the feature, and avoid asking at launch unless the app can't work without it
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.apple.com/design/human-interface-guidelines/privacy
- secondary: no

## apple-hig-purpose-strings
- check: permission-purpose-strings
- source-id: apple-hig
- applies-to: iOS apps
- strength: Good practice
- reference: Apple Human Interface Guidelines, Privacy: a purpose string is a brief, complete, specific sentence saying how and why the app uses the data
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.apple.com/design/human-interface-guidelines/privacy
- secondary: no

## android-log-info-disclosure
- check: prod-logging-personal-data
- source-id: android-docs
- applies-to: Android apps
- strength: Good practice
- reference: Android security guidance, Log info disclosure: don't log credentials or personal data to logcat; strip logs from release builds with R8
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.android.com/privacy-and-security/risks/log-info-disclosure
- secondary: no

## apple-logging-privacy
- check: prod-logging-personal-data
- source-id: apple-docs
- applies-to: iOS apps
- strength: Good practice
- reference: Apple documentation, Generating log messages from your code: keep messages to static text and numbers, and redact values with sensitive user information
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.apple.com/documentation/os/generating-log-messages-from-your-code
- secondary: no

## owasp-logging
- check: prod-logging-personal-data
- source-id: owasp
- applies-to: Everywhere
- strength: Good practice
- reference: OWASP Logging Cheat Sheet: tokens, passwords, session ids and sensitive personal data should usually not be logged directly
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- secondary: no

## owasp-secrets
- check: secrets-in-client
- source-id: owasp
- applies-to: Everywhere
- strength: Good practice
- reference: OWASP Secrets Management Cheat Sheet: keep secrets out of code (detect them before commit); revoke an exposed key immediately, rotate it and remove it from code and logs (section 9.2)
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- secondary: no

## stripe-keys
- check: secrets-in-client
- source-id: vendor-docs
- applies-to: Everywhere
- strength: Good practice
- reference: Stripe docs, API keys: only publishable keys may be exposed; keep secret and restricted keys out of code and rotate a compromised key
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://docs.stripe.com/keys
- secondary: no

## supabase-rls
- check: open-database-rules
- source-id: vendor-docs
- applies-to: Everywhere
- strength: Good practice
- reference: Supabase docs, Row Level Security: enable RLS on every table in an exposed schema
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://supabase.com/docs/guides/database/postgres/row-level-security
- secondary: no

## firebase-insecure-rules
- check: open-database-rules
- source-id: vendor-docs
- applies-to: Everywhere
- strength: Good practice
- reference: Firebase docs, Avoid insecure rules: open read and write rules, and rules that only check sign-in, let others reach the data
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://firebase.google.com/docs/rules/insecure-rules
- secondary: no

## it-act-s10a-terms-acceptance-record
- check: terms-acceptance-record
- source-id: it-act-2000
- applies-to: India
- strength: Good practice
- reference: Information Technology Act 2000, s.10A: a contract is not unenforceable only because its proposal and acceptance were made electronically. Saving which terms version each user accepted, and when, is good practice so the acceptance can be shown later; the Act does not itself require that record
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.indiacode.nic.in/bitstream/123456789/13116/1/it_act_2000_updated.pdf
- secondary: no

## owasp-tls-everywhere
- check: cleartext-traffic
- source-id: owasp
- applies-to: Everywhere
- strength: Good practice
- reference: OWASP Transport Layer Security Cheat Sheet, Use TLS For All Pages: use TLS for all pages, and API-only endpoints should disable plain HTTP
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html
- secondary: no

## android-cleartext-communications
- check: cleartext-traffic
- source-id: android-docs
- applies-to: Android apps
- strength: Good practice
- reference: Android security guidance, Cleartext communications: send data over encrypted channels, and use the network security config to turn off cleartext, with exceptions only for named debug domains
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.android.com/privacy-and-security/risks/cleartext-communications
- secondary: no

## wcag-1-1-1-text-alternatives
- check: image-alt-missing
- source-id: wcag
- applies-to: Websites and apps
- strength: Good practice
- reference: WCAG 2.2 (W3C Recommendation, 12 December 2024), SC 1.1.1 Non-text Content (Level A): non-text content needs a text alternative, and a control needs a name that says its purpose; failure F65: an img with no alt attribute
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.w3.org/TR/WCAG22/#non-text-content
- secondary: no

## wcag-form-labels
- check: form-label-missing
- source-id: wcag
- applies-to: Websites and apps
- strength: Good practice
- reference: WCAG 2.2, SC 3.3.2 Labels or Instructions (Level A): labels or instructions are provided when content needs user input; SC 1.3.1 Info and Relationships and SC 4.1.2 Name, Role, Value (Level A): the label must be programmatically determined
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.w3.org/TR/WCAG22/#labels-or-instructions
- secondary: no

## wcag-1-4-3-contrast
- check: low-contrast-text
- source-id: wcag
- applies-to: Websites and apps
- strength: Good practice
- reference: WCAG 2.2, SC 1.4.3 Contrast (Minimum) (Level AA): text at least 4.5:1 against its background, large-scale text (18pt, or 14pt bold) 3:1; inactive controls, decoration and logotypes are exempt
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.w3.org/TR/WCAG22/#contrast-minimum
- secondary: no

## wcag-keyboard-focus
- check: keyboard-focus-missing
- source-id: wcag
- applies-to: Websites and apps
- strength: Good practice
- reference: WCAG 2.2, SC 2.1.1 Keyboard (Level A): all functionality works from a keyboard; SC 2.4.7 Focus Visible (Level AA): keyboard focus is visible. Understanding 2.4.7 lists failures F78 (outline styled away) and F55 (script removes focus)
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.w3.org/TR/WCAG22/#focus-visible
- secondary: no

## wcag-1-4-4-resize-text
- check: zoom-disabled
- source-id: wcag
- applies-to: Websites
- strength: Good practice
- reference: WCAG 2.2, SC 1.4.4 Resize Text (Level AA): text can be resized to 200 percent without loss of content or function. The W3C ACT rule Meta viewport allows for zoom fails user-scalable=no or a maximum-scale below 2
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.w3.org/TR/WCAG22/#resize-text
- secondary: no

## wcag-3-1-1-page-language
- check: page-lang-missing
- source-id: wcag
- applies-to: Websites
- strength: Good practice
- reference: WCAG 2.2, SC 3.1.1 Language of Page (Level A): the default human language of each web page can be programmatically determined
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.w3.org/TR/WCAG22/#language-of-page
- secondary: no

## owasp-a01-access-control
- check: open-database-rules
- source-id: owasp
- applies-to: Everywhere
- strength: Good practice
- reference: OWASP Top 10:2025, A01 Broken Access Control: except for public resources deny by default, and model access controls to enforce record ownership rather than letting users create, read, update or delete any record
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/
- secondary: no

## owasp-masvs-auth-1
- check: unauthenticated-data-route
- source-id: owasp
- applies-to: Android and iOS apps
- strength: Good practice
- reference: OWASP MASVS, MASVS-AUTH-1: the app uses secure authentication and authorization; enforcement must be on the remote endpoint
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://mas.owasp.org/MASVS/controls/MASVS-AUTH-1/
- secondary: no

## owasp-api4-resource-consumption
- check: rate-limit-missing
- source-id: owasp
- applies-to: Everywhere
- strength: Good practice
- reference: OWASP API Security Top 10 2023, API4 Unrestricted Resource Consumption: limit how often a client can call the API and each operation (such as OTP or password recovery), and set spending limits or billing alerts for paid providers (email, SMS)
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/
- secondary: no

## owasp-dos-rate-limiting
- check: rate-limit-missing
- source-id: owasp
- applies-to: Everywhere
- strength: Good practice
- reference: OWASP Denial of Service Cheat Sheet, Rate limiting: control request rates per IP or other key; it can be set on infrastructure as well as in the application
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html
- secondary: no

## owasp-masvs-storage-2-logs
- check: prod-logging-personal-data
- source-id: owasp
- applies-to: Android and iOS apps
- strength: Good practice
- reference: OWASP MASVS, MASVS-STORAGE-2: the app prevents leakage of sensitive data, including through logs (weakness MASWE-0005, sensitive data inserted into logs)
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://mas.owasp.org/MASVS/controls/MASVS-STORAGE-2/
- secondary: no

## owasp-masvs-network-1
- check: cleartext-traffic
- source-id: owasp
- applies-to: Android and iOS apps
- strength: Good practice
- reference: OWASP MASVS, MASVS-NETWORK-1: the app secures all network traffic according to current best practice, normally TLS, without turning off the platform's secure defaults
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://mas.owasp.org/MASVS/controls/MASVS-NETWORK-1/
- secondary: no

## owasp-maswe-0004-hardcoded-secrets
- check: secrets-in-client
- source-id: owasp
- applies-to: Android and iOS apps
- strength: Good practice
- reference: OWASP MASWE-0004 (MASVS-STORAGE-1), Sensitive Data Hardcoded in the App Package: API keys, credentials and private keys in the package can be recovered by anyone who downloads it, including keys for billed AI services
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://mas.owasp.org/MASWE/MASVS-STORAGE/MASWE-0004/
- secondary: no

## android-permissions-degrade
- check: forced-login-or-permissions
- source-id: android-docs
- applies-to: Android apps
- strength: Good practice
- reference: Android developer docs, Request runtime permissions, basic principles: don't block the user, let them cancel an explanation, and if a permission is denied, degrade gracefully so the app stays usable
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.android.com/training/permissions/requesting
- secondary: no

## apple-hig-request-only-needed
- check: forced-login-or-permissions
- source-id: apple-hig
- applies-to: iOS apps
- strength: Good practice
- reference: Apple Human Interface Guidelines, Privacy, Best practices: request access only to data the app actually needs, and make each request as specific as possible
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.apple.com/design/human-interface-guidelines/privacy
- secondary: no

## apple-hig-tracking-requests
- check: forced-login-or-permissions
- source-id: apple-hig
- applies-to: iOS apps
- strength: Good practice
- reference: Apple Human Interface Guidelines, Privacy, Tracking requests: don't offer incentives for allowing tracking, and don't withhold functionality or content until people allow it
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://developer.apple.com/design/human-interface-guidelines/privacy
- secondary: no

## oss-gpl-agpl-source
- check: open-source-licence-terms
- source-id: oss-licences
- applies-to: Everywhere: code under the GNU GPL or AGPL
- strength: Good practice
- reference: GNU GPL FAQ (UnreleasedMods, UnreleasedModsAGPL): GPL programs sent to site visitors, such as JavaScript, must have their source released under the GPL; a modified AGPL program used over a network must offer its source; GPL code kept on a server need not. Licence condition, not a statute
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://www.gnu.org/licenses/gpl-faq.html
- secondary: no

## owasp-api1-object-authorization
- check: unauthenticated-data-route
- source-id: owasp
- applies-to: Everywhere
- strength: Good practice
- reference: OWASP API Security Top 10 2023, API1 Broken Object Level Authorization: every endpoint that takes an object id and acts on the object must check that the logged-in user may perform that action on that record
- rule-started: n/a
- status: In force
- verified-on: 2026-11-03
- source: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
- secondary: no
