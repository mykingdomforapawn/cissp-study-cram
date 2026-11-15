Type 2 authentication: the subject proves possession of a physical or cryptographic object. Resists guessing and bulk credential theft, but is lost, stolen, or — for weaker forms — cloned.

## Smartcards and Certificates

A **smartcard** holds a private key and certificate in a tamper-resistant chip and performs the cryptographic operation **on the card**, so the key never leaves it. The card is proof of possession; adding a **PIN** makes it multifactor.

- **Contact** cards (inserted) vs. **contactless** (NFC field). Many issue both interfaces.
- **PIV** (US federal civilian) and **CAC** (US Department of Defense) are the standard government smartcard credentials, carrying identity certificates plus a photo badge.
- Depends on a working **PKI** for issuance, validation, and revocation — see [[Public Key Infrastructure]].
- Physical badge and proximity-card mechanics are in [[Physical Access Controls]].

## One-Time Passwords

| Type | Mechanism | Note |
|---|---|---|
| **HOTP** | HMAC over a **counter** shared with the server | Stays valid until used; counter can drift out of sync |
| **TOTP** | HMAC over the **current time window** (typically 30 s) | Expires on its own; requires clock synchronization |

Both are **synchronous** — derived from shared state. **Asynchronous** tokens instead answer a server **challenge** with a computed response.

## Authenticator Forms

- **Hardware tokens** — standalone key fobs and display cards; no general-purpose OS to compromise, but cost money and get lost.
- **Software authenticators** — an app on a phone; free and convenient, but exposed to a compromised or malware-infected device.
- **Push authenticators** — the server sends an approval prompt. Convenient, and vulnerable to **MFA fatigue**: an attacker with the password spams prompts until the user taps accept. **Number matching** and request context are the countermeasures.
- **SMS and email OTPs** — "something you have" only loosely; broken by SIM swapping, SS7 interception, and mailbox compromise. NIST treats SMS as a restricted authenticator.
- **FIDO2 / WebAuthn security keys** — public-key authentication bound to the site's origin, so a phished site cannot use the response. The **phishing-resistant** class, and the basis of passkeys — see [[Multifactor and Passwordless Authentication]].

## Key Points

- **A smartcard's private key never leaves the chip; PIV and CAC are the government forms.**
- **HOTP is counter-based and stays valid until used; TOTP is time-based and expires.**
- **Push MFA is defeated by prompt fatigue; number matching counters it.**
- **SMS OTP is the weakest possession factor; FIDO2/WebAuthn is the phishing-resistant one.**
