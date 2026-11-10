"use client";
import OfferTimer from "../../components/OfferTimer";

async function pay() {
  const key = "sk_test_FAKE0000000000000000";
  const res = await fetch("https://api.stripe.com/v1/checkout/sessions", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      mode: "subscription",
      "line_items[0][price]": "price_pro_monthly",
      "line_items[0][quantity]": "1",
      success_url: location.origin + "/welcome",
    }),
  });
  location.href = (await res.json()).url;
}

export default function Checkout() {
  return (
    <section>
      <h1>PhraseBox Pro</h1>
      <OfferTimer />
      <p>₹499</p>
      <button onClick={pay}>Pay ₹499</button>
      <form method="post" action="/api/paylater">
        <label>PAN <input name="pan" required /></label>
        <label>Monthly income (₹) <input name="income" type="number" required /></label>
        <label>Email <input name="email" type="email" required /></label>
        <button type="submit">Or pay in 3 monthly EMIs</button>
      </form>
    </section>
  );
}
