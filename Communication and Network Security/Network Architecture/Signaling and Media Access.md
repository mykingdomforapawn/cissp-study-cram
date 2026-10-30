## Signaling Sub-technologies

Several independent choices describe how bits are put on a medium. They are orthogonal: a link can be digital, synchronous, baseband, and use CSMA/CD all at once.

### Analog vs Digital

- **Analog** signals are continuous waves; information is carried by varying amplitude, frequency, or phase. They degrade gradually with noise and distance, and noise cannot be separated from signal.
- **Digital** signals are discrete states (on/off, voltage levels, light pulses). They are more reliable over distance because a repeater can regenerate a clean copy, they are easier to encrypt and compress, and they resist noise until a threshold is crossed.

A **modem** (modulator/demodulator) converts between the two. Nearly all modern networking is digital; analog survives in the last mile of some phone and radio systems.

### Synchronous vs Asynchronous

- **Synchronous** communication uses a **shared clock** (embedded in the signal or on a separate line); data is sent as a continuous stream of frames, which supports high throughput. Used by most high-speed links (Ethernet, SONET, T-carriers).
- **Asynchronous** communication has no shared clock; each character or small unit is framed with **start and stop bits** so the receiver can synchronize per unit. Simpler and tolerant of irregular timing, but lower efficiency. Classic serial ports and modems work this way.

### Baseband vs Broadband

- **Baseband** uses the **whole bandwidth** of the medium for **one channel**; only one signal at a time, usually digital. **Ethernet is baseband** (the "Base" in 10BaseT, 1000BaseT).
- **Broadband** divides the medium into **multiple channels** by frequency (frequency-division multiplexing), so several signals share it, often analog modulated. Cable TV, cable internet, DSL, and cellular are broadband. (In marketing, "broadband" just means fast internet; the technical meaning is multi-channel.)

### Casting: Unicast, Multicast, Broadcast, Anycast

| Casting | Delivery | Example |
|---|---|---|
| **Unicast** | One sender to **one** receiver | Almost all client-server traffic |
| **Multicast** | One sender to a **group** of receivers that have joined (IGMP, class D addresses) | IPTV, stock feeds, routing protocol updates (OSPF uses 224.0.0.5) |
| **Broadcast** | One sender to **every** device in the broadcast domain | ARP requests, DHCP discover; IPv6 has no broadcast |
| **Anycast** | One sender to the **nearest** of several receivers sharing an address | DNS root servers, CDNs; also a DDoS mitigation technique since load spreads geographically |

Broadcast and multicast traffic cannot be confined by a switch (except by VLANs), which is why broadcast domains should be kept small and why broadcast storms are a denial of service risk.

## LAN Media Access Technologies

When several devices share a medium, something must decide who may transmit. The technologies differ in whether they **avoid**, **detect**, or **schedule around** collisions.

| Technology | How it works | Used by |
|---|---|---|
| **CSMA** (carrier-sense multiple access) | Listen before transmitting; if the medium is quiet, send. No collision handling by itself | Basis of the two below |
| **CSMA/CD** (collision detection) | Listen, transmit, **detect** a collision while sending, stop, send a jam signal, wait a random back-off, retry | **Ethernet** on shared media (hubs, coax). Irrelevant on full-duplex switched links, where collisions cannot occur |
| **CSMA/CA** (collision avoidance) | Listen, then **announce intent** to transmit and wait for clearance (RTS/CTS), or wait a random interval, because the sender cannot hear a collision while transmitting | **Wi-Fi (802.11)**, AppleTalk. Wireless radios cannot transmit and listen at once, so detection is impossible |
| **Token passing** | A **token** frame circulates; only the holder may transmit, then passes the token on. No collisions, deterministic | Token Ring, FDDI; obsolete for LANs, still in some industrial networks |
| **Polling** | A **primary** device asks each secondary in turn whether it has data to send; secondaries only speak when polled | Mainframe SDLC terminals, some industrial and sensor networks. Priority can be given by polling some devices more often |

Contention-based methods (CSMA) are simple and efficient at low load but degrade under heavy load as collisions increase; deterministic methods (token, polling) guarantee access and bounded delay but add overhead and a single point of failure (lost token, failed primary).

The security relevance is mostly availability: contention-based media can be saturated by a single misbehaving or malicious device, and on wireless the CSMA/CA mechanism itself can be abused (a device claiming the medium continuously is a form of jamming).

## Key Points

- **Digital signals can be regenerated and are easier to secure; analog degrades gradually.**
- **Synchronous = shared clock, continuous stream, high speed; asynchronous = start/stop bits per unit.**
- **Baseband = one channel on the whole medium (Ethernet); broadband = many channels by frequency (cable, DSL).**
- **Unicast one-to-one, multicast one-to-group, broadcast one-to-all, anycast one-to-nearest.**
- **CSMA/CD detects collisions (wired Ethernet); CSMA/CA avoids them because radios cannot detect (Wi-Fi); token passing and polling are collision-free and deterministic.**
