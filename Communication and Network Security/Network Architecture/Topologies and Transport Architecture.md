## Physical vs Logical Topology

A **topology** describes how devices are connected. The **physical topology** is the cabling layout; the **logical topology** is the path that signals or data actually take. They can differ: a Token Ring network is cabled as a star to a central hub but behaves logically as a ring. Most modern LANs are physically and logically star-based Ethernet with switches.

## Network Topologies

| Topology | Layout | Strengths | Weaknesses |
|---|---|---|---|
| **Bus** | All devices on one shared cable (trunk) with terminators at both ends | Cheap, simple | One cable break stops the whole segment; collisions; hard to troubleshoot; obsolete |
| **Ring** | Each device connected to the next in a closed loop; data passes in one direction, often with a **token** | Predictable, no collisions | A single break or device failure stops the ring unless a second counter-rotating ring exists (FDDI) |
| **Star** | Every device connected to a central hub or switch | A single cable break affects one device; easy to add and troubleshoot | The central device is a single point of failure |
| **Mesh** | Every device connected to every other (**full mesh**) or to several others (**partial mesh**) | Highest redundancy and fault tolerance | Expensive cabling and configuration; used for WAN cores, data center fabrics, and wireless mesh |
| **Tree / hierarchical** | Stars of stars: access, distribution, core layers | Scales; the enterprise standard | Failures higher in the tree affect more devices |

Resilience follows from the topology: mesh and star survive single failures best, bus and single ring worst. **Redundant paths** in a switched star network require **spanning tree** to prevent loops, or newer fabric protocols.

## Transport Architecture

The **transport architecture** describes how a network is organized to move traffic, both in functional planes and in traffic direction.

Three planes of a network device or network:

| Plane | Function | Security concern |
|---|---|---|
| **Data plane** (forwarding plane) | Moves user packets from ingress to egress according to the forwarding table | Volume; this is what DDoS attacks saturate |
| **Control plane** | Builds the forwarding table: routing protocols, spanning tree, ARP; in SDN, the centralized controller | Spoofed routing updates and controller compromise redirect everything |
| **Management plane** | Configures and monitors the device: SSH, SNMP, web UI, APIs | Must be isolated and authenticated; the usual way in for an attacker |

Separating these planes is what **SDN** does explicitly (control plane in software, data plane in switches) and what secure operation does implicitly by isolating the management network (see [[Network Devices]] and [[Converged and Multilayer Protocols]]).

Traffic directions:

- **North-south**: traffic entering or leaving the network (client to data center, internal to internet). Traditionally where firewalls and IDS sit.
- **East-west**: traffic between systems **inside** the network or data center (server to server, VM to VM). Historically unfiltered, now the majority of data center traffic and the path of lateral movement. Internal segmentation firewalls, microsegmentation, and visibility into virtual switches address it.

Switching methods are a minor point: **cut-through** switching forwards a frame as soon as the destination MAC is read (fast, forwards errors), **store-and-forward** receives the whole frame and checks the CRC first (slower, drops corrupted frames).

## Ethernet

**Ethernet (IEEE 802.3)** is the dominant LAN technology. It is a shared-media, **broadcast** technology: every frame carries a 48-bit source and destination **MAC address**, and frames addressed to the broadcast MAC go to all devices in the broadcast domain. Media access is **CSMA/CD** on shared media, though with switches and full-duplex links collisions no longer occur (see [[Signaling and Media Access]]).

Speeds have gone from 10 Mbps through Fast Ethernet (100 Mbps), Gigabit, 10 Gbps, 40 and 100 Gbps and beyond, over twisted pair or fiber (see [[Transmission Media]]). Ethernet uses **frames** of 64 to 1518 bytes (**jumbo frames** up to about 9000 bytes in data centers) and supports **802.1Q VLAN tagging**.

Security relevant properties: MAC addresses are **not authenticated** (spoofable), broadcast means any device in the domain hears ARP and DHCP traffic, and the same frame format carries everything, so switch features (port security, 802.1X, VLANs, DHCP snooping) are where Ethernet security lives.

## Key Points

- **Physical topology is the cabling; logical topology is the signal path; they can differ.**
- **Bus fails entirely on one break; ring fails on one break unless dual; star isolates failures to one link but the hub is a single point of failure; mesh is most resilient and most expensive.**
- **Data plane forwards, control plane decides routes, management plane configures; isolate the management plane and protect the control plane.**
- **North-south crosses the perimeter; east-west moves inside and is where lateral movement happens.**
- **Ethernet is broadcast, MAC-addressed, and unauthenticated; its security is in switch features.**
