export default function SignUp() {
  return (
    <form method="post" action="/api/signup">
      <h1>Create your account</h1>
      <label>Email <input name="email" type="email" required /></label>
      <label>Password <input name="password" type="password" required /></label>
      <label>
        <input name="terms" type="checkbox" required /> I accept the <a href="/terms">Terms</a> and have read the{" "}
        <a href="/privacy">Privacy policy</a>
      </label>
      <label>
        <input name="marketing" type="checkbox" /> Send me offers and product news by email (optional)
      </label>
      <button type="submit">Sign up</button>
    </form>
  );
}
