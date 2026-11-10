"use client";
import { useEffect } from "react";
import LogRocket from "logrocket";

export default function Replay() {
  useEffect(() => {
    LogRocket.init("phrasebox-fake/web");
  }, []);
  return null;
}
