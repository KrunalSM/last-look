# Communication

## marketing-email-footer
- title: Marketing email without unsubscribe link or postal address
- area: communication
- needs: email
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: marketing or promotional email templates (offers, newsletters, "weekly", "deals"; `.html`, `.mjml`, React Email, Handlebars, SendGrid or Mailchimp templates) with no unsubscribe link and no postal address. Cite the template file.
  - code: sending code that ignores an opt-out flag (`marketing_opt_in`, `unsubscribed`).
  - site: none
  - ask: none
- why: Marketing email needs consent in the EU, with a way for existing customers to refuse more offers, US law requires a working opt-out and a postal address, and an opt-out link is commonly expected everywhere.
- fix: Add an unsubscribe link to every marketing email, honour it within 10 business days, and put your postal address in the footer.
- exceptions: Transactional email (receipts, password resets, security alerts) is largely exempt. A template sent through a provider that adds its own footer may be a Maybe; say which provider setting to check.
- elsewhere: US | CAN-SPAM requires an opt-out and a postal address in every marketing email | https://www.govinfo.gov/content/pkg/USCODE-2024-title15/html/USCODE-2024-title15-chap103-sec7704.htm

## push-marketing-consent
- title: Marketing push notifications without opt-in and opt-out
- area: communication
- needs: push notifications in an iOS app
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (ios): push used for promotions or marketing (promo or campaign topics, marketing segments in OneSignal, Braze, Firebase Messaging or Customer.io) with no consent text in the app for promotional notifications before the opt-in, or no setting in the app to stop them. Cite the push setup.
  - code (ios): the app stops working when push permission is denied, or push messages carry sensitive personal or confidential data (health details, account balances, passwords).
  - ask: none
- why: Apple bars marketing push notifications unless users opted in through consent text in the app and can opt out in the app, and bars making push a condition of using the app.
- fix: Add a separate opt-in with clear consent text for promotional notifications, a switch in the app's settings to turn them off, keep the app working when push is denied, and keep sensitive data out of push messages.
- exceptions: Notifications the user expects from their own activity (order updates, messages, reminders they set) are not marketing. Asking for push at launch: see permission-at-launch.
- elsewhere: none
