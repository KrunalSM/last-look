# Licences

## content-rights-unclear
- title: Third-party content, brands or services used without clear rights
- area: licences
- needs: mobile app
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: report Maybe when the app uses others' brands or media: another company's name, logo or characters in the app name, icon or screens, a suggested link to another company or a government, or media with no licence noted. Cite the asset or name.
  - code (ios): Apple look-alike designs or endorsement claims, bundled Apple emoji images, or other platforms' names or icons.
  - code: media downloading or converting from YouTube, SoundCloud, Vimeo or Apple Music, scraping another service, or showing another service's content. Cite the call, and check that the service's terms allow it.
  - ask: none
- why: Both stores remove apps that use others' trademarks, copyrighted works or services without permission or impersonate other companies or apps, and Apple also bars implied Apple endorsement.
- fix: Keep a list of each third-party brand, asset and service with its licence or terms, get written permission where needed (Google Play asks to see it before submission), remove Apple look-alike designs, bundled Apple emoji and other platforms' names, and drop media downloading that the source hasn't authorised.
- exceptions: Unicode characters that render as Apple emoji are fine. Assets and SDKs used within their licence, and Apple's own RSS feeds, are fine. Other platforms' names or icons are allowed only for specific interactive functionality that App Review accepts. Only for apps on the App Store or Google Play.
- elsewhere: none

## open-source-licence-terms
- title: Open-source code used without meeting its licence terms
- area: licences
- needs: none
- severity: Medium
- evidence-default: maybe
- look-for:
  - code: a GPL or AGPL header or SPDX id (`SPDX-License-Identifier: GPL-`, `AGPL-`, "GNU General Public License", "GNU Affero") in code the app ships or runs, when the app has no open-source licence (no open LICENSE or COPYING file, `"license": "UNLICENSED"`, or a proprietary licence). Cite the header.
  - code: there, note whether the app offers its source: modified AGPL code that users reach over a network, and GPL code sent to browsers or bundled in a mobile app, need the source offered under the same licence.
  - ask: none
- why: Open-source licences are permissions with conditions, so shipping copyleft code without offering its source can breach the licence.
- fix: For AGPL or GPL code, either release your app's source under that licence (with a source link users can reach), replace the code with permissively licensed code, or buy a commercial licence if offered.
- exceptions: GPL code that runs only on your own server and is never sent to users needs no source release (GNU GPL FAQ); modified AGPL code does once users reach it over a network. LGPL, MPL and dual-licensed code have their own terms. Licence fit is a legal question, so report Maybe, never Confirmed.
- elsewhere: none
