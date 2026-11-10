# User content

## uploads-takedown-process
- title: User uploads with no report or takedown process
- area: user-content
- needs: user content
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: upload routes or public galleries (`upload`, public storage buckets, comments, posts, shared decks) where users publish content that others see, and no report button, report route, abuse email or copyright contact anywhere in the project. Cite the upload route.
  - site: no "report" link on shared content and no copyright or complaints contact
  - ask: none
- why: Hosts of user content need a way to receive complaints and remove unlawful content: India requires a published complaint route for users and victims, and in the US a registered DMCA agent keeps the safe harbour.
- fix: Add a report link on shared content and a complaints route with fields for the link and what is wrong, publish a contact for copyright notices, and for US users register a DMCA agent with the Copyright Office and renew it every 3 years.
- exceptions: Uploads that only the uploader can see, such as private files, are out of scope, except AI content creation features in App Store apps, which Apple Guideline 1.2 covers.
- elsewhere: none

## user-content-rules-missing
- title: Terms don't tell users what they may not post
- area: user-content
- needs: user content
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: users post or upload content the service stores or shows to others (uploads, posts, comments, profiles, messages, listings), and the terms, user agreement or community rules have no section on what users may not post. Cite the terms file, or the footer where a rules link should be.
  - code: a banned-content section leaves out India's categories: no right to share; obscene or privacy-invading; gender harassment, hate, money laundering, gambling; harm to children; IP infringement; false or misleading; impersonation; threats to security or order; malware; other unlawful. Name gaps.
  - code: the terms don't say the service may remove content or end access for breaking them; since 20 February 2026, also confirm when they don't mention suspension, legal penalties for users, and reporting of offences that must be reported.
  - code: the terms or rules exist, but nothing on the home page or main screen, or one step from it, links to them.
  - site: the terms page lists no banned content, or the home page has no link to the terms
  - ask: none
- why: India requires services hosting users' content to publish their rules, privacy policy and user agreement prominently and tell users what they may not post and what breaking the rules costs, or risk losing legal protection for users' posts.
- fix: Add a section of the rules that lists banned content categories; say you may remove content and suspend or close accounts, that lawbreakers may face penalties, and that you report offences the law requires. Link it from the home page or main screen, in English or a scheduled language of choice. Remind users of the consequences at least every three months and of the rules at least once a year.
- exceptions: Intermediaries offered to people in India only: services that store or pass on content for users (uploads, posts, comments, messages, listings). A site where only the owner publishes is not one; skip. Files only the uploader sees: Maybe. Suspension, penalties, offence reporting and the three-monthly reminder date from 20 February 2026; before, a yearly notice of removal and termination sufficed. The online-game categories (unverified games and their ads) wait for r.4B: don't flag them (see regulated-field-present).
- elsewhere: none

## significant-social-media-intermediary
- title: Extra duties for large social platforms in India
- area: user-content
- needs: user content
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: code does not settle this. Raise it only for a social platform (users follow, message or share with strangers, and content can spread) with signs of a very large Indian user base, or when the user says so. Report Maybe, with the README or terms as the location.
  - code: when raised, note missing code-visible parts: complaint ticket numbers with reasons; voluntary verification with a visible mark; notice and a dispute route before own-motion removal; labels on paid or sponsored posts; a declaration and label step for AI-made uploads.
  - ask: none
- why: Social platforms above 50 lakh registered users in India owe extra duties, such as officers resident in India, monthly reports, ticket numbers, voluntary verification, notice before removal, ad labels, automated detection and AI-upload labels.
- fix: If over the threshold: appoint a Chief Compliance Officer, a 24x7 nodal contact and a Resident Grievance Officer, all resident in India; publish monthly reports and an address in India; add ticket numbers, voluntary verification (data used for nothing else), notice and dispute before removal, sponsored labels, human-reviewed detection of abuse and re-uploads removed on orders, and AI labels.
- exceptions: Only significant social media intermediaries: services mainly for users to interact and share, above 50 lakh registered users in India (S.O. 942(E), 25 Feb 2021). MeitY's FAQ says services mainly for business transactions, internet access, search, email or storage are typically not social media intermediaries. The Ministry can order others to comply (rule 6). Messaging services must also trace a first originator on a lawful order. No sign of that scale: not a finding; list under Not checked or skipped. Its ticket and ad-label items are IT Rules duties.
- elsewhere: none

## ugc-moderation-missing
- title: No in-app filtering, reporting or blocking for user content
- area: user-content
- needs: user content in a mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code: users post content others can see (posts, comments, profiles, media, live or AR content) or message each other, and the app has no in-app report action for content and for users. Cite the post or message screen.
  - code: one-to-one messages, mentions or a public feed with no in-app block-user action (no block on profiles, messages or comments, no blocked-users list), or no admin tool to remove content and suspend users.
  - code (Google Play): users can post before accepting the terms or community rules, or those rules don't ban objectionable content and child sexual abuse material.
  - code (ios): nothing filters objectionable material before it appears (no moderation API, keyword or image filter, or review queue). Cite the post handler.
  - code (ios): creator content, mini apps or mini games with no flag on items above the app's age rating and no age check (declared or verified age) before showing them.
  - ask: none
- why: Both stores require apps with user content to offer in-app reporting and blocking and to act on reports; Google Play adds rules accepted before posting, and Apple adds filtering and age limits above the rating.
- fix: Require acceptance of rules that ban objectionable content and child sexual abuse before the first post, add Report on each post and profile and Block on each user, give moderators tools to remove content and ban users, filter posts before they appear (App Store), and put content above the app's age rating behind an age check.
- exceptions: Content only the poster can see is out of scope. Google Play: apps for a verified closed group need in-app reporting, and blocking only for one-to-one features. App Store: content from a web service may show incidental NSFW content only if hidden by default and turned on via the website. Complaints contact: see uploads-takedown-process. AI output: see ai-content-safeguards. Child safety standards and contact: see store-listing-review. Apps mainly for porn or random chat: see store-content-policy.
- elsewhere: none
