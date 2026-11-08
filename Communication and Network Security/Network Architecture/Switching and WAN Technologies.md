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

**Security consequence**: a circuit is a fixed, known path — easier to physically protect, and traffic analysis is trivial since the circuit itself reveals who is talking to whom. Packets take unpredictable paths through networks nobody controls, so **encryption, not routing, is what protects them**.

## Virtual Circuits

A **virtual circuit** is a logical connection built **on top of a packet-switched network** that behaves like a dedicated circuit: packets follow a defined path, arrive in order, and get agreed performance. It is the compromise between the two models.

| | Description |
|---|---|
| **PVC** (permanent virtual circuit) | Always on, configured by the provider. The analogue of a **leased line**: it is simply there |
| **SVC** (switched virtual circuit) | Built on demand, used, then torn down. The analogue of a **dial-up call** |

Virtual circuits can carry a **quality of service commitment**: Frame Relay's **CIR** (committed information rate) guarantees a minimum bandwidth, with bursting above it when capacity allows.

## WAN Technologies

A **WAN** connects sites across distances that the organization does not own cabling for, so it buys a carrier's service. The terminology:

- **Dedicated (leased) line**: a permanent, exclusive connection between two points, billed as a flat rate whether used or not. Predictable and private.
- **Non-dedicated line**: a shared connection established as needed (broadband, cellular, historically dial-up and ISDN).
- **CSU/DSU**: the device between the LAN router and the carrier's digital line — the "modem" for a leased line.
- **Last mile**: the link from the carrier to the premises, usually the bottleneck and the single point of failure.

| Technology | Nature | Notes |
|---|---|---|
| **MPLS** | Label switching | Forwards on a short **label** instead of a routing lookup, creating engineered paths with QoS classes. The standard provider WAN; **private, but not encrypted** — the carrier sees the traffic |
| **SD-WAN** | Overlay | Software-defined control over several underlying links (MPLS, broadband, LTE), steering traffic by policy and usually **encrypting** site-to-site over the internet. This is why pure MPLS designs are being replaced |
| **Broadband (DSL, cable, fiber)** | Shared, non-dedicated | The common site and home connection; cable is a **shared medium** in the neighborhood segment |
| **Cellular (4G/5G) and satellite** | Wireless WAN | Remote sites and backup links; satellite adds high latency. See [[Edge Networks and CDNs]] |
| **Leased line (T-carrier / E-carrier)** | Dedicated digital | Still sold where a guaranteed private circuit is required. **T1** = 1.544 Mbps, **T3** = 44.736 Mbps, **E1** = 2.048 Mbps in Europe; **fractional** rents a subset of channels |

**Legacy technologies** that appear in older material and in comparisons, none of which is deployed today: **X.25** (the first public packet network, slow because of heavy error checking for noisy lines), **Frame Relay** (its faster successor — error correction left to the endpoints, shared provider cloud, **CIR** for a guaranteed rate), **ATM** (cell switching with fixed **53-byte cells** for predictable latency), and **ISDN** (circuit-switched digital over phone lines, **BRI** = 2B+D, **PRI** = 23B+D). Their lasting points are the ones already made above: virtual circuits, committed rates, and the trade-off between error checking and speed.

## WAN Encapsulation Protocols

The layer 2 protocols that frame data on these links:

- **PPP** — the point-to-point protocol in current use; replaced SLIP, supports multiple network protocols, error detection, and **authentication negotiation** (PAP, CHAP, EAP) — see [[Authentication Protocols]].
- **HDLC**, and IBM's older **SDLC** before it, are the synchronous serial encapsulations PPP displaced: bit-oriented, no authentication.

## Security Considerations for WAN Links

- **A private WAN is not an encrypted WAN.** MPLS and leased lines are private only in the sense that the carrier keeps customers logically separate. The carrier, and anyone who compromises the carrier, sees the traffic. Encrypt site-to-site links regardless of the underlying technology (see [[Virtual Private Networks]]).
- **The carrier is a third party** with access to the organization's traffic and an outage that is outside its control — contract terms, SLAs, and an alternative path matter (see [[Remote Access and Telecommuting]] on third-party connectivity).
- **Redundancy**: diverse carriers and diverse physical paths, since two "redundant" links often share the same conduit. A backhoe cutting one trench is the common WAN outage.
- **Bandwidth and latency drive design**: a WAN link is slow and expensive compared with a LAN, which is why caching, compression, and QoS live at WAN edges.

## Key Points

- **Circuit switching reserves a dedicated path (constant performance, wasteful, PSTN/ISDN/leased lines); packet switching routes each packet independently (efficient, variable, the internet).**
- **A virtual circuit is a logical dedicated path over a packet network: PVC = always on like a leased line, SVC = built on demand like a dial-up call.**
- **MPLS forwards on labels and is the provider WAN; SD-WAN steers traffic across several links by policy and encrypts over the internet.**
- **T1 = 1.544 Mbps, T3 = 44.736 Mbps, E1 = 2.048 Mbps.**
- **Legacy, for recognition only: X.25 (slow, heavy error checking), Frame Relay (faster, CIR), ATM (53-byte cells), ISDN (BRI 2B+D, PRI 23B+D).**
- **PPP is the current serial encapsulation and the one that adds authentication; HDLC and SDLC do not.**
- **Provider WANs are private, not encrypted — encrypt over them anyway, and plan for physically diverse paths.**
