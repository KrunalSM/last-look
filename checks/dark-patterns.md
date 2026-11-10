# Dark patterns

## dark-pattern-urgency
- title: Fake urgency or scarcity
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a countdown timer that resets (loops back to the start, restarts on reload, or counts a fixed time from page load instead of to a real end date). Cite the line that resets or sets the timer.
  - code: hard-coded scarcity or demand text ("Only 3 in stock", "5 people are viewing", "Price rises at midnight"), or random numbers shown as live stock or demand.
  - site: reload the page and see whether the timer or stock count starts again
  - ask: is the deadline or stock count real, and where does it come from?
- why: False urgency pushes people to buy in a hurry, and India lists it as a banned dark pattern.
- fix: Remove the timer and scarcity text, or drive them from a real end date and real stock data that does not reset.
- exceptions: A real sale end date or a real stock count from the server is not a finding.
- elsewhere: none

## sponsored-listing-unlabelled
- title: Ads or sponsored listings not labelled
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: product or search results that mix in paid or promoted items (`sponsored`, `promoted`, `is_ad`, paid `boost` or `featured` flags) rendered with no visible "Sponsored" or "Ad" label. Cite the component that renders the item.
  - code: a label that is hard to notice: tiny, low contrast, only in a tooltip or `aria-label`, or shown only on hover.
  - code: ads, paid or affiliate posts styled as articles, reviews or user posts with no "Ad" or "Sponsored" label. Cite the component.
  - site: search for a product and look for a label on paid or promoted results
  - ask: none
- why: India bans ads disguised as other content, such as posts, reviews or articles, and from 1 January 2027 its e-commerce rules require sponsored listings to be marked clearly, so paid content isn't mistaken for neutral content.
- fix: Render a visible "Sponsored" or "Ad" label on every paid or promoted item, next to its title, in readable size and contrast, driven by the same flag that marks the item as paid.
- exceptions: The Dark Patterns rule has applied since 30 November 2023; a seller or advertiser posting content on a platform must label it. The E-Commerce rule applies from 1 January 2027 to businesses selling online to consumers in India (scope in business-identity-missing). Items placed by the platform's own criteria without payment are not sponsored listings. A clear "affiliate link" or "paid partnership" note on the post counts as a label.
- elsewhere: none

## fake-reviews
- title: Reviews or ratings not from real buyers
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: ratings, review counts or reviews generated at random or hard-coded as if from buyers (`Math.random()` star ratings, a fixed "4.9 from 2,341 reviews", invented customer reviews in production seed data). Cite the line.
  - code: scripts or admin tools that post reviews as customers from staff or bot accounts. Cite the script.
  - site: none
  - ask: are the reviews and ratings shown written by real buyers?
- why: Indian e-commerce rules ban sellers from posing as consumers to post reviews or misrepresenting goods, and invented ratings mislead buyers.
- fix: Show only reviews and ratings from real buyers, computed from stored reviews, and remove hard-coded or random values.
- exceptions: Testimonials quoted with the customer's permission are not a finding; report hard-coded testimonials as Maybe unless they are clearly invented. Seed data used only in development or tests is out. Applies to online stores selling their own goods and to sellers on marketplaces, selling to consumers in India (r.7(2), r.6(2)); scope limits in business-identity-missing apply. Rewards for store ratings or review prompts: see custom-review-prompt, and report one finding.
- elsewhere: none

## confirm-shaming
- title: Shaming or scary wording on the decline option
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: decline, skip or cancel wording that shames, scares or guilt-trips the user, such as "No thanks, I don't like saving money", "I'll stay unprotected", "Accept risk" or "I don't care about charity", on offers, add-ons, donations, paid sign-ups or cancel flows, in any language. Cite the string.
  - code: emotional messages, images, video or sound on the decline or cancel path meant to make the user feel guilty or afraid (a crying mascot, "You are letting the children down").
  - site: read the wording on public offer, add-on and cancel pages without clicking through; a cancel flow behind a login is `Not tested`
  - ask: none
- why: India bans using shame, fear or guilt to push users into buying something or keeping a subscription.
- fix: Use neutral wording for the decline option, such as "No thanks" or "Don't renew", and state plainly and accurately what the user gives up.
- exceptions: Plain, true facts about what declining or cancelling means ("Pro features stop on 30 June") are fine.
- elsewhere: none

## forced-action
- title: Purchase or use tied to an unrelated sign-up, app or data
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: buying or using a product or service requires something unrelated: subscribing to a newsletter, signing up for another service, or installing a separate app. Cite the gate.
  - code: a purchase, or content advertised as free, that demands ID (such as Aadhaar), card, phone or email details, contacts or social accounts it doesn't need (a card for a free trial or plan: see renewal-terms-checkout). Cite the required field or permission.
  - code: something already paid for stops working, or can't be used, until the user upgrades or buys something more, though the original price covered it. Cite the gate.
  - site: on public product and free-item pages, note what you must give or join before buying or opening; never start a purchase
  - ask: none
- why: India bans forcing users to buy more, sign up for something unrelated or share personal data that isn't needed in order to get what they chose.
- fix: Let users buy or use what they chose without a newsletter, another app, an upgrade or extra data; make extra steps optional and ask only for the data the order needs.
- exceptions: Data the order or a law needs (a delivery address, an email for the receipt, KYC a regulator requires) is fine, and so is an account where the service needs one (synced data, saved progress). Plan limits and higher-tier features the user never paid for are not findings: confirm the upgrade item only when the code shows the user's purchase includes the feature. On iOS apps, report sign-in gates and unused permissions once, under forced-login-or-permissions, and cite dark-patterns-forced-action there.
- elsewhere: none

