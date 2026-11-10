# Money

## renewal-terms-checkout
- title: Renewal terms hidden or subscription hard to cancel
- area: money
- needs: payments
- severity: High
- evidence-default: confirm
- look-for:
  - code: a subscription checkout (`mode: "subscription"`, recurring prices, Razorpay or Stripe subscriptions, StoreKit `SubscriptionStoreView`, Play Billing subscriptions, RevenueCat) whose pay-button screen doesn't say it renews, how often, the price per period and how to cancel. Cite the page.
  - code (App Store apps): the paywall doesn't say what the user gets for the price (features, storage, issues or access per period).
  - code: no way for the user to cancel (no cancel action in settings and no link to a billing portal).
  - code: cancelling takes much more effort than subscribing: a hidden or tiny cancel link, cancelling only by email, phone or chat, or a chain of retention screens or confusing steps before it takes effect. Cite the flow.
  - code: a free trial or free plan that needs card details or an auto-debit mandate (card on file, UPI AutoPay, e-mandate) to start, or doesn't say when it turns paid and at what price; or a product or app sold as free whose continued use needs a purchase. Cite the sign-up.
  - code: billing code that adds items, raises the price or switches the plan of a running subscription, or charges a saved card off-session for something the user didn't approve, with no notice or consent step (usage billing the plan states is fine). Cite the call.
  - code: a trial or intro offer that doesn't say how to cancel before it turns paid; a yearly plan shown mainly as a monthly price; a paywall with no way to close it.
  - code (India): renewals charged by the app's own scheduler to a saved card, UPI or wallet off-session, with no gateway subscription or e-mandate (an RBI e-mandate needs extra authentication at sign-up and above Rs 15,000). Report Maybe: the gateway may hold the mandate.
  - code (Google Play, from 27 January 2027): an eligibility discount, such as a student plan, that doesn't say how eligibility is checked and what price and benefits follow when it ends.
  - site: the text next to the pay button on the checkout page
  - ask: none
- why: Charging again without clear renewal terms is a common complaint: California law requires the terms before purchase, and India bans hard-to-cancel subscriptions, card demands for free trials and silent recurring charges as dark patterns.
- fix: Next to the pay button, state what the plan includes, the price, that it renews every period until cancelled, and where to cancel. Send a confirmation with the same terms, and add a cancel option in settings. Make cancelling as easy as subscribing, start free trials without card details or a mandate, and tell users before any new or changed charge.
- exceptions: One-time purchases with no renewal are out of scope. App Store and Google Play subscriptions show the store's own sheet, but the app's paywall must still state the terms. Requiring a card or mandate for a free trial is an India rule item only. Receipts and reminders can be sent from Stripe, Razorpay or store settings, so don't confirm a missing receipt or reminder from code alone. Confirm a "free" product needing a purchase only when the app's or site's own text calls it free with no word of a time or use limit, otherwise Maybe: store listings disclose in-app purchases outside the code.
- elsewhere: none

## price-breakdown-missing
- title: Total price or its breakdown not shown before payment
- area: money
- needs: payments
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a charge (delivery, handling, convenience, platform or payment fee, tax) added at the last step or after the pay button that the product page or cart doesn't show, or a checkout that shows only a base price or "+ taxes" with no amount. Cite the cart or checkout component.
  - code: no single total before payment, or a pay button amount that differs from the itemised total. Cite the line.
  - site: go to the last step before payment and compare the total with the listed price
  - ask: none
- why: Indian rules require the total price as one figure, broken down into every charge such as delivery, handling and tax, before the buyer pays, and ban revealing charges late (drip pricing).
- fix: On the cart and the last checkout step, show one total with a line for each charge (price, delivery, handling or convenience fee, payment fee, tax), and use the same total on the pay button; never add a charge after the buyer reaches the pay step.
- exceptions: The E-Commerce rule's scope is as in business-identity-missing; the Dark Patterns rule also covers platforms, advertisers and sellers offering goods or services in India. A free item or plan is out. Price changes by third-party sellers on a marketplace don't make the marketplace liable. A single price with no other charge and no word on tax, and bundled marketplace fees, are not findings here: name them in ecommerce-operations.
- elsewhere: none

## discount-prior-price-missing
- title: Price cut shown without the real prior price
- area: money
- needs: payments
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: an announced price cut ("50% off", "Sale", a discount badge, an offer email) with no prior price shown next to the reduced price. Cite the line. A prior price that is shown, even if typed in, is not a finding here.
  - code: a struck-through or "was" price (`compare_at_price`, `original_price`) computed from a markup on the current price rather than from past prices. Cite the line that sets it.
  - site: note each price cut and whether a prior price is shown next to it
  - ask: none
- why: From 1 January 2027 Indian e-commerce rules require any announced price cut to show the prior price, meaning the lowest price in the 30 days before the cut, next to the reduced price.
- fix: Keep a price history per item, compute the prior price as the lowest price in the 30 days before the cut, show it next to the reduced price, and remove "was" prices that don't come from it.
- exceptions: Applies from 1 January 2027 to price cuts announced by the business or a seller on its platform; scope limits in business-identity-missing apply. A price with no claimed reduction is out. A prior price typed in by hand, or a discount against MRP, can't be checked from code: name it in ecommerce-operations, not here.
- elsewhere: none

