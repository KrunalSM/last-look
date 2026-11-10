# Apple App Review Guidelines
- source-id: apple-review-guidelines
- walk: full
- url: https://developer.apple.com/app-store/review/guidelines/
- read-on: 2026-11-03

Walked from the official page, "Last Updated: October 16, 2026" (Apple developer news for that update: https://developer.apple.com/news/?id=92th7e5i). Every numbered guideline, lettered or numbered sub-item, the Introduction, Before You Submit and After You Submit has a row. Sub-items are listed on their own rows where Apple numbers them; bullets inside one numbered item share its row.

Dates. The page gives no start dates, so rules use `before 2026-10-16` unless Apple developer news gives one: privacy policy 2018-10-03 (https://developer.apple.com/news/?id=08312018a), account deletion 2022-06-30 (https://developer.apple.com/news/?id=12m75xbj), current 4.8 wording 2024-01-25 (https://developer.apple.com/news/?id=7j1f99yf), third-party AI wording in 5.1.2(i) 2025-11-13 (https://developer.apple.com/news/?id=ey6d8onl). Other news items read for history: https://developer.apple.com/news/?id=vvzx6cul (16 Oct 2026), https://developer.apple.com/news/?id=a233fmpw (8 Jun 2026), https://developer.apple.com/news/?id=r9dcmrvs (9 Jun 2025), https://developer.apple.com/news/?id=9txfddzf (1 May 2025).

App Store Connect. Notes say "App Store Connect" where the item lives in its forms (metadata, privacy answers, age rating, review notes, demo account). Those items are grouped into `Maybe` checks: store-data-disclosure for privacy answers, store-listing-review for the rest. Content and app-type rules are grouped into restricted-app-type, feature and framework rules into apple-feature-rules, and rights rules into content-rights-unclear.

Linked page read for one definition: Apple's User Privacy and Data Use page (https://developer.apple.com/app-store/user-privacy-and-data-use/), linked from 5.1.2(i) as "Learn more about tracking", for what counts as tracking in tracking-without-att.

Not walked: the rest of that page, the Apple Developer Program License Agreement (including Schedule 2, which 3.1.2(c) points to), the Human Interface Guidelines and other linked documents. "Notarization" highlighting only marks which guidelines also apply to apps distributed outside the App Store; it adds no rules.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| Intro | Introduction: curated store, kids and teens, cheating review, SDKs, entitlements | Doesn't concern apps | - | 2026-11-03 | Principles and links. The points about kids, SDKs and cheating review are applied through the numbered guidelines below. |
| Before You Submit | Checklist: test for crashes, complete metadata, contact details, demo account, live backend, review notes, regulatory documents | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect: metadata, contact details, review notes and demo account. Crashes need a device. |
| 1 | Safety (section intro) | Doesn't concern apps | - | 2026-11-03 | Heading and intro; rules are in 1.1 to 1.7. |
| 1.1 | Objectionable content | Can't tell from code | store-content-policy | 2026-11-03 | Content judgement, raised as Maybe when the app's content falls in these groups. |
| 1.1.1 | Defamatory, discriminatory or mean-spirited content | Can't tell from code | store-content-policy | 2026-11-03 | The satire and humour exemption is in the check's exceptions. |
| 1.1.2 | Realistic violence or abuse; game enemies targeting real groups | Can't tell from code | store-content-policy | 2026-11-03 |  |
| 1.1.3 | Reckless use of weapons; firearms or ammunition sales | Can't tell from code | store-content-policy | 2026-11-03 |  |
| 1.1.4 | Sexual or pornographic material, hookup apps | Can't tell from code | store-content-policy | 2026-11-03 |  |
| 1.1.5 | Inflammatory religious commentary | Can't tell from code | store-content-policy | 2026-11-03 |  |
| 1.1.6 | False information and features, fake trackers, anonymous or prank calls and SMS | Can't tell from code | store-content-policy | 2026-11-03 |  |
| 1.1.7 | Profiting from recent tragedies | Can't tell from code | store-content-policy | 2026-11-03 |  |
| 1.2 | User-generated content: filtering, reporting, blocking, published contact | Covered | ugc-moderation-missing, uploads-takedown-process, ai-content-safeguards, store-content-policy | 2026-11-03 | Includes AI content creation apps (see ai-content-safeguards). Apps used mainly for pornography, random chat, "hot-or-not" voting or bullying: store-content-policy. |
| 1.2.1 | Creator content: moderated as user content, IAP rules, say which content costs extra | Partly covered | ugc-moderation-missing, in-app-purchase-billing | 2026-11-03 | Telling users which creator content needs extra purchases is not checked. |
| 1.2.1(a) | Creator apps flag content above the age rating and restrict it by age | Covered | ugc-moderation-missing | 2026-11-03 | New guideline in Apple news of 13 Nov 2025. |
| 1.3 | Kids Category | Partly covered | child-app-sdks-ads | 2026-11-03 | Third-party analytics and ads, data sent to third parties, and links and purchases outside a parental gate are checked. Following children's privacy laws (see 5.1.4) and keeping to these rules after leaving the category are not. Joining is chosen in App Store Connect; the check asks. |
| 1.4 | Physical harm (intro) | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 1.4.1 | Medical apps: accuracy, methodology, see a doctor, regulatory clearance | Can't tell from code | restricted-app-type, store-listing-review | 2026-11-03 | The regulatory clearance link goes to App Review through App Store Connect. |
| 1.4.2 | Drug dosage calculators | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 1.4.3 | Tobacco, vape, illegal drugs, excess alcohol; sale of controlled substances | Can't tell from code | restricted-app-type | 2026-11-03 | Licensed pharmacy and legal cannabis exception in the check. |
| 1.4.4 | DUI checkpoints; reckless driving | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 1.4.5 | Activities that risk physical harm | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 1.5 | Developer information: contact in the app and Support URL; Wallet pass issuer details | Can't tell from code | store-listing-review, apple-feature-rules | 2026-11-03 | Support URL is in App Store Connect. The check notes whether the app shows a support contact. |
| 1.6 | Data security | Partly covered | secrets-in-client, open-database-rules | 2026-11-03 | Exposed keys and open databases are checked; other security measures can't be seen in code. |
| 1.7 | Reporting criminal activity | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 2 | Performance (section heading) | Doesn't concern apps | - | 2026-11-03 | Heading only. |
| 2.1 | App completeness (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see 2.1(a) and 2.1(b). |
| 2.1(a) | Final versions: no placeholders, working URLs, tested, demo account, live backend | Partly covered | placeholder-content, store-listing-review | 2026-11-03 | Placeholders and dead links are checked. Demo account and backend are App Store Connect review items; crashes need a device. |
| 2.1(b) | In-app purchases complete, visible and working | Can't tell from code | store-listing-review | 2026-11-03 | IAP setup and review notes are in App Store Connect. |
| 2.2 | Beta testing: TestFlight, no paid testers | Can't tell from code | store-listing-review | 2026-11-03 | TestFlight distribution is in App Store Connect. |
| 2.3 | Accurate metadata, including privacy information | Can't tell from code | store-data-disclosure, store-listing-review | 2026-11-03 | App Store Connect metadata and privacy answers. |
| 2.3.1 | Accurate metadata (heading of (a) and (b)) | Doesn't concern apps | - | 2026-11-03 | Heading; see 2.3.1(a) and (b). |
| 2.3.1(a) | Describe new features in review notes; no misleading marketing or false prices | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect review notes and marketing. Hidden features moved to 2.5.19. |
| 2.3.1(b) | Removal from the program for egregious or repeated behaviour | Doesn't concern apps | - | 2026-11-03 | States Apple's sanction. |
| 2.3.2 | Show which items need extra purchases; promoted IAPs | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect metadata. Handling a promoted IAP purchase at launch is not checked. |
| 2.3.3 | Screenshots show the app in use | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. |
| 2.3.4 | Previews use screen captures of the app | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. |
| 2.3.5 | Most fitting category | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. |
| 2.3.6 | Honest age rating answers; local content rating rules | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect age rating questions. The check lists what the answers must reflect. |
| 2.3.7 | Unique name up to 30 characters, accurate keywords, no keyword stuffing | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. The check notes the app name length in the project. |
| 2.3.8 | Metadata fit for 4+; "For Kids" reserved for the Kids Category; matching icons | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. |
| 2.3.9 | Rights to listing materials; fictional account data in screenshots | Can't tell from code | store-listing-review, content-rights-unclear | 2026-11-03 | App Store Connect. |
| 2.3.10 | No other platforms' or marketplaces' names or imagery; relevant metadata | Can't tell from code | content-rights-unclear, store-listing-review | 2026-11-03 | In the app and in App Store Connect metadata. |
| 2.3.11 | Pre-orders complete and as advertised | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. |
| 2.3.12 | What's New text describes changes | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. |
| 2.3.13 | In-app events | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. |
| 2.3.14 | Creative assets | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect. New guideline in Apple news of 16 Oct 2026. |
| 2.4 | Hardware compatibility (heading) | Doesn't concern apps | - | 2026-11-03 | Heading only. |
| 2.4.1 | iPhone apps should run on iPad | Can't tell from code | apple-feature-rules | 2026-11-03 | An encouragement ("whenever possible"). |
| 2.4.2 | Efficient power use, no device damage, no unrelated background processes such as mining | Partly covered | deceptive-app-behavior, apple-feature-rules | 2026-11-03 | On-device crypto mining is checked; battery and heat need a device. |
| 2.4.3 | Apple TV apps work with the Siri remote or game controllers | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.4.4 | No restart or unrelated system-setting changes | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.4.5 | Mac App Store extra requirements (intro) | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac App Store builds only. |
| 2.4.5(i) | Sandboxing; APIs for other apps' data | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(ii) | Packaged with Xcode, self-contained | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(iii) | No auto-launch or lingering processes without consent | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(iv) | No downloading apps, kexts or code to add features | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(v) | No root escalation or setuid | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(vi) | No licence screens, keys or own copy protection | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(vii) | Updates only through the Mac App Store | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(viii) | Current OS, no deprecated or optional technologies | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.4.5(ix) | All localisations in one bundle | Can't tell from code | apple-feature-rules | 2026-11-03 | Mac only. |
| 2.5 | Software requirements (heading) | Doesn't concern apps | - | 2026-11-03 | Heading only. |
| 2.5.1 | Public APIs only, current OS, frameworks for their intended purpose | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.2 | Self-contained bundle; no downloaded code that adds or changes features | Partly covered | unsafe-code-loading | 2026-11-03 | Downloaded code is checked; reading or writing outside the container is not. Teaching-app exception in the check. |
| 2.5.3 | No code that harms the OS or hardware features, including push and Game Center | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.4 | Background services only for their intended purposes | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.5 | Works on IPv6-only networks | Can't tell from code | apple-feature-rules | 2026-11-03 | Needs a network test. |
| 2.5.6 | WebKit for web browsing; alternative engine entitlement | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.7 | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text (deleted, Apple news of 25 Jan 2024). |
| 2.5.8 | Alternate desktop or home screen environments | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 2.5.9 | Altering standard switches or native behaviours, blocking links out | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.10 | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text (deleted, Apple news of 13 Nov 2025). |
| 2.5.11 | SiriKit and Shortcuts (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) to (iii). |
| 2.5.11(i) | Only intents the app can handle and users would expect | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.11(ii) | Vocabulary and aliases relate to the app | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.11(iii) | Resolve requests directly, no ads in between | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.12 | CallKit and SMS fraud extensions: confirmed spam only, disclose criteria, no other data use | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.13 | Face login uses LocalAuthentication; another method under 13 | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.14 | Consent and a clear indicator when recording user activity | Partly covered | session-replay-consent, apple-feature-rules | 2026-11-03 | Session replay SDKs are checked; camera, microphone and screen recording are Maybe. |
| 2.5.15 | File pickers include Files and iCloud documents | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.16 | Widgets, extensions and notifications relate to the app | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.16(a) | App Clip features in the main app; no ads in App Clips | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.17 | Matter pairing and certified components | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 2.5.18 | Ads: placement, age fit, targeting info, no sensitive-data targeting, clear interstitials, ad reporting | Can't tell from code | apple-feature-rules | 2026-11-03 | Ad behaviour comes from the ad network at run time. |
| 2.5.19 | Hidden, dormant or undocumented features | Covered | deceptive-app-behavior | 2026-11-03 | New number in Apple news of 16 Oct 2026 for a long-standing rule. |
| 3 | Business (section intro): explain the business model, rip-off prices, review manipulation | Partly covered | custom-review-prompt, store-listing-review | 2026-11-03 | Incentivised or filtered reviews are checked; the business model explanation is in App Store Connect; pricing can't be judged from code. |
| 3.1 | Payments (heading) | Doesn't concern apps | - | 2026-11-03 | Heading only. |
| 3.1.1 | In-App Purchase | Partly covered | in-app-purchase-billing, iap-purchase-rules | 2026-11-03 | IAP for digital goods, restore, credit expiry, loot-box odds and trial terms are checked. Tips, gifting refunds, NFTs and Mac plug-ins are not. |
| 3.1.1(a) | Links to other purchase methods; entitlements; US storefront | Covered | in-app-purchase-billing | 2026-11-03 | Entitlements are granted outside the code; the US storefront scope is in the check. |
| 3.1.2 | Auto-renewable subscriptions (intro) | Doesn't concern apps | - | 2026-11-03 | Heading; rules in 3.1.2(a) to (c). |
| 3.1.2(a) | Permissible uses: ongoing value, 7 days minimum, all devices, no extra tasks, keep paid features, no bait-and-switch | Partly covered | forced-login-or-permissions, renewal-terms-checkout, store-listing-review | 2026-11-03 | Extra tasks and clear terms are checked. Period length, devices and offers are set in App Store Connect. |
| 3.1.2(b) | Upgrades and downgrades | Can't tell from code | store-listing-review | 2026-11-03 | Subscription groups are set in App Store Connect. |
| 3.1.2(c) | Subscription information before subscribing | Covered | renewal-terms-checkout | 2026-11-03 | Schedule 2 of the Developer Program License Agreement was not walked. |
| 3.1.3 | Other purchase methods; no encouraging them in the app outside the US storefront | Covered | in-app-purchase-billing | 2026-11-03 |  |
| 3.1.3(a) | Reader apps | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check. The External Link Account Entitlement is granted outside the code. |
| 3.1.3(b) | Multiplatform services | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check. |
| 3.1.3(c) | Enterprise services | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check. |
| 3.1.3(d) | Person-to-person services | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check (one-to-one, real time). |
| 3.1.3(e) | Goods and services outside the app must not use IAP | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check. |
| 3.1.3(f) | Free stand-alone companion apps | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check. |
| 3.1.3(g) | Advertising management apps | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check; boosts shown in the same app still need IAP. |
| 3.1.4 | Hardware-specific content | Partly covered | in-app-purchase-billing | 2026-11-03 | Hardware-tied unlocks, and the IAP option needed for optional add-on products, are in the check's exceptions; requiring unrelated purchases or marketing to unlock is not checked. |
| 3.1.5 | Cryptocurrencies (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) to (v). |
| 3.1.5(i) | Wallets offered by organisations | Can't tell from code | restricted-app-type | 2026-11-03 | Enrolment type is in the developer account. |
| 3.1.5(ii) | No on-device mining | Covered | deceptive-app-behavior | 2026-11-03 | Cloud mining is allowed. |
| 3.1.5(iii) | Exchanges only where licensed | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.1.5(iv) | ICOs and crypto-securities trading from approved institutions | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.1.5(v) | No crypto rewards for tasks | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2 | Other business model issues (intro) | Doesn't concern apps | - | 2026-11-03 | Heading; see 3.2.1 and 3.2.2. |
| 3.2.1 | Acceptable (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) to (viii). |
| 3.2.1(i) | Promoting your own apps, but not merely a catalog of them | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.1(ii) | Curated third-party app collections with editorial content | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.1(iii) | Approved rentals may expire; other items may not | Covered | iap-purchase-rules | 2026-11-03 |  |
| 3.2.1(iv) | Wallet pass uses | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 3.2.1(v) | Insurance apps free, legal, no IAP | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.1(vi) | Approved nonprofits may fundraise, with Apple Pay | Can't tell from code | restricted-app-type | 2026-11-03 | Nonprofit approval is outside the code. |
| 3.2.1(vii) | Optional person-to-person monetary gifts | Covered | in-app-purchase-billing | 2026-11-03 | An exception in the check. |
| 3.2.1(viii) | Financial trading, investing or money management from licensed institutions | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.2 | Unacceptable (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) to (x). |
| 3.2.2(i) | Store-like interfaces for third-party apps | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.2(ii) | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text (moved to 4.10, Apple news of 25 Jan 2024). |
| 3.2.2(iii) | Artificial ad impressions or clicks; apps mainly for ads | Partly covered | webview-only-app, apple-feature-rules | 2026-11-03 | Apps that are mainly ads are checked; ad fraud can't be seen in code. |
| 3.2.2(iv) | Collecting charity funds in the app | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.2(v) | Arbitrarily restricting users by location or carrier | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 3.2.2(vi) | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text (deleted; a version now in 5.1.2(i), Apple news of 25 Jan 2024). |
| 3.2.2(vii) | Manipulating visibility or rank on other services | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.2(viii) | Binary options; licensed CFD and derivatives trading | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.2(ix) | Personal loans: full terms, APR at most 36%, no full repayment within 60 days | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 3.2.2(x) | Forcing ratings, reviews or downloads of other apps | Covered | custom-review-prompt | 2026-11-03 | Rewards for in-app actions are allowed (in the check). |
| 4 | Design (section intro) | Doesn't concern apps | - | 2026-11-03 | Heading and intro; rules in 4.1 to 4.10. |
| 4.1 | Copycats (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (a) to (c). |
| 4.1(a) | Copying another app | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 4.1(b) | Impersonating other apps or services | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 4.1(c) | Another developer's icon, brand or product name | Can't tell from code | content-rights-unclear | 2026-11-03 | New guideline in Apple news of 13 Nov 2025. |
| 4.2 | Minimum functionality | Covered | webview-only-app | 2026-11-03 | Apps that are only a song, film, book or game guide belong in other Apple stores; the check reports Maybe when the native part is small. |
| 4.2.1 | Rich ARKit experiences | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.2.2 | Not mainly marketing, ads, web clippings, aggregators or links | Covered | webview-only-app | 2026-11-03 | Catalogs are allowed (in the check). |
| 4.2.3 | Works on its own (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) and (ii). |
| 4.2.3(i) | Works without another app installed | Covered | webview-only-app | 2026-11-03 |  |
| 4.2.3(ii) | Disclose size and ask before extra first-launch downloads | Covered | webview-only-app | 2026-11-03 |  |
| 4.2.4 | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text (deleted, Apple news of 25 Jan 2024). |
| 4.2.5 | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text (deleted, Apple news of 25 Jan 2024). |
| 4.2.6 | Apps from templates or app generation services | Can't tell from code | store-listing-review | 2026-11-03 | Who submits the app is set in App Store Connect. |
| 4.2.7 | Remote desktop clients (intro) | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 4.2.7(a) | Only user-owned hosts on a local network | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 4.2.7(b) | Software runs and renders on the host | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 4.2.7(c) | Accounts created and managed on the host | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 4.2.7(d) | No store-like client UI | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 4.2.7(e) | Thin clients for cloud apps not allowed | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 4.3 | Spam (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (a) and (b). |
| 4.3(a) | Several bundle IDs for the same app | Can't tell from code | store-listing-review | 2026-11-03 | Seen across App Store Connect submissions, not in one project. |
| 4.3(b) | Copies of crowded or low-effort app types | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 4.4 | Extensions: function, disclosure, no marketing, ads or IAP | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.4.1 | Keyboard extensions | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.4.2 | Safari extensions | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.4.3 | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text (deleted, Apple news of 25 Jan 2024). |
| 4.5 | Apple sites and services (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see 4.5.1 to 4.5.6. |
| 4.5.1 | Apple RSS feeds only; no scraping Apple sites | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 4.5.2 | Apple Music (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) to (iii). |
| 4.5.2(i) | MusicKit playback and no monetising Apple Music access | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.5.2(ii) | Licences beyond MusicKit; cover art use | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 4.5.2(iii) | Apple Music data: purpose string, no sharing, no ads | Partly covered | permission-purpose-strings, apple-feature-rules | 2026-11-03 | The purpose string is checked; data use is Maybe. |
| 4.5.3 | No spam or phishing through Apple services; Game Center data | Partly covered | push-marketing-consent, apple-feature-rules | 2026-11-03 | Unsolicited marketing push is checked; Game Center and Live Activities are Maybe. |
| 4.5.4 | Push notifications: not required, no sensitive data, marketing only with opt-in and opt-out | Covered | push-marketing-consent | 2026-11-03 |  |
| 4.5.5 | Game Center Player IDs | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.5.6 | Apple emoji only as Unicode, not embedded | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 4.6 | Intentionally omitted | Doesn't concern apps | - | 2026-11-03 | No text in the version read. |
| 4.7 | Mini apps, mini games, streaming games, chatbots, plug-ins and emulators (intro) | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.7.1 | Such software follows privacy rules, has filtering, reporting and blocking, and uses IAP | Partly covered | ugc-moderation-missing, uploads-takedown-process, in-app-purchase-billing | 2026-11-03 | The privacy of each piece of software can't be seen in code. |
| 4.7.2 | No exposing native APIs to the software without permission | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.7.3 | Consent each time before sharing data or permissions with the software | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.7.4 | Index of the software with universal links | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 4.7.5 | Age restriction for software above the app's age rating | Covered | ugc-moderation-missing | 2026-11-03 |  |
| 4.8 | Login services: an equivalent private login next to social logins | Covered | sign-in-with-apple-missing | 2026-11-03 | Exemptions in the check. |
| 4.9 | Apple Pay: material purchase information, branding, recurring payment disclosures | Partly covered | renewal-terms-checkout, apple-feature-rules | 2026-11-03 | Recurring payment terms are checked; branding is Maybe. |
| 4.10 | No monetising built-in capabilities | Can't tell from code | apple-feature-rules | 2026-11-03 |  |
| 5 | Legal (section intro): local law, criminal behaviour, trafficking and child exploitation | Can't tell from code | restricted-app-type | 2026-11-03 | Local laws are walked as their own sources in this skill. Trafficking wording updated in Apple news of 16 Oct 2026. |
| 5.1 | Privacy (intro) | Doesn't concern apps | - | 2026-11-03 | Heading and intro; rules in 5.1.1 to 5.1.5. |
| 5.1.1 | Data collection and storage (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) to (x). |
| 5.1.1(i) | Privacy policy in App Store Connect and in the app, with required contents | Covered | privacy-policy-missing, privacy-notice-incomplete | 2026-11-03 | The App Store Connect URL field is asked about in privacy-policy-missing. |
| 5.1.1(ii) | Consent for collection, easy withdrawal, clear purpose strings, paid features not tied to data | Partly covered | trackers-before-consent, consent-withdrawal-missing, permission-purpose-strings, forced-login-or-permissions | 2026-11-03 | Consent for first-party collection outside analytics and ads, and GDPR legitimate-interest processing, are not checked here. |
| 5.1.1(iii) | Data minimisation; pickers instead of full access | Partly covered | forced-login-or-permissions | 2026-11-03 | Unneeded permissions and full-library access are checked; collecting more than needed on a server is not. |
| 5.1.1(iv) | Respect permission settings; no tricked or forced consent; alternatives | Covered | forced-login-or-permissions | 2026-11-03 |  |
| 5.1.1(v) | Login only with account features; in-app account deletion; personal data; social network rules | Partly covered | forced-login-or-permissions, account-deletion-missing | 2026-11-03 | Social network token storage and in-app revocation are not checked. |
| 5.1.1(vi) | Secretly discovering passwords or private data | Covered | deceptive-app-behavior | 2026-11-03 |  |
| 5.1.1(vii) | SafariViewController visible, no tracking without consent | Partly covered | deceptive-app-behavior | 2026-11-03 | A hidden or obscured SafariViewController is checked; tracking through a visible one is not. |
| 5.1.1(viii) | Compiling personal data not from the user or without consent | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 5.1.1(ix) | Regulated fields submitted by a legal entity; cannabis geo-restricted | Can't tell from code | restricted-app-type | 2026-11-03 | The submitting entity is in the developer account. |
| 5.1.1(x) | Basic contact details optional | Covered | forced-login-or-permissions | 2026-11-03 |  |
| 5.1.2 | Data use and sharing (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (i) to (vii). |
| 5.1.2(i) | Permission before use or sharing; disclose third parties including AI; ATT; no required system features | Partly covered | ai-data-disclosure, tracking-without-att, trackers-before-consent, privacy-notice-incomplete, forced-login-or-permissions | 2026-11-03 | Sharing limited to improving the app or serving ads is not checked on its own. |
| 5.1.2(ii) | No reuse for another purpose without consent | Partly covered | protected-data-misuse | 2026-11-03 | Ordinary permission data sent to ad or analytics SDKs is raised as Maybe, since further consent may have been asked; other reuse can't be seen. |
| 5.1.2(iii) | No secret profiles; no identifying anonymous users | Partly covered | tracking-without-att | 2026-11-03 | Fingerprinting and re-identification code are checked. |
| 5.1.2(iv) | No contact databases from Contacts or Photos; no installed-app scans for ads | Covered | protected-data-misuse | 2026-11-03 |  |
| 5.1.2(v) | Contacting people from Contacts or Photos: user-initiated, no Select All, preview | Covered | deceptive-app-behavior | 2026-11-03 |  |
| 5.1.2(vi) | HomeKit, HealthKit, Clinical Health Records, MovementDisorder, ClassKit and face-mapping data not for ads or data mining | Covered | protected-data-misuse | 2026-11-03 | All the listed APIs are named in the check. |
| 5.1.2(vii) | Apple Pay data shared only to deliver goods and services | Covered | protected-data-misuse | 2026-11-03 |  |
| 5.1.3 | Health and health research (intro) | Doesn't concern apps | - | 2026-11-03 | Heading and intro; see (i) to (iv). |
| 5.1.3(i) | Health data not for ads or data mining; direct-benefit exception; disclose health data collected | Partly covered | protected-data-misuse | 2026-11-03 | Disclosing the specific health data collected is not checked. |
| 5.1.3(ii) | No false data in HealthKit; no personal health data in iCloud | Covered | protected-data-misuse | 2026-11-03 |  |
| 5.1.3(iii) | Consent for health research | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 5.1.3(iv) | Ethics board approval for health research | Can't tell from code | restricted-app-type | 2026-11-03 | Approval is a document outside the code. |
| 5.1.4 | Kids (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (a) and (b). |
| 5.1.4(a) | Children's privacy laws; birth date and parental contact only to comply; no third-party analytics or ads in apps mainly for kids | Partly covered | age-handling, child-app-sdks-ads | 2026-11-03 | Useful function for every age is not checked. |
| 5.1.4(b) | Limited third-party services; privacy policy for kids' data; "For Kids" wording | Partly covered | child-app-sdks-ads, privacy-policy-missing, age-handling, store-listing-review | 2026-11-03 | "For Kids" wording in the listing is App Store Connect. |
| 5.1.5 | Location Services: only when relevant, consent first, explain the purpose | Partly covered | permission-purpose-strings, forced-login-or-permissions | 2026-11-03 | The ban on location for emergency services or vehicle control is not checked. |
| 5.2 | Intellectual property (intro) | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 5.2.1 | Third-party material without permission; misleading names | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 5.2.2 | Third-party sites and services used within their terms | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 5.2.3 | Audio and video downloading; illegal file sharing | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 5.2.4 | Apple endorsements (heading) | Doesn't concern apps | - | 2026-11-03 | Heading; see (a) and (b). |
| 5.2.4(a) | No implied Apple endorsement | Can't tell from code | content-rights-unclear | 2026-11-03 |  |
| 5.2.4(b) | Editor's Choice badge applied by Apple | Doesn't concern apps | - | 2026-11-03 | Describes what Apple does. |
| 5.2.5 | Apple look-alikes, Apple emoji, music previews, Activity rings, WeatherKit attribution | Can't tell from code | content-rights-unclear, apple-feature-rules | 2026-11-03 |  |
| 5.3 | Gaming, gambling and lotteries (intro) | Can't tell from code | restricted-app-type | 2026-11-03 | India real-money games: also regulated-field-present. |
| 5.3.1 | Sweepstakes and contests sponsored by the developer | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 5.3.2 | Official rules in the app; Apple not a sponsor | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 5.3.3 | No IAP for real-money gaming credit | Can't tell from code | restricted-app-type | 2026-11-03 |  |
| 5.3.4 | Real-money gaming and lotteries licensed, geo-restricted, free | Can't tell from code | restricted-app-type | 2026-11-03 | Licences are outside the code. |
| 5.4 | VPN apps | Can't tell from code | restricted-app-type | 2026-11-03 | Licence information goes in the App Store Connect review notes. |
| 5.5 | Mobile device management | Can't tell from code | restricted-app-type | 2026-11-03 | The MDM capability is requested from Apple. |
| 5.6 | Developer Code of Conduct: respect, no preying on users or forcing unnecessary data | Partly covered | forced-login-or-permissions, renewal-terms-checkout | 2026-11-03 | Forced data sharing and unclear purchase terms are checked; conduct toward Apple and customers can't be seen in code. |
| 5.6.1 | App Store reviews: respectful replies; use the provided review API | Partly covered | custom-review-prompt | 2026-11-03 | Replies to reviews are in App Store Connect. |
| 5.6.2 | Developer identity accurate and current | Can't tell from code | store-listing-review | 2026-11-03 | App Store Connect and the developer account. |
| 5.6.3 | Discovery fraud | Partly covered | custom-review-prompt | 2026-11-03 | Incentivised and filtered review prompts are checked; chart, search and referral manipulation can't be seen. |
| 5.6.4 | App quality: customer reports, reviews and refund requests | Doesn't concern apps | - | 2026-11-03 | Describes how Apple judges conduct from reviews and refunds. |
| After You Submit | Timing, status, expedite requests, release date, rejections, appeals, bug fix submissions | Doesn't concern apps | - | 2026-11-03 | Review process steps in App Store Connect. |
