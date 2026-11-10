# Third-party data

## google-fonts-remote
- title: Google Fonts loaded from Google's servers
- area: third-party-data
- needs: none
- severity: Medium
- evidence-default: confirm
- look-for:
  - code (web): a `<link>` or CSS `@import` pointing to `fonts.googleapis.com` or `fonts.gstatic.com`, in HTML, layout files, CSS or `_document`. Cite that line.
  - code (mobile): WebView HTML that links Google Fonts.
  - site: the page requests fonts.googleapis.com or fonts.gstatic.com when it loads
  - ask: none
- why: Each page view sends the visitor's IP address to Google without consent, and a German court awarded damages for this.
- fix: Host the font files yourself (downloaded files or an `@fontsource` package) and remove the fonts.googleapis.com link.
- exceptions: Not a finding for `next/font/google` in Next.js, which downloads the font at build time and serves it from your own domain. Not a finding for self-hosted font files or `@fontsource` packages.
- elsewhere: EU | A German court found remote Google Fonts unlawful without consent (LG München I, January 2022) | https://www.gesetze-bayern.de/Content/Document/Y-300-Z-GRURRS-B-2022-N-612
