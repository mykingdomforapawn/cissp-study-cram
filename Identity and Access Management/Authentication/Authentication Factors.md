An **authentication factor** is a category of evidence a subject offers to prove a claimed identity. Three types are recognized, and the type — not the count — is what matters.

| Type | Name | Examples | Fails when |
|---|---|---|---|
| **Type 1** | Something you **know** | Password, passphrase, PIN, security questions | Guessed, phished, reused, breached |
| **Type 2** | Something you **have** | Smartcard, OTP token, phone, security key | Lost, stolen, cloned |
| **Type 3** | Something you **are** | Fingerprint, iris, face, voice | Copied; cannot be reissued |

Strength roughly follows the order, but each type fails differently — which is the point of combining them. See [[Knowledge-Based Authentication]], [[Token and Certificate Authentication]], [[Biometric Authentication]].

## Attributes vs. Factors

**Attributes** add context but are not accepted as standalone proof:

- **Somewhere you are** — geolocation, IP range, the physical terminal used.
- **Something you do** — behavioral biometrics: typing rhythm, gait, signature dynamics. Sometimes classed as Type 3.
- **Someone you know** — vouching by a verified party, used in web-of-trust models.

Attributes are what **adaptive authentication** evaluates to decide whether to demand another factor.

## Combining Factors

Two credentials of the **same type are not multifactor** — a password plus a security question is still one factor, as is a smartcard plus a proximity badge. See [[Multifactor and Passwordless Authentication]].

Independence also matters in practice: a password and an OTP both delivered to the same unlocked phone share a single point of failure even though they are formally Type 1 and Type 2.

**Authenticator Assurance Levels (AAL)** grade the result: AAL1 single factor, AAL2 two factors, AAL3 two factors with a **hardware-based**, phishing-resistant authenticator.

## Key Points

- **Type 1 know, Type 2 have, Type 3 are — MFA requires factors from different types.**
- **Attributes (somewhere you are, something you do) qualify a decision; they do not replace a factor.**
- **AAL1/2/3 grade authenticator strength, independently of identity proofing (IAL).**
