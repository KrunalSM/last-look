# Web Content Accessibility Guidelines (WCAG) 2.2
- source-id: wcag
- walk: targeted
- url: https://www.w3.org/TR/WCAG22/
- read-on: 2026-11-03

W3C Recommendation of 12 December 2024. Also read: Understanding notes for 1.4.3, 1.4.4, 2.4.7 and 3.3.2, failure technique F65, and the ACT rule "Meta viewport allows for zoom" (https://www.w3.org/WAI/standards-guidelines/act/rules/b4f0c3/). Only success criteria that a basic code check relies on are listed; the others are not walked.

| Section | Topic | Status | Checks | Verified on | Note |
|---|---|---|---|---|---|
| SC 1.1.1 | Non-text Content: text alternatives for images and names for icon controls | Partly covered | image-alt-missing | 2026-11-03 | F65: img with no alt. Media alternatives are not checked. |
| SC 1.3.1 | Info and Relationships: structure and labels programmatically determined | Partly covered | form-label-missing | 2026-11-03 | Only form field labels; headings, lists and tables are not checked. |
| SC 1.4.3 | Contrast (Minimum): 4.5:1 for text, 3:1 for large text | Partly covered | low-contrast-text | 2026-11-03 | Only literal colour pairs applied together in code; rendered pages and themed or transparent colours are not checked. |
| SC 1.4.4 | Resize Text: text resizable to 200 percent | Partly covered | zoom-disabled | 2026-11-03 | Only viewport settings that block zoom; layout breakage at 200 percent needs a browser. |
| SC 2.1.1 | Keyboard: all functions work from a keyboard | Partly covered | keyboard-focus-missing | 2026-11-03 | Only clickable non-button elements and removed focus. |
| SC 2.4.7 | Focus Visible: keyboard focus indicator visible | Covered | keyboard-focus-missing | 2026-11-03 | F78 and F55. |
| SC 3.1.1 | Language of Page | Covered | page-lang-missing | 2026-11-03 |  |
| SC 3.3.2 | Labels or Instructions for user input | Partly covered | form-label-missing | 2026-11-03 | Fields with no label at all; placeholder-only fields and instructions are not reported. |
| SC 4.1.2 | Name, Role, Value for interface components | Partly covered | form-label-missing, image-alt-missing | 2026-11-03 | Names of fields and icon-only controls only; custom widget roles and states are not checked. |
