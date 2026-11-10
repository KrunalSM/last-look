# Google Play
- coverage-summary: Developer Program Policy (version effective 29 October 2026) and its linked Play Console Help requirement pages fully walked on 2026-11-03; items that live in Play Console forms are reported as Maybe. "before 2026-11-03" means in force when read.

## play-account-deletion-missing
- check: account-deletion-missing
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, account deletion: apps with account creation need an in-app path and a web link to delete the account and its data. Data deletion questions due 7 December 2023, extension to 31 May 2024 (same page)
- rule-started: 2023-12-07
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/13327111
- secondary: no

## play-data-safety-store-data-disclosure
- check: store-data-disclosure
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, Data safety: declare the data the app and its third-party SDKs collect and share. Start from the same page: "After July 20, 2022, all apps will be required to have completed an accurate Data safety form"
- rule-started: 2022-07-20
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/10787469
- secondary: no

## play-data-sale-limits
- check: store-data-disclosure
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data: limit personal and sensitive data to disclosed, expected purposes, never sell it, and make SDK providers comply. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-permissions-in-context
- check: permission-at-launch
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Permissions and APIs that Access Sensitive Information: request only permissions that current listed features need, in context (incremental requests). Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/12579724
- secondary: no

## play-prominent-disclosure
- check: prominent-disclosure-missing
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data > Prominent Disclosure & Consent: for data use users may not expect, an in-app disclosure right before the consent or runtime request, then affirmative consent. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-restricted-permissions
- check: restricted-permission-declared
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Permissions: restricted permissions (SMS, Call Log, all files, media, location, package visibility, Accessibility, install packages, VPN, alarms, full-screen intent, FGS) only for permitted core uses. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/12579724
- secondary: no

## play-photo-video-permissions
- check: restricted-permission-declared
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, minimum scope permissions: READ_MEDIA_IMAGES or READ_MEDIA_VIDEO (API 33+) only when pickers don't suffice, with a declaration. Full compliance mandatory 28 May 2025 (same page)
- rule-started: 2025-05-28
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/14115180
- secondary: no

## play-background-location
- check: restricted-permission-declared
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, background location: only for core features with a significant user benefit, never only for ads or analytics, with a declaration and a prominent disclosure. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9799150
- secondary: no

## play-loan-app-permissions
- check: restricted-permission-declared
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Financial Services > General Requirements: loan and earned-wage apps may not use photos, video, external storage, contacts, fine location, phone numbers or QUERY_ALL_PACKAGES. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9876821
- secondary: no

## play-full-screen-intent
- check: restricted-permission-declared
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, full-screen intent: for apps targeting Android 14+, auto-granted only to alarm and calling apps; declaration required starting 31 May 2024 (same page)
- rule-started: 2024-05-31
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/13392821
- secondary: no

## play-contacts-location-2027
- check: restricted-permission-declared
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, Permissions preview, apps targeting API 37+: READ_CONTACTS only when the Contact Picker can't serve; the location button for one-time precise location; a declaration for ACCESS_FINE_LOCATION. Effective 27 January 2027 (same page)
- rule-started: 2027-01-27
- status: Coming 2027-01-27
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/16909972
- secondary: no

## play-local-network-contacts-2027
- check: restricted-permission-declared
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, Permissions preview: ACCESS_LOCAL_NETWORK (API 37+) and MANAGE_CONTACTS (API 38+) only when pickers or intents can't serve, with a declaration. Effective 25 August 2027 (same page)
- rule-started: 2027-08-25
- status: Coming 2027-08-25
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/16909972
- secondary: no

## play-target-api-level
- check: target-api-too-low
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, target API level: new apps and updates target API 36 from 31 August 2026 (Wear OS and Automotive 35, TV and XR 34); existing apps need 35 (Wear OS and XR 34, TV 33, Automotive 32) to stay visible. Same page
- rule-started: 2026-08-31
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/11926878
- secondary: no

