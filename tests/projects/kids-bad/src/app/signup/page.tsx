export default function SignUp() {
  return (
    <form method="post" action="/api/signup">
      <h1>Make your reading profile</h1>
      <label>Your first name <input name="child_name" required /></label>
      <label>Your age <input name="child_age" type="number" min={6} max={12} required /></label>
      <label>Your school <input name="school" /></label>
      <label>Your parent's email <input name="parent_email" type="email" required /></label>
      <label>
        <input name="parent_ok" type="checkbox" required /> My parent says it's OK
      </label>
      <button type="submit">Start reading</button>
    </form>
  );
}
