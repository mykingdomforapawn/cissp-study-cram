**Single sign-on (SSO)** lets a subject authenticate **once** and reach every system in the domain without authenticating again. Each system still **authorizes** separately — SSO centralizes authentication, not permissions.

| | Benefit | Cost |
|---|---|---|
| Users | One strong credential instead of many weak reused ones | — |
| Admins | One place to disable an account; consistent policy; fewer resets | — |
| Risk | — | **Single point of compromise** — one stolen credential opens everything, and an outage of the SSO service blocks all access |

This is why SSO is deployed **with MFA and session controls**, not on a password alone.

## Centralized vs. Decentralized Access Control

| | **Centralized** | **Decentralized** |
|---|---|---|
| Decisions made | By one authority (directory, IdP, AAA server) | By each system or local administrator |
| Strengths | Consistent policy, one audit trail, immediate revocation | No single point of failure, local autonomy |
| Weaknesses | Single point of failure and compromise | Inconsistent policy, orphaned accounts, no unified view |

Centralized is the norm; decentralized survives where systems cannot reach the authority or are administered by separate organizations.

## Directory Services and LDAP

A **directory service** is the central database of identities, groups, and resources. **LDAP** (Lightweight Directory Access Protocol, TCP 389, or **LDAPS** on 636 / StartTLS) is the protocol used to query and modify it. **Active Directory** is the common implementation, with **Kerberos** as its authentication protocol — see [[Secure Communication Protocols]]; Kerberos mechanics and attacks belong with the access-control chapter.

The directory is hierarchical: entries have **distinguished names** (`cn=jsmith,ou=finance,dc=example,dc=com`) mirroring the organization. That hierarchy is what makes group- and OU-based authorization administrable — the abstraction described in [[AAA Framework]].

Because the directory is the single source of identity truth, it is a **primary attack target**: compromising it grants everything. Harden it with encrypted transport (never plain LDAP for credentials), restricted anonymous binds, tiered administration, and close monitoring.

## LDAP and PKI

The directory and the PKI reinforce each other:

- The directory **publishes certificates** and CRLs, so clients can retrieve a user's public key or check revocation by directory lookup.
- The PKI **authenticates directory access** — LDAPS uses a server certificate, and clients may present certificates instead of passwords.

Both are centralized trust stores, and their compromise is equally total. See [[Public Key Infrastructure]].

## Key Points

- **SSO centralizes authentication only; authorization stays with each system.**
- **SSO's trade-off is convenience against a single point of compromise — pair it with MFA.**
- **LDAP (389) / LDAPS (636) queries the directory; Active Directory combines the directory with Kerberos.**
- **The directory publishes certificates and CRLs; the PKI secures and authenticates directory access.**
