import { NextResponse } from "next/server";
import { supabase } from "../../../lib/db";

export async function POST(req: Request) {
  const form = await req.formData();
  await supabase.from("content_reports").insert({ url: String(form.get("url")), reason: String(form.get("reason")) });
  return NextResponse.redirect(new URL("/report/thanks", req.url), 303);
}
