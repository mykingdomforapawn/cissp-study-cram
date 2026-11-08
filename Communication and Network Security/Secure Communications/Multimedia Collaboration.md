## What Collaboration Tools Are

**Multimedia collaboration** is the use of shared real-time tools — remote meetings, instant messaging, chat channels, shared whiteboards and documents — to work across distance. Technologically these are **converged** applications: voice, video, screen content, files, and text over one IP platform, usually a cloud service (see [[Converged and Multilayer Protocols]]).

The security story is short because it repeats: these tools make **an organization's internal conversation available on an outside platform**, in a form that is easy to record and easy to join.

## Remote Meetings

Remote meeting, video conferencing, and virtual presentation platforms carry audio, video, screen sharing, chat, and recordings.

Risks and the controls that answer them:

- **Unauthorized attendance** — meeting IDs guessed or links forwarded ("meeting bombing"). Require **authentication to join**, unique IDs with passcodes, a **waiting room**, and lock the meeting once started.
- **Recording** — meetings are recorded by the platform or quietly by a participant. Control who may record, require notification (often a legal requirement, see [[Laws]]), and classify and retain the recordings like any other records.
- **Screen-share leakage** — the accidental disclosure: notifications, other documents, open tabs, and the wrong window shared. The control is procedural (share one window, not the desktop; enable do-not-disturb).
- **Eavesdropping in transit** — require TLS for signaling and encrypted media; prefer **end-to-end encryption** where the content warrants it, noting that it usually disables cloud recording and transcription.
- **Platform trust and data residency** — the provider sees everything not end-to-end encrypted, and stores recordings and transcripts in a jurisdiction that may matter (see [[Data Localization and Sovereignty]]).
- **The endpoints are cameras and microphones** in homes and public spaces: background disclosure, people overheard, and malware that activates the camera.

## Instant Messaging and Chat

IM and persistent chat (team channels, direct messages) are the informal layer, which is exactly what makes them risky.

- **Informality bypasses process.** Decisions, approvals, credentials, and sensitive data get typed into chat because it feels transient. It is not: chat is **logged, retained, and discoverable**, and it is a prime target after an account compromise.
- **Shadow IT and consumer apps.** Staff use whatever is convenient when the sanctioned tool is awkward, moving corporate data onto unmanaged platforms. The control is providing a usable sanctioned tool and stating the policy.
- **Malware and phishing in chat.** Links and file transfers in IM bypass the email gateway entirely, and a message from a compromised colleague's account carries far more trust than an email.
- **External and guest participants** in shared channels, and **federated** connections with partner organizations, extend the audience beyond the organization — guest access needs review and expiry.
- **Bots and integrations** hold broad tokens into the workspace and into other systems; they are a supply-chain path and an over-privileged one.
- **Weak legacy protocols**: older IM protocols lacked encryption and authentication entirely; current enterprise platforms use TLS, but **transport encryption does not hide content from the provider**.

**Presence information** — "available", "in a meeting", location, device — is useful and is also **metadata disclosure**: it reveals schedules, travel, and working patterns, internally and sometimes to outside contacts.

## Common Controls

- **Sanction specific platforms** and state which data classifications may be discussed on them; block or discourage the rest.
- **Identity**: SSO and MFA on the collaboration platform; deprovision on termination, including guest accounts.
- **Retention and eDiscovery**: define retention for chat and recordings deliberately — too short destroys evidence, too long creates liability.
- **DLP and monitoring** on file sharing and messages, balanced against the privacy expectation staff have in a chat tool, which should be stated in policy.
- **Awareness**: what not to put in chat, how to verify an unexpected request from a colleague's account, and meeting hygiene.

## Key Points

- **Collaboration platforms move internal conversation onto an outside service, recorded and searchable by default.**
- **Meeting controls: authentication to join, passcodes, waiting rooms, locking, and a policy on recording and notification.**
- **Chat is informal but permanent, logged, discoverable, and unfiltered by the email gateway — a compromised account is trusted by colleagues.**
- **Presence data is metadata disclosure about schedules and location.**
- **Transport encryption does not hide content from the provider; end-to-end encryption usually costs recording and transcription.**
