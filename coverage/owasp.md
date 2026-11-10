# OWASP: Top 10, API Security Top 10, MASVS and cheat sheets
- source-id: owasp
- walk: targeted
- url: https://owasp.org/Top10/2025/
- read-on: 2026-11-03

Also read: API Security Top 10 2023 items API1, API2 and API4, MASVS (https://mas.owasp.org/MASVS/) control pages and MASWE-0004, and the Authorization, Denial of Service, Logging, Secrets Management and Transport Layer Security cheat sheets (https://cheatsheetseries.owasp.org/). These exposure checks find a few common leaks; the rest is left to dedicated security tools.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| Top 10:2025 A01 | Broken Access Control | Partly covered | open-database-rules, unauthenticated-data-route, rate-limit-missing | 2026-11-03 | Record ownership (rule on open-database-rules), routes without login, rate limits; CORS, JWT handling and directory listing are left to security tools. |
| Top 10:2025 A02-A10 | Misconfiguration, supply chain, cryptography, injection, design, authentication, integrity, logging and alerting, exceptions | Not done yet | - |  | Left to dedicated security tools. |
| API Security 2023 API1 | Broken Object Level Authorization | Covered | unauthenticated-data-route | 2026-11-03 |  |
| API Security 2023 API2 | Broken Authentication | Not done yet | - |  |  |
| API Security 2023 API4 | Unrestricted Resource Consumption | Can't tell from code | rate-limit-missing | 2026-11-03 | Grouped into the rate-limit-missing Maybe: request rates and spending limits for AI, email and SMS. Memory, payload and timeout limits are not checked. |
| Authorization Cheat Sheet | Deny by default; check every request on the server | Partly covered | unauthenticated-data-route | 2026-11-03 | No rule from this page; the check cites API1 and MASVS-AUTH-1. |
| Denial of Service Cheat Sheet: Rate limiting | Request rate limits in the app or infrastructure | Can't tell from code | rate-limit-missing | 2026-11-03 | Infrastructure limits are outside the repo, so the check reports Maybe. |
| Logging Cheat Sheet: Data to exclude | No tokens, passwords, session ids or sensitive personal data in logs | Covered | prod-logging-personal-data | 2026-11-03 |  |
| Secrets Management Cheat Sheet: 9 Incident Response | Revoke, rotate and remove exposed secrets | Partly covered | secrets-in-client | 2026-11-03 | Only secrets exposed in client code; secret storage and rotation are not checked. |
| Transport Layer Security Cheat Sheet: Use TLS For All Pages | TLS everywhere; API endpoints refuse plain HTTP | Covered | cleartext-traffic | 2026-11-03 |  |
| MASVS-STORAGE-1 (MASWE-0004) | Sensitive data hardcoded in the app package | Covered | secrets-in-client | 2026-11-03 |  |
| MASVS-STORAGE-2 | Prevent leakage of sensitive data, logs included | Partly covered | prod-logging-personal-data | 2026-11-03 | Backups and other leak paths are not checked. |
| MASVS-NETWORK-1 | Secure all network traffic | Partly covered | cleartext-traffic | 2026-11-03 | Certificate validation and pinning are not checked. |
| MASVS-AUTH-1 | Secure authentication and authorization, enforced on the remote endpoint | Partly covered | unauthenticated-data-route | 2026-11-03 |  |
