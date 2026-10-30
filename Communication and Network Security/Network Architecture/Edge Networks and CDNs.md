## Edge Networks

An **edge network** moves computing and content **closer to the users or devices** that produce or consume data, instead of sending everything to a central data center or cloud. The point is **latency, bandwidth, and resilience**: a factory controller, a vehicle, or a retail store keeps working and reacts in milliseconds even if the link to the core is slow or down.

Related terms: **edge computing** (processing at or near the data source), **fog computing** (a layer of intermediate nodes between devices and the cloud), and the **Internet of Things** devices that generate the data. The architecture and its security concerns (many small, physically exposed, hard-to-patch devices) are covered in [[IoT, Edge, and Fog Computing]].

From the network view, edge means: more locations to secure, more links to protect, and policy that must follow the data to wherever it is processed. **SASE** (secure access service edge) is the response on the service side, delivering firewalling, secure web gateway, CASB, and zero trust access from cloud points of presence near the user rather than from a corporate data center.

## Content Distribution Networks

A **content distribution network (CDN)** is a geographically distributed set of **caching servers** that serve copies of content (static files, video, software updates, whole web front ends) from a location close to each user. The origin server is contacted only for cache misses and dynamic content.

| Benefit | Mechanism |
|---|---|
| Performance | Content served from a nearby edge node; lower latency and transit cost |
| Availability and **DDoS absorption** | Attack traffic is spread across the provider's global capacity and scrubbed before it reaches the origin |
| Origin hiding | Clients see only the CDN's addresses; the origin can be firewalled to accept connections only from the CDN |
| **Web application firewall** and TLS termination | Most CDNs bundle a WAF, bot management, and certificate handling at the edge |

Concerns:

- **TLS is terminated at the CDN**, so the provider sees cleartext; the CDN-to-origin leg must be encrypted separately.
- **Third-party dependency**: a CDN outage or compromise affects every customer at once; a malicious or compromised CDN can alter content (**Subresource Integrity** hashes in HTML protect against altered scripts).
- **Stale content** after an update if cache invalidation is wrong, which matters for security fixes and revoked material.
- **Client-side CDNs** (peer-to-peer distribution, as in some game and update platforms) use the users' own machines as edge nodes, which raises integrity and consent questions.

## Satellite Communications

Satellite links provide connectivity where cables and cell towers do not reach: remote sites, ships, aircraft, rural broadband, and backup links.

- **Geostationary (GEO)** satellites sit at about 36,000 km: wide coverage, but **high latency** (around 500 to 600 ms round trip), which hurts interactive protocols and VPN handshakes.
- **Low Earth orbit (LEO)** constellations (Starlink and similar) are much closer: low latency and higher throughput, but require many satellites and ground terminals that track them.
- **Medium Earth orbit (MEO)** is in between and is where GPS lives.

Security points: a satellite downlink is a **broadcast** over a huge footprint, so anyone with a dish can receive it; unencrypted satellite traffic has been intercepted repeatedly. Encryption at a higher layer (VPN, TLS) is mandatory. **Jamming** and **GPS spoofing** are availability and integrity threats; the ground station and the provider's network are part of the trust chain.

## Cellular Networks

Mobile devices and increasingly fixed sites (branch backup, IoT) connect through cellular networks: **4G/LTE** and **5G**, with 2G/3G being retired.

- **5G** brings higher bandwidth, lower latency, **network slicing** (virtual networks with separate characteristics on shared infrastructure), and support for massive IoT density. It also moves more of the core to software and virtualization, with the same supply chain and SDN concerns.
- The **air interface is encrypted** between the handset and the tower, but that protection ends at the carrier. Traffic across the carrier's core and the internet is in whatever state the application left it, so sensitive traffic still needs TLS or a VPN.
- **Rogue base stations** (IMSI catchers, "stingrays") impersonate a tower to track devices or downgrade them to weaker legacy encryption. 5G reduces this with encrypted subscriber identifiers, but downgrade to 4G/2G remains the attacker's approach.
- **SIM swapping** at the carrier defeats SMS-based authentication; **SS7** signaling weaknesses allow interception and location tracking at the carrier level.
- Organizations usually cannot inspect cellular traffic from their devices, which bypasses the corporate perimeter; MDM and always-on VPN restore some control (see [[Mobile Device Security Features]]).

## Key Points

- **Edge networks process near the source for latency and resilience, at the cost of more locations and links to secure.**
- **A CDN caches content near users, absorbs DDoS, hides the origin, and usually terminates TLS, so the provider is a trusted third party.**
- **Satellite downlinks are broadcasts: encrypt above the link. GEO is high latency, LEO is low latency.**
- **Cellular encrypts only the air interface; rogue base stations, SIM swapping, and SS7 are the characteristic attacks, and 5G adds network slicing and a software-defined core.**
