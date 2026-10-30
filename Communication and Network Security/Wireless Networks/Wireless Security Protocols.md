## The Progression

Each wireless security protocol exists because the previous one was broken. The sequence, and what each fixed, is the core knowledge.

| Protocol | Year | Encryption | Authentication | Status |
|---|---|---|---|---|
| **WEP** | 1997 | RC4 with a 24-bit IV, 40- or 104-bit key | Open or shared key | **Broken**; crackable in minutes |
| **WPA** | 2003 | **TKIP** (RC4 with per-packet key mixing, longer IV, message integrity check) | PSK or 802.1X | Deprecated; TKIP is attackable |
| **WPA2** (802.11i) | 2004 | **CCMP** (AES in counter mode with CBC-MAC) | PSK or 802.1X | Acceptable with a strong passphrase or enterprise mode; vulnerable to **KRACK** (patched) and offline PSK cracking |
| **WPA3** | 2018 | AES-CCMP (personal) or AES-GCMP-256 (enterprise 192-bit mode) | **SAE** (personal) or 802.1X | Current standard |

## WEP

**Wired Equivalent Privacy** was the original 802.11 security. It used **RC4** with a static shared key and a **24-bit initialization vector** sent in cleartext. The IV is too short (repeats after a few thousand frames on a busy network), the key never changes, the integrity check (CRC-32) is linear and does not detect tampering, and the shared key authentication actually leaks keystream. Tools recover the key from captured traffic in minutes. WEP should never be used; its only lasting lesson is why IVs must be long and never reused (see [[Wireless Attacks]] on IV abuse).

## WPA

**Wi-Fi Protected Access** was an interim fix that could run on WEP-era hardware. **TKIP** kept RC4 but added per-packet key mixing, a 48-bit IV, and a message integrity check (Michael). It bought time, but TKIP has known attacks and is now deprecated; any network still offering TKIP is effectively WPA-era.

## WPA2

**WPA2** implements the full **IEEE 802.11i** standard with **CCMP**, which uses **AES** for confidentiality and CBC-MAC for integrity. It comes in two modes:

- **Personal (WPA2-PSK)**: everyone shares one **pre-shared key** (passphrase). The passphrase derives the keys through a four-way handshake that can be captured and attacked **offline** by dictionary or brute force; a weak passphrase is crackable, a long random one is not. Anyone with the PSK can decrypt other users' traffic captured from the handshake on, and a departing employee means changing the key everywhere.
- **Enterprise (WPA2-EAP)**: each user authenticates individually through **802.1X** to a RADIUS server, and each session gets unique keys. This is the correct mode for organizations.

The **KRACK** attack (2017) exploited the four-way handshake to force nonce reuse; it was fixed in client and AP software, not in the protocol design.

## WPA3

**WPA3** replaces PSK with **Simultaneous Authentication of Equals (SAE)**, a password-authenticated key exchange based on Dragonfly. Benefits:

- **Resists offline dictionary attacks**: an attacker gets one guess per interaction with the network, not an offline capture to crack at leisure.
- **Forward secrecy**: capturing the passphrase later does not decrypt earlier sessions.
- **Enterprise 192-bit mode** with stronger cipher suites for government and high-security use.
- **Protected Management Frames** are mandatory, which blocks the deauthentication attacks that work against WPA2.
- **Enhanced Open (OWE)** for networks without a password: opportunistic encryption so that open hotspots are not sniffable.
- **Easy Connect (DPP)** replaces WPS for onboarding IoT devices using QR codes.

Early implementations had side-channel weaknesses (Dragonblood), and "transition mode" running WPA2 and WPA3 together inherits WPA2's weaknesses. Still, WPA3 is the target state.

## 802.1X and EAP

**IEEE 802.1X** is **port-based network access control**, used on both wired switch ports and wireless associations. Three roles:

1. **Supplicant**: the client device requesting access.
2. **Authenticator**: the switch or access point; it blocks all traffic except authentication until the client is approved.
3. **Authentication server**: usually **RADIUS** (or TACACS+, Diameter), which checks credentials against a directory and tells the authenticator to open the port, often also assigning a VLAN.

802.1X carries **EAP** (Extensible Authentication Protocol), which is a framework, not an authentication method; the method inside decides the security:

| EAP method | Mechanism | Assessment |
|---|---|---|
| **EAP-TLS** | Mutual certificate authentication; a client certificate on every device | Strongest; requires a PKI |
| **EAP-TTLS** | Server certificate creates a TLS tunnel, client authenticates inside with any method (password) | Strong; no client certificates needed |
| **PEAP** (Protected EAP) | Like TTLS: server certificate, TLS tunnel, usually **MS-CHAPv2** inside | Common in Windows environments; safe if the client validates the server certificate |
| **EAP-FAST** | Cisco; tunnel based on a shared "protected access credential" instead of a certificate | Convenient; initial provisioning is the weak point |
| **LEAP** | Cisco's early method using MS-CHAP without a tunnel | **Broken** (offline dictionary attack); do not use |
| **EAP-MD5** | Plain challenge-response hash | No mutual authentication, no key derivation; unsuitable for wireless |
| **EAP-SIM / EAP-AKA** | Authenticate with a cellular SIM | Carrier Wi-Fi offload |

The common failure is clients **not validating the RADIUS server's certificate**, which lets an evil twin with its own RADIUS harvest credentials (see [[Wireless Attacks]]).

## Key Points

- **WEP (RC4, 24-bit IV) is broken; WPA (TKIP) was a patch; WPA2 (AES-CCMP) is the minimum; WPA3 (SAE) is current.**
- **PSK means one shared secret, offline-crackable from a captured handshake; enterprise means per-user 802.1X authentication and per-session keys.**
- **WPA3's SAE resists offline dictionary attacks and gives forward secrecy; protected management frames stop deauthentication attacks.**
- **802.1X = supplicant, authenticator, authentication server (RADIUS); EAP is the framework, the method decides the strength.**
- **EAP-TLS is strongest (certificates both ways); PEAP and EAP-TTLS tunnel passwords inside server-authenticated TLS; LEAP and EAP-MD5 are unacceptable.**
