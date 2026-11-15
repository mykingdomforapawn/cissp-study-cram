**Multifactor authentication (MFA)** requires evidence from **two or more different factor types**, so that compromising one does not grant access. Two of the same type is single-factor regardless of count — see [[Authentication Factors]].

- **Two-factor (2FA)** is MFA with exactly two.
- **Step-up authentication** demands an additional factor only for a sensitive action (a wire transfer, a privilege change), not at every login.
- **Adaptive / risk-based authentication** scores context — device, location, time, impossible travel, behavior — and challenges only when the score is poor. It raises security without raising friction for routine logins, at the cost of a scoring engine that can be wrong in both directions.

Strength depends on the **weakest accepted path**: offering FIDO2 but also allowing SMS fallback leaves the account as strong as SMS. The same applies to the recovery flow — see [[Identity Proofing and Registration]].

## Passwordless Authentication

Authentication with **no shared secret** to phish, reuse, or steal from the verifier. The user holds a private key; the service holds only the public key, so a breach of the service yields nothing usable.

- **FIDO2 / WebAuthn** — the underlying standard. The authenticator signs a challenge, and the signature is **bound to the site's origin**, so a lookalike site cannot relay it. This is what *phishing-resistant* means.
- **Passkeys** — FIDO2 credentials that are discoverable and can **sync across a user's devices** through a platform account. Convenience at the cost of trusting that sync provider; **device-bound** passkeys on a security key are stronger.
- **Platform authenticators** — Windows Hello, Touch ID, Face ID: the device unlocks the private key with a local biometric or PIN.

A single passkey gesture is effectively **multifactor**: possession of the device plus the biometric or PIN that unlocks the key. The biometric is verified **locally** and never sent to the service.

Other passwordless forms are weaker: **magic links** and **email OTPs** reduce the account to the security of the mailbox.

## Key Points

- **MFA needs different factor types; 2FA is MFA with two.**
- **Adaptive authentication challenges on risk score; step-up challenges on sensitive action.**
- **An MFA deployment is only as strong as its weakest fallback and its recovery path.**
- **FIDO2/WebAuthn is phishing-resistant because the signature is bound to the origin; passkeys trade device-binding for sync convenience.**
