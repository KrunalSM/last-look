import type { ReactNode } from "react";
import Script from "next/script";
import Replay from "../components/Replay";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet" />
      </head>
      <body style={{ fontFamily: "Inter, sans-serif" }}>
        <Script src="https://www.googletagmanager.com/gtag/js?id=G-FAKE000000" strategy="afterInteractive" />
        <Script id="gtag-init" strategy="afterInteractive">{`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'G-FAKE000000');
        `}</Script>
        <Replay />
        <main>{children}</main>
        <footer>
          <a href="/terms">Terms</a>
        </footer>
      </body>
    </html>
  );
}
