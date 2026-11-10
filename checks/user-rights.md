# User rights

## account-deletion-missing
- title: No way to delete an account
- area: user-rights
- needs: accounts
- severity: High
- evidence-default: confirm
- look-for:
  - code: the settings, profile or account screen has no delete-account action (a button, link, route or API such as `/account/delete`, `deleteUser`, `auth.admin.deleteUser`, `deleteAccount`). Cite the settings screen file.
  - code: an action that only deactivates, hides or logs out the account is not deletion.
  - code (mobile): Apple and Google Play need deletion to start inside the app; Google Play also needs a web link where users can ask for deletion.
  - site: public help, privacy or account pages say nothing about deleting an account; settings behind a login are `Not tested`
  - ask: none
- why: People can ask for their data to be erased, and both app stores require account deletion inside the app.
- fix: Add an account deletion action in settings that deletes the account record, its personal data and uploads, cancels any subscription, and tells the user what is kept and why. Keep only what a law requires, such as records India requires to be kept for one year or, for services hosting users' content in India, sign-up details for 180 days after the account closes.
- exceptions: Does not apply when the project has no accounts. A delete action that exists but may leave some data behind (a paging limit, a missed table) is not this check; report Maybe and say what to check. On the web, a deletion request by email may be enough for some laws; report Maybe. It is not enough for the app stores. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## data-rights-request-missing
- title: No published way to ask for your data or have it corrected
- area: user-rights
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: the privacy page, help pages and account settings say nothing about how to ask for a copy or summary of your data, or for a correction, and give no form, email address or settings action for it. Cite the privacy page or settings file where it should be.
  - code: the only way stated does not exist (for example, the privacy page points to a setting that the settings screen does not have), and no other way is given.
  - site: the privacy page gives no way to make a data request
  - ask: none
- why: People can ask what data you hold about them and who you shared it with, and ask you to correct it, so the way to ask must be published.
- fix: Publish how to make a request (a form, an email address or settings actions) and which identifier you need, such as the account email. Answer access requests with a summary of the data, what you do with it and who you shared it with, correct data on request, and let users name someone who can act for them if they die or can't act.
- exceptions: An account deletion option covers erasure but not access or correction. A published email address for data requests is enough to avoid this finding, except under the CCPA for a business that is not online-only (two methods, one a toll-free number). The CCPA rule covers only businesses over a CCPA threshold. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)). A Government notification under DPDP s.17(3), such as for startups, would lift the access right (s.11) and the accuracy duty (s.8(3)); none was found.
- elsewhere: none
