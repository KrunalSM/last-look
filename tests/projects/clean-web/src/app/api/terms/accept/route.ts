import { NextResponse } from "next/server";
import { supabase } from "../../../../lib/db";
import { sessionUserId } from "../../../../lib/session";
import { CURRENT_TERMS_VERSION } from "../../../../lib/terms";

export async function POST(req: Request) {
  const userId = await sessionUserId();
  await supabase
    .from("profiles")
    .update({ terms_version: CURRENT_TERMS_VERSION, terms_accepted_at: new Date().toISOString() })
    .eq("id", userId);
  const res = NextResponse.redirect(new URL("/", req.url), 303);
  res.cookies.set("terms_version", CURRENT_TERMS_VERSION, { httpOnly: true, secure: true, sameSite: "lax" });
  return res;
}
