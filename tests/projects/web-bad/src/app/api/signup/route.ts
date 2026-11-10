import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { supabase } from "../../../lib/db";

export async function POST(req: Request) {
  const form = await req.formData();
  const email = String(form.get("email"));
  const password_hash = await bcrypt.hash(String(form.get("password")), 10);
  const marketing = form.get("marketing") === "on";

  const { error } = await supabase.from("profiles").insert({
    email,
    password_hash,
    marketing_opt_in: marketing,
  });
  if (error) return NextResponse.json({ error: error.message }, { status: 400 });

  console.log("new signup:", email);
  return NextResponse.redirect(new URL("/welcome", req.url), 303);
}
