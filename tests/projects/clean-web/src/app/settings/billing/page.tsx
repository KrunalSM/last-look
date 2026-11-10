export default function Billing({ searchParams }: { searchParams: { cancelled?: string } }) {
  return (
    <section>
      <h1>Billing</h1>
      <p>PhraseBox Pro renews every month at ₹499, including GST, until you cancel.</p>
      {searchParams.cancelled ? (
        <p>Your subscription is cancelled. You keep Pro until the end of the month you paid for, and you will not be charged again.</p>
      ) : (
        <form method="post" action="/api/billing/cancel">
          <button type="submit">Cancel subscription</button>
        </form>
      )}
    </section>
  );
}
