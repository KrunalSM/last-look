import { NextResponse } from "next/server";
import { cancelSubscriptions } from "../../../../lib/billing";
import { supabase } from "../../../../lib/db";
import { sessionUserId } from "../../../../lib/session";

export async function POST(req: Request) {
  const userId = await sessionUserId();
  const folder = `gallery/${userId}`;
  const gallery = supabase.storage.from("public-gallery");
  const { data: files } = await gallery.list(folder, { limit: 1000 });
  if (files?.length) await gallery.remove(files.map((f) => `${folder}/${f.name}`));
  await cancelSubscriptions(userId);
  await supabase.from("profiles").delete().eq("id", userId);
  return NextResponse.redirect(new URL("/goodbye", req.url), 303);
}
