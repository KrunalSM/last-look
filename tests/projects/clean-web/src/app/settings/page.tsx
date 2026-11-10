export default function Settings() {
  return (
    <section>
      <h1>Settings</h1>
      <a href="/settings/password">Change password</a>
      <a href="/settings/billing">Billing</a>
      <a href="/api/logout">Log out</a>
      <form method="post" action="/api/account/delete">
        <p>Deleting your account removes your profile and uploaded images, and cancels any subscription.</p>
        <button type="submit">Delete my account</button>
      </form>
    </section>
  );
}
