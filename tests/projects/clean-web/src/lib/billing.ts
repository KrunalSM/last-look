import Stripe from "stripe";

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

// A new subscriber has no earlier subscription of any status.
export async function isNewSubscriber(userId: string): Promise<boolean> {
  const found = await stripe.subscriptions.search({ query: `metadata['user_id']:'${userId}'`, limit: 1 });
  return found.data.length === 0;
}

// Stop renewal at the end of the paid period for every subscription of this user that is not already cancelled.
export async function cancelSubscriptions(userId: string): Promise<void> {
  const found = await stripe.subscriptions.search({ query: `metadata['user_id']:'${userId}'` });
  for (const sub of found.data) {
    if (sub.status !== "canceled") await stripe.subscriptions.update(sub.id, { cancel_at_period_end: true });
  }
}
