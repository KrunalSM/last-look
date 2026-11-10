import { CURRENT_TERMS_VERSION } from "../lib/terms";

export default function TermsUpdateBanner({ acceptedVersion }: { acceptedVersion?: string }) {
  if (!acceptedVersion || acceptedVersion === CURRENT_TERMS_VERSION) return null;
  return (
    <form method="post" action="/api/terms/accept">
      <p>
        We updated our <a href="/terms">Terms</a> (version {CURRENT_TERMS_VERSION}). Please read them and accept to keep using PhraseBox.
      </p>
      <button type="submit">Accept the updated Terms</button>
    </form>
  );
}
