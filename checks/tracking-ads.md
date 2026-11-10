# Tracking and ads

## trackers-before-consent
- title: Analytics or ad trackers load before consent
- area: tracking-ads
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code (web): analytics or ad scripts (`googletagmanager.com`, `gtag(`, Google Analytics, Meta Pixel `fbq(`, Hotjar, TikTok pixel, Segment, Mixpanel, PostHog) rendered with no consent check first. A script placed unconditionally in the root layout or `index.html` is typical. Cite the line.
  - code (mobile): Firebase Analytics, the Facebook SDK, AppsFlyer or similar starting at launch with no consent gate and no setting that turns collection off until consent (`firebase_analytics_collection_enabled`, `setAnalyticsCollectionEnabled(false)`).
  - site: with a browser, load the page fresh, choose nothing, and record cookies and third-party requests; analytics or ad requests before any choice give `Confirmed on live site`. Without a browser, read the HTML and mark the network check `Not tested`, as some scripts only show in a real browser.
  - ask: none
- why: Storing or reading identifiers on a visitor's device for analytics or ads needs consent first in the EU, and India's DPDP Act needs consent for this kind of processing from 13 May 2027.
- fix: Load analytics and ad scripts only after the visitor accepts, with a reject button as easy as accept. For example, render the gtag scripts only when the stored consent value is "granted".
- exceptions: Strictly necessary cookies (login, cart, security) need no consent. Cookieless analytics with no personal data may not need consent (Maybe if unsure), except in App Store apps: Apple asks for consent even for anonymous usage data unless the app meets GDPR legitimate interest or a similar law (Maybe then). UK: some statistics or appearance storage needs no consent under the PECR rule's conditions: report Maybe, never clear it from code alone; ad tags still do. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## session-replay-consent
- title: Session replay records visitors without consent
- area: tracking-ads
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code: a session replay SDK started with no consent check: LogRocket (`LogRocket.init`), FullStory, Hotjar recordings, Microsoft Clarity, Smartlook, Mouseflow, PostHog session recording, Sentry Replay (`replayIntegration`). Cite the line that starts it.
  - code: note whether inputs are masked; unmasked inputs make the problem worse.
  - site: with a browser, look for requests to the replay vendor before any consent choice
  - ask: none
- why: Replay tools record what visitors type and click, which needs consent in the EU and has been sued as wiretapping in California.
- fix: Start the replay SDK only after consent (call `LogRocket.init` inside the consent-granted branch), mask all inputs, and name the vendor in the privacy policy. In iOS apps, also show a clear sign while recording.
- exceptions: Error monitoring without replay (plain Sentry errors) is not session replay. California courts are split on these claims, so the US rule is a risk, not a settled ban. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## disruptive-ads
- title: Ads that interrupt, trick or show outside the app
- area: tracking-ads
- needs: ads in a mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code: full-screen ads that show unexpectedly: video ads before the splash or loading screen, ads on back or exit, at the start of a level or content, or after each tap or screen change (`InterstitialAd` `show` calls in navigation or button handlers one after another). Cite the call.
  - code: full-screen ads with no close button or not closeable after 15 seconds; ads placed where users usually tap, styled as app buttons or features, or sent as notifications.
  - code: ads shown while the app is not in the foreground (overlay windows, `SYSTEM_ALERT_WINDOW`, lockscreen activities), hidden or zero-size ad views, or code that clicks ads for the user.
  - ask: none
- why: Google Play bans ads that appear unexpectedly, can't be dismissed, mimic app or system UI or show outside the app, and treats hidden ads and automatic clicks as ad fraud.
- fix: Show full-screen ads only at natural breaks (after a level or a finished task), never before the splash screen, on exit or after consecutive taps; give each one a visible close within 15 seconds; label ads clearly and keep them inside your app's screens.
- exceptions: Rewarded ads the user chooses to watch, and banners or ads inside video content that don't block use, are allowed. Full-screen ads the user opts into, or shown where they don't interrupt (after a score screen), may stay up longer than 15 seconds. Lockscreen ads are allowed only in apps whose sole purpose is a lockscreen. The app's own deals in its notifications are allowed. Apps for children: see child-app-sdks-ads. Marketing push notifications: see push-marketing-consent. Ads disguised as content for users in India: see sponsored-listing-unlabelled. Only for apps on Google Play.
- elsewhere: none

