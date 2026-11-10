import type { ReactNode } from "react";
import Script from "next/script";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Script src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-0000000000000000" strategy="afterInteractive" crossOrigin="anonymous" />
        <main>{children}</main>
        <footer>
          <a href="/privacy">Privacy policy</a>
          <p>Grievance Officer: Ravi Iyer, grievance@tinytales.example. We acknowledge complaints within 24 hours and resolve them within 7 days.</p>
          <p>TinyTales Learning Pvt Ltd, 4 Example Lane, Bengaluru 560001, India. Help: help@tinytales.example, +91 80 0000 0000</p>
        </footer>
      </body>
    </html>
  );
}