## return-refund-policy-missing
- title: No return, refund or delivery terms before purchase
- area: money
- needs: payments
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: no returns and refunds information anywhere (no "Refunds" or "Returns" page or footer link, nothing near the pay button), or, for goods, no delivery, shipping, exchange or warranty terms before purchase. Cite the footer or checkout file.
  - code: a policy that refuses every return or refund, even for defective, deficient or wrong items or late delivery, or that doesn't say who pays return shipping. Cite the line.
  - site: look for return, refund, shipping and payment pages linked from the footer and the checkout
  - ask: none
- why: Indian e-commerce rules require clear return, refund, exchange, warranty, delivery and payment information before purchase, and sellers must take back defective, deficient, wrong or late goods.
- fix: Publish a Returns and refunds page (what can be returned and how fast, who pays return shipping, refund time and method, warranty), a Shipping page for goods, and a Payments section (methods, fees, security, charge-backs, provider contact), and link them from the footer and the checkout.
- exceptions: Scope as in business-identity-missing. Delivery and shipping items apply only to goods. The rules don't require returns for a change of mind; refusing them for defective, deficient or spurious goods or services, items not as described, or late delivery (except force majeure) is not allowed. Best before or use before dates join the list from 1 January 2027 (see country-of-origin-missing). Recurring-payment cancel terms: see renewal-terms-checkout. Payment information shown only on the provider's page: name it in ecommerce-operations.
- elsewhere: none

## in-app-purchase-billing
- title: Digital goods sold outside the store's billing
- area: money
- needs: payments in a mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code (android): subscriptions, premium features, virtual currency or other digital content paid through Stripe, Razorpay, PayPal, a web checkout or a WebView instead of Play Billing (`BillingClient`, RevenueCat), or buttons, links or messages that send users to pay elsewhere. Cite the checkout call.
  - code (android): the reverse: Play Billing used for physical goods or services, bill payments, peer-to-peer payments, donations or regulated clinical services.
  - code (ios): features, content, subscriptions, credits or a full version unlocked through the app's own payments (Stripe, Razorpay, PayPal or Braintree SDKs, a web checkout in a web view) rather than StoreKit or an IAP library (RevenueCat, `react-native-iap`). Cite the payment call.
  - code (ios): unlocks by licence keys, codes, QR codes, AR markers or crypto wallets, or digital gift cards and vouchers sold outside In-App Purchase.
  - code (ios): buttons, links or text that send users to buy digital goods elsewhere. Outside the US storefront these need an Apple external purchase link entitlement; report Maybe when the storefronts are unknown.
  - code: paid random items (loot boxes, gacha, mystery packs) with no odds for each item type shown before purchase; on Google Play, prices in the app that differ from the Play billing price.
  - ask: for Google Play, are you enrolled in an alternative billing or external offers program for your users' countries?
- why: Both stores require their own billing for digital goods sold in the app, limit links and buttons to other ways to pay, and require loot box odds before purchase.
- fix: Sell digital goods through Play Billing or StoreKit (directly or through RevenueCat or react-native-iap); remove links and prompts to pay elsewhere unless an Apple entitlement, the US storefront or an enrolled Play program allows them; use your own payment provider for physical goods; show the odds next to each randomised purchase.
- exceptions: Google Play: physical goods and services, bill payments, peer-to-peer, auctions, tax-exempt donations and licensed gambling must not use Play Billing; enrolled programs allow other methods. App Store: physical goods and services must not use IAP; also allowed without it: reader apps, items also sold as IAP, enterprise sales, real-time one-to-one services, free companions to paid web tools with no buying or calls to buy, ad-campaign apps (boosts shown in the same app still need IAP), hardware-tied unlocks (optional add-on products also need an IAP option) and gifts paid to another person.
- elsewhere: none

## iap-purchase-rules
- title: In-App Purchases without restore, lasting access or trial terms
- area: money
- needs: iOS app with In-App Purchase
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (ios): non-consumables or subscriptions are sold and there is no restore action: no "Restore purchases" button calling `AppStore.sync()`, `restoreCompletedTransactions()` or the library's restore (RevenueCat `restorePurchases`). Cite the paywall or settings screen.
  - code (ios): paid credits, coins or items given an expiry date or taken away after a time.
  - code (ios): a free trial before a full-unlock purchase that doesn't first state how long it lasts, what stops working after it and what it will cost.
  - ask: none
- why: Apple expects a way to restore purchases that can be restored, bars paid credits and items that expire, and requires trial terms before purchase.
- fix: Add a "Restore purchases" button on the paywall or in settings that calls `AppStore.sync()` (or `restoreCompletedTransactions()`, or your library's restore) and refreshes access; remove expiry from paid credits and items; state trial length, what ends and the price before a trial starts.
- exceptions: Consumables used up as designed are not restorable. Access rebuilt from a signed-in account, or from `Transaction.currentEntitlements` at launch, may already count as a restore mechanism; report Maybe. Rentals of films, TV, music or books may end when the rental period ends. Subscription renewal terms: see renewal-terms-checkout. Loot box odds: see in-app-purchase-billing.
- elsewhere: none
