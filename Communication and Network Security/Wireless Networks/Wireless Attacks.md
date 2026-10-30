## Why Wireless Is Attacked Differently

Everything on the air can be received by anyone in range, management frames were unauthenticated until WPA3, and clients automatically reconnect to known networks. Most wireless attacks exploit one of these three facts.

## Reconnaissance

- **War driving** (walking, flying, chalking): moving around with a wireless scanner to find and map networks, recording SSID, BSSID, channel, security mode, and GPS position. **War chalking** marked the findings with symbols. Free tools and smartphone apps make it trivial; the defense is to assume every network is already mapped and to secure it accordingly.
- **Sniffing**: passive capture with a wireless adapter in **monitor mode**. On open networks and WEP everything is readable; on WPA2-PSK anyone with the key and the handshake can decrypt; on WPA3 and enterprise modes only metadata (MACs, SSIDs, timing) is visible.

## Rogue Access Points

A **rogue access point** is any AP connected to the organization's network **without authorization**. Two origins:

- An **employee** plugging in a consumer AP for convenience, often with no security, which punches a wireless hole straight into the wired LAN past every firewall.
- An **attacker** planting a small device (or a compromised printer or laptop acting as an AP) to gain persistent wireless access from outside the building.

Defenses: **802.1X on wired switch ports** so an unauthorized device cannot join the LAN, **NAC**, disabling unused ports, a **wireless IDS/IPS** that detects APs not in the authorized list, and periodic **site surveys** to physically locate them.

## Evil Twin

An **evil twin** is an attacker's AP that **imitates a legitimate network** (same SSID, often a stronger signal) so that clients connect to it instead. Clients that remember a network reconnect automatically, and a deauthentication burst pushes them off the real AP. Once connected the attacker is on-path: sniffing, injecting, serving a fake captive portal to harvest credentials, or presenting a fake RADIUS server to capture enterprise credentials from clients that do not validate the server certificate.

Related: a **rogue hotspot** in a public place with a plausible name ("Airport Free WiFi"), and **Karma / known-beacon** attacks where the device answers every probe request with "yes, I am that network".

Defenses: **mutual authentication** (EAP-TLS, or PEAP with strict server certificate validation), WPA3 so that passphrase knowledge is required, **protected management frames**, wireless IDS detecting duplicate SSIDs, user awareness, and VPN/TLS so that an on-path position yields nothing.

## Disassociation and Deauthentication

802.11 **management frames** tell a client to disconnect: **deauthentication** (ends authentication) and **disassociation** (ends association). Before WPA3 these frames were **unauthenticated**, so anyone can forge them with the victim's or AP's MAC. Uses:

- **Denial of service**: continuous deauth keeps clients off the network.
- **Forcing a reconnection** to capture the WPA2 four-way handshake for offline cracking, or to push the client onto an evil twin.
- **Hotel and venue abuse**: deauthing personal hotspots so guests must pay for the venue's Wi-Fi (the FCC has fined this).

Defense: **802.11w Protected Management Frames**, optional in WPA2 and **mandatory in WPA3**, which authenticates management frames so forged ones are ignored.

## Jamming

**Jamming** is a denial of service by **transmitting noise or continuous traffic** on the channel. Deliberate jammers are illegal in most jurisdictions but cheap. Unintentional jamming comes from **interference**: microwaves, cordless phones, Bluetooth, and neighboring networks on overlapping channels. Defense is limited: locate the source (spectrum analyzer), move channels or bands, use directional antennas, increase power, and keep a wired fallback for anything critical. Wireless cannot be made jam-proof, which is why availability-critical systems should not depend on it alone.

## Initialization Vector Abuse

An **initialization vector (IV)** is a nonce combined with the key so that encrypting the same data twice produces different ciphertext. It must be long enough and never repeat. **WEP's 24-bit IV** repeats on a busy network within hours, and because RC4 is a stream cipher, two frames with the same IV and key use the **same keystream**; XORing the ciphertexts cancels the keystream and exposes the plaintexts. Related IVs also leak key bytes (the FMS attack). Tools recover a WEP key from a few tens of thousands of captured frames, and attackers can **inject traffic** to generate those frames faster. WPA's 48-bit IV and WPA2's per-session keys remove the problem; the general lesson is in [[Block Ciphers and Modes of Operation]].

## Replay

A **replay attack** records legitimate frames and retransmits them later to repeat their effect: re-sending an authentication exchange, an authorization frame, or a transaction. WEP had no replay protection; WPA/WPA2 add **sequence counters** (the TKIP sequence counter, the CCMP packet number) so that out-of-order or repeated frames are discarded, and the four-way handshake uses nonces. At higher layers, replaying captured application traffic is prevented by TLS and by session tokens with timestamps or nonces. KRACK was in effect a replay of handshake message 3 that forced nonce reuse.

## Other Attacks Worth Knowing

- **Brute-forcing WPA2-PSK** offline from a captured handshake, and **WPS PIN** brute force (see [[Wireless Fundamentals]]).
- **MAC spoofing** to bypass MAC filtering or to impersonate a client on a captive portal network.
- **Bluetooth and NFC** attacks are in [[Bluetooth, RFID, and NFC]].

## Key Points

- **War driving maps networks; assume yours is already mapped.**
- **Rogue AP = unauthorized AP on your wired network (insider or attacker); evil twin = attacker's AP imitating yours to capture clients.** Wired 802.1X and NAC stop the first; mutual authentication and PMF stop the second.
- **Deauthentication and disassociation frames were unauthenticated before 802.11w / WPA3**, enabling DoS, handshake capture, and forcing clients onto evil twins.
- **Jamming is radio-level DoS and cannot be fully prevented; keep a wired fallback.**
- **IV abuse broke WEP: a short, repeating IV with a stream cipher reuses keystream. Replay is stopped by sequence counters and nonces.**
