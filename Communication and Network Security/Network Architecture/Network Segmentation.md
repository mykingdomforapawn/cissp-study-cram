## Why Segment

**Network segmentation** divides a network into zones so that traffic between them must cross a control point. It serves three goals:

- **Security**: limit lateral movement and contain a compromise; enforce different trust levels; keep sensitive systems unreachable from general users.
- **Performance**: reduce broadcast traffic and congestion by shrinking broadcast domains.
- **Compliance**: isolate regulated systems (cardholder data, medical records, industrial controls) so that the scope of audits and controls is smaller.

Segments can be **physical** (separate switches and cabling) or **logical** (VLANs, subnets, virtual networks), with physical being stronger and logical being cheaper and more flexible.

## Zones by Trust

| Zone | Who is in it | Characteristic control |
|---|---|---|
| **Intranet** | Internal users and systems; the private network | Firewall at the edge; internal services not reachable from outside |
| **Extranet** | A segment opened to **specific outside parties** (partners, suppliers, customers) | Authentication and a firewall between it and the intranet and the internet; often a VPN |
| **Screened subnet** (historically **DMZ**, demilitarized zone) | **Public-facing services** (web, mail, DNS) that must be reachable from the internet | Firewalls on both sides; a compromise here should not reach the intranet |
| **Internet** | Everyone, untrusted | No control; everything from it is treated as hostile |
| **Management network** | Admin interfaces of switches, servers, hypervisors, out-of-band consoles | Isolated from user traffic; access only through jump hosts / privileged access workstations |
| **Guest / IoT / OT segments** | Low-trust or unmanaged devices | No path to internal resources beyond what is explicitly needed |

A **bastion host** is a hardened system exposed to an untrusted network, typically sitting in the screened subnet or acting as the single entry point (jump box) into a protected one.

## Mechanisms

- **VLANs** (802.1Q): a switch feature that puts ports into separate broadcast domains; traffic between VLANs must go through a router or layer 3 switch, where ACLs apply. Risks: **VLAN hopping** through double tagging or switch spoofing, and **misconfigured trunks**. Keep the native VLAN unused and disable unused ports.
- **Subnets and routers with ACLs**: the layer 3 boundary; coarse but universal.
- **Firewalls** between zones, from stateful to next-generation (see [[Firewalls and Proxies]]).
- **Microsegmentation**: policy enforced per workload or per host, usually in software (host firewalls, hypervisor or SDN policies, cloud security groups), so that even two servers on the same subnet cannot talk unless allowed. This is the segmentation model behind **zero trust**, where location on the network grants nothing and every connection is authenticated and authorized (see [[Secure Design Principles]]).
- **Air gap**: no network connection at all between a system and others. The strongest isolation, used for the most sensitive or safety-critical systems, but it moves the risk to removable media and maintenance laptops (Stuxnet crossed an air gap on USB). A **unidirectional gateway / data diode** allows data out of an isolated network while physically preventing anything from going in.
- **Network access control** decides which segment a device lands in based on its identity and posture (see [[Network Access Control and Endpoint Security]]).

## Design Points

- **Traffic between segments is where monitoring lives**: IDS sensors, flow logs, and DLP are placed at the choke points segmentation creates.
- **Segmentation is only as good as the rules**: an "any/any" rule between zones is no segmentation at all; rules need review and least privilege.
- **East-west vs north-south**: traditional perimeters filter north-south (in and out of the network) and leave east-west (inside) open. Microsegmentation closes that gap.
- Segmentation also limits the **blast radius** of broadcast storms and misconfigurations, not only of attackers.

## Key Points

- **Segmentation creates control points; the security benefit is containment of lateral movement.**
- **Intranet is private, extranet is for specific partners, screened subnet holds public-facing services with firewalls on both sides.**
- **VLANs are logical segmentation at layer 2; inter-VLAN traffic must pass a router where ACLs apply; beware VLAN hopping.**
- **Microsegmentation enforces policy per workload and underpins zero trust.**
- **An air gap is the strongest isolation; its residual risk is removable media. A data diode allows one-way flow.**
