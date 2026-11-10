# Cross-border data

## cross-border-transfers
- title: Outside services and data sent abroad to check on your own
- area: cross-border
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: list each outside service that processes users' personal data for you once, with its region where the code shows one: hosting and database (`region`, `us-east-1`, the Supabase or Firebase project region), email and SMS, analytics, payments, support chat, crash reporting, AI APIs.
  - code: contracts and transfer limits are set outside the code, so report one Maybe, name each service in Why, and use one location: the line that sets a hosting or database region, else the main config file or the package manifest.
  - ask: none
- why: You stay responsible for what your service providers do with users' data, so India requires a valid contract with each one, and it can restrict transfers of personal data to countries it notifies.
- fix: For each service, accept its data processing agreement, check it covers security safeguards and stopping and erasing data on your instruction, and keep a list, because users can ask who got their data. Check the Government's notifications under DPDP s.16 and orders under rule 15 for the countries you send data to, and any sector law, and pick regions or providers that meet them.
- exceptions: Services that receive no personal data are out of scope, and the transfer part applies only when data leaves the users' country. For India, transfers are allowed unless the Government restricts the destination, a stricter law applies, or a Significant Data Fiduciary is told to keep listed data in India. For data of people outside India that an Indian business processes under a contract with a foreign party (DPDP s.17(1)(d)), only its overall responsibility (s.8(1)) and security duties, processor security terms included (r.6(1)(f)), still apply.
- elsewhere: none
