## What NAT Does

**Network address translation** rewrites the IP addresses (and often ports) in packet headers as they cross a boundary, so that hosts using one address space appear to the other side as something else. It was created to solve **IPv4 address exhaustion**: many internal hosts share a few public addresses.

Two effects, only one of which was the goal:

- **Address conservation** — a whole organization behind one or a few public addresses.
- **Topology hiding** — outsiders see the translated address, not the internal addressing scheme, and cannot initiate a connection to an internal host that has no mapping.

NAT runs on the router, firewall, or gateway at the boundary and is **transparent to the hosts**, which believe they are using their own address.

## Private IP Addresses

NAT is paired with the **RFC 1918 private ranges**, which are not routable on the internet and may be reused by every organization:

| Range | CIDR | Size |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | One class A |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | 16 class B |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | 256 class C |

Other special ranges: **127.0.0.0/8** loopback, **169.254.0.0/16** APIPA (below), **224.0.0.0/4** multicast (class D), and in IPv6 **fc00::/7** unique local and **fe80::/10** link-local.

A packet with a private source address arriving from the internet is **spoofed by definition**; filtering those (ingress/egress filtering, **bogon filtering**) is a basic perimeter control.

## Types of Translation

| Type | Mapping | Use |
|---|---|---|
| **Static NAT** | One internal address permanently to one public address | Publishing a server; the mapping exists before any traffic, so inbound connections work |
| **Dynamic NAT** | Internal addresses to a **pool** of public addresses, assigned as needed | Conserves addresses; a host gets a public address only while it has traffic, and connections fail when the pool is exhausted |
| **PAT** (port address translation, NAT overloading) | **Many** internal addresses to **one** public address, distinguished by **source port** | What home routers and most organizations actually do; the real address multiplier |

**Stateful NAT** is the key property: the translator keeps a **translation table** of internal address/port to external address/port per session, and uses it to map replies back to the right host. It therefore **tracks the state of each connection** and times entries out. Because an unsolicited inbound packet matches no table entry, it has nowhere to go and is dropped.

**Port forwarding** (destination NAT) is the deliberate exception: a static rule maps an external port to an internal host, creating the inbound path that NAT otherwise prevents.

## NAT Is Not a Firewall

NAT drops unsolicited inbound traffic as a **side effect** of having no mapping, not as a policy decision. It does not:

- inspect content or enforce rules on what is allowed out — any internal host can reach anything, and malware calling home is an outbound session like any other;
- protect against anything carried inside an allowed session (malware, phishing, exfiltration over HTTPS);
- protect hosts from each other **inside** the translated network.

Treat it as topology hiding plus an accidental default-deny inbound, behind a real firewall (see [[Firewalls and Proxies]]).

**What NAT breaks**: protocols that embed IP addresses in their **payload** rather than only in the header — older FTP (active mode), SIP and other VoIP signaling, and some IPsec configurations. The workarounds are **application-layer gateways** (ALGs) that rewrite the payload too, and **NAT-T**, which wraps IPsec ESP in UDP so it survives translation. NAT also complicates logging and attribution: many users share one public address, so an external log entry does not identify a host without the translation log.

IPv6's address space removes the need for NAT, which is why IPv6 designs expose hosts with global addresses and rely on firewall policy instead (see [[IP, ICMP, and ARP]]).

## APIPA

**Automatic Private IP Addressing** (link-local addressing) is what a host does when it is configured for **DHCP and gets no answer**: it self-assigns an address in **169.254.0.0/16**, checking that no one else on the link uses it.

- It allows communication with other APIPA hosts **on the same subnet only** — there is no gateway and no DNS, so nothing beyond the local link works.
- Seeing a 169.254 address is a **diagnostic signal**: the DHCP server is down, unreachable, out of leases, or the host is on the wrong VLAN or a dead link.
- Security angle: a failed DHCP server can leave a set of hosts able to talk to each other but isolated, and an attacker who **DoSes DHCP** (DHCP starvation) can push clients into this state or onto a **rogue DHCP server** offering real settings. The defenses are **DHCP snooping** on the switch and monitoring for unexpected link-local addresses (see [[Switch and VLAN Security]]).

## Key Points

- **NAT translates addresses at a boundary to conserve public addresses and hide internal topology; it is transparent to hosts.**
- **Private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 — not routable on the internet, so a private source address from outside is spoofed.**
- **Static NAT = one-to-one, dynamic NAT = a pool, PAT = many-to-one using ports. Stateful NAT keeps a translation table per session, which is why unsolicited inbound traffic is dropped.**
- **NAT is not a firewall: no policy, no inspection, no protection inside the network.**
- **NAT breaks protocols that embed addresses in the payload (FTP, SIP, IPsec) — hence ALGs and NAT-T.**
- **APIPA = 169.254.0.0/16, self-assigned when DHCP fails; local link only, and a sign that DHCP is broken or attacked.**
