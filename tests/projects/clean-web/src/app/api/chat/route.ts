import { NextResponse } from "next/server";
import { Ratelimit } from "@upstash/ratelimit";
import { Redis } from "@upstash/redis";
import { sessionUserId } from "../../../lib/session";

// 20 messages a minute per member keeps the OpenAI bill bounded.
const limiter = new Ratelimit({ redis: Redis.fromEnv(), limiter: Ratelimit.slidingWindow(20, "1 m") });

export async function POST(req: Request) {
  const userId = await sessionUserId();
  if (!(await limiter.limit(userId)).success) {
    return NextResponse.json({ error: "Too many messages. Try again in a minute." }, { status: 429 });
  }
  const { message } = await req.json();
  const res = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.OPENAI_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ model: "gpt-4o-mini", messages: [{ role: "user", content: message }] }),
  });
  const data = await res.json();
  return NextResponse.json({ reply: data.choices[0].message.content });
}
