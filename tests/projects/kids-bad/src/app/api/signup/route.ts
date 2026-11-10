import { NextResponse } from "next/server";
import { supabase } from "../../../lib/db";

export async function POST(req: Request) {
  const form = await req.formData();
  const { data, error } = await supabase.from("children").insert({
    child_name: String(form.get("child_name")),
    child_age: Number(form.get("child_age")),
    school: String(form.get("school") ?? ""),
    parent_email: String(form.get("parent_email")),
    parental_consent: form.get("parent_ok") === "on",
    consent_at: new Date().toISOString(),
  }).select("id").single();
  if (error) return NextResponse.json({ error: "Could not sign up" }, { status: 400 });

  const res = NextResponse.redirect(new URL("/stories", req.url), 303);
  res.cookies.set("child_id", data.id, { httpOnly: true, secure: true, sameSite: "lax" });
  return res;
}
