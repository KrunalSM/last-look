import { NextResponse } from "next/server";
import { supabase } from "../../../lib/db";

// Study-deck images go to a public bucket and show on the gallery page.
export async function POST(req: Request) {
  const form = await req.formData();
  const image = form.get("image") as File;
  const path = `gallery/${Date.now()}-${image.name}`;
  await supabase.storage.from("public-gallery").upload(path, image);
  return NextResponse.json({ path });
}
