**Kerberos** is the SSO authentication protocol used inside a network — the authentication half of Active Directory, and the reference example of **ticket-based** authentication over an untrusted network. It is built entirely on **symmetric cryptography** and a trusted third party; no public keys are required in the basic exchange.

The problem it solves: let a user prove identity once and reach many services, **without the password ever crossing the network** and without each service holding a copy of it.

## Components

| Term | Meaning |
|---|---|
| **KDC** (Key Distribution Center) | The trusted third party holding a secret key for every principal |
| **AS** (Authentication Service) | The KDC component that authenticates the user and issues the TGT |
| **TGS** (Ticket Granting Service) | The KDC component that exchanges a TGT for service tickets |
| **Principal** | Any entity with an identity in the realm — user, host, or service |
| **Realm** | The administrative domain the KDC is authoritative for |
| **TGT** (Ticket Granting Ticket) | Proof that the user authenticated; presented to get service tickets |
| **Service ticket** | Proof of authorization to use one specific service |

## How the Exchange Works

1. **Authentication.** The client sends its identity to the **AS**. The AS replies with a **TGT** and a session key, encrypted with a key derived from the user's password. Only a client that knows the password can decrypt it — **the password itself is never sent**.
2. **Ticket request.** To reach a file server, the client presents the TGT to the **TGS** and names the service.
3. **Ticket issue.** The TGS returns a **service ticket** encrypted with the **service's** own key, plus a session key for client and service.
4. **Service access.** The client presents the ticket to the service. The service decrypts it with its own key — it never contacts the KDC — and the session proceeds under the shared session key.

Two consequences worth holding on to:

- The target service **never sees the user's password** and does not have to query the KDC; it trusts a ticket it can decrypt.
- Tickets are **time-stamped and short-lived** (typically 10 hours for a TGT), which is the replay defense. This is why **Kerberos requires synchronized clocks** — a skew beyond the tolerance (5 minutes by default) makes authentication fail outright. Clock skew is the classic Kerberos troubleshooting answer.

## Strengths and Weaknesses

- **Strengths**: no password on the wire, mutual authentication, replay protection through timestamps, and a single place to revoke an identity.
- **The KDC is a single point of failure** — it is unavailable and nobody authenticates; it is compromised and every identity in the realm is forgeable. Deploy it redundantly and treat it as the most protected asset in the domain (compare the directory itself in [[Single Sign-On and Directory Services]]).
- Depends on **time synchronization** and on the strength of the key derived from the user's password — a weak password remains offline-crackable from captured material.

## Kerberos Attacks

| Attack | Mechanism | Defense |
|---|---|---|
| **Kerberoasting** | Any authenticated user may request a service ticket for a service account; the ticket is encrypted with that account's password key and can be cracked **offline** | Long random passwords for service accounts, managed service accounts, strong encryption types, alert on bulk ticket requests |
| **AS-REP roasting** | Accounts with Kerberos pre-authentication disabled hand out crackable material to anyone who asks | Require pre-authentication on every account |
| **Pass-the-ticket** | A stolen ticket is reused from another machine; it is valid until it expires, regardless of where it came from | Protect credential memory, short ticket lifetimes, privileged access workstations |
| **Golden ticket** | With the **KDC's own key** (the `krbtgt` account hash), an attacker forges TGTs for any user, including fabricated administrators | Treat as full domain compromise; rotate the krbtgt key twice, rebuild trust |
| **Silver ticket** | With **one service account's** key, an attacker forges tickets for that service alone — quieter, since the KDC is never contacted | Service account key rotation, monitor service-side logons without matching KDC events |

Golden and silver tickets are the reason domain controller compromise is treated as unrecoverable by patching alone. The credential-theft tooling that harvests the underlying hashes is covered in [[Access Control Attacks]].

## Key Points

- **Kerberos uses symmetric cryptography and a trusted KDC; the password never crosses the network.**
- **The AS issues a TGT, the TGS exchanges it for a service ticket, and the service validates the ticket with its own key.**
- **Tickets are time-stamped and short-lived, so Kerberos depends on synchronized clocks — skew breaks authentication.**
- **The KDC is a single point of failure and the highest-value target in the realm.**
- **Kerberoasting cracks service tickets offline; a golden ticket forges any identity from the KDC key, a silver ticket forges access to one service.**
