# Platforms

## permission-at-launch
- title: Permissions requested at app launch
- area: platforms
- needs: mobile app
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (android): `ActivityCompat.requestPermissions`, `requestPermissions` or a `RequestMultiplePermissions` launcher called in the launcher activity's `onCreate` or in `Application.onCreate`, especially for several permissions at once. Cite the call.
  - code (ios): permission requests (`AVCaptureDevice.requestAccess`, `requestWhenInUseAuthorization`, `CNContactStore().requestAccess`, `PHPhotoLibrary.requestAuthorization`, `UNUserNotificationCenter.current().requestAuthorization`, `ATTrackingManager.requestTrackingAuthorization`).
  - code (ios): any of those in `didFinishLaunchingWithOptions`, or in the first screen's `viewDidLoad` or `onAppear`. Cite the calls.
  - code (React Native and Expo): `requestCameraPermissionsAsync`, `requestForegroundPermissionsAsync`, `Notifications.requestPermissionsAsync` or `PermissionsAndroid.request` in the root component's first `useEffect`. Cite the calls.
  - ask: none
- why: Asking for everything at launch, before people see why, gets more denials, and a denied permission may never be offered again.
- fix: Ask for each permission when the user starts the feature that needs it, after a short explanation, and keep the app usable if they say no.
- exceptions: A permission the app cannot work without at all, such as location in a navigation app, may be asked at launch with an explanation.
- elsewhere: none

## permission-purpose-strings
- title: Vague or missing permission purpose strings
- area: platforms
- needs: iOS app
- severity: High
- evidence-default: confirm
- look-for:
  - code (ios): usage description keys in `Info.plist`, or in Expo `app.json` under `ios.infoPlist` (`NSCameraUsageDescription`, `NSLocationWhenInUseUsageDescription`, `NSContactsUsageDescription`, `NSMicrophoneUsageDescription`, `NSPhotoLibraryUsageDescription`, `NSUserTrackingUsageDescription`).
  - code (ios): confirm each one whose text does not say what the data is used for, such as "Required for app features." Cite each vague string.
  - code (ios): code that asks for a protected resource with no matching usage description key.
  - ask: none
- why: Apple requires purpose strings that clearly describe how the data is used, and rejects apps that lack them.
- fix: Rewrite each string as one specific sentence that says how and why, for example "Your location is used to show stores near you."
- exceptions: Expo config plugins can add default strings; check the configured text before reporting.
- elsewhere: none

## store-data-disclosure
- title: App store privacy forms may not match the code
- area: platforms
- needs: mobile app
- severity: High
- evidence-default: maybe
- look-for:
  - code: list what the app collects and which SDKs it ships (analytics, crash reporting, ads, location, contacts, installed apps, health, financial data, identifiers, AI); all of it must appear in App Store Connect "App Privacy" and in the Play Console "Data safety" form.
  - code: the forms are not in the repo, so report `Maybe: check on your own`, name the data types and SDKs to declare, and use the build file, Podfile or `package.json` as the location.
  - ask: have you filled in App Privacy and Data safety, and do they include the SDKs found? Does the app or any SDK sell personal data, or use it for purposes users weren't told about?
- why: Both stores require you to declare all data the app and its SDKs collect, and a mismatch can get the app rejected or removed.
- fix: In App Store Connect (App Privacy) and Play Console (Data safety), declare every data type found, including data collected by SDKs, and update the answers when the app changes. On Google Play, also stop any sale or undisclosed use of the data, including by SDKs.
- exceptions: Does not apply to apps not distributed through the App Store or Google Play.
- elsewhere: none

## prominent-disclosure-missing
- title: No in-app disclosure before collecting data users wouldn't expect
- area: platforms
- needs: mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code (android): unexpected data use: background location, installed-apps lists (`getInstalledPackages`), contacts or call logs sent off the device, screen recording (`MediaProjection`), an `AccessibilityService`, or an SDK collecting such data by default. Cite it.
  - code: no in-app screen, just before that request or collection, naming the data, the feature using it and any sharing; a privacy policy, terms or store text alone does not count.
  - code: a consent dialog that counts back, tapping outside or a timeout as yes, closes itself, is bundled with unrelated text, or lets collection start before the user agrees.
  - ask: none
