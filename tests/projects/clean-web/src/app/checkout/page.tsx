import { isNewSubscriber } from "../../lib/billing";
import { sessionUserId } from "../../lib/session";

export default async function Checkout() {
  const firstMonth = await isNewSubscriber(await sessionUserId());
  return (
    <section>
      <h1>PhraseBox Pro</h1>
      <p>First month ₹349 for new subscribers, then ₹499 per month. Prices include GST.</p>
      <p>You are charged {firstMonth ? "₹349" : "₹499"} today and the plan renews every month at ₹499 until you cancel.</p>
      <p>Cancel any time under <a href="/settings/billing">Settings, Billing</a>, before the next charge date. Your access then runs to the end of the paid month.</p>
      <form method="post" action="/api/checkout">
        <button type="submit">Pay {firstMonth ? "₹349" : "₹499"} and subscribe</button>
      </form>
      <p><a href="/refunds">Refunds and payments</a></p>
    </section>
  );
}
