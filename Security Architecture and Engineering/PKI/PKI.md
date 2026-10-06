## Certificates

A **digital certificate** binds an identity to a public key, signed by a trusted third party. This is the piece missing from Public and Private Keys up to now: a public key alone doesn't prove *whose* key it is — anyone could publish a key and claim to be anyone. A certificate solves that by having a trusted party vouch for the binding.

Conceptually, a certificate holds (the X.509 standard, named only — field-level detail isn't exam-relevant):

- The **subject**'s identity (person, server, organization).
- The subject's **public key**.
- The **issuer** — the certificate authority that vouched for this binding.
- A **validity period** (not-before / not-after dates).
- The issuer's own **digital signature** over all of the above — see Digital Signatures for the sign/verify mechanism this relies on.

## Certificate Authorities (CAs)

A **Certificate Authority** is the trusted third party that verifies an identity and signs the resulting certificate. Trust isn't flat — it's a **chain of trust**:

- A **root CA** sits at the top, self-signed, and is the ultimate trust anchor — relying parties are configured in advance to trust specific root CAs (e.g., bundled into an OS or browser).
- **Intermediate CAs** are themselves issued a certificate by the root (or another intermediate), and in turn sign end-entity certificates. This limits the root's exposure — it rarely has to sign anything directly, and can be kept offline.
- An end-entity certificate is trusted only if every link in the chain, up to a trusted root, verifies.

A **Registration Authority (RA)** is sometimes split out from the CA: the RA handles verifying the requester's identity, while the CA itself handles the actual signing — separating "who are you" from "here is your signed certificate."

## Certificate Lifecycle

### Enrollment

1. The subject generates a key pair (see Key Pair Generation in Public and Private Keys).
2. The subject submits a **Certificate Signing Request (CSR)** — their public key plus identity details — to the RA/CA.
3. The RA/CA verifies the claimed identity actually matches the requester.
4. The CA issues the certificate, signing it with its own private key.

### Verification

A relying party checking a certificate validates, in order:

- The **chain of trust** — each certificate's signature verifies against its issuer's public key, all the way up to a root the relying party already trusts.
- The **validity period** — the certificate hasn't expired or isn't used before its start date.
- That the certificate hasn't been **revoked** (below).

### Revocation

A certificate sometimes needs to be invalidated before its validity period ends — e.g., the private key was compromised, the subject (an employee, a server) is decommissioned, or the issuing CA itself was compromised. Two mechanisms:

- **CRL (Certificate Revocation List)** — a signed, periodically published list of revoked certificate serial numbers; a relying party downloads and checks it. Simple, but can lag reality between publications.
- **OCSP (Online Certificate Status Protocol)** — a relying party queries the CA (or a designated responder) in real time for one certificate's current status. More up-to-date than a CRL, at the cost of needing a live connection to the responder at verification time.

## Certificate Formats

Named-only distinctions in how a certificate (and sometimes its private key) is packaged and encoded:

- **PEM** — base64-encoded text, the most common format; readable as plain text (`-----BEGIN CERTIFICATE-----` style).
- **DER** — the same underlying data as PEM, but binary-encoded rather than base64 text.
- **PKCS#12 / PFX** — bundles a certificate *together with its private key* (and often the chain of trust) in one password-protected file; used for exporting/importing a full identity, not just a public certificate.
- **CER / CRT** — generic certificate file extensions; the file may be either PEM or DER encoded underneath, so the extension alone doesn't tell you which.
