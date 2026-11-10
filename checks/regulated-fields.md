# Regulated fields

## regulated-field-present
- title: Regulated field that needs its own rules
- area: regulated-fields
- needs: none
- severity: High
- evidence-default: maybe
- look-for:
  - code: real-money games, where users pay or deposit money or value to play for winnings (wallets, paid contests with cash prizes, fantasy sports, betting or odds; `deposit`, `withdraw`, `winnings`, `wager`, `bet`, `prize pool`, `rake`). Cite the wallet or contest.
  - code: loans or credit the app offers or arranges for a bank or lender: loan or credit-line applications, pay-later or EMI plans from a lending partner, interest or APR (`loan`, `emi`, `apr`, `credit_limit`, `disburse`, `repayment`, a lender's API). Cite the call.
  - code: crypto services for others: exchanging crypto for money or other crypto, sending it, or holding users' wallets or keys (`custody`, an exchange API, withdrawal of tokens). Cite it.
  - code: medical features meant to diagnose, monitor or treat a condition: symptom checkers, dose or insulin calculators, readings of blood glucose, ECG or blood pressure used to advise treatment. Cite it.
  - code: report Maybe and name the field. Raise nothing for other apps.
  - ask: none
- why: Real-money games, lending, crypto services and medical software each have their own laws and licences, which this skill flags but does not audit.
- fix: Before launch, get advice from a lawyer who knows the field in each target country, starting with the rule cited here. India: check the Promotion and Regulation of Online Gaming Act 2025 first (not walked here; it may ban online money games), the RBI Digital Lending Directions, FIU-IND registration for crypto services, and the medical device rules.
- exceptions: Not for: payments, card EMI, pay-later or cardless EMI that a payment gateway or a lender's own widget offers while the app only redirects; wallet-connect dApps holding no keys or funds; games with no paid entry or prize; fitness or wellness tracking; health content that only informs. Children's services: see children checks. Store rules: restricted-app-type. Insurance, investing, telemedicine, pharmacy: no rules yet; list under Not checked or skipped. IT Rules gaming duties start three months after three gaming self-regulatory bodies are named, unless notified earlier (r.4B); none found.
- elsewhere: none
