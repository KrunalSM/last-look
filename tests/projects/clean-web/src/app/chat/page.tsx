"use client";
import { useState } from "react";

export default function Chat() {
  const [reply, setReply] = useState("");
  async function send(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const message = new FormData(e.currentTarget).get("message");
    const res = await fetch("/api/chat", { method: "POST", body: JSON.stringify({ message }) });
    setReply((await res.json()).reply);
  }
  return (
    <form onSubmit={send}>
      <h1>Practice chat</h1>
      <p>Your messages are sent to OpenAI to write the replies. Do not enter sensitive details. See our <a href="/privacy">Privacy policy</a>.</p>
      <label>Message <input name="message" placeholder="Say something in Spanish" /></label>
      <button>Send</button>
      <p>{reply}</p>
    </form>
  );
}