## interface-interference
- title: Decline option hidden or made hard to see
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a "No", decline, close or cancel option on a buy, renew, add-on or consent choice made much harder to see than the accept option next to it: faint or low-contrast colour, tiny text, or hidden or placed off-screen. Cite both elements.
  - code: a close (X), Skip or No control on a pop-up or ad whose handler opens another ad or page instead of closing it. Cite the handler.
  - code: symbols or colours used against their usual meaning, such as a tick or green button that declines, or an X that accepts.
  - site: open each pop-up and offer and compare how easy the accept and decline options are to see
  - ask: none
- why: India bans designs that highlight one choice and obscure another to steer users away from what they meant to do.
- fix: Give accept and decline options similar size, contrast and placement, make the X close the pop-up, and use symbols with their usual meaning.
- exceptions: A readable text link or secondary button is fine; confirm only a faint, tiny or hidden decline on a buy, renew, add-on or consent choice. Cookie Accept and Reject parity: see trackers-before-consent.
- elsewhere: none

## bait-and-switch
- title: Advertised item or result swapped for another
- area: dark-patterns
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code: a product shown as available, or at a price, from hard-coded or separate data, while the cart or checkout checks real stock and then offers a dearer alternative. Cite both lines.
  - code: cart or checkout code that replaces the item the user chose with a different or dearer one without the user picking it. Cite the line.
  - code: a button or link whose label promises one result ("Download free", "Skip") but whose handler starts a paid plan or another purchase. Cite the handler. An X that opens an ad is interface-interference; a link serving an installer is scareware-warnings.
  - site: compare an item's price across the public pages that show it; never add to a cart, so the cart itself is `Not tested`
  - ask: none
- why: India bans advertising one outcome and then serving another, such as luring buyers with an item or price that turns into a dearer one at checkout.
- fix: Show availability and price from the same live data the cart uses, let users choose any substitute themselves, and make each button do what its label says.
- exceptions: An item that really sells out between listing and checkout, shown honestly with no pushed dearer swap, is not a finding; neither is a substitute the user picks. A buy button labelled Continue or Start, on a screen that shows the plan and price and is followed by a store or payment sheet, is not a finding.
- elsewhere: none

## nagging-prompts
- title: Prompts that keep coming back or offer no "No"
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a prompt shown again after the user dismisses it (install-our-app banners, notification, cookie, sign-up or offer pop-ups) because the dismissal is not saved or is ignored, or one shown on every visit or screen. Cite the show condition.
  - code: a notification, cookie or app-install request with no way to say no (only "Allow" or "Later", or no close) that keeps coming back, or repeated requests for a phone number or other details "for security". Cite the prompt.
  - site: dismiss each prompt, then reload or move between pages and see whether it returns
  - ask: none
- why: India bans disrupting users with repeated requests or interruptions to make a sale or other gain, unless the user asked for them.
- fix: Give every prompt a clear "No" or "Don't ask again", save the answer, and ask again only if the user opts back in.
- exceptions: Reminders the user asked for, and notices the user must act on to keep using the service (such as updated terms or a security alert about their account), are not nagging. A one-off notice with only "Got it", or a single "Not now" pre-prompt, is not nagging.
- elsewhere: none

## trick-question
- title: Confusing wording on a consent or opt-out choice
- area: dark-patterns
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: consent or opt-out wording with double negatives or reversed sense ("Uncheck to not stop emails"), or a question whose answers don't match it, such as "Opt out of updates?" answered by "Yes, send me updates" and "Not now". Read translated strings too. Cite the string.
  - code: a checkbox or toggle whose label means the opposite of the value it stores (ticking "Don't email me" saves marketing as on). Cite the label and the handler.
  - site: read each consent and opt-out choice and check that the answers match the question
  - ask: none
- why: India bans deliberately confusing wording, such as double negatives, that misleads users into a choice they did not mean to make.
- fix: Ask one plain question in the positive ("Send me offers by email?"), give answers that match it ("Yes" and "No"), and store the value the label describes.
- exceptions: A plain opt-out box ("Don't send me offers") that stores what it says is fine.
- elsewhere: none

## scareware-warnings
- title: Fake security warnings, or ads that redirect or install software
- area: dark-patterns
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code: fake virus, infection or "device at risk" warnings styled like system alerts, with a button to pay for or install a cleaner or other tool. Cite the component.
  - code: ad or partner scripts that open pop-ups or pop-unders, or redirect the page, without the user clicking that ad, and lead to a fake warning, a paid "cleaner" or an installer. Cite the script. Report other self-opening ad pop-ups or redirects as Maybe.
  - code: a download link for promised free content that serves an installer (`.exe`, `.apk`, `.dmg`) or a different file. Cite the link.
  - ask: none
- why: India bans scareware that tricks users into paying for or installing fake security tools, and ads that lead users to malware.
- fix: Remove fake warnings, drop ad networks that redirect or open pop-ups by themselves, and serve only the file the user asked for.
- exceptions: Real security software showing the results of a real scan, and links to the project's own app labelled as such, are not findings, and neither are `window.open` calls for sign-in, payment or sharing that the user starts. Fake system or virus warnings in a mobile app: see deceptive-app-behavior, and report one finding.
- elsewhere: none
