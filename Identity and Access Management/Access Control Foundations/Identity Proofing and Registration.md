Before any credential can be issued, the organization must decide **that this person is who they claim to be**. This is **identity proofing**, and the resulting account is created by **registration** (enrollment).

Everything downstream inherits this step's quality. A certificate, a hardware token, and a biometric are all strong proof of *continuity* with registration — and worthless if the wrong person registered.

## Proofing Methods

| Method | How | Weakness |
|---|---|---|
| **In-person** | Applicant appears before a trusted authority with government-issued ID | Expensive, does not scale |
| **Documentary (remote)** | Photo of ID plus a liveness selfie, validated against the issuer | Forged and stolen documents, deepfakes |
| **Knowledge-based (KBA)** | Questions from credit or public records ("which of these streets have you lived on") | Answers are often in breach data or on social media |
| **Trusted referee / sponsor** | An existing verified employee vouches for the applicant | Only as trustworthy as the sponsor |
| **Out-of-band** | Code sent to a phone number or postal address already tied to the identity | Proves control of a channel, not identity |

**Identity Assurance Levels (IAL)** grade this: IAL1 self-asserted (no proofing), IAL2 remote or in-person evidence, IAL3 in-person with verified biometric capture. They are independent of **AAL** (authenticator strength) and **FAL** (federation assurance) — a system can proof weakly and authenticate strongly, or the reverse.

## Registration and Credential Issuance

- Issue credentials over a **different channel** than the one used to request them.
- **Initial passwords are temporary** and must be changed at first use.
- Hardware tokens and smartcards are handed over against a signature; the binding between token and identity is recorded.
- Re-proofing is needed for **account recovery** — a weak reset path silently lowers the assurance of the whole scheme, which is how most "strong" MFA deployments are actually broken.

Registration is the technical half of hiring; the HR half is in [[Personnel Security Lifecycle]], and account creation itself in [[Identity and Access Provisioning Lifecycle]].

## Key Points

- **Proofing establishes identity once; authentication only proves continuity with that moment.**
- **IAL grades proofing, AAL grades the authenticator, FAL grades the federation — they are set independently.**
- **The account recovery path is a second registration and must match the original's rigor.**