## device-id-linking
- title: Device identifiers linked or used against store rules
- area: tracking-ads
- needs: Android app
- severity: High
- evidence-default: confirm
- look-for:
  - code (android): persistent identifiers (`Settings.Secure.ANDROID_ID`, `getImei`, `getDeviceId`, `getSubscriberId`, `getSimSerialNumber`, `Build.getSerial`, MAC address) sent together with personal data (email, phone, user id, location) or with the advertising ID. Cite the call.
  - code (android): the advertising ID (`AdvertisingIdClient`) joined to an email, phone or user id for analytics, used without checking the ads-personalisation opt-out, or a reset ID linked to the old one; the App Set ID used for ads or ad measurement.
  - ask: none
- why: Google Play allows persistent device identifiers to be linked to personal data only for telephony and enterprise uses, and allows the advertising ID only for ads and analytics under strict linking and opt-out rules.
- fix: Use the advertising ID only for ads and analytics, check `isLimitAdTrackingEnabled` on each access, use the App Set ID or a random app-made ID for analytics and fraud checks, never link ANDROID_ID, IMEI or MAC to user data or the advertising ID, and disclose ID use in the privacy policy.
- exceptions: Wi-Fi calling tied to a SIM identity and enterprise device-owner apps may link persistent identifiers, with prominent disclosure. The advertising ID may be linked to personal data for advertising with the user's explicit consent. Only for apps on Google Play.
- elsewhere: none

## tracking-without-att
- title: Tracking on iOS without App Tracking Transparency permission
- area: tracking-ads
- needs: iOS app
- severity: High
- evidence-default: confirm
- look-for:
  - code (ios): tracking across other companies' apps and sites: the advertising identifier (`advertisingIdentifier`), ad networks (Google Mobile Ads, Meta, AppLovin, Unity Ads), attribution SDKs (AppsFlyer, Adjust, Branch, Singular), or the Facebook SDK with advertiser tracking on. Cite the start call.
  - code (ios): no `ATTrackingManager.requestTrackingAuthorization` (or `expo-tracking-transparency`, `react-native-tracking-transparency`) before those start, no `NSUserTrackingUsageDescription`, or tracking that still runs when the answer is not authorised.
  - code (ios): fingerprinting or re-identification: an identifier built from device signals (model, fonts, IP address, settings), or "anonymised" data matched back to people.
  - ask: none
- why: Apple requires explicit permission through App Tracking Transparency before an app tracks people's activity, and bars secret profiling and re-identifying anonymous users.
- fix: Add `NSUserTrackingUsageDescription`, call `ATTrackingManager.requestTrackingAuthorization` before starting tracking SDKs, start them with tracking and the advertising identifier off unless the answer is `.authorized`, and remove fingerprinting code.
- exceptions: Apple's tracking page (linked from 5.1.2(i)) defines tracking as linking app data with other companies' data for targeted ads or ad measurement, or sharing it with data brokers. Analytics the developer keeps for itself, with no advertising identifier (for example Firebase Analytics with ad features off), is not that by itself; report Maybe if unsure. Consent before analytics in general: see trackers-before-consent.
- elsewhere: none

## opt-out-signal-ignored
- title: Ad tags ignore opt-out signals and no "Do Not Sell or Share" link
- area: tracking-ads
- needs: ad or retargeting tags on a website
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (web): third-party ad or retargeting tags (Meta Pixel `fbq(`, Google Ads `AW-` conversion tags, TikTok `ttq`, LinkedIn, Pinterest, Snap or Reddit pixels) that load with no check of `navigator.globalPrivacyControl` in the page or the `Sec-GPC` header on the server. Cite the tag.
  - code (web): and no "Do Not Sell or Share My Personal Information" link (or one combined privacy-choices link) in the footer or privacy page that stops those tags. Confirm only when both are missing.
  - ask: does the business meet a CCPA threshold: annual revenue over $26,625,000 (2025-26 figure; CPPA adjusts it on 1 January 2027, see cppa.ca.gov), buying, selling or sharing data of 100,000 or more California consumers or households, or half its revenue from selling or sharing data?
- why: In California, passing visitor data to ad networks for cross-site ads counts as sharing, which people can stop through a browser opt-out signal or a "Do Not Sell or Share" link.
- fix: Before loading ad or retargeting tags, read `navigator.globalPrivacyControl` (or `Sec-GPC: 1` on the server) and skip the tags when it is set, and add a "Do Not Sell or Share My Personal Information" link that turns them off and remembers the choice.
- exceptions: With no US (California) users in scope, report Skipped, never Later. Analytics such as GA4 (`G-` ids) with no ad tag is out of scope. Threshold answer "no": skip; "yes": Confirmed; "I don't know": one Maybe. If a consent platform (OneTrust, Cookiebot, Osano and similar) or tag manager is present and its signal setting can't be seen, or it may inject the "Do Not Sell" link by script, report Maybe.
- elsewhere: none
