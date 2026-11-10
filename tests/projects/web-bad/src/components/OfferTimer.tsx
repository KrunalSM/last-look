"use client";
import { useEffect, useState } from "react";

export default function OfferTimer() {
  const [left, setLeft] = useState(15 * 60);
  useEffect(() => { const t = setInterval(() => setLeft((s) => (s <= 1 ? 15 * 60 : s - 1)), 1000); return () => clearInterval(t); }, []);
  const mm = String(Math.floor(left / 60)).padStart(2, "0"), ss = String(left % 60).padStart(2, "0");
  return <p className="offer">Hurry! Price goes up in {mm}:{ss}. Only 2 spots left!</p>;
}
