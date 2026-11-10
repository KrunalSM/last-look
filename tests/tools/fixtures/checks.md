## terms-acceptance-record
- title: Terms acceptance not saved with version and time
- area: consent-records
- needs: accounts
- severity: High
- evidence-default: confirm
- look-for:
  - code: sign-up or checkout handler stores no terms version or acceptance timestamp
  - site: sign-up form has a terms checkbox
  - ask: none
- why: Without a record you can't show what a user agreed to.
- fix: Save terms_version and accepted_at with the user at acceptance.
- exceptions: none
- elsewhere: none

## privacy-policy-missing
- title: No privacy policy page
- area: privacy-notices
- needs: none
- severity: Critical
- evidence-default: confirm
- look-for:
  - site: no link to a privacy policy in the footer
- why: Users can't see how their data is used.
- fix: Publish a privacy policy and link it from every page.
- exceptions: none
- elsewhere: EU | GDPR Art. 13 expects an equivalent notice | https://example.org/gdpr