## play-secure-transmission
- check: cleartext-traffic
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data > Personal and Sensitive User Data: handle it securely, including transmitting it with modern cryptography such as HTTPS. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-privacy-policy
- check: privacy-policy-missing
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data > Privacy Policy: every app needs a privacy policy link in Play Console and in the app, on an active, public, non-geofenced, non-editable URL, not a PDF. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-privacy-policy-content
- check: privacy-notice-incomplete
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data > Privacy Policy: give developer details and a privacy contact, data types and recipients, secure handling, retention and deletion, a clear title and the listed name. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-secure-handling-logs
- check: prod-logging-personal-data
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data: handle personal and sensitive data, which includes authentication information, securely. Applied to tokens, credentials and personal data in logs; the policy doesn't name logs (this skill's reading). Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: yes

## play-security-vulnerabilities-secrets
- check: secrets-in-client
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Device and Network Abuse: no code that introduces security vulnerabilities. The policy doesn't name keys; treating a shipped secret key as one is this skill's reading. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888379
- secondary: yes

## play-third-party-ai
- check: ai-data-disclosure
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data: the duties extend to third-party AI integrations, and the developer stays responsible for limited use, disclosure and consent. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-advertising-id
- check: device-id-linking
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Ads > Android Advertising ID: only for ads and analytics; check the opt-out on each access; no link to persistent IDs, or to personal data without consent; keep reset IDs unlinked. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9857753
- secondary: no

## play-persistent-identifiers
- check: device-id-linking
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data: persistent identifiers such as IMEI may be linked to other data only for SIM telephony or enterprise device owner apps; App Set ID not for ads. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-disruptive-ads
- check: disruptive-ads
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Ads: no deceptive, disruptive or out-of-app ads, no unexpected full-screen ads or video ads before the splash screen, close within 15 seconds, no lockscreen ads, no ad fraud. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9857753
- secondary: no

## play-families-requirements
- check: child-app-sdks-ads
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Families: apps whose audience includes children follow data, SDK, ad format, social and AR rules, send no listed identifiers, and use only self-certified ads SDKs. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9893335
- secondary: no

## play-ugc-moderation
- check: ugc-moderation-missing
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Generated Content: terms accepted before posting that ban objectionable content, in-app reporting and blocking, and action on content and users. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9876937
- secondary: no

## play-child-safety-standards
- check: ugc-moderation-missing
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Child Safety Standards: social, dating, anonymous and random chat apps publicly ban CSAE and offer in-app feedback; chat apps added 26 August 2026 (Policy Deadlines). Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9878809
- secondary: no

## play-ai-generated-content
- check: ai-content-safeguards
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, AI-Generated Content: prevent restricted content and offer in-app reporting or flagging of offensive output without leaving the app. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/13985936
- secondary: no

## play-payments
- check: in-app-purchase-billing
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Payments: Play billing for in-app digital goods, not for physical goods and listed exceptions; no steering outside enrolled programs; matching prices; loot box odds. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9858738
- secondary: no

## play-subscriptions
- check: renewal-terms-checkout
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Subscriptions: state price, billing cycle, auto-renewal and offer terms; trial length, conversion and how to cancel; an easy online cancel route in the app. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9900533
- secondary: no

## play-subscriptions-eligibility-2027
- check: renewal-terms-checkout
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, Subscriptions preview: eligibility-based discounts such as student plans must disclose criteria, verification and post-eligibility price and benefits. Effective 27 January 2027 (same page)
- rule-started: 2027-01-27
- status: Coming 2027-01-27
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/18204939
- secondary: no

## play-device-network-abuse
- check: unsafe-code-loading
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Device and Network Abuse: no self-updates outside Play, no executable code from outside Play, no installs without consent, no WebView JavaScript interface on untrusted content. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888379
- secondary: no

## play-deceptive-behavior
- check: deceptive-app-behavior
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Deceptive Behavior: no unconsented or irreversible settings changes, mimicked system warnings, hidden features or review evasion; show download sizes first. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888077
- secondary: no

## play-appfunctions-2027
- check: deceptive-app-behavior
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, Permissions preview: AppFunctions must not deceive or manipulate AI agents, bypass security controls or interfere with other apps. Effective 14 April 2027 (same page)
- rule-started: 2027-04-14
- status: Coming 2027-04-14
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/16909972
- secondary: no

