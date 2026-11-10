import { NextResponse } from "next/server";
import { supabase } from "../../../lib/db";
import { sessionUserId } from "../../../lib/session";

// Members share study-deck images; the bucket is public. Reports go through /report.
export async function POST(req: Request) {
  const userId = await sessionUserId();
  const image = (await req.formData()).get("image") as File;
  if (!["image/png", "image/jpeg"].includes(image.type) || image.size > 2_000_000) {
    return NextResponse.json({ error: "PNG or JPEG under 2 MB only" }, { status: 400 });
  }
  const path = `gallery/${userId}/${Date.now()}.${image.type.split("/")[1]}`;
  await supabase.storage.from("public-gallery").upload(path, image);
  return NextResponse.json({ path });
}
