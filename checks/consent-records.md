# Consent and records

## terms-acceptance-record
- title: Terms acceptance not saved with version and time
- area: consent-records
- needs: accounts
- severity: High
- evidence-default: confirm
- look-for:
  - code: find the handler that runs when a user accepts the terms at sign-up, checkout or onboarding (a form field such as `terms`, `acceptTerms` or `agreed`), and read what it saves (database insert, user document, API call).
  - code: confirm when the saved record has no terms version and no acceptance time (`terms_version`, `accepted_at`, `termsAcceptedAt` or similar). Cite the line where the record is saved.
  - code: a `required` checkbox on the form is not a record. The server must store the version and time.
  - site: the sign-up or checkout form shows a terms checkbox or "By signing up you agree" text
  - ask: none
- why: Without a saved version and time you can't show which terms a user agreed to, or when.
- fix: Save the terms version and acceptance time with the user when they accept, for example `termsVersion: TERMS_VERSION, termsAcceptedAt: new Date().toISOString()`.
- exceptions: Does not apply when the project has no accounts, no checkout and no terms to accept. If an outside sign-in or payment provider records the acceptance, report Maybe and name what to check there.
- elsewhere: none

## terms-change-notice
- title: No notice or re-acceptance when terms change
- area: consent-records
- needs: accounts
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: the terms or privacy page says changes apply at any time, or that continued use means acceptance ("These terms can be updated whenever we like", "Using the service after a change counts as agreement"). Cite that line.
  - code: no stored terms version compared with a current version, and no banner, email or re-accept step for existing users (search for `terms_version`, `TERMS_VERSION`, "updated our Terms").
  - site: the terms page shows a "last updated" date but describes no way users are told about changes
  - ask: none
- why: Users may not be bound by changed terms they never saw; India requires hosts of users' content to tell users of changes, the EU requires telling users before data is used for a new purpose, and in the US quiet changes can be unfair or deceptive.
- fix: Store the accepted terms version for each user. Before a material change applies, email users or show a banner, and ask for acceptance of the new version at the next sign-in.
- exceptions: Small edits that change nothing material (typos, contact details) need no notice. Not a finding when the code shows a notice or re-acceptance step. The India rule covers only services that store or pass on content for their users (IT Rules 2021).
- elsewhere: US | The FTC says quietly changing terms or privacy policies to use data more widely can be unfair or deceptive | https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/02/ai-other-companies-quietly-changing-your-terms-service-could-be-unfair-or-deceptive

## prechecked-consent
- title: Consent box or paid add-on selected by default
- area: consent-records
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code (web): a consent or marketing checkbox with `defaultChecked`, `checked` or `checked={true}` before the user acts, or opt-in state that starts as `true` (`useState(true)`). Cite the checkbox line.
  - code (android): a `CheckBox` or `Switch` with `android:checked="true"`, or `isChecked = true` in code, for marketing, data sharing or terms consent. Read its label through `@string/` in every `res/values*` folder, including other languages such as Hindi in `values-hi`, to learn what it asks.
  - code (ios): a `UISwitch` with `isOn = true`, or a SwiftUI `Toggle` whose state starts `true`, for a consent option.
  - code: one checkbox that bundles terms acceptance with marketing or data sharing.
  - code: a cart or checkout that adds a paid item the buyer didn't pick (insurance, a donation, an extended warranty, a subscription, a paid service), pre-ticked or as a ready-added line, or that records a purchase without the buyer pressing a buy or pay control. Cite the line.
  - site: open the sign-up form and note which boxes are ticked before you touch anything
  - ask: none
- why: A pre-ticked box is not a clear affirmative action, so it does not count as consent, and India bans adding paid items at checkout without the buyer's choice.
- fix: Start every consent box unticked (remove `defaultChecked`, or set `android:checked="false"`), keep marketing consent separate from terms acceptance, and add paid extras or donations only when the buyer picks them.
- exceptions: A settings screen may show a choice the user already saved. Boxes that are not consent, such as "remember me" or "show password", are out of scope. Free samples, complimentary services and fees needed for the order (delivery, tax) shown before payment are not sneaked items. The E-Commerce purchase rule covers sales to consumers in India (scope in business-identity-missing). The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## consent-withdrawal-missing
- title: Consent can't be withdrawn as easily as it was given
- area: consent-records
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: find where consent is given (a cookie or analytics banner, a marketing opt-in, a data-sharing toggle), then look for a way to withdraw that same consent later: a cookie or privacy choices link, a settings toggle or an unsubscribe link.
  - code: confirm when the choice can't be reached again after the first answer (for example, a banner shown only while no choice is stored) and nothing else lets the user change it. Cite the line that hides the choice, or the settings screen where a withdraw option should be.
  - code: withdrawing takes much more effort than giving consent, for example one click to accept but an email to support to withdraw.
  - code: a withdrawal is saved but not acted on: an opt-out flag that the sending or tracking code never reads, or tracking that still loads after the user turns it off.
  - site: after accepting, look for a link or setting that lets you change the choice
  - ask: none
- why: People can withdraw consent at any time, about as easily as they gave it, and processing based on that consent must then stop.
- fix: Add a privacy or cookie choices link in the footer and the app settings that reopens the same choice, make withdrawing a single action, and stop the tracking or messages, and erase the data collected under that consent unless a law requires keeping it.
- exceptions: Processing that does not rest on consent (a login session, an order the user asked for, a legal duty) has nothing to withdraw. Withdrawal does not undo processing already done, and an order already paid for can still be delivered. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)). A Government notification under DPDP s.17(3), such as for startups, would lift the erasure duty (s.8(7)); none was found.
- elsewhere: none

## consent-record-missing
- title: Consent not recorded with its purpose, the notice shown and the time
- area: consent-records
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: find where a consent to processing is saved (a marketing or data-sharing opt-in, a consent screen, consent at sign-up, a consent platform callback). Confirm when the record has no time and nothing showing which notice the user saw, such as a bare `marketing_opt_in: true`. Cite the line.
  - code: when only one of the two is missing (a time but no notice or privacy policy version, or a version but no time), report Maybe and name the missing part.
  - code: consent kept only in the browser (localStorage or a cookie set by a cookie banner) can't be shown later. Report Maybe, unless a consent platform or a server log records it.
  - site: none
  - ask: none
- why: Where processing rests on consent, the business must be able to prove that the notice was given and the consent was given, so each consent needs its own record.
- fix: Save each consent as a record with the user id, the purpose (for example "marketing email"), the version of the notice shown, the time given and the time of any withdrawal, for example a `consents` table with `user_id, purpose, notice_version, given_at, withdrawn_at`.
- exceptions: Processing that does not rest on consent needs no consent record. Acceptance of the terms of service is checked by terms-acceptance-record. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none
