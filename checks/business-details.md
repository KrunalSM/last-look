# Business details

## grievance-officer-missing
- title: No grievance contact or response time for Indian users
- area: business-details
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: no grievance officer name and contact ("grievance", "Grievance Officer", "nodal officer") in the footer, contact, terms or about pages of a service for people in India that hosts user content, publishes news or a streaming catalogue, or sells online. Cite the footer or layout file.
  - code: for a service hosting user content for people in India: no response times, or times longer than the IT Rules allow (acknowledge in 24 hours, resolve in 7 days since 20 February 2026; older pages often say 15 days), or details more than one step from the home page or main screen. Cite the line.
  - code: for an online seller to consumers in India: stated times over 48 hours to acknowledge or one month to resolve, or a consumer complaint route giving no ticket number (from 2027 also a copy as recorded). A stated emailed ticket is enough; content-report forms don't count. Cite the line.
  - code: for a service processing personal data in India, or processing it abroad in connection with offering goods or services to people in India: no published way to raise a grievance about personal data, or no stated time to respond to it. Cite the footer or privacy file where it should be.
  - site: the footer and contact page show no grievance officer name and contact
  - ask: none
- why: Indian rules make platforms hosting user content, news and streaming publishers and online sellers publish a grievance officer and answer on time, and from 13 May 2027 any business processing personal data in India needs a grievance route.
- fix: Publish the grievance officer's name, designation and contact in the footer or contact page, with how to complain and reply times: user-content platforms acknowledge in 24 hours, resolve in 7 days; news and streaming publishers acknowledge in 24 hours, decide in 15 days; online sellers acknowledge in 48 hours, resolve in a month, issue ticket numbers; personal data grievances, answer in 90 days.
- exceptions: The officer and times apply only to services offered to people in India that host user content or publish news or a streaming catalogue (IT Rules 2021), or sell online to consumers (E-Commerce Rules 2020; scope in business-identity-missing). The personal data route applies from 13 May 2027 to processing in India, or abroad when offering goods or services to people in India (DPDP s.3). The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## privacy-contact-missing
- title: No contact for questions about personal data
- area: business-details
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: no contact (an email address, a form or a named person) for questions about personal data in the privacy page, footer, contact page, app settings or help screens. Cite the layout, footer or privacy file where it should be.
  - code: a consent request (sign-up consent, cookie banner) that neither shows such a contact nor links to a page that has one.
  - site: the privacy and contact pages give no privacy contact
  - ask: none
- why: Indian law requires a business to publish, prominently on its site or app, a contact who can answer users' questions about how their personal data is used.
- fix: Publish a privacy contact (for example privacy@ your domain, or your Data Protection Officer's details if you have one) on the privacy page and in the footer, link it from consent screens, and include it in every reply to a data rights request.
- exceptions: A grievance or support contact that says it answers questions about personal data is enough. Applies to services processing personal data in India, or processing it abroad in connection with offering goods or services to people in India (DPDP s.3), from 13 May 2027. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)).
- elsewhere: none

## significant-data-fiduciary
- title: Extra duties if notified as a Significant Data Fiduciary
- area: business-details
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: code does not settle this. Raise it only when the answers or the project show processing of personal data of people in India at a very large scale, or of sensitive data at scale (health, finance, children). Then report Maybe and use the privacy page or README as the location.
  - ask: none
- why: A business the Government of India notifies as a Significant Data Fiduciary must have a Data Protection Officer based in India, an independent data auditor, and a yearly impact assessment and audit.
- fix: If notified: appoint a Data Protection Officer based in India and publish their contact, appoint an independent data auditor, run a Data Protection Impact Assessment and an audit every 12 months and send the main findings to the Data Protection Board, check that algorithms used on personal data don't put users' rights at risk, and keep any data the Government lists inside India.
- exceptions: Does not apply unless the Government has notified the business, or a class it belongs to, as Significant Data Fiduciaries. A small project with no sign of large-scale or sensitive processing is not a finding; list this check under Not checked or skipped with that reason. The DPDP rule skips data of people outside India that an Indian business processes under a contract with a foreign party (s.17(1)(d)). A Government notification under DPDP s.17(3), such as for startups, would lift this (s.10); none was found.
- elsewhere: none

