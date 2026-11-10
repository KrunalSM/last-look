import { cookies } from "next/headers";
import { jwtVerify } from "jose";

export async function sessionUserId(): Promise<string> {
  const token = cookies().get("session")?.value ?? "";
  const { payload } = await jwtVerify(token, new TextEncoder().encode(process.env.SESSION_SECRET!));
  return String(payload.sub);
}
