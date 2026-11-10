# Accessibility

## image-alt-missing
- title: Images without a text alternative
- area: accessibility
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (web): `<img>` with no `alt` attribute, including JSX `<img>`, an `<Image>` component passed no `alt`, and `<input type="image">` with no `alt`. Cite the tag.
  - code (web): an icon-only link or button (only an `<svg>` or icon component inside) with no text, `aria-label` or `aria-labelledby`.
  - code (android): an `ImageButton`, icon button or meaningful image with no `contentDescription` and not marked decorative. (React Native) a pressable icon with no `accessibilityLabel`.
  - ask: none
- why: Screen reader users can't tell what an image or icon button shows or does when it has no text alternative.
- fix: Add `alt` text that says what the image shows or does (for example `alt="Bar chart of monthly sign-ups"`), or `alt=""` for a purely decorative image; give icon-only controls an `aria-label`, `contentDescription` or `accessibilityLabel`.
- exceptions: `alt=""` on a decorative image is correct, not a finding. An `<img>` named by `aria-label`, `aria-labelledby` or `title` is not the F65 failure. Images hidden from assistive technology (`aria-hidden="true"`, `role="presentation"`) are not findings. A control whose text is visible next to the icon, inside it, needs no extra label.
- elsewhere: none

## form-label-missing
- title: Form fields without a label
- area: accessibility
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (web): `<input>`, `<select>` or `<textarea>` that is not inside a `<label>`, has no `<label for>` (JSX `htmlFor`) matching its `id`, and has no `aria-label`, `aria-labelledby` or `title`. Cite the field.
  - code (web): a field whose only label is its `placeholder` is not a finding here: mention it under Looked at, nothing found.
  - ask: none
- why: A field with no label leaves screen reader users, and anyone once the placeholder is gone, guessing what to enter.
- fix: Wrap the field in a `<label>` or add `<label for="id">` with visible text, for example `<label>Email <input name="email" type="email" /></label>`; use `aria-label` only where a visible label truly can't fit.
- exceptions: Hidden fields (`type="hidden"`), and buttons whose own text names them, need no label. A group of fields with one visible label and `aria-labelledby` is labelled.
- elsewhere: none

## low-contrast-text
- title: Text colours with too little contrast
- area: accessibility
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code: confirm only when a text colour and its background are both literal values with no transparency, applied together in one CSS rule, one component or an explicit foreground and background token pair, and their contrast ratio is below 4.5:1 (3:1 for large text). Cite both colours.
  - code: example of a clear failure: grey `#999999` text on a white `#ffffff` background is about 2.8:1.
  - code: any other case (colours set apart, inherited, themed at run time, or with alpha) is not a finding: list it under Looked at, nothing found.
  - ask: none
- why: Low-contrast text is hard or impossible to read for people with low vision, and for everyone on a phone in sunlight.
- fix: Darken the text colour or lighten the background until body text reaches at least 4.5:1 and large text 3:1 (for example `#595959` or darker on white), and change the token so every use updates.
- exceptions: Text in disabled controls, pure decoration, logos and brand names has no contrast minimum. Large text (at least 18pt, about 24px, or 14pt bold, about 18.7px) needs only 3:1.
- elsewhere: none

## keyboard-focus-missing
- title: Keyboard users can't reach controls or see focus
- area: accessibility
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (web): `outline: none`, `outline: 0` or Tailwind `outline-none` on `:focus`, `*` or buttons, links and fields, with no `:focus-visible`, ring, border, box-shadow, background or underline focus style in its place. Cite the rule.
  - code (web): a `div` or `span` with `onClick` that acts as a button or link, missing any of `tabIndex`, `role` or a key handler; use a real `<button>` or `<a>` instead.
  - code (web): script that moves focus away as soon as an element gets it (`onFocus={e => e.target.blur()}`).
  - ask: none
- why: People who use a keyboard or switch device can't use a control they can't reach, or find where they are when the focus outline is removed.
- fix: Remove `outline: none`, or replace it with a visible `:focus-visible` style (for example `outline: 2px solid` in a colour with 3:1 contrast), and use `<button>` and `<a href>` for clickable elements instead of `div` or `span`.
- exceptions: An `outline: none` that another visible focus style replaces is not a finding. Elements that are not interactive need no focus. A modal backdrop `div` with `onClick` is fine when Esc or a close button also closes the modal.
- elsewhere: none

## zoom-disabled
- title: Page zoom turned off
- area: accessibility
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (web): a viewport meta tag with `user-scalable=no`, or `maximum-scale` below 2 (such as `maximum-scale=1`). Cite the tag.
  - code (web): the same set through a framework, such as a Next.js `viewport` export with `userScalable: false` or `maximumScale: 1`.
  - ask: none
- why: People with low vision zoom in to read, and a viewport that blocks zoom stops them from enlarging text on phones.
- fix: Use `<meta name="viewport" content="width=device-width, initial-scale=1">` with no `user-scalable` or `maximum-scale` limit, and fix any layout that breaks when zoomed instead of blocking zoom.
- exceptions: A `maximum-scale` of 2 or more still allows text at 200 percent. Canvas games or maps that handle pinch-zoom themselves and offer their own text sizing are a Maybe, not Confirmed.
- elsewhere: none

## page-lang-missing
- title: Page language not set
- area: accessibility
- needs: none
- severity: Low
- evidence-default: confirm
- look-for:
  - code (web): the root `<html>` element in the root layout, `_document`, `index.html` or base template has no `lang` attribute, or an empty one. Cite the tag.
  - code (web): `lang` names the wrong language, such as `lang="en"` on a site whose pages are written in Hindi.
  - ask: none
- why: Without a page language, screen readers and translation tools may read the text with the wrong voice and pronunciation.
- fix: Set the main language on the root element, for example `<html lang="en">` or `<html lang="hi">`, and mark passages in another language with their own `lang`.
- exceptions: A page that sets `lang` from the user's chosen language at run time is not a finding.
- elsewhere: none
