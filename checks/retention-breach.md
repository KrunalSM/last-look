# Retention and breach

## breach-readiness
- title: Incident and breach readiness to check on your own
- area: retention-breach
- needs: none
- severity: High
- evidence-default: maybe
- look-for:
  - code: report Maybe. Note whether personal data is encrypted at rest, access is logged (audit or storage logs) and backups are set up, and whether the repo has a breach or incident plan (`SECURITY.md`, `incident`, `runbook`). Cite the database config, else the main config file or `.`.
  - code: check that every user can be reached through their account, a registered email or phone number, or an in-app message, because breach notices go to each affected user.
  - code: for organisations in India or serving users there, also note self-set time sources that may drift (`server` or `pool` lines in `ntp.conf` or `chrony.conf`, `NTP=` in `timesyncd.conf`, a faked clock), log times with no time zone, logs held only outside India, and audit logging off.
  - code: logs: if the repo sets no retention, name the host or log service to check for 180 days, and for 365 days for logs of personal-data processing from 2027-05-13 (DPDP r.6(1)(e), r.8(3)).
  - ask: do you have a written plan for a security incident or personal data breach, saying who reports it to CERT-In within 6 hours and who tells the regulator and the users?
- why: India requires reporting listed cyber incidents to CERT-In within 6 hours of noticing, synced clocks, logs kept 180 days and a named CERT-In contact, and from 13 May 2027 telling affected users and the Data Protection Board of a personal data breach.
- fix: Plan who reports to CERT-In within 6 hours of noticing (incident@cert-in.org.in; what you know first, the rest later), and who tells the Board (without delay, details in 72 hours) and each affected user. Email CERT-In your point of contact (info@cert-in.org.in). Use NIC or NPL time or the cloud's time service, with time zones in logs. Turn on encryption at rest, access logs and backups.
- exceptions: CERT-In duties bind organisations in India and foreign ones serving users there, personal data or not, a person running a business included, not individuals as users (FAQ Q7, Q25, Q26). All Annexure I types have the 6 hours (direction (ii)). Any accurate time source that conforms to NIC and NPL is fine, the cloud's own included; IST is not required (FAQ Q40, Q42). Board and user breach notices apply in India from 13 May 2027, but not to data of people outside India processed under a foreign contract (DPDP s.17(1)(d)); other countries set their own. Short retention: see log-retention-too-short.
- elsewhere: none

## retention-periods-unset
- title: No set time to erase personal data
- area: retention-breach
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: look for anything that erases personal data once its purpose is served: scheduled jobs (`cron`, scheduled functions), database TTLs or expiry fields (`expires_at`, `ttl`), clean-up of inactive accounts, old leads or abandoned carts.
  - code: if there is none and the privacy notice states no retention period, report Maybe, name the kinds of personal data with no end date, and use the schema or migration file as the location.
  - code: for very large Indian platforms (e-commerce platforms, not marketplace sellers, and social media, with 2 crore or more registered users in India, or online gaming with 50 lakh or more), check for erasure after 3 years without use or a rights request, with a warning at least 48 hours before.
  - ask: none
- why: Personal data must be erased when consent is withdrawn or its purpose is no longer served, unless a law requires keeping it, and India sets a 3-year limit for inactive users of very large platforms.
- fix: Decide how long each kind of personal data is kept, state it in the privacy notice, and add a scheduled job that erases it after that time, keeping only what a law requires. Make the services that process data for you erase it too.
- exceptions: Data a law requires you to keep (for example tax or banking records, and in India processing logs for a year or provider records for 5 years, see provider-customer-records) is not a finding. The 3-year rule covers only the large platforms above and skips data needed to let users reach their account or a balance or token they can spend. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)). A Government notification under DPDP s.17(3), such as for startups, would lift the erasure duty (s.8(7)); none was found.
- elsewhere: none

## log-retention-too-short
- title: Logs turned off or deleted too soon
- area: retention-breach
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: retention under 180 days for any server, app or security log, or 365 days for logs of access to or processing of personal data: CloudWatch `retention_in_days`, Google Cloud `retention_days`, Azure `retentionInDays`, Loki `retention_period`, OpenSearch `min_age`, `logrotate` count. Cite it.
  - code: logging switched off for a whole production server, site or service: a server-wide nginx `access_log off`, or load balancer, CDN or bucket access logs set to false. Cite it.
  - site: none
  - ask: none
- why: India requires logs of all IT systems to be kept for a rolling 180 days, and from 13 May 2027 logs of access to and processing of personal data for a year, so incidents and misuse can be investigated.
- fix: Turn on logs for servers, apps, databases and security tools and keep them at least 180 days, or 365 days for logs of access to or processing of personal data (for example `retention_in_days = 365`); then erase personal data in them unless a law needs more. Keep records of processing, such as orders and payments, for at least a year even when the account is deleted.
- exceptions: No retention in the repo, logs held only outside India, or audit logging off: not a finding here; note them under breach-readiness. `access_log off` for single paths (static files, health checks) is routine. Local development and debug-only logs are out of scope. Not a finding when logs are archived elsewhere long enough; an export with no stated retention is Maybe. The 180 days bind any business, sole proprietors included (FAQ Q25), not individuals as users; the 365 days apply from 13 May 2027. Kept logs must still not hold tokens or passwords (see prod-logging-personal-data).
- elsewhere: none

## provider-customer-records
- title: Customer records that hosting, VPN and crypto providers must keep
- area: retention-breach
- needs: accounts
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: raise only for data centres, VPS, cloud hosting or infrastructure, or public VPN services, or virtual asset exchanges, custodian wallets or service providers. Never for a SaaS app alone. Report Maybe and cite the sign-up or account schema.
  - code: hosting and VPN: note missing validated name, address and phone, ownership type, purpose, hire dates, allotted IPs, or sign-up email, IP and time. Virtual assets: note missing KYC records, or transactions stored without parties, IPs, time zone, ID, keys or addresses, and amount.
  - ask: none
- why: India requires these providers to keep validated customer details, or KYC and transaction records for virtual assets, for 5 years, so cyber incidents can be investigated.
- fix: Collect and validate the listed customer details at sign-up and keep them, protected, for 5 years after the account ends, or longer if another law says so. Virtual asset providers: keep KYC documents and transaction records for 5 years, detailed enough to rebuild each transaction.
- exceptions: Only the providers named above; non-custodial wallets are not named. "Cloud service provider" is not defined; whether software sold as a service counts is unsettled. A company VPN for its own staff is not a VPN service here (FAQ Q34). Foreign virtual asset providers are bound only in the matter of cyber incidents (FAQ Q27). Keeping these records after account deletion is not a retention finding. Validated names, addresses and contact numbers apply from 25 September 2022. KYC documents: Annexure III.
- elsewhere: none