## play-health-apps-declaration
- check: store-listing-review
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, Health apps declaration: every app completes it, even with no health features. Start from the same page: "After August 31, 2024, all apps will be required to have completed an accurate Health apps declaration"
- rule-started: 2024-08-31
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/14738291
- secondary: no

## play-financial-features-declaration
- check: store-listing-review
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Play Console Help, Financial features declaration: every app completes it; loan apps add licences. Start from the same page: "After August 31, 2023, all apps will be required to have completed an accurate Financial features declaration"
- rule-started: 2023-08-31
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/13849271
- secondary: no

## play-console-forms
- check: store-listing-review
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, full text: permissions declarations, the content rating questionnaire, Families target audience, age-restriction tools and Play Console Requirements. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/17190352
- secondary: no

## play-content-and-listing
- check: store-content-policy
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, full text: Restricted Content, Misrepresentation, Metadata, Repetitive Content, Broken Functionality, Inappropriate Ads and the Android Emoji Policy. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/17190352
- secondary: no

## play-incentivized-ratings
- check: custom-review-prompt
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Ratings, Reviews, and Installs: no ratings or reviews inflated by illegitimate means, such as incentives. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9898684
- secondary: no

## play-minimum-functionality
- check: webview-only-app
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Functionality, Content, and User Experience: no apps with limited functionality or content, such as static text-only or PDF apps. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9898783
- secondary: no

## play-webview-spam
- check: webview-only-app
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Spam > Webviews and Affiliate Spam: no apps mainly showing a website in a webview without the owner's permission, or driving affiliate traffic. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9899034
- secondary: no

## play-ip-impersonation
- check: content-rights-unclear
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, full text: Intellectual Property (copyright, trademark, counterfeit) and Impersonation (no implied link to another developer, company or app). Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/17190352
- secondary: no

## play-respect-permission-declines
- check: forced-login-or-permissions
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Permissions > Restricted Permissions: respect declined requests, don't force consent to non-critical permissions, and accommodate users who decline. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/12579724
- secondary: no

## play-malware
- check: deceptive-app-behavior
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Malware: bans spyware, stalkerware (monitoring apps need the IsMonitoringTool flag, a persistent notification and disclosure), billing fraud, privilege abuse, rooting, trojans and riskware. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888380
- secondary: no

## play-mobile-unwanted-software
- check: deceptive-app-behavior
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Mobile Unwanted Software: be clear about functions and system changes, don't misstate device security or mimic OS prompts, don't ask users to turn off Play Protect. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9970222
- secondary: no

## play-message-spam
- check: deceptive-app-behavior
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Spam > Message Spam: no SMS, email or other messages sent for the user without letting them confirm the content and recipients. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9899034
- secondary: no

## play-cryptomining
- check: deceptive-app-behavior
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Blockchain-based Content > Cryptomining: no mining cryptocurrency on devices; remote management of mining is allowed. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/13607354
- secondary: no

## play-health-connect-age-signals
- check: protected-data-misuse
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, Permissions: Health Connect Limited Use bars transfers to ad platforms and data brokers, ad use and credit decisions, allowing third-party transfers only with explicit consent for security, legal or merger reasons; Age Signals data only for legal duties, never for ads, analytics or sharing. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/12579724
- secondary: no

## play-public-ids-contacts
- check: protected-data-misuse
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, User Data > Restrictions for Personal and Sensitive Data Access: never publicly disclose financial, payment or government ID data, and no unauthorised publishing of non-public contacts. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/9888076
- secondary: no

## play-regulated-apps
- check: restricted-app-type
- source-id: google-play-policy
- applies-to: Google Play
- strength: Store rule
- reference: Developer Program Policy, full text: Financial Services, Real-Money Gambling, Health Content and Services and Blockchain-based Content: licences, applications or declarations, listing disclosures, a reminder to consult a healthcare professional, and bans on binary options and loans due in 60 days or less. Start day not stated.
- rule-started: before 2026-11-03
- status: In force
- verified-on: 2026-11-03
- source: https://support.google.com/googleplay/android-developer/answer/17190352
- secondary: no
