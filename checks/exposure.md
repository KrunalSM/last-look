# Exposure

## secrets-in-client
- title: Secret key in client-side code
- area: exposure
- needs: none
- severity: Critical
- evidence-default: confirm
- look-for:
  - code (web): secret keys in code that runs in the browser (`"use client"` files, pages, components, `public/`, `NEXT_PUBLIC_*`, `VITE_*` or `REACT_APP_*` variables). Patterns: `sk_live_`, `sk_test_`, `rk_live_`, `AKIA`, `-----BEGIN PRIVATE KEY-----`, `service_role`, OpenAI `sk-` keys. Cite it.
  - code (mobile): the same patterns in app source, `Info.plist`, `strings.xml`, `BuildConfig` fields or bundled config files.
  - code: committed `.env` files that hold real secrets.
  - site: secrets visible in the page source or loaded JavaScript bundles
  - ask: none
- why: Anyone can read client code, so a secret key there gives strangers your account, your data or your bill.
- fix: Move the call to a server route that reads the key from an environment variable, then revoke and replace the exposed key, because it is already public.
- exceptions: Keys meant for clients (Stripe `pk_` keys, the Firebase web `apiKey`, the Supabase anon key) are not secrets by themselves. Never write the secret value in the report, only its location.
- elsewhere: none

## open-database-rules
- title: Database open to anyone
- area: exposure
- needs: database
- severity: Critical
- evidence-default: confirm
- look-for:
  - code (Supabase or Postgres): `disable row level security`, a table in the `public` schema with no `enable row level security`, or insert, update or delete policies written `using (true)`. Cite the line.
  - code (Firebase): `allow read, write: if true;`, `allow read, write;` with no condition, Realtime Database `".read": true` or `".write": true`, or rules that only check `request.auth != null` for data that belongs to one user.
  - site: none
  - ask: none
- why: With open rules, anyone with your public project key can read or change the data, including personal data.
- fix: Enable row level security on every table and add policies that limit each user to their own rows. In Firebase, write rules that compare `request.auth.uid` with the owner of the document.
- exceptions: Tables that hold only public data, such as a published product list, may be readable by everyone, but not writable.
- elsewhere: none

## prod-logging-personal-data
- title: Tokens or personal data written to production logs
- area: exposure
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code (android): `Log.d`, `Log.i`, `Log.v`, `Log.w`, `Log.e`, `println` or Timber calls writing tokens, passwords, credentials, session ids, emails, phone numbers, locations or other personal data to logcat, with no release stripping (R8 `-assumenosideeffects`, `BuildConfig.DEBUG`). Cite it.
  - code (ios): `print`, `debugPrint`, `NSLog`, `os_log` or `Logger` calls that write tokens, passwords, credentials or personal data; `os_log` and `Logger` values marked `privacy: .public` or `%{public}` count too.
  - code (web and server): `console.log`, `console.info`, `console.debug` or server loggers that write emails, tokens, passwords, request bodies or whole user objects.
  - code (React Native and Expo): `console.log` of location, contacts, tokens or user data.
  - code: severity depends on what is logged. Tokens, passwords, credentials and personal data are High. Debug messages with no personal data ("screen opened") are Low.
  - site: the browser console shows personal data or tokens
  - ask: none
- why: Logs are kept, copied to log services and read by other tools, so tokens and personal data in them can leak.
- fix: Remove the log line, or log a value that identifies nobody (an internal id, not the email or token), and strip debug logging from release builds.
- exceptions: Logging behind a debug-only guard that release builds remove is not a finding. Never copy the logged value into the report.
- elsewhere: none

## cleartext-traffic
- title: Personal data sent over unencrypted HTTP
- area: exposure
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code: API base URLs, uploads or SDK endpoints that start with `http://` (not localhost or emulator addresses) and carry personal data or tokens. Cite the line.
  - code (android): `android:usesCleartextTraffic="true"`, or a network security config with `cleartextTrafficPermitted="true"` for production domains.
  - code (ios): `NSAllowsArbitraryLoads` set to true in `Info.plist`, or exceptions that allow plain HTTP for production domains.
  - site: forms or API calls that send data to `http://` URLs
  - ask: none
- why: Anyone on the network can read or change data sent over plain HTTP, and Google Play requires personal and sensitive data to be sent with modern encryption such as HTTPS.
- fix: Serve every API over HTTPS, change the URLs to `https://`, remove the cleartext and arbitrary-loads flags, and limit any exception to named local or test hosts.
- exceptions: Local development hosts (`localhost`, `10.0.2.2`, LAN test servers) in debug-only config are not findings. Plain HTTP for public content with no personal data or tokens is Low.
- elsewhere: none

## unauthenticated-data-route
- title: Server route gives out or changes personal data without a login check
- area: exposure
- needs: none
- severity: High
- evidence-default: confirm
- look-for:
  - code (server): a route, server action or function that reads, returns, changes or deletes personal data (profiles, emails, orders, messages, files) picked by a request value (`id`, `userId`, `email`), with no session or token check in the handler or in middleware covering the path. Cite the query.
  - code (server): confirm only when that query runs with a client that skips database rules (a Supabase service-role key, `firebase-admin` or another admin SDK, a direct database connection or ORM), or the project has no database rules.
  - code (server): a client bound to the caller's session under row rules (Supabase anon key or cookie-based server client with RLS on, a Firebase client SDK under security rules): report Maybe, or nothing if the rules limit rows to the owner.
  - code (server): a handler that checks sign-in but picks whose data to return from a user id in the request, not the session, with such a privileged client.
  - code (mobile or web client): requests for personal data to an API whose server code is not in the repo, sent with no token: report Maybe.
  - ask: none
- why: A route anyone can call with any id lets strangers read or change other people's personal data, and access checks only count when the server makes them.
- fix: Check the session or token on the server in every such route, take the user id from the verified session (not from the request), and return 404 or 403 when the record isn't theirs; put the check in shared middleware so new routes get it.
- exceptions: Public data (published posts, product lists) and sign-up, login and password-reset routes need no login. When a gateway, edge rule or middleware outside the repo may do the check, report Maybe, not Confirmed. Database rules themselves: see open-database-rules. This is a short list of common leaks, not a security audit.
- elsewhere: none

## rate-limit-missing
- title: AI, email or SMS endpoint with no rate limit
- area: exposure
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code (server): a route that calls a paid AI API, or sends email, SMS, OTP or password-reset messages, with no limit per user or IP: no limiter (`@upstash/ratelimit`, `express-rate-limit`, `rate-limiter-flexible`, `slowapi`), no per-user quota or counter, no 429 response. Cite the call.
  - code: report Maybe, because limits and spending caps can be set outside the repo (edge or gateway rules, the provider's dashboard).
  - ask: none
- why: Without a rate limit, anyone can loop requests to such a route and run up your AI or messaging bill, or use it to spam people.
- fix: Add a per-user and per-IP limit to each such route (for example 20 requests a minute, returning 429), require sign-in for AI routes where the feature allows, and set spending limits or billing alerts with each provider.
- exceptions: Routes with a limiter, quota or counter in the code are not findings. Transactional messages the server sends itself, not on a client request, are out of scope.
- elsewhere: none
