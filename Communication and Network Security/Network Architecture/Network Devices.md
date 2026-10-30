## Devices by OSI Layer

Network devices are best understood by the **layer at which they make forwarding decisions**, because that decides what they can see and what they can separate.

| Device | Layer | What it does | Domains |
|---|---|---|---|
| **Repeater / concentrator / amplifier** | 1 | Regenerates the signal to extend cable length | Extends one collision domain |
| **Hub** | 1 | Multiport repeater; every bit goes out every port | One collision domain, one broadcast domain; anyone can sniff everything |
| **Modem** | 1 | Converts digital to analog (or to a carrier's signalling) for phone, cable, DSL, or cellular lines | n/a |
| **Bridge** | 2 | Connects two segments and forwards frames by MAC address; learns which MACs are on which side | Separates collision domains; keeps one broadcast domain |
| **Switch** | 2 (layer 3 switches also route) | Multiport bridge; forwards frames only to the port that owns the destination MAC, using its **CAM table** | Each port is its own collision domain; one broadcast domain per VLAN |
| **Router** | 3 | Forwards packets between networks by IP address, using a routing table; applies ACLs | Separates broadcast domains |
| **Gateway** | 3 to 7 | Connects networks that use **different protocols**, translating between them (mail gateway, VoIP gateway, IoT protocol gateway) | n/a |
| **Firewall** | 3 to 7 depending on type | Enforces a security policy on traffic between zones | See [[Firewalls and Proxies]] |
| **LAN extender** | 2 | Remote-access, multilayer switch that connects distant LANs over a WAN link as if they were local | n/a |
| **Wireless access point** | 2 | Bridges 802.11 wireless clients onto the wired LAN | See [[Wireless Fundamentals]] |
| **Proxy** | 7 | Terminates the client connection and makes its own on the client's behalf | See [[Firewalls and Proxies]] |

Switches versus hubs is the classic point: a switch sends a frame only to its destination port, so a sniffer on another port sees nothing unless the attacker uses a mirror port, ARP poisoning, or MAC flooding (see [[IP, ICMP, and ARP]]). Switches also support **VLANs**, **port security**, **802.1X**, DHCP snooping, and dynamic ARP inspection, which makes them security devices, not just connectivity.

**Collision domain**: the set of devices that can collide on a shared medium; split by bridges and switches. **Broadcast domain**: the set of devices that receive a layer 2 broadcast; split by routers and VLANs.

## Secure Operation of Network Hardware

Network devices are themselves systems with operating systems, credentials, and configurations. The common failures are operational rather than protocol-level.

- **Default credentials and configurations** on switches, routers, access points, and management interfaces. Change them before deployment; disable unused services (Telnet, HTTP, SNMPv1/2, CDP where not needed).
- **Firmware and OS patching** is often neglected because devices are "infrastructure". Treat them like servers with a patch cycle, and verify firmware integrity (signed images, see [[Firmware]]).
- **Management plane isolation**: administer devices only from a dedicated **management network** or **out-of-band** path (console server, dedicated management port), with SSH/HTTPS and SNMPv3, MFA for admins, and role-based access. Never expose management interfaces to user segments or the internet.
- **Configuration management**: back up configurations, version them, review diffs, and alert on unexpected changes; **change control** applies to network changes as much as to servers.
- **Logging and monitoring**: send syslog, SNMP traps, and flow records (NetFlow/IPFIX) to a central collector; time-synchronize with **NTP** so logs can be correlated.
- **Physical security**: devices in locked rooms or cabinets; console ports are full access. Unused ports **administratively disabled** and, on switches, assigned to an unused VLAN.
- **Redundancy and resilience**: redundant power supplies, dual uplinks, spanning tree or link aggregation, and redundant routers (HSRP/VRRP) so that a single device failure does not become an outage; keep spares and vendor support for critical devices.
- **Secure disposal**: configurations and credentials live in flash; wipe before resale or disposal.
- **Supply chain**: buy through authorized channels, validate hardware and firmware authenticity; counterfeit devices and tampered firmware are documented risks (see [[Supply Chain Risk Management]]).

## Key Points

- **Hubs and repeaters are layer 1 (everything everywhere), bridges and switches are layer 2 (forward by MAC), routers are layer 3 (forward by IP), gateways translate protocols.**
- **Switches split collision domains; routers (and VLANs) split broadcast domains.**
- **A switch limits sniffing to the attacker's own port**, which is why ARP poisoning and MAC flooding exist.
- **Network hardware fails the same way servers do**: defaults, missing patches, exposed management interfaces, no logging. Isolate the management plane and apply change control.
