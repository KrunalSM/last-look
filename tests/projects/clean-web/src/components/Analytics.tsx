"use client";
import { useEffect, useState } from "react";
import Script from "next/script";

type Choice = "granted" | "denied" | null;

export default function Analytics() {
  const [choice, setChoice] = useState<Choice>(null);
  useEffect(() => setChoice(localStorage.getItem("analytics-consent") as Choice), []);

  function decide(value: "granted" | "denied") {
    const before = localStorage.getItem("analytics-consent");
    localStorage.setItem("analytics-consent", value);
    // Withdrawing after Accept: reload so the analytics scripts already on the page stop.
    if (before === "granted" && value === "denied") return window.location.reload();
    setChoice(value);
  }

  return (
    <>
      {choice === "granted" && (
        <>
          <Script src="https://www.googletagmanager.com/gtag/js?id=G-FAKE000000" strategy="afterInteractive" />
          <Script id="gtag-init" strategy="afterInteractive">{`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-FAKE000000');
          `}</Script>
        </>
      )}
      {choice !== null && (
        <button type="button" onClick={() => setChoice(null)}>
          Cookie settings
        </button>
      )}
      {choice === null && (
        <div role="dialog" aria-label="Analytics cookies">
          <p>
            We use analytics cookies to see which pages are used. They stay off unless you accept.{" "}
            <a href="/privacy">Privacy policy</a>
          </p>
          <button onClick={() => decide("denied")}>Reject</button>
          <button onClick={() => decide("granted")}>Accept</button>
        </div>
      )}
    </>
  );
}
