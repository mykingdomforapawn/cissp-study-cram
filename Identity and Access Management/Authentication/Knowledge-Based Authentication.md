Type 1 authentication: the subject proves identity by producing a secret. Cheap, universal, and the weakest factor — it can be guessed, phished, reused across sites, and stolen in bulk from the verifier.

## Forms

- **Password** — an arbitrary string. **Passphrase** — a long sequence of words, easier to remember at much greater length.
- **PIN** — short numeric, only safe when paired with a possession factor and a lockout.
- **Cognitive password / security questions** — answers about the user's life. Treated as a **weak recovery mechanism, not a factor**: answers are guessable, public, or in breach data.

## Password Policy Components

| Component | Purpose |
|---|---|
| **Minimum length** | The dominant defense against guessing and cracking |
| **Complexity** | Required character classes; raises the keyspace but pushes users into predictable patterns |
| **History** | Blocks reuse of the last *n* passwords |
| **Minimum age** | Stops cycling through history to return to a favorite password |
| **Maximum age (expiration)** | Bounds the window a stolen password stays valid |
| **Lockout threshold / duration** | Stops online guessing; too aggressive invites denial of service |
| **Breach-list screening** | Rejects passwords already known to attackers |

## Current Guidance

**NIST SP 800-63B** reversed much of the traditional advice, and the shift is worth knowing:

| Traditional | Current |
|---|---|
| Complexity rules enforced | **No** composition rules |
| Expire every 60–90 days | **No routine expiration** — change only on evidence of compromise |
| 8 characters | **At least 8, support 64+**; favor passphrases |
| Hints and security questions | **Prohibited** |
| — | **Screen against breached-password lists** |
| — | Allow paste and password managers |

The reasoning: forced rotation and complexity produce `Summer2024!` → `Summer2025!`, trading real entropy for predictability, while breach screening removes the passwords actually being tried.

## Protecting Stored Passwords

Verifiers store a **salted hash** produced by a deliberately slow function (bcrypt, scrypt, Argon2, PBKDF2), never the password or a plain hash. The salt defeats rainbow tables; the work factor defeats bulk cracking. See [[Hashing Algorithms]] and [[Cryptographic Attacks]], and [[Access Control Attacks]] for the attacks each policy component is aimed at.

## Key Points

- **Length beats complexity; passphrases beat composition rules.**
- **NIST SP 800-63B drops forced expiration, composition rules and hints, and adds breach-list screening.**
- **Security questions are a recovery mechanism, not an authentication factor.**
- **Store passwords salted and hashed with a slow KDF, never encrypted or plainly hashed.**
