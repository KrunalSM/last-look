import { NextResponse } from "next/server";
import { isNewSubscriber, stripe } from "../../../lib/billing";
import { sessionUserId } from "../../../lib/session";

export async function POST(req: Request) {
  const userId = await sessionUserId();
  const session = await stripe.checkout.sessions.create({
    mode: "subscription",
    line_items: [{ price: process.env.PRO_MONTHLY_PRICE_ID!, quantity: 1 }],
    // First month ₹349 for new subscribers: a ₹150-off coupon with duration "once".
    discounts: (await isNewSubscriber(userId)) ? [{ coupon: process.env.FIRST_MONTH_COUPON_ID! }] : undefined,
    subscription_data: { metadata: { user_id: userId } },
    success_url: new URL("/welcome", req.url).toString(),
    cancel_url: new URL("/checkout", req.url).toString(),
  });
  return NextResponse.redirect(session.url!, 303);
}
