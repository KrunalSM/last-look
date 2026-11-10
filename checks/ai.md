# AI

## ai-data-disclosure
- title: User data sent to an AI service without telling users
- area: ai
- needs: AI services
- severity: High
- evidence-default: confirm
- look-for:
  - code: calls to AI APIs (`api.openai.com`, the `openai` package, `@anthropic-ai/sdk`, `generativelanguage.googleapis.com`, Gemini, Mistral, Replicate, Hugging Face) that send user text, images or files. Cite the line that sends the request.
  - code: then check the screen where users enter that data for a notice naming the AI provider, and the privacy policy for the provider as a recipient. No notice and no policy mention confirms it.
  - code (ios): Apple also needs explicit permission before personal data goes to a third-party AI.
  - site: the chat or AI feature page shows no notice
  - ask: none
- why: Users must be told who receives their data, and Apple requires explicit permission before personal data is shared with a third-party AI.
- fix: Show a short notice where users type ("Messages you type here go to OpenAI, which writes each reply"), name the provider in the privacy policy, and on iOS ask permission before the first request.
- exceptions: On-device models that send nothing off the device are out of scope.
- elsewhere: none

## synthetic-media-labels
- title: AI-made images, video or audio not labelled
- area: ai
- needs: AI services, or user uploads and shared content
- severity: High
- evidence-default: confirm
- look-for:
  - code (generation): an AI feature that creates or changes images, video or audio (OpenAI images, Stability, Replicate, fal, ElevenLabs or other voice cloning, face swap, video models) returns or saves output with no visible AI-generated label, or audio with no spoken notice first. Cite that line.
  - code (generation): that image, video or audio output gets no provenance metadata (C2PA content credentials, an IPTC AI source type, an identifier of the service) though its format can carry it, or the code strips it, or offers a download without watermark or metadata.
  - code (generation): prompts or outputs of that image, video or audio feature pass no safety filter (a moderation call, provider safety settings) that blocks child abuse material, non-consensual intimate images, fake documents, help with weapons or explosives, or deceptive fakes of real people.
  - code (generation): the terms or the screen of that image, video or audio feature don't warn that misuse can mean removal, suspension, disclosure of the user's identity to a victim, and legal penalties.
  - code (hosting or sharing): users share images, video or audio with others. Report Maybe, never Confirmed: check that unlawful AI-made media is blocked, AI-made media is labelled, provenance metadata survives upload (re-encoding can strip it), and the terms warn of misuse. Cite the upload route.
  - site: AI-made images, video or audio appear without a label
  - ask: none
- why: Since 20 February 2026, India requires services that make, publish or share realistic AI-made images, video or audio to block unlawful ones, label the rest, embed provenance metadata where technically feasible, and keep labels from being removed.
- fix: Generation: add a visible "AI-generated" label (a spoken notice for audio), embed C2PA or similar metadata with your service's identifier, keep label and metadata through downloads and edits, filter prompts and outputs for unlawful content, and warn of misuse in the terms and on screen. Hosting: keep provenance metadata on upload, label AI-made media, and act on reports of unlawful ones.
- exceptions: Intermediaries offered to people in India whose service lets users create, change, publish or share AI-made audio, images or video (MeitY FAQ Q20). Hosting or sharing alone: Maybe only. Missing metadata is fine only where the output format can't carry it; a step the developer chose that strips it doesn't count, and the label still applies. Not covered: text-only output, routine edits that keep the meaning (colour, compression, transcription, translation, accessibility), good-faith documents and teaching material, and output that couldn't pass as a real person or event (Maybe if unsure).
- elsewhere: none

## ai-content-safeguards
- title: AI-made content has no in-app report or safety filter
- area: ai
- needs: AI services in a mobile app
- severity: High
- evidence-default: confirm
- look-for:
  - code: a chatbot or a text, image, video or voice generator whose output appears in the app with no in-app way to report or flag it (a flag button or report menu on the message or image). Cite the screen that shows the output.
  - code: prompts and outputs pass no safety filter (a moderation API call, or the provider's safety settings) that blocks sexual content involving children, deceptive impersonation and other banned content. For image, video or audio this is the synthetic-media-labels filter line: report one finding.
  - ask: none
- why: Both stores require apps that generate content with AI to filter or prevent objectionable content and let users report offensive output in the app.
- fix: Add a report or flag action on each AI message or generated item, send reports to a review queue and use them to tune filtering, and run prompts and outputs through a moderation check or the provider's strictest safety settings.
- exceptions: AI used only behind the scenes, with no generated content shown to users, is out of scope. Labels for AI-made media in India: see synthetic-media-labels. Apple counts AI content creation apps as user content apps, so blocking abusive users also applies there (see ugc-moderation-missing). Applies to apps on Google Play and the App Store.
- elsewhere: none
