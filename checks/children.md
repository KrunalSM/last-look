# Children

## age-handling
- title: Child users not handled
- area: children
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code: signs the service is aimed at children: words such as "kids", "children" or "ages 6-12", school or toy themes, the Apple Kids Category, "Designed for Families", a child ad age tag (`data-tag-for-age-treatment`, `setAgeRestrictedTreatment`, `tfat`; older `tagForChildDirectedTreatment`).
  - code: if it is aimed at children, check for a parental consent step before any personal data is collected, and for ad or tracking SDKs.
  - code: a service aimed at children loads ads with no child age tag in code: Maybe at that line, since the setting may sit in Search Console, AdMob or Ad Manager. Confirm only if code turns personalised ads on, or the ad service has no such setting outside code.
  - code: signs of actual knowledge of child users, such as a birth-date field that accepts a child's age and then carries on as normal.
  - ask: is the service aimed at children, or do you know that children use it?
- why: Services aimed at children, or that know they have child users, need a parent's consent before collecting personal data, and from 13 May 2027 India's DPDP s.9(1) needs it for any child under 18, with no knowledge test.
- fix: For a child-directed service or known child users, get verifiable parental consent before collecting personal data, and remove behavioural ads and tracking, or tag ads as child: `data-tag-for-age-treatment="1"` (AdSense), `setAgeRestrictedTreatment(CHILD)` or `ageRestrictedTreatment = .child` (AdMob), `tfat=1` (Ad Manager). A general-audience service needs no age gate by default.
- exceptions: The FTC COPPA FAQ says the rule "does not require operators to ask the age of visitors". A general-audience service with no child-directed content and no actual knowledge of child users is not a finding: never confirm a missing age check; list it under nothing found, or as Maybe when the answers say "I don't know". India's DPDP Act needs a parent's consent for users under 18 from 13 May 2027, so an India service that may have minors gets Maybe, not Confirmed. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## parental-consent-unverified
- title: Parental consent taken without checking the parent
- area: children
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code: a parental consent step (a parent's email or phone field, an "I am the parent" box, a consent switch on a child profile) that saves the parent's word and goes on to process the child's data, with no check that the person is an identifiable adult. Cite the handler that saves the consent.
  - code: a check counts if it uses age and identity details the service already holds for an adult account, details the parent provides, or an age or identity token from an authorised issuer, such as one made available through a Digital Locker service.
  - code: a child's data is saved or tracking starts before the parent's consent is recorded. Saving only what is needed to check a user's age, or to hold a consent request until the parent answers, is not this mistake.
  - code: consent from someone claiming to be the lawful guardian of a person with disability is accepted with no check that a court or authority appointed them.
  - ask: none
- why: In India, before processing a child's data (under 18), you need the verifiable consent of a parent, after checking that the parent is an identifiable adult.
- fix: Before saving the child's data, check the parent: match an existing adult account whose age and identity you hold, ask the parent for their own age and identity details, or accept an age or identity token from an authorised issuer (for example through a Digital Locker service). Store the consent with the parent's account and the time.
- exceptions: Only for services aimed at, or knowing of, child users (see age-handling). The DPDP Rules' Fourth Schedule exempts, each within its limit: health services (as needed for health), schools (tracking and monitoring for education or pupils' safety), crèches (safety), child transport (location tracking during travel to and from the school, crèche or centre), email-only accounts, real-time location for safety, and checks that a user isn't a child, with parent checks. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## curated-content-ratings
- title: Streaming catalogue has no age ratings or parental locks
- area: children
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a catalogue of films, series, shows, documentaries or podcasts offered on demand (a titles or episodes model, a player screen) with no age rating field and no content descriptors (the Code of Ethics uses U, U/A 7+, U/A 13+, U/A 16+ and A). Cite the model or the player file.
  - code: the title page or player doesn't show the rating and descriptors before playback starts.
  - code: titles rated U/A 13+ or higher with no parental lock or other access control, or titles rated A with no reliable age check. Report these as Maybe, not Confirmed (see exceptions).
  - site: title pages show no rating before playback
  - ask: none