## digital-media-publisher-duties
- title: Duties for news and streaming publishers to check on your own
- area: business-details
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: code does not settle this. Raise it only when the project publishes news and current affairs content as a business (a news site, portal or aggregator) or offers a curated catalogue of films, series or podcasts on demand. Then report Maybe and use the README or about page as the location.
  - ask: none
- why: In India, digital news and streaming publishers must follow a Code of Ethics (stayed, see exceptions), run a grievance process, join a self-regulating body, give the Ministry of Information and Broadcasting their details and publish monthly reports.
- fix: Give the Ministry of Information and Broadcasting your details within 30 days of starting, join a self-regulating body, appoint a Grievance Officer based in India (see grievance-officer-missing), publish monthly grievance and compliance reports, keep records of published content for at least 60 days, follow the Code of Ethics; for streaming, show ratings in promotion and captions where feasible.
- exceptions: Only publishers of news and current affairs content, or of online curated content, that operate in India or make content available there as a systematic business. Newspapers, their replica e-papers, and individuals not publishing as a business are out. The Bombay High Court stayed rule 9(1) (the Code of Ethics duty) and rule 9(3) in an interim order reported on 14 August 2021; status not confirmed, so present those parts as uncertain. Neither kind of publisher: not a finding; list this check under Not checked or skipped.
- elsewhere: none

## business-identity-missing
- title: Business name, address or customer care contact not shown
- area: business-details
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a site or app selling goods or services to consumers in India shows no registered legal name, no geographic address of its headquarters, or no customer care contact (email or phone) in the footer, contact, about or terms pages. Cite the footer or layout file.
  - code: details only inside a PDF, an image or a page nothing links to are not displayed prominently: report Maybe. One contact labelled for both customer care and grievances counts for both.
  - site: the footer, contact and about pages show no legal name, address or customer care contact
  - ask: none
- why: Indian e-commerce rules make every business selling online to consumers in India display its legal name, address, website and customer care and grievance contacts prominently.
- fix: Show in the footer and on a contact page the registered legal name (such as "Example Pvt Ltd"), the address of the headquarters and every branch, the website name, and customer care email and phone numbers; add the grievance officer as in grievance-officer-missing.
- exceptions: Only businesses selling goods or services online, including digital products and subscriptions, to consumers in India; foreign ones too if they systematically offer to them (E-Commerce Rules r.2). Sales only to businesses for commercial use are likely out: those buyers aren't consumers under Consumer Protection Act s.2(7), though r.2 doesn't say so. Individuals selling in a personal capacity, not as a regular business, are out. A seller only on someone else's marketplace is not an e-commerce entity (r.3(1)(b)); see seller-details-missing.
- elsewhere: none

## seller-details-missing
- title: Marketplace doesn't show who the seller is
- area: business-details
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a marketplace (other sellers list goods or services, such as a `vendors` table linked to products) whose product or offer page shows no seller business name, geographic address or customer care number before purchase, or hides the seller's rating where one exists. Cite the product page.
  - code: seller onboarding that collects no legal name, address, email, phone, or GSTIN and PAN where applicable, so the platform can't show them. Cite the form or schema.
  - code: from 1 January 2027: no seller website and email where available, or no GSTIN or MSME number, on the listing; an invoice that omits the seller's name or prints it smaller than the platform's name. Cite the template.
  - site: a product page names no seller, or the seller page shows no address or contact
  - ask: none
- why: Indian e-commerce rules make marketplaces show each seller's name, address, contact and rating before purchase, so buyers know who they are dealing with.
- fix: On each product or offer page show the seller's business name, whether registered, address, customer care number, website and email where available, rating, grievance officer, and GSTIN or other government ID number; on invoices print the seller's name in the same font size as yours.
- exceptions: Only marketplaces: platforms where other sellers offer goods or services to consumers in India (E-Commerce Rules r.3(1)(g)). A business selling only its own goods or services is out; see business-identity-missing, whose scope limits also apply. The website, email, ID number and invoice items start on 1 January 2027.
- elsewhere: none

## country-of-origin-missing
- title: Goods listed without country of origin, importer or expiry date
- area: business-details
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a marketplace product schema or listing page for goods with no country of origin, or no expiry date for goods that have one. Cite the schema or page.
  - code: imported goods or services listed by any online store or marketplace without the importer's name and details, and imported goods from 1 January 2027 without the full name of the country of origin. Cite the schema or page.
  - code: from 1 January 2027, goods with a best before or use before date, such as food or cosmetics, listed without it. Cite the page.
  - site: open a product page and look for the country of origin, importer and expiry or best before date
  - ask: none