- why: Google Play requires a prominent in-app disclosure and affirmative consent before collecting personal or sensitive data users may not expect, such as background data.
- fix: Just before the runtime prompt or a consent step with a decline option, show a disclosure like "[App] collects [data] to enable [feature], even when the app is closed", naming any sharing.
- exceptions: Data use clearly expected from a feature the user just started (camera for a photo) needs only the runtime prompt. A disclosure followed at once by the runtime prompt needs no Accept button, so never confirm on a missing button alone. Requests at launch: see permission-at-launch. Applies to apps on Google Play.
- elsewhere: none

## restricted-permission-declared
- title: Restricted permission or API without a permitted core use
- area: platforms
- needs: Android app
- severity: High
- evidence-default: confirm
- look-for:
  - code (android): SMS or Call Log, `MANAGE_EXTERNAL_STORAGE`, `ACCESS_BACKGROUND_LOCATION`, `READ_MEDIA_IMAGES`/`_VIDEO`, `QUERY_ALL_PACKAGES`, `REQUEST_INSTALL_PACKAGES`, `USE_EXACT_ALARM`, `USE_FULL_SCREEN_INTENT`, `BODY_SENSORS`, `android.permission.health.*`.
  - code (android): an `AccessibilityService` or `VpnService`, a foreground service with no matching type and permission, or a user-initiated data transfer job started without a user action.
  - code: confirm only when the app's purpose (README, listing, screens) clearly fits no permitted use or exception on Play's Help page for that permission; if it might, or a photo feature the picker can't serve needs media access, report Maybe.
  - code: allowed outside the default SMS, Phone or Assistant role: SMS or Call Log for backup, caller ID and spam blocking, companions, sync, automation, enterprise or CRM, proxy calls, emergency SMS, cell broadcast, UPI and banking, budget tracking. Exact alarms: alarm, timer, calendar apps.
  - code: all-files access fits file managers, backup, antivirus, document management, search, encryption, device migration, carrier, OEM and Managed Google Play private apps.
  - code: fine location where coarse would do, background location for a non-core feature, or location only for ads or analytics; loan, credit or earned-wage apps with contacts, fine location, media, storage, phone numbers or all-packages access.
  - code: permissions added by libraries or Expo plugins (expo-location `isAndroidBackgroundLocationEnabled`) count; Maybe if only the merged manifest would show one. Contacts, fine location and local network on API 37+: see exceptions.
  - ask: which core feature needs each restricted permission?
- why: Google Play allows restricted permissions and sensitive APIs only for listed core uses, usually with a declaration, and rejects or removes other uses.
- fix: Remove permissions the core feature doesn't need and use the narrow option (photo picker, Storage Access Framework, SMS Retriever, coarse or foreground location, a targeted `<queries>` block); for a permitted use, describe it in the listing and declare it.
- exceptions: Media limits apply from target API 33, all-files and package visibility from API 30. Private and enterprise device management apps are exempt from the media, contacts and local-network limits. Coming for apps targeting API 37+: contacts and precise location from 27 January 2027, local network from 25 August 2027; manage contacts (API 38+) from 25 August 2027.
- elsewhere: none

## target-api-too-low
- title: Android target API level below Google Play's minimum
- area: platforms
- needs: Android app
- severity: High
- evidence-default: confirm
- look-for:
  - code (android): `targetSdk` or `targetSdkVersion` in the Gradle files or version catalog (React Native: `android/build.gradle`). Since 31 August 2026 new apps and updates must target API 36 (Wear OS and Automotive 35, TV and XR 34). Cite the line.
  - code (Expo and Flutter): the level comes from expo-build-properties `android.targetSdkVersion`, `flutter.targetSdkVersion` or the framework version; with none stated, report Maybe and name the version.
  - ask: none
