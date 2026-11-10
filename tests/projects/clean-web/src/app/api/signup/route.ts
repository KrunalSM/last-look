import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { supabase } from "../../../lib/db";
import { CURRENT_PRIVACY_VERSION, CURRENT_TERMS_VERSION } from "../../../lib/terms";

export async function POST(req: Request) {
  const form = await req.formData();
  if (form.get("terms") !== "on") return NextResponse.json({ error: "Accept the Terms" }, { status: 400 });
  const email = String(form.get("email"));
  const password_hash = await bcrypt.hash(String(form.get("password")), 10);
  const marketing = form.get("marketing") === "on";
  const now = new Date().toISOString();

  const { error } = await supabase.from("profiles").insert({
    email,
    password_hash,
    marketing_opt_in: marketing,
    marketing_opt_in_at: marketing ? now : null,
    privacy_version: CURRENT_PRIVACY_VERSION,
    terms_version: CURRENT_TERMS_VERSION,
    terms_accepted_at: now,
  });
  if (error) return NextResponse.json({ error: "Could not sign up" }, { status: 400 });

  const res = NextResponse.redirect(new URL("/welcome", req.url), 303);
  res.cookies.set("terms_version", CURRENT_TERMS_VERSION, { httpOnly: true, secure: true, sameSite: "lax" });
  return res;
}
