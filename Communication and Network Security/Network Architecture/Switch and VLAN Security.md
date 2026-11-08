## Why Layer 2 Matters

A switch forwards frames only to the port that owns the destination MAC, which is why a sniffer on another port normally sees nothing. **Layer 2 attacks all aim to undo that**: to make the switch send the attacker traffic it should not, or to let the attacker reach a segment they should not. They are launched from **inside** the broadcast domain, so they are insider or post-compromise attacks, and the perimeter does not see them.

The switch's forwarding table is the **CAM table** (content-addressable memory), mapping MAC addresses to ports. It is learned automatically from traffic, with no authentication — the root of most of what follows.

## Eavesdropping on a Switched Network

**Eavesdropping (sniffing)** is passive capture of traffic. On a hub, everything is visible to everyone; on a switch, an attacker has to work for it:

- **Port mirroring (SPAN) or a network tap** — the legitimate mechanisms, used by IDS and packet capture. An attacker with switch administration can configure a mirror; an attacker with physical access can insert a tap. Both are nearly undetectable from the network.
- **ARP poisoning** — forged ARP replies redirect traffic through the attacker, the standard on-path attack on a LAN (see [[IP, ICMP, and ARP]]).
- **MAC flooding** — forces the switch to behave like a hub (below).
- **Physical access to the medium** — a tapped copper run or an unused wall port.

The two generic defenses: **encrypt** so captured traffic is useless (TLS, IPsec, and at layer 2 **MACsec**), and **control the port** so an unauthorized device never attaches.

## MAC Flooding

The attacker sends a flood of frames with **random source MAC addresses**, filling the switch's CAM table. Once it is full, the switch cannot learn new entries, and many switches **fail open**: unknown-destination frames are **flooded out every port**, so the switch degrades into a hub and the attacker sees traffic for other hosts.

Defense: **port security** limiting the number of MAC addresses per port, which is the direct counter.

## MAC Cloning and Spoofing

**MAC cloning (spoofing)** is changing a NIC's MAC address to one belonging to another device. A MAC is software-settable, so this is trivial.

Uses:

- **Impersonating an authorized device** to defeat **MAC filtering** on a switch port or wireless network — which is why MAC filtering is not a security control, only a convenience (see [[Wireless Fundamentals]]).
- **Taking over an address** so the switch re-learns the victim's MAC on the attacker's port, redirecting their traffic (a layer 2 denial of service or hijack).
- **Evading address-based tracking or licensing.**

Defense: **802.1X** authenticates the device or user with a credential rather than an address; port security with sticky MACs raises the effort; **DHCP snooping** plus **IP source guard** binds address to port.

## VLAN Hopping

A **VLAN** is logical segmentation at layer 2: ports (or frames, tagged with **802.1Q**) belong to separate broadcast domains, and traffic between VLANs must pass a router where ACLs apply. **VLAN hopping** is reaching a VLAN the attacker is not a member of.

Two methods:

- **Switch spoofing** — the attacker's port negotiates a **trunk link** (which carries all VLANs) because dynamic trunking is enabled. Defense: disable automatic trunk negotiation and configure access ports explicitly as access ports.
- **Double tagging** — the attacker sends a frame with **two 802.1Q tags**; the first switch strips the outer tag (its own native VLAN) and forwards the frame on the trunk, where the second switch acts on the inner tag and delivers it to the target VLAN. It is one-way (no reply path) but enough for an attack. Defense: make the **native VLAN an unused VLAN** and tag it, and never use VLAN 1 for user traffic.

A VLAN is a **logical** boundary enforced by a device's configuration; a misconfiguration or a compromised switch collapses it, which is why a physically separate network is still stronger for genuinely hostile separation (see [[Network Segmentation]]).

## Port Security and Layer 2 Hardening

| Control | What it stops |
|---|---|
| **Port security** (limit MACs per port, sticky learning, shutdown or restrict on violation) | MAC flooding and casual unauthorized devices |
| **802.1X** port-based authentication | Any unauthorized device attaching at all — the strongest form of port security (see [[Authentication Protocols]]) |
| **Disable unused ports** and place them in an unused VLAN | Someone plugging into a wall port in a lobby or meeting room |
| **DHCP snooping** | Rogue DHCP servers handing out an attacker gateway; builds the binding table the next two controls use |
| **Dynamic ARP inspection (DAI)** | ARP poisoning, by validating ARP packets against the DHCP snooping bindings |
| **IP source guard** | Hosts spoofing source IP addresses on their port |
| **BPDU guard / root guard** | A rogue switch becoming the spanning-tree root and attracting traffic |
| **Disable dynamic trunking; tag and isolate the native VLAN** | VLAN hopping |
| **MACsec (802.1AE)** | Eavesdropping and tampering on the wire, by encrypting link by link |
| **Private VLANs / port isolation** | Lateral movement between hosts in the same VLAN (guest, hosting, hotel networks) |

Plus the management-plane basics for the switch itself — no defaults, encrypted management, out-of-band access, logging (see [[Network Devices]]).

## Key Points

- **The CAM table is learned without authentication; layer 2 attacks exploit that and are launched from inside the broadcast domain.**
- **MAC flooding fills the CAM table so the switch fails open and floods frames everywhere — effectively turning it into a hub. Port security is the counter.**
- **MAC cloning defeats MAC filtering trivially, because MAC addresses are software-settable; 802.1X authenticates with a credential instead.**
- **VLAN hopping works by switch spoofing (negotiating a trunk) or double tagging (abusing the native VLAN); disable dynamic trunking and use an unused, tagged native VLAN.**
- **DHCP snooping, dynamic ARP inspection, and IP source guard are the layered counters to rogue DHCP, ARP poisoning, and IP spoofing.**
- **A VLAN is a configuration-enforced boundary, not a physical one.**