- why: India requires publishers of online curated content to rate every title and show the rating and what it warns about before it is watched; its Code of Ethics adds parental locks from U/A 13+ and age checks for A-rated titles.
- fix: Give each title a rating (U, U/A 7+, U/A 13+, U/A 16+ or A) and content descriptors, show them on the title page and at the start of playback, add a parental PIN or lock for U/A 13+ and above, and verify age before A-rated titles play.
- exceptions: Only publishers of online curated content offered to people in India: a business that chooses and offers audio-visual titles on demand as a systematic business. User-uploaded titles make the service an intermediary instead; news, and individuals not in systematic business, are out. Categories, display at each programme's start, parental locks, age checks and child limits come from the Code of Ethics via rule 9(1), stayed by the Bombay High Court (interim order reported 14 August 2021, status unconfirmed): report them as Maybe. Rule 11(4) and (5) were not stayed.
- elsewhere: none

## child-app-sdks-ads
- title: App for children uses SDKs, data sharing, ads or links that store rules ban
- area: children
- needs: mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code: first settle that children are in the audience (age-handling signals, a neutral age screen, the Kids Category, the answers). Then, on Google Play: ad SDKs that aren't Families self-certified, or ads without child age settings (`setAgeRestrictedTreatment`, `setMaxAdContentRating`).
  - code (android): from children or unknown-age users, sending the advertising ID, SIM or build serial, MAC, SSID, BSSID, IMEI or IMSI; in child-only apps, `AD_ID` (target API 33+) or any location permission; the phone number from `TelephonyManager`; Bluetooth without `CompanionDeviceManager`.
  - code (Google Play): SDKs or sign-in APIs whose terms bar child-directed use; interest-based ads or remarketing; ads at launch, not closeable after 5 seconds, more than one per page, offerwalls, or not clearly set apart from content.
  - code (Google Play): social features open to children with no in-app online-safety reminder, no adult step before sharing personal information, or no way for adults to manage them; an AR section with no safety warning when it opens.
  - code (Google Play): a dating app, or an app mainly for chatting with strangers or anonymously, whose target audience includes children; such apps must not target children (anonymous chat named from 26 August 2026).
  - code (ios): an app in Apple's Kids Category, or intended primarily for kids, that ships third-party analytics or ad SDKs (Firebase Analytics, Google Mobile Ads, Meta, AppLovin, Unity Ads, Mixpanel, Amplitude). Cite the SDK.
  - code (ios, Kids Category only): personal or device data sent to third parties; links out, web views to other sites, purchase buttons or other distractions children can reach without a parental gate (a check only an adult can pass). Cite it.
  - ask: which age groups did you select in Play Console's Target audience, and will the app be in the App Store Kids Category?
- why: Both stores restrict third-party analytics, ads and data sharing in apps for children: Google Play requires self-certified SDKs and ads suited to children, and Apple's Kids Category also needs a parental gate for links and purchases.
- fix: Google Play: serve child ads only from Families self-certified SDK versions with the child age treatment set, stop sending identifiers and location, screen mixed audiences by age, and add the safety reminder and adult step to social features. Kids Category: drop third-party ad and analytics SDKs (or keep only identifier-free analytics and contextual ads) and gate links and purchases.
- exceptions: Applies only when the audience includes children, or the app is in or mainly for the Kids Category. Google Play: mixed-audience apps may use other SDKs behind a neutral age screen or with no data from children; in-house promotion and direct deals need no certified SDK. App Store: the parental gate and third-party data rules are for Kids Category apps; the analytics and ads limits also cover apps mainly for kids, where analytics with no IDFA or identifying data and contextual ads with public kids policies and human review are allowed. A parental gate is not parental consent: see age-handling.
- elsewhere: none
