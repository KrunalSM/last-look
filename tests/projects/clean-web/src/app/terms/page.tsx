import { CURRENT_TERMS_VERSION } from "../../lib/terms";

export default function Terms() {
  return (
    <article>
      <h1>Terms of Service</h1>
      <p>Version {CURRENT_TERMS_VERSION}</p>
      <p>PhraseBox is provided as is. You are responsible for what you share on the service.</p>
      <h2>What you may not post</h2>
      <ul>
        <li>Content you have no right to share, or that infringes a patent, trademark or copyright.</li>
        <li>Obscene, pornographic or paedophilic content, or content that invades someone's privacy, including bodily privacy.</li>
        <li>Harassment on the basis of gender, racially or ethnically objectionable content, content promoting money laundering or gambling, or content stirring up hatred between religious or caste groups.</li>
        <li>Content harmful to children.</li>
        <li>False or misleading content, or content that impersonates another person.</li>
        <li>Content that threatens India's unity, integrity, security or sovereignty, its relations with other countries or public order, or that incites an offence.</li>
        <li>Viruses or other harmful code, or anything else that breaks the law.</li>
      </ul>
      <p>
        We may remove content that breaks these rules and suspend or close the account that posted it. If you break
        the law you may face penalties, and we report offences that the law requires us to report.
      </p>
      <h2>Changes to these Terms</h2>
      <p>
        For a material change we email registered users at least 30 days before it applies and ask them to accept
        the new version when they next sign in. Earlier versions stay available on request.
      </p>
    </article>
  );
}
