## What These Protocols Do

**Authentication protocols** prove who is at the other end of a link before traffic is allowed to flow. They sit below the application: the user has not yet reached a login page, the question is whether this *connection* or this *switch port* may exist at all. Three things distinguish them:

- **Are credentials sent in the clear?**
- **Is authentication one-time at setup, or repeated during the session?**
- **Is it mutual**, or does only the client prove itself?

The progression from PAP to CHAP to EAP is the answer to those questions getting better over time.

## PPP and Its Authentication Options

**Point-to-Point Protocol (PPP)** is the layer 2 framing used on point-to-point links (dial-up, DSL via PPPoE, serial WAN links, and inside L2TP tunnels). It replaced **SLIP**, which had no error checking, no authentication, and no support for multiple network protocols. PPP itself carries no security; it **negotiates an authentication protocol** at link setup.

| Protocol | How it works | Weakness |
|---|---|---|
| **PAP** (Password Authentication Protocol) | Client sends username and password in **cleartext**, server compares | Anyone on the path reads the password; no replay protection. Obsolete |
| **CHAP** (Challenge Handshake Authentication Protocol) | Server sends a **random challenge**; client returns a hash of the challenge plus the shared secret; server computes the same hash and compares. Repeated **periodically during the session** | Password never crosses the wire, and re-challenging defeats session hijacking — but the server must store the secret in a recoverable form |
| **MS-CHAP / MS-CHAPv2** | Microsoft's CHAP variants; v2 adds **mutual authentication** (the server also proves itself) | Cryptographically broken (DES-based); must be wrapped in TLS, as PEAP does |
| **EAP** (Extensible Authentication Protocol) | Not an authentication method but a **framework** that carries whichever method both sides agree on | Only as strong as the method chosen inside it |

**Remember the order**: PAP sends the password, CHAP sends a hash of a challenge, EAP lets you choose.

## EAP Methods

**EAP** is a container. The security depends entirely on which method is negotiated, which is why the method names matter.

| Method | Credential | Notes |
|---|---|---|
| **EAP-TLS** | **Certificates on both sides** | Strongest and mutual; requires a PKI and a certificate on every client, which is the deployment cost |
| **EAP-TTLS** | Server certificate, then any legacy method inside the TLS tunnel | Tunneled; clients need no certificate |
| **PEAP** (Protected EAP) | Server certificate builds a TLS tunnel, **MS-CHAPv2 runs inside it** | The common enterprise Wi-Fi choice; safe only if clients **validate the server certificate** — otherwise an evil twin harvests credentials |
| **LEAP** | Cisco-proprietary, MS-CHAP-based | Broken (asleap); replaced by EAP-FAST |
| **EAP-FAST** | Shared secret (a **PAC**) instead of a certificate | Cisco's LEAP replacement; weak if the PAC is provisioned anonymously |
| **EAP-MD5** | Password hash, no server authentication, no key material | One-way only, no mutual authentication; unusable for wireless |
| **EAP-SIM / EAP-AKA** | The credential on a cellular **SIM** card | Carrier Wi-Fi offload; the phone authenticates to Wi-Fi with its mobile identity |

The pattern: **tunnel first, authenticate inside**. Any EAP method that exposes the inner exchange to the network is attackable offline.

## 802.1X: Where EAP Is Carried

**IEEE 802.1X** is **port-based network access control**, on wired switch ports and wireless associations alike. Three roles:

- **Supplicant** — the client requesting access.
- **Authenticator** — the switch or access point; it keeps the port in an **unauthorized state** where only EAP traffic passes.
- **Authentication server** — usually RADIUS, which holds the credentials and makes the decision.

EAP is carried over the LAN as **EAPOL** between supplicant and authenticator, and inside RADIUS between authenticator and server. On success the port opens, often with a **VLAN or ACL assignment** pushed back with the accept message — the hook that [[Network Access Control and Endpoint Security]] uses to quarantine unhealthy devices. See [[Wireless Security Protocols]] for WPA2/WPA3-Enterprise, which is 802.1X applied to Wi-Fi.

Limitation: 802.1X authenticates the **port at association time**. A hub or an already-authenticated device behind the authenticated port can piggyback, which is why MACsec or periodic reauthentication is used where this matters.

## Centralized Authentication Services

The authenticator does not hold credentials itself; it asks a central service. This is the **AAA** pattern (see [[AAA Framework]]).

| Service | Transport | Characteristics |
|---|---|---|
| **RADIUS** | UDP (1812/1813, historically 1645/1646) | Encrypts **only the password**, rest of the packet in the clear; combines authentication and authorization; the standard for **network access** (VPN, Wi-Fi, 802.1X). **RADIUS over TLS (RadSec)** fixes the exposure |
| **TACACS+** | TCP 49 | Encrypts the **entire payload**; **separates** authentication, authorization, and accounting, so command-level authorization is possible. Cisco-originated; the standard for **device administration** |
| **Diameter** | TCP/SCTP, with TLS/IPsec | RADIUS successor: reliable transport, better capacity and failover; used in mobile (LTE/IMS) and telecom networks |

**RADIUS decides who may get on the network; TACACS+ decides who may type which command on the router.**

## Key Points

- **PAP sends the password in cleartext; CHAP sends a hash of a server challenge and re-challenges during the session; EAP is a framework, not a method.**
- **PPP carries these on point-to-point links and replaced SLIP, which had no authentication at all.**
- **EAP-TLS is mutual certificate authentication and the strongest; PEAP tunnels MS-CHAPv2 in TLS and depends on the client validating the server certificate; LEAP and EAP-MD5 are broken.**
- **802.1X = supplicant, authenticator, authentication server; the port stays unauthorized until EAP succeeds, then a VLAN or ACL can be assigned.**
- **RADIUS encrypts only the password and merges authentication with authorization; TACACS+ encrypts everything and separates all three; Diameter is the modern RADIUS successor.**
