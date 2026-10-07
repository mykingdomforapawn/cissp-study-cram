Both solve the same problem — confidentiality, integrity, authentication, and non-repudiation for email — using the same hybrid cryptosystem pattern (see Hybrid Cryptosystems in Asymmetric Key Algorithms), but differ in how trust is established.

## PGP (Pretty Good Privacy)

Uses a **web of trust** instead of a centralized Certificate Authority: users sign each other's public keys directly, and trust is established through a decentralized network of these peer endorsements rather than a hierarchical chain of trust (contrast with Certificate Authorities in Public Key Infrastructure). No central authority is required, which made PGP popular for individual and grassroots use, but it also means trust doesn't scale as cleanly in large organizations the way a CA hierarchy does.

## S/MIME (Secure/Multipurpose Internet Mail Extensions)

Uses traditional **PKI** — certificates issued by a trusted CA, following the same chain-of-trust model described in Public Key Infrastructure. This is the model most enterprises use, since it integrates directly with existing corporate PKI and certificate management rather than requiring a separate web of trust.

## Comparison

| | Trust model | Typical use |
|---|---|---|
| PGP | Web of trust (peer-signed keys) | Individual/grassroots use |
| S/MIME | PKI (CA-issued certificates) | Enterprise, integrates with existing PKI |
