## What a Firewall Does

A **firewall** enforces a policy on traffic crossing a boundary between zones of different trust. It permits or denies based on a rule set, and it is the primary control at the points that [[Network Segmentation]] creates. The baseline rule is **deny by default** (implicit deny): everything not explicitly allowed is dropped. A firewall is only as good as its rule base, which needs documentation, least privilege, regular review, and change control; and it is **blind to traffic that does not pass through it** (encrypted content, traffic on a bypass path, insider traffic within a zone).

## Firewall Generations and Types

| Type | Layer | How it decides | Strengths / weaknesses |
|---|---|---|---|
| **Static packet filtering** (first generation) | 3 (and 4 headers) | Rules on source/destination IP, port, protocol, per packet, no memory of previous packets | Fast and simple; cannot tell a reply from an unsolicited packet; fooled by fragmentation and spoofing |
| **Application-level gateway** / proxy firewall (second generation) | 7 | Understands a specific protocol (HTTP, FTP, SMTP), inspects content, and makes the connection on behalf of the client | Deepest inspection; one proxy per protocol, higher latency |
| **Circuit-level gateway** (second generation) | 5 | Validates the session setup (TCP handshake) and then relays without inspecting content; **SOCKS** is the classic example | Protocol-independent, fast; no content inspection |
| **Stateful inspection** (third generation) | 3 to 4 | Tracks the **state of each connection** in a table; allows return traffic for established sessions, blocks unsolicited packets | The baseline of modern firewalls; still does not understand application content |
| **Next-generation firewall (NGFW)** | 3 to 7 | Stateful inspection plus **deep packet inspection**, application identification regardless of port, user identity awareness, integrated IPS, TLS decryption, threat intelligence feeds | A unified threat management (UTM) style device; complexity and performance cost; TLS inspection has privacy implications |
| **Internal segmentation firewall (ISFW)** | 3 to 7 | An NGFW placed **inside** the network between segments rather than at the edge | Addresses east-west traffic; must be fast and transparent |
| **Web application firewall (WAF)** | 7 | Inspects HTTP(S) specifically for application attacks (SQL injection, XSS, path traversal), often with signatures and behavioral rules | Protects web applications; not a general firewall |
| **Host-based firewall** | varies | Software firewall on an endpoint or server | Last line of defense; enables microsegmentation; managed centrally |
| **Virtual / cloud firewall** | varies | Firewall as a virtual appliance or a cloud provider control (security groups, network ACLs) | Protects east-west traffic hypervisor-level that physical firewalls cannot see |

**Stateless vs stateful** is the essential distinction: stateless looks at each packet in isolation; stateful remembers the session and can therefore apply the rule "allow established connections back in" automatically.

A **multihomed firewall** has more than one network interface, so it can sit between several zones at once; a **dual-homed** host has exactly two, with IP forwarding disabled so that nothing passes except through the firewall software.

## Deployment Architectures

| Architecture | Layout | Trade-off |
|---|---|---|
| **Single-tier** | One firewall between the internet and the private network | Simple; one rule set protects everything; no place for public servers except inside |
| **Two-tier** | One firewall with three interfaces (internet, screened subnet, intranet), or two firewalls in series with the screened subnet between them | Public servers isolated in the screened subnet; the standard design |
| **Three-tier** (multi-tier) | Multiple firewalls in series creating multiple subnets of increasing trust (public, application, database) | Defense in depth; a compromise of one tier faces another firewall; more cost and complexity |

Using **firewalls from different vendors** at different tiers avoids one vulnerability defeating all layers. A **screened host** is a single bastion host protected by a packet-filtering router.

## Proxies

A **proxy** sits between client and server, terminates the client's connection, and opens its own to the server. Because it speaks the application protocol, it can inspect, filter, cache, log, and authenticate.

- **Forward proxy**: used by internal clients going out; enforces web policy, hides internal addresses (clients appear as the proxy), caches content, and logs usage. May be **transparent** (clients do not know) or explicit (configured in the browser).
- **Reverse proxy**: sits in front of servers for inbound traffic; load balances, terminates TLS, caches, and hides the server topology. A WAF is usually a reverse proxy.
- **Anonymizing / open proxies** and **proxy chaining** on the attacker side hide origin; on the defender side, mixing proxies from different vendors is the same defense in depth idea as mixed firewalls.

**NAT** is sometimes grouped with proxies because it also hides internal addresses, but it works at layer 3 and does not inspect content.

## Content and URL Filtering

A **content filter** (secure web gateway) inspects what passes through a proxy and blocks by **URL / domain category** (gambling, malware, phishing), by **content type** (executables, scripts), by **keywords or patterns** (data loss prevention), and by malware scanning. Lists come from reputation feeds; policies differ by user group. Limits: encrypted traffic is opaque unless TLS inspection is performed; categorization lags behind new sites; and filtering is a policy and privacy decision as much as a technical one, so it needs an acceptable use policy behind it.

## Key Points

- **Deny by default; a firewall is blind to what bypasses it or is encrypted through it.**
- **Packet filter = per-packet headers, stateless; stateful = tracks sessions; application-level gateway = per-protocol proxy with content inspection; circuit-level = validates the session only (SOCKS); NGFW = all of this plus application and user awareness and IPS.**
- **ISFW addresses east-west traffic inside the network; WAF protects web applications at layer 7.**
- **Two-tier with a screened subnet is the standard design; multi-tier with mixed vendors is defense in depth.**
- **Forward proxy protects and polices clients going out; reverse proxy protects servers receiving traffic.**
