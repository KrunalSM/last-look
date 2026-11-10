import type { ReactNode } from "react";
import { cookies } from "next/headers";
import { Inter } from "next/font/google";
import Analytics from "../components/Analytics";
import TermsUpdateBanner from "../components/TermsUpdateBanner";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <TermsUpdateBanner acceptedVersion={cookies().get("terms_version")?.value} />
        <main>{children}</main>
        <Analytics />
        <footer>
          <a href="/terms">Terms</a> · <a href="/privacy">Privacy policy</a> · <a href="/refunds">Refunds and payments</a> · <a href="/report">Report content</a>
          <p>Customer care: support@phrasebox.example, +91 20 0000 0000</p>
          <p>Grievance Officer: Asha Verma, grievance@phrasebox.example. We acknowledge complaints within 24 hours with a ticket number you can use to track them, and resolve them within 7 days.</p>
          <p>PhraseBox Learning Pvt Ltd, 12 Example Road, Pune 411001, India</p>
        </footer>
      </body>
    </html>
  );
}