- why: Indian e-commerce rules require the importer of imported goods, and on marketplaces the country of origin and any expiry date, to be shown before purchase, and from 1 January 2027 every online store must name the origin of imports.
- fix: Add `country_of_origin`, `importer` (name and details) and `expiry_or_best_before` fields to the product model, require them for imported or dated goods, and show them on the product page near the price.
- exceptions: Country of origin and dates apply to goods only; the importer duty (r.4(6)) also covers imported services. A store selling its own goods must name the country of origin only for imports under these rules, plus notices other laws require (r.7(1)(b)), so a missing origin on its domestic goods is a Maybe. Food dates follow food safety law. On marketplaces sellers supply the details and the platform displays them. Scope limits in business-identity-missing apply.
- elsewhere: none

## ranking-parameters-undisclosed
- title: Marketplace doesn't explain how it ranks products or sellers
- area: business-details
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: a marketplace with search or listing ranking (a score, boost, relevance sort, featured sellers) but no public page or help text naming the main ranking parameters and their relative importance. Cite the ranking code and where the explanation should be.
  - code: from 1 January 2027 the explanation must list the parameters in descending order of importance.
  - site: look for a "How we rank" or "About these results" link near search results or in the help pages
  - ask: none
- why: Indian e-commerce rules make marketplaces publish, in plain language, the main parameters that decide how goods and sellers are ranked and how much each one counts.
- fix: Add a public "How we rank results" page, linked from search results, that lists the main ranking parameters (such as relevance to the query, price, rating, delivery time, paid placement) in descending order of importance, in plain language.
- exceptions: Only marketplaces where other sellers offer goods or services to consumers in India (r.3(1)(g)); a single-seller store is out. Paid placements must also be labelled; see sponsored-listing-unlabelled. Scope limits in business-identity-missing apply.
- elsewhere: none

## ecommerce-operations
- title: Indian e-commerce and content-hosting duties to check on your own
- area: business-details
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: code does not settle this. Raise it only when the project sells goods or services online to consumers in India, runs a marketplace for them, or hosts users' content for people in India. Report one Maybe for all of it, at the terms page or README.
  - code: name in that one finding any of these if seen: a cancellation fee charged to buyers; prices set by user group, device or location, or surge prices; refunds held for days or given only as store credit; search results boosted regardless of the query.
  - code: also name there: a price with no word on tax (no "incl. GST" or tax line); a price cut whose prior price was typed in by hand or is an MRP; payment methods, fees or charge-back options explained only on the payment provider's page.
  - code: for a marketplace also name: no seller undertaking that listings are accurate; seller terms silent on preferential treatment; buyer data used for the platform's own brands or associated sellers; bundled fees for unrelated services (from 1 January 2027).
  - code: for hosts of users' content also name: no quick admin removal of one item, removed content hard-deleted rather than kept, or account deletion that erases sign-up details at once.
  - ask: none
- why: Indian rules add duties code can't fully show: for online sellers a nodal officer, the consumer helpline, timely refunds and fair prices; for hosts of users' content removal clocks of 2 to 36 hours, 180 days of records and 72 hours for agencies.
- fix: Sellers: companies name a nodal officer resident in India; join the National Consumer Helpline; pay accepted refunds in reasonable time; charge cancellation fees only if you bear similar ones; keep prices and ads true; from 2027, self-audit dark patterns yearly. Hosts: name who takes orders and removes a URL at once; keep removed content and records 180 days; answer agencies in 72 hours.
- exceptions: Each duty binds only whom its rule names: companies for the nodal officer, marketplaces for seller items, intermediaries offered in India for content duties (a site where only the owner publishes is not one). From 1 January 2027 the helpline is a must, and the search, self-audit, data-use and bundled-fee duties start. The 3-hour clock starts only from a court order or authorised officer's notice; the 36 hours exclude ownership, IP and general unlawfulness complaints; the 2-, 3- and 36-hour limits apply from 20 February 2026. See also grievance-officer-missing, synthetic-media-labels.
- elsewhere: none
