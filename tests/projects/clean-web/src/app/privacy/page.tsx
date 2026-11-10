import { CURRENT_PRIVACY_VERSION } from "../../lib/terms";

export default function Privacy() {
  return (
    <article>
      <h1>Privacy policy</h1>
      <p>Version {CURRENT_PRIVACY_VERSION}</p>
      <p>PhraseBox Learning Pvt Ltd, 12 Example Road, Pune 411001, India, runs PhraseBox and decides how this data is used. Contact: privacy@phrasebox.example.</p>
      <h2>What we collect, why, and on what legal basis</h2>
      <ul>
        <li>Email address and password hash: to run your account (needed for our contract with you).</li>
        <li>Images you upload: to show them in your public gallery, which anyone with the link can see (contract).</li>
        <li>Chat messages you send: passed on to OpenAI to write the replies, not kept by us (contract).</li>
        <li>Payment status from Stripe: to manage your subscription (contract).</li>
        <li>Content reports: the link and reason you send, to review the report (our legitimate interest in keeping the service lawful).</li>
        <li>A session cookie to keep you signed in, and a cookie noting which terms version you accepted (needed to run the service).</li>
        <li>Offers and news by email: only if you tick the box at sign-up (your consent).</li>
        <li>Analytics: only if you accept cookies, to see which pages are used (your consent).</li>
      </ul>
      <h2>Who receives it</h2>
      <p>Supabase (hosting), Upstash (counting chat messages per member id, to limit them, our legitimate interest in preventing abuse), Stripe (payments), OpenAI (chat replies) and Google (analytics, only with consent). We do not sell personal data. Some of these providers are in the United States; for EU users we rely on standard contractual clauses.</p>
      <h2>How long we keep it</h2>
      <p>Until you delete your account, then up to 30 days in backups.</p>
      <p>Where Indian law requires it, we keep records of processing, such as order and payment records and access logs, for one year, then erase them (a legal obligation).</p>
      <h2>Withdrawing consent</h2>
      <p>You can withdraw consent at any time, as easily as you gave it: use the Unsubscribe link in any offers email, and use Cookie settings at the bottom of every page to turn analytics off.</p>
      <h2>Your rights</h2>
      <p>Delete your account under Settings. To get a copy of your data, a list of who we shared it with, or a correction, write to privacy@phrasebox.example. You can also ask us to restrict how we use your data, object to a use based on our legitimate interest, or receive your data in a portable format.</p>
      <h2>Complaints</h2>
      <p>Write to our Grievance Officer (details in the footer). If you are in India and our answer does not resolve it, you can complain to the Data Protection Board of India. If you are in the EU, you can complain to your local data protection authority.</p>
    </article>
  );
}
