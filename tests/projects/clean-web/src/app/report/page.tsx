export default function Report() {
  return (
    <form method="post" action="/api/report">
      <h1>Report content</h1>
      <p>Tell us about content that is illegal or breaks our Terms. We review reports within 24 hours and remove content that is unlawful.</p>
      <label>Link to the content <input name="url" type="url" required /></label>
      <label>What is wrong with it? <textarea name="reason" required /></label>
      <button type="submit">Send report</button>
    </form>
  );
}
