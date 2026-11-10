# Privacy notices

## privacy-policy-missing
- title: No privacy policy, or none linked
- area: privacy-notices
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code (web): no privacy page or route (`privacy`, `privacy-policy`, `datenschutz`) and no privacy link in the shared layout, footer or sign-up form. Cite the layout or footer file where the link should be.
  - code (mobile): no privacy policy link or URL anywhere in the app code. Confirm it even with no settings, about or sign-up screen. Cite the first that exists: settings, about screen, sign-up screen, the file that draws the main screen, the main config file (`Info.plist`, `AndroidManifest.xml`).
  - code (mobile): report Maybe instead when the link may come from outside the code: a WebView app whose loaded site holds it, remote config or a server-driven menu, or a consent SDK's privacy screen. In-app policy text meets Google Play; Apple 5.1.1(i) asks for a link.
  - code (Google Play apps): the in-app privacy link opens a PDF, an editable document or a page blocked in some regions.
  - code: a privacy policy exists but is incomplete, or leaves out data or recipients: never this check. Report privacy-notice-incomplete instead.
  - site: no privacy policy link in the footer or on the sign-up page
  - ask: for store apps, whether the privacy policy URL is filled in App Store Connect or Play Console (that part is Maybe)
- why: Users must be told what data is collected, why and who gets it, and both app stores reject apps without a privacy policy.
- fix: Publish a privacy policy that matches what the code collects and shares, and link it from the footer, the sign-up form and the app settings.
- exceptions: A site that collects no personal data at all (no forms, accounts, analytics or third-party scripts) may not need one; report Maybe in that case. Google Play apps need one even with no personal data. The CCPA rule covers only businesses over a CCPA threshold (see the rule); CalOPPA has none. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)). A Government notification under DPDP s.17(3), such as for startups, would lift the DPDP notice duty (s.5); none was found.
- elsewhere: none

## privacy-notice-incomplete
- title: Privacy notice leaves out what users must be told
- area: privacy-notices
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: open the privacy notice (privacy page, consent screen or in-app notice). Confirm when it lacks any of: an item-by-item list of personal data; its purposes and what processing provides; how to withdraw consent; how to use access, correction and erasure rights; how to complain to the regulator.
  - code: the notice leaves out personal data the code clearly collects, or third parties the code sends personal data to; report that mismatch in the data map as well.
  - code: the only privacy information sits inside the terms of service or another long document, with no notice that can be read on its own.
  - code (store apps): no retention and deletion policy; on Google Play also no developer or app name, privacy contact, recipients, security or "privacy policy" title; on the App Store also nothing on how data is collected, how to revoke consent or ask for deletion, or third parties' equal protection.
  - site: read the privacy page for the same items
  - ask: none
- why: The notice is what makes consent informed: it must say what is collected and why, and how to withdraw consent, use rights and complain.
- fix: Add the missing parts to the notice: an itemised list of data with the purposes it is used for, a link or steps to withdraw consent, how to ask for access, correction or erasure, and, for users in India, that they can take a complaint to the Data Protection Board of India. Keep it as its own page, not only inside the terms. For store apps, also add the store items listed.
- exceptions: If there is no notice, report privacy-policy-missing and list this check as skipped. A site collecting no personal data needs no notice, but every Play app needs one. Name the regulator (India: the Data Protection Board). In India the notice comes with a consent request, so processing resting only on a legitimate use (DPDP s.7) needs no DPDP notice. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)). A Government notification under DPDP s.17(3), such as for startups, would lift this duty (s.5); none was found.
- elsewhere: none

## privacy-notice-delivery
- title: Privacy notice may not be offered in the user's language or sent to existing users
- area: privacy-notices
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: note which languages the notice and the consent screens exist in (translation files, `values-*` folders, `lang` attributes, locale routes). Name them, and use the notice or translation config file as the location.
  - code: for a service processing personal data in India, or abroad when offering goods or services to people in India, report Maybe: users must be able to read the notice and the consent request in English or an Eighth Schedule language.
  - code: if the service already has users in India, check for a way to send all of them a notice (an email to every user, an in-app message), because users who consented before 13 May 2027 must be sent the notice as soon as practicable after that date.
  - ask: none
- why: In India, people must be able to read the notice and the consent request in English or a scheduled language, and users who consented before the law started must also get the notice.
- fix: Offer the notice and consent text in the languages your Indian users read, with a language switch, and after 13 May 2027 email or message existing users the notice: what data you hold, why, how to withdraw consent and use their rights, and how to complain to the Data Protection Board.
- exceptions: Applies only to processing personal data in India, or processing it abroad in connection with offering goods or services to people in India (DPDP s.3). Like the notice itself, it concerns processing that rests on consent, not on a legitimate use (s.7). The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)). A Government notification under DPDP s.17(3), such as for startups, would lift the s.5 part; none was found.
- elsewhere: none
