import { NextResponse } from "next/server";
import { cancelSubscriptions } from "../../../../lib/billing";
import { sessionUserId } from "../../../../lib/session";

export async function POST(req: Request) {
  await cancelSubscriptions(await sessionUserId());
  return NextResponse.redirect(new URL("/settings/billing?cancelled=1", req.url), 303);
}
