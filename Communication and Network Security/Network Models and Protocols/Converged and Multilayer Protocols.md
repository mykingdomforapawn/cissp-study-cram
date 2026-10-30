## Multilayer Protocols

TCP/IP is a **multilayer protocol** suite: a web request is HTTP inside TCP inside IP inside Ethernet. The same mechanism that lets any application ride over any medium has security implications:

- **Encapsulation can hide traffic.** A protocol can be wrapped in another to pass a filter: HTTP tunneled in DNS, SSH in HTTPS, or an entire IP packet inside an encrypted VPN. **Covert channels** and firewall bypass exploit this; so does legitimate VPN use.
- **Filters are layer-specific.** A control that inspects only one layer misses what is encapsulated above it. Defense in depth across layers, and deep packet inspection, respond to this.
- **Logical segmentation is only as strong as the lowest layer.** VLAN hopping (double tagging) abuses the tag encapsulation of 802.1Q to cross a layer 2 segment boundary.
- **Legacy protocols inherit the problem.** Wrapping an unauthenticated industrial protocol in TCP/IP exposes it to every IP attack.

## Converged Protocols

**Converged protocols** merge specialty or proprietary protocols with standard TCP/IP so that **one network** carries storage, voice, and data instead of separate dedicated infrastructures. The benefit is cost and simplicity; the cost is that a failure or compromise of the shared network now affects everything, and that traffic which previously ran on an isolated physical network is now reachable from the data LAN.

| Protocol | What converges | Notes |
|---|---|---|
| **Fibre Channel over Ethernet (FCoE)** | Storage area network traffic over 10 Gbps+ Ethernet | Replaces dedicated Fibre Channel switching; operates at layer 2, not routable |
| **iSCSI** | SCSI storage commands over IP | Routable, cheaper SAN; needs isolation (dedicated VLAN) and CHAP authentication, as it is cleartext by default |
| **MPLS** (Multiprotocol Label Switching) | Carrier WAN transport for any protocol | Forwards on short **labels** rather than IP lookups, between layer 2 and 3 ("layer 2.5"); supports traffic engineering and QoS; private but **not encrypted** |
| **VoIP** | Voice over the data network | See below |
| **SDN** | Network control over the data network | See below |
| **InfiniBand over Ethernet, SMB/NFS over IP, video** | Other examples | Same pattern |

Storage protocols deserve emphasis: a SAN that was once physically separate becomes a target on the data network, and most of these protocols have weak or no authentication. Segmentation, dedicated interfaces, and encryption where supported are the controls.

## VoIP

**Voice over IP** carries calls as packets: **SIP** (Session Initiation Protocol) sets up and tears down the call, **RTP** carries the audio. Protocols are standard, so the attacks are standard too:

- **Eavesdropping** on unencrypted RTP; mitigated with **SRTP** and SIP over TLS.
- **Caller ID spoofing** and **vishing** (voice phishing), since SIP headers are trivially forged.
- **Toll fraud**: compromising a PBX to place premium-rate calls.
- **Denial of service**: flooding SIP registrations or the network; voice is sensitive to latency and jitter, so even partial DoS degrades it.
- **SPIT** (spam over internet telephony), and **hopping** between the voice VLAN and the data VLAN if the segmentation is weak.

Controls: separate voice VLAN, SRTP/TLS, authentication of endpoints, a session border controller at the edge, and QoS. Note the availability dependency: when the network is down, so are the phones, which affects emergency calling.

## Software-Defined Networking

**SDN** separates the **control plane** (deciding where traffic goes) from the **data plane** (forwarding it) and centralizes control in software, typically speaking **OpenFlow** to the switches. The concepts, benefits, and the risk of the controller as a single high-value target are covered in [[Virtual Networking and Software-Defined Everything]].

From a network security view the additional points are:

- SDN makes **microsegmentation** and rapid policy changes practical, which strengthens zero trust designs.
- The **northbound API** (applications to controller) and **southbound API** (controller to devices) are new attack surfaces that need authentication and encryption.
- **SD-WAN** applies the same idea to WAN links, choosing paths per application across MPLS, broadband, and cellular, usually with built-in encryption.
- **Virtual SAN (VSAN)** is the storage analogue: a logical SAN carved out of shared fabric, isolating storage traffic logically rather than physically.

## Key Points

- **Encapsulation hides traffic from single-layer controls**, enabling tunneling, covert channels, and VLAN hopping.
- **Converged protocols put storage, voice, and data on one network**: cheaper, but formerly isolated traffic becomes reachable and a shared failure point.
- **FCoE is layer 2 storage; iSCSI is routable storage; MPLS forwards on labels and is private, not encrypted.**
- **VoIP uses SIP for signaling and RTP for media; SRTP and SIP over TLS encrypt it; vishing and toll fraud are the characteristic attacks.**
- **SDN centralizes the control plane; its controller and APIs become the crown jewels.**
