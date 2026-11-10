import { NextResponse } from "next/server";

// Pro in 3 monthly instalments, financed by our NBFC partner.
export async function POST(req: Request) {
  const form = await req.formData();
  const res = await fetch("https://api.nbfc-partner.example/v1/loan-applications", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.LENDER_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      product: "phrasebox-pro",
      tenure_months: 3,
      pan: String(form.get("pan")),
      monthly_income: Number(form.get("income")),
      email: String(form.get("email")),
    }),
  });
  const { approved, loan_id } = await res.json();
  return NextResponse.json({ approved, loan_id });
}
