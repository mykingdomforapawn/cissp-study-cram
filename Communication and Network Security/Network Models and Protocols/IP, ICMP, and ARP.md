## Internet Protocol

**IP** provides **logical addressing and routing** between networks at the network layer. It is connectionless and best-effort; reliability comes from TCP above it, if at all. Every packet carries source and destination addresses, and routers forward on the destination address alone.

## IPv4 vs IPv6

| | IPv4 | IPv6 |
|---|---|---|
| Address size | 32 bits, dotted decimal (192.168.1.10) | 128 bits, hexadecimal groups (2001:db8::1) |
| Address space | About 4.3 billion, exhausted | Effectively unlimited |
| NAT | Needed to stretch the address space | Designed to be unnecessary |
| IPsec | Optional add-on | Built into the specification (though still optional to use) |
| Configuration | Manual or DHCP | **Stateless autoconfiguration (SLAAC)** or DHCPv6 |
| Broadcast | Yes | No; multicast and anycast instead |
| Header | Variable, with checksum and fragmentation by routers | Fixed 40 bytes, simpler, fragmentation only by the sender |

Security notes on IPv6: it is often **enabled by default and unmonitored**, so an attacker can use it to bypass IPv4-only filters; **dual stack** doubles the attack surface; the loss of NAT exposes hosts directly; and link-local **neighbor discovery** can be spoofed like ARP. **Scope** also matters: an address can be link-local (fe80::), unique local (fc00::/7, the private range), or global.

## IPv4 Address Classes and Private Ranges

Original **classful** addressing split the space by first octet:

| Class | First octet | Default mask | Use |
|---|---|---|---|
| A | 1 to 126 | /8 | Very large networks |
| B | 128 to 191 | /16 | Large networks |
| C | 192 to 223 | /24 | Small networks |
| D | 224 to 239 | n/a | **Multicast** |
| E | 240 to 255 | n/a | Experimental |

127.0.0.0/8 is **loopback**; 169.254.0.0/16 is **APIPA** (link-local, assigned when DHCP fails). **CIDR** (classless inter-domain routing) replaced classes with variable-length masks written as a prefix length (/22), allowing subnets of any size and route aggregation.

**Private address ranges** (RFC 1918), not routable on the internet and translated by **NAT**:

- 10.0.0.0/8
- 172.16.0.0/12 (172.16.0.0 to 172.31.255.255)
- 192.168.0.0/16

NAT hides internal addressing and conserves public addresses, but it is not a firewall in itself and breaks protocols that embed addresses in their payload (older FTP, SIP). **PAT** (port address translation, overloading) maps many internal hosts to one public address by varying the port. Related: a **bastion host** or a **screened subnet** uses these ranges to keep the internal network unaddressable from outside; see [[Network Segmentation]].

## ICMP

The **Internet Control Message Protocol** carries **error and diagnostic messages** at the network layer: echo request/reply (**ping**), destination unreachable, time exceeded (**traceroute**), redirect. It has no ports and no authentication.

Abuse:

- **Ping flood / Smurf**: ICMP echo requests sent to a broadcast address with a spoofed source so every host replies to the victim (amplification). **Fraggle** is the same with UDP.
- **Ping of death**: oversized ICMP packet crashing old stacks.
- **ICMP redirect** can alter a host's routing; **ICMP tunneling** hides data in echo payloads.
- **Reconnaissance**: ping sweeps and traceroute map the network.

Defense is to filter ICMP selectively at the perimeter (block inbound echo and redirects, allow needed types such as fragmentation needed), not to block it entirely, since path MTU discovery depends on it.

## IGMP

The **Internet Group Management Protocol** lets hosts **join and leave multicast groups** so that routers forward multicast streams only where there are listeners. It is a network layer management protocol and has no security of its own; multicast content that needs protection must be encrypted at a higher layer.

## ARP

The **Address Resolution Protocol** maps an **IP address to a MAC address** on the local network. A host broadcasts "who has 192.168.1.1?" and the owner replies with its MAC; the answer is cached in the **ARP table**.

The problem is that ARP has **no authentication and accepts unsolicited replies**. **ARP poisoning** (ARP spoofing, cache poisoning) sends forged replies claiming the attacker's MAC for the gateway's IP (and vice versa). Traffic is then routed through the attacker, enabling **on-path (man-in-the-middle)** interception, modification, or a denial of service (if the attacker drops it). **MAC spoofing** is simply changing a NIC's MAC to impersonate another device.

Defenses:

- **Static ARP entries** for critical hosts (does not scale).
- **Dynamic ARP Inspection (DAI)** on switches, which validates ARP against the DHCP snooping binding table.
- **Port security** limiting MACs per switch port.
- **Encryption** of traffic end to end, so interception yields nothing readable.
- Detection tools that alert when a MAC-to-IP mapping changes (arpwatch, XArp).

Related layer 2 attack: **MAC flooding** overflows the switch's CAM table so it fails open and floods all frames like a hub, letting the attacker sniff. Port security is the control.

## Key Points

- **IPv4 is 32-bit and exhausted; IPv6 is 128-bit, has no broadcast, uses SLAAC, and is often enabled but unmonitored.**
- **Private ranges: 10/8, 172.16/12, 192.168/16; NAT translates them; 127/8 is loopback; 169.254/16 is APIPA; class D is multicast.**
- **ICMP is diagnostics with no authentication: Smurf, ping of death, redirects, tunneling. Filter selectively, not entirely.**
- **IGMP manages multicast group membership.**
- **ARP has no authentication, so ARP poisoning enables on-path attacks on a LAN; DAI, port security, and encryption are the defenses.**
