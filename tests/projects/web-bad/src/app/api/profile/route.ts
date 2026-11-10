import { NextResponse } from "next/server";
import { supabase } from "../../../lib/db";

// The settings page loads the member's details from here.
export async function GET(req: Request) {
  const id = new URL(req.url).searchParams.get("id");
  const { data } = await supabase.from("profiles").select("email, marketing_opt_in, created_at").eq("id", id).single();
  return NextResponse.json(data);
}
