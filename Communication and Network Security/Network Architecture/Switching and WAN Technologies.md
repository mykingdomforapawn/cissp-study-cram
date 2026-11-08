## Circuit Switching vs Packet Switching

The fundamental division in how a network moves traffic.

| | **Circuit switching** | **Packet switching** |
|---|---|---|
| **Path** | A **dedicated physical circuit** is reserved end to end for the whole conversation | Each packet is routed independently and may take a different path |
| **Capacity** | Reserved whether used or not; **constant, predictable** bandwidth and latency | Shared; bandwidth and latency vary with load |
| **Setup** | Connection established before data flows, torn down after | No setup; stateless forwarding |
| **Efficiency** | Wasteful for bursty data (idle circuit is still reserved) | Efficient; idle capacity goes to others |
| **Failure** | A broken link kills the call | Traffic reroutes around a failure |
| **Examples** | PSTN voice calls, ISDN, T-carrier/leased lines | The internet, X.25, Frame Relay, ATM, MPLS, Ethernet |

**Security consequence**: a circuit is a fixed, known path — easier to physically protect, and traffic analysis is trivial since the circuit itself reveals who is talking to whom. Packets take unpredictable paths through networks nobody controls, so **encryption, not routing, is what protects them** — the argument for end-to-end protection and for VPNs.

## Virtual Circuits

A **virtual circuit** is a logical connection built **on top of a packet-switched network** that behaves like a dedicated circuit: packets follow a defined path, arrive in order, and get agreed performance. It is the compromise between the two models.

| | Description |
|---|---|
| **PVC** (permanent virtual circuit) | Always on, configured by the provider. The analogue of a **leased line**: it is simply there |
| **SVC** (switched virtual circuit) | Built on demand, used, then torn down. The analogue of a **dial-up call** |

Virtual circuits give a **quality of service commitment** — Frame Relay's **CIR** (committed information rate) is the classic example, a guaranteed minimum bandwidth with bursting above it when capacity allows.

## WAN Technologies

A **WAN** connects sites across distances that the organization does not own cabling for, so it buys a carrier's service. The terminology:

- **Dedicated (leased) line**: a permanent, exclusive connection between two points, billed as a flat rate whether used or not. Predictable and private.
- **Non-dedicated line**: a connection established as needed (dial-up, ISDN, DSL, cable), shared with other customers.
- **CSU/DSU**: the device between the LAN router and the carrier's digital line — the "modem" for a leased line.
- **Last mile**: the link from the carrier to the premises, usually the bottleneck and the single point of failure.

| Technology | Nature | Notes |
|---|---|---|
| **T-carrier / E-carrier** | Dedicated digital | **T1** = 1.544 Mbps (24 channels), **T3** = 44.736 Mbps; **E1** = 2.048 Mbps in Europe. **Fractional T1** rents a subset of channels |
| **ISDN** | Circuit-switched digital over phone lines | **BRI** = 2 B channels (64 kbps each) + 1 D channel for signaling; **PRI** = up to 23 B + 1 D. Early out-of-band signaling example |
| **X.25** | Packet-switched, virtual circuits | The first public packet network; heavy error checking for noisy lines, hence slow. Obsolete |
| **Frame Relay** | Packet-switched, virtual circuits (PVC/SVC) | X.25's faster successor: assumes clean lines, so error correction is left to the endpoints. Shared provider cloud, **CIR** for guarantees. Obsolete but a classic comparison |
| **ATM** | Cell-switched, virtual circuits | Fixed **53-byte cells** make switching fast and latency predictable; strong QoS. Used in carrier backbones and early DSL |
| **MPLS** | Label switching | Forwards on a short **label** rather than a routing lookup, creating engineered paths with QoS classes. The modern provider WAN; **private, but not encrypted** — the carrier can see the traffic |
| **SONET/SDH** | Optical circuit | Carrier fiber transport with self-healing **rings** that survive a cut |
| **DSL / cable** | Shared broadband | Cheap internet access; cable is a **shared medium** in the neighborhood segment |
| **Cellular (4G/5G) and satellite** | Wireless WAN | Backup links and remote sites; see [[Edge Networks and CDNs]] |
| **SD-WAN** | Overlay | Software-defined control over multiple underlying links (MPLS, broadband, LTE), steering traffic by policy and usually **encrypting** site-to-site over the internet — which is why it displaced MPLS-only designs |

## WAN Encapsulation Protocols

The layer 2 protocols that frame data on these links:

- **HDLC** — the standard synchronous encapsulation for serial links; bit-oriented, no authentication. Vendor variants (Cisco HDLC) are not interoperable.
- **SDLC** — IBM's predecessor to HDLC, used in SNA mainframe networks; polled, with a primary station controlling secondaries.
- **PPP** — the point-to-point protocol that replaced SLIP; supports multiple network protocols, error detection, and **authentication negotiation** (PAP, CHAP, EAP) — see [[Authentication Protocols]].

## Security Considerations for WAN Links

- **A private WAN is not an encrypted WAN.** MPLS, Frame Relay, and leased lines are private only in the sense that the carrier keeps customers logically separate. The carrier, and anyone who compromises the carrier, sees the traffic. Encrypt site-to-site links regardless of the underlying technology (see [[Virtual Private Networks]]).
- **The carrier is a third party** with access to the organization's traffic and an outage that is outside its control — contract terms, SLAs, and an alternative path matter (see [[Remote Access and Telecommuting]] on third-party connectivity).
- **Redundancy**: diverse carriers and diverse physical paths, since two "redundant" links often share the same conduit. A backhoe cutting one trench is the common WAN outage.
- **Bandwidth and latency drive design**: a WAN link is slow and expensive compared with a LAN, which is why caching, compression, and QoS live at WAN edges.

## Key Points

- **Circuit switching reserves a dedicated path (constant performance, wasteful, PSTN/ISDN/leased lines); packet switching routes each packet independently (efficient, variable, the internet).**
- **A virtual circuit is a logical dedicated path over a packet network: PVC = always on like a leased line, SVC = built on demand like a dial-up call.**
- **T1 = 1.544 Mbps, T3 = 44.736 Mbps, E1 = 2.048 Mbps; ISDN BRI = 2B+D, PRI = 23B+D; ATM uses fixed 53-byte cells; MPLS forwards on labels.**
- **X.25 checked errors heavily and was slow; Frame Relay dropped that and added CIR for guaranteed bandwidth.**
- **HDLC and SDLC are serial encapsulations without authentication; PPP adds it.**
- **Provider WANs are private, not encrypted — encrypt over them anyway, and plan for physically diverse paths.**