- why: Google Play rejects new apps and updates with an old target API level and hides lagging apps from new users on newer Android versions.
- fix: Raise `targetSdk` to 36 (or the form factor's level), test each skipped version's behaviour changes, and publish an update. Apps left un-updated need at least 35 (Wear OS and XR 34, TV 33, Automotive 32) to stay visible to new users on newer devices.
- exceptions: Permanently private apps for one organisation, and apps not on Google Play, are out of scope. The extension to 1 November 2026 has passed.
- elsewhere: none

## unsafe-code-loading
- title: App downloads code or updates itself outside the store
- area: platforms
- needs: mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code (android): `DexClassLoader`, `InMemoryDexClassLoader`, `PathClassLoader` or `System.load` used on files the app downloads (`.dex`, `.jar`, `.so`, `.apk`). Cite the call.
  - code (android): a downloaded APK installed (`PackageInstaller`, `ACTION_INSTALL_PACKAGE`, `application/vnd.android.package-archive`) to update the app or add apps the user didn't choose.
  - code (android): `addJavascriptInterface` on a WebView loading `http://` pages or URLs from intents or deep links.
  - code (ios): code downloaded and run to add or change features (`eval` of fetched JavaScript, `JSContext.evaluateScript` or `dlopen` on downloaded files, a remote bundle that loads a different app). Cite the call.
  - ask: none
- why: Both stores bar downloading code that changes features outside review, and Google Play also bans self-updates and code that opens security holes.
- fix: Ship code changes as store updates (on Android, the Play In-App Updates API), and remove the JavaScript interface or load only HTTPS pages you control in that WebView.
- exceptions: Over-the-air JavaScript updates (Expo Updates, CodePush) and JavaScript in a WebView or interpreter are allowed if the new code follows store policy. App Store: flag them only when the code shows new or changed features, else Maybe; teaching apps may run viewable, editable student code. Device management apps, and browsers, messaging, file-sharing, backup, transfer and companion apps (user-chosen packages), may install packages. Mini apps: see apple-feature-rules.
- elsewhere: none

## deceptive-app-behavior
- title: Hidden, deceptive or unconsented app behaviour
- area: platforms
- needs: mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code: features switched on by reviewer, emulator or region checks, dates, secret gestures or remote flags that the listing and review notes don't describe (a different app, gambling, adult content, outside payments). Cite the check.
  - code (android): hiding the launcher icon (`setComponentEnabledSetting`), or changing the wallpaper, ringtone, shortcuts, default apps or other settings without a user action and a way to undo it.
  - code: fake system dialogs or virus or battery warnings, third-party ads sent as system notifications, or prompts to turn off Play Protect.
  - code: SMS, email or invites sent for the user (`SmsManager.sendTextMessage`, contact invites) with no screen first showing the text and recipients; on the App Store also who it appears to come from, and no "Select all" or all-selected default for contacts.
  - code (ios): views used out of sight (zero-size, transparent or offscreen `SFSafariViewController` or web views), or silent pasteboard or keystroke reading to collect passwords or private data.
  - code: on-device crypto mining (miner libraries, `stratum+tcp://` URLs); extra downloads started before showing their size.
  - code (android): tracking another person without the `IsMonitoringTool` flag, a persistent notification and store disclosure; device admin or accessibility used to block uninstalling; rooting without telling the user; bypassing other apps' `FLAG_SECURE` or `REQUIRE_SECURE_ENV`.
  - ask: none
- why: Both stores remove apps that hide features, mislead users or reviewers, collect data in secret or send messages for users without their say.
- fix: Remove the hidden or deceptive path, describe every feature in the listing and review notes, and ask the user before changing a setting (with a way to undo it), sending a message or starting a large download.
- exceptions: Rollout flags, A/B tests and regional differences described in the listing or review notes are fine; Maybe if a flag unlocks something undescribed. Play-compliant parental-control and enterprise monitoring apps, prefilled messages the user sends from their own app, the app's own deals in notifications and remote mining management are allowed. Downloaded code: see unsafe-code-loading. Fake virus warnings: see scareware-warnings. AppFunctions rules start 14 April 2027.
- elsewhere: none

## store-content-policy
- title: App content or listing may break store content rules
- area: platforms
- needs: mobile app
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: report Maybe and cite the screen when the app shows or sells: sexual or hookup content, hate, defamation or inflammatory religious commentary, graphic violence, extremism, bullying, child exploitation or trafficking.
  - code: weapons, drugs, marijuana, tobacco or vapes, fake documents, false health claims, content exploiting tragedies, prank or anonymous calls or texts, fake device data, or user content mainly for porn, random or anonymous chat, "hot-or-not" voting or bullying.
  - code (Google Play): listing files with ranking or price claims, emoji or capitals in the title, or a title over 30 characters; near-identical apps; TV, Wear OS, Auto or XR targets (own quality rules); no ad rating cap matching the app; custom emoji libraries lagging Unicode.
  - ask: does the app show or sell any of this content?
- why: Both stores remove apps whose content breaks their rules, and Google Play also checks listings and basic quality.
- fix: Remove the restricted content or the feature offering it, keep the Play listing accurate (no rankings, prices or emoji in the title), cap ad content at the app's rating, and answer rating questions truthfully.
- exceptions: Educational, documentary, scientific or artistic content may be allowed with context; professional political satire is generally exempt from Apple's defamation rule. Brands and licences: see content-rights-unclear. Wrapped websites: see webview-only-app. Licensed regulated sales: see restricted-app-type.
- elsewhere: none

## sign-in-with-apple-missing
- title: Social login without Sign in with Apple or an equal private login
- area: platforms
- needs: iOS app with accounts
- severity: High
- evidence-default: confirm
- look-for:
  - code (ios): a third-party or social login for the user's main account: Google Sign-In (`GIDSignIn`, `@react-native-google-signin`), Facebook Login (`FBSDKLoginKit`), X, LinkedIn, Amazon or WeChat login, or social providers in Firebase Auth, Auth0, Supabase or Clerk. Cite the sign-in screen.
  - code (ios): no Sign in with Apple beside it (`ASAuthorizationAppleIDProvider`, `SignInWithAppleButton`, `expo-apple-authentication`, the `com.apple.developer.applesignin` entitlement), and no other login offered that collects only name and email, can hide the email and doesn't track for ads.
  - ask: none
- why: Apple requires apps with a third-party or social login for the main account to also offer one that limits data to name and email, can hide the email and doesn't track for ads without consent.
- fix: Add Sign in with Apple beside the other social buttons (`ASAuthorizationAppleIDButton`, `expo-apple-authentication`), or another login with the same three privacy features.
- exceptions: Not needed for apps using only their own accounts, alternative-marketplace apps using its login, apps requiring an existing education or enterprise account, government or industry citizen IDs, or a client for one third-party service holding the user's content. Social login only for sharing or invites is not this mistake.
- elsewhere: none

## forced-login-or-permissions
- title: App demands sign-in, personal details or permissions it doesn't need
- area: platforms
- needs: mobile app
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (ios): everything behind sign-in though the main features (browsing, reading, on-device tools) need no account. Cite the gate.
  - code (ios): permissions or full-library access the features don't use, or full Photos or Contacts access where a picker would do (`PHPickerViewController`, `CNContactPickerViewController`). Cite the request.
  - code: a denied non-critical permission (location, notifications, tracking, contacts, call log) blocks the app, a paid feature or a reward with no alternative, closes the app or asks again in a loop, such as no manual address entry when location is denied.
  - code (ios): personal fields required that the feature doesn't need, or paid features that also need extra tasks (social posts, uploading contacts, repeated check-ins).
  - ask: none
- why: Both stores require apps to respect a denied permission, and Apple also rejects apps that demand a login, personal details or permissions the features don't need.
- fix: Let people use features without an account where possible, ask only for permissions a feature uses (prefer system pickers), make personal fields optional unless needed, and offer another way when a permission is denied.
- exceptions: Account-based apps (messaging, banking, social networks, synced data) may require sign-in, and data a law or the feature needs may be required. A permission the app can't work without may be required. Asking at launch, then carrying on if denied, is permission-at-launch. Birth date and parental contact asked only for children's privacy laws are allowed.
- elsewhere: none

## webview-only-app
- title: App is only a wrapped website, static content or a set of links
- area: platforms
- needs: mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code: the only real screen is a web view of a live site (root `WKWebView` or `WebView`, `react-native-webview` as the only screen, Capacitor or Cordova `server.url` on a live site), with no native features. Cite it.
  - code: the app is mainly marketing, ads, web clippings, a feed of others' content, a list of links, or static text or a PDF, with no features of its own.
  - code (ios): the app needs another app installed to work, or downloads first-launch resources without stating the size and asking.
  - ask: is the website your own, or used with its owner's permission?
- why: Both stores reject apps that are only a website, static content, marketing, ads or links, and Google Play also bans webviews of others' sites without permission.
- fix: Add features that work as an app (native screens, offline use, device features the service needs), or offer it as a website; show the size and ask before first-launch downloads.
- exceptions: Web views for some screens (help, terms, checkout, articles) beside native features are fine, and so are catalogs. Maybe when the native part is small but real. Google Play: a webview of your own or a permitted site is not webview spam, but a thin wrapper can still fail its limited-functionality rule (Maybe).
- elsewhere: none

## placeholder-content
- title: Placeholder or unfinished content in the app
- area: platforms
- needs: iOS app
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (ios): user-facing text in screens or string files with "Lorem ipsum", "TODO", "TBD", "Test", sample names, or "Coming soon" on features that do nothing. Cite the line.
  - code (ios): buttons or menu items with empty handlers or "not implemented" alerts, empty screens, and links shown to users that point at `#`, `about:blank` or placeholder domains.
  - code (ios): support, privacy or terms links in the app that point at pages that don't exist or are empty.
  - ask: none
- why: Apple rejects submissions with placeholder text, empty websites, broken links or features that don't work.
- fix: Finish or remove placeholder text, hide unfinished features from the release build, and point every link at a live page.
- exceptions: Placeholders in tests, previews (`#Preview`, Storybook), debug-only code and comments don't ship, and input hints (`placeholder` attributes) are fine. Backend URLs are not user-facing links; a live backend for review: see store-listing-review.
- elsewhere: none

## protected-data-misuse
- title: Protected personal data used for ads, third parties or other purposes
- area: platforms
- needs: mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code (ios): HealthKit, Clinical Health Records, Motion and Fitness, MovementDisorder, HomeKit, ClassKit or face or depth data sent to ad, marketing or analytics SDKs or used for data mining; Apple Pay data shared beyond delivery. Cite the line.
  - code (ios): other permission data (location, contacts, photos) sent to ad or analytics SDKs: Maybe, since sharing for ads or improvement is allowed with disclosure and permission, and a new purpose needs further consent.
  - code (ios): the whole address book uploaded to build a contact database; installed-app checks (`canOpenURL` over a long `LSApplicationQueriesSchemes` list) for analytics or ads; health data stored in iCloud; false data written to HealthKit.
  - code (android): Health Connect data sent to ads, data brokers, lenders or other third parties without explicit consent for a listed reason, or Age Signals data used for ads, analytics or profiling, or shared. Cite the call.
  - code (Google Play): financial or government ID numbers, or users' non-public contacts, shown to other users or made public. Cite it.
  - ask: none
- why: Both stores keep health and other protected data out of ads and third-party sharing; Apple also bars reuse without consent, and Google Play bars publishing ID numbers or private contacts.
- fix: Keep protected data (HealthKit, HomeKit, ClassKit, health research, face mapping, Health Connect, Age Signals) away from ads, marketing and third parties; disclose other sharing and ask again before a new use; keep health data out of iCloud; show ID numbers and contacts only to their owner.
- exceptions: App Store: health data may give the user a direct benefit (such as a lower premium) when the entity giving it submits the app and shares nothing with third parties; health research needs permission; Apple Pay data may go to third parties only to deliver the goods. Google Play: Health Connect transfers with explicit consent for security, legal or merger reasons, and Age Signals sharing required by law, are allowed. Invites: see deceptive-app-behavior.
- elsewhere: none

## custom-review-prompt
- title: Custom or incentivised review prompt
- area: platforms
- needs: mobile app
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (ios): a home-made "Rate us" dialog or screen that opens the App Store review page (`itms-apps://` or `apps.apple.com` with `action=write-review`) instead of `SKStoreReviewController.requestReview`, SwiftUI's `requestReview` or `expo-store-review`. Cite the dialog.
  - code: rewards (coins, unlocks, discounts) for rating or reviewing; on the App Store also features locked until the user rates, reviews or downloads another app, or a "Do you like the app?" step that sends only happy users to the store.
  - ask: none
- why: Both stores bar incentivised or manipulated ratings and reviews, and Apple also bars custom review prompts and filtered or forced reviews.
- fix: On iOS use `SKStoreReviewController.requestReview(in:)`, SwiftUI's `requestReview` or `expo-store-review`, ask everyone alike, and give no reward for ratings or reviews.
- exceptions: A settings link the user taps to write a review is not a prompt. Rewards for in-app actions (finishing a level) are allowed. Google Play bars incentives, not custom prompts, so on Android a home-made prompt alone is not a finding. Fake reviews shown in the app: see fake-reviews.
- elsewhere: none

## store-listing-review
- title: Store listing, forms and review access to check on your own
- area: platforms
- needs: mobile app
- severity: Medium
- evidence-default: maybe
- look-for:
  - code (ios): report Maybe, naming what review needs: a demo account or mode, a live backend, IAP products set up, flagged features described in the notes; age rating answers for user content, chat, web access, gambling, mature or medical content and ads.
  - code (ios): a name of 30 characters at most, "For Kids" only in the Kids Category, a support contact, subscription periods of 7 days or more in one group, template-built apps submitted by the content provider, and one app, not copies per city or venue.
  - code (Google Play): forms the code makes relevant: the Permissions Declaration Form per restricted permission, foreground service and full-screen intent, Health apps and Financial features (every app), Target audience and content, ads, the IARC rating and News declarations.
  - code (Google Play): app access details or a demo account; the Child Safety Standards link and contact for social, dating and chat apps; age-restriction tools for dating, chat and real-money apps; an organisation account for finance, health, VPN or government apps; trader status; package names.
  - ask: have you completed these store forms, and do they match the code?
- why: Both stores reject apps with incomplete or inaccurate listings, ratings, declarations or review access, which live in App Store Connect and Play Console.
- fix: Give review access and notes for non-obvious features, answer the rating questions honestly, complete each Play declaration from what the code and SDKs do, and keep listings accurate.
- exceptions: Only for apps on the App Store or Google Play. Privacy answers: see store-data-disclosure. Licences and banned app types: see restricted-app-type.
- elsewhere: none

## restricted-app-type
- title: App type the stores restrict or license
- area: platforms
- needs: mobile app
- severity: High
- evidence-default: maybe
- look-for:
  - code: raise only for a restricted field, naming it: loans, credit, earned-wage, banking, trading, crypto, NFTs, gambling, contests, lotteries, fantasy sports, VPN, device management, medical or dosage tools, health research, tobacco, drugs, alcohol; on the App Store also insurance and fundraising.
  - code (ios): or an Apple-restricted type: crime reports, risky challenges, people search, app stores, home-screen replacements, remote desktop, rank manipulation, low-effort copies.
  - code (Google Play): loan apps must give the repayment period, maximum APR and a cost example in the listing, and health apps a medical device declaration or disclaimer; binary options and loans due in 60 days or less are banned.
  - ask: are you licensed for this field in each target country, and have you made the store's application?
- why: Both stores ban some app types and allow others only with licences, applications, an organisation account, disclosures or geo-restriction.
- fix: Read each store's rule for the field: get the licences, make Play's gambling application or declarations, use an organisation account, add the listing disclosures, and have medical apps remind users to consult a doctor. Apple, for example, caps loan APR at 36% and bars full repayment within 60 days.
- exceptions: Raise nothing outside these fields, or for apps that only give general information and handle no money, prizes, tokens or health data. Licensed pharmacies and cannabis dispensaries may sell on the App Store, geo-restricted; Google Play bans marijuana sales. Indian real-money gaming: see regulated-field-present.
- elsewhere: none

## apple-feature-rules
- title: Apple rules for specific features to check on your own
- area: platforms
- needs: iOS app
- severity: Medium
- evidence-default: maybe
- look-for:
  - code (ios): raise only for features used, naming the guideline: ads (2.5.18), extensions, widgets, keyboards, App Clips (2.5.16, 4.4), Siri (2.5.11), CallKit or SMS filters (2.5.12), face login (2.5.13), recording (2.5.14), Matter (2.5.17), background modes (2.5.4).
  - code (ios): browser engines (2.5.6), private APIs (2.5.1), file pickers (2.5.15), ARKit (4.2.1), Apple Music (4.5.2), Game Center (2.5.3, 4.5.3, 4.5.5), mini apps (4.7), Apple Pay (4.9), Wallet (1.5, 3.2.1(iv)), Mac or TV builds (2.4.3, 2.4.5).
  - code (ios): iPhone-only builds (2.4.1), battery use (2.4.2), restart prompts (2.4.4), IPv6 (2.5.5), changed switches or blocked links (2.5.9), region blocks (3.2.2(v)), charging for built-in features (4.10).
  - ask: none
- why: Apple sets extra rules for many frameworks and features that code alone can't show are met.
- fix: Read each feature's guideline before submitting; for example, interstitial ads need a close button, extensions carry no ads, and recording needs consent and an indicator.
- exceptions: Raise nothing for unused features.
- elsewhere: none
