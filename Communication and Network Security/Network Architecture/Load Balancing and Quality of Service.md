## Load Balancing

A **load balancer** distributes incoming requests across a pool of servers. It serves **availability** (a failed server is taken out of rotation) and **scalability** (capacity grows by adding servers), which makes it a security control for the A in the CIA triad, not only a performance device.

It usually works at layer 4 (TCP/UDP, fast, protocol-agnostic) or layer 7 (HTTP-aware, able to route by URL or header and to terminate TLS). A layer 7 balancer terminating TLS becomes the place where certificates live and where traffic is briefly in cleartext — a sensitive point that also enables inspection and WAF functions.

## Virtual IP Addresses

A **virtual IP (VIP)** is the single address clients connect to, which is not bound to one physical server. The load balancer owns the VIP and relays each connection to a **real server** in the pool.

Consequences:

- Clients and DNS know **one stable address**; servers can be added, patched, or removed behind it without anyone noticing.
- The VIP also **hides the internal addressing** of the server farm, in the same way NAT hides a client network.
- A VIP can likewise float between **two devices** in a failover pair: the standby claims the VIP (via gratuitous ARP or a protocol such as VRRP/HSRP) when the active one dies. This is how router and firewall redundancy works too.

## Active-Active vs Active-Passive

| | **Active-active** | **Active-passive** (active-standby) |
|---|---|---|
| **Normal state** | All nodes carry traffic simultaneously | One node carries all traffic; the other waits |
| **Capacity** | Sum of all nodes — but if sized at 100% and one fails, the survivors are overloaded | Capacity of one node; the standby is idle investment |
| **Failover** | Traffic simply stops going to the failed node; effectively instant | Standby must **detect failure and take over** (VIP, state, sometimes storage) — a brief outage |
| **Complexity** | Higher: shared or synchronized state, session affinity, split-brain risk | Lower: only one node is authoritative |
| **Typical use** | Web and application tiers, stateless workloads | Firewalls, databases, anything where two writers would corrupt state |

**Active-active must be sized for failure** (N+1, not N). Its characteristic failure is **split-brain**: both nodes believe they are active after losing contact with each other, addressed with quorum or a separate heartbeat path.

## Scheduling and Persistence

**Scheduling algorithms** decide which server gets the next request: **round robin** (in turn), **weighted round robin** (by server capacity), **least connections** (to the least busy), **least response time**, **source IP hashing** (same client to the same server), and **random**.

**Session persistence (affinity, sticky sessions)** keeps a client on one server when the application holds session state locally. It is a crutch: it limits balancing quality and concentrates a user's exposure on one node. The better design keeps session state in a shared store so any server can answer.

**Health checks** are what make the whole thing work: the balancer must probe the servers (TCP connect, HTTP response, application-level check) and remove failures from rotation. A health check that only tests whether the port is open will keep sending traffic to a broken application.

Related ideas: **DNS round robin** is primitive balancing with no health awareness; a **CDN** balances geographically (see [[Edge Networks and CDNs]]); **clustering** is load balancing plus shared state between the nodes.

**The balancer itself is a single point of failure** and a high-value target — it sees all traffic, often holds the TLS keys, and is the obvious DDoS target. It is deployed in pairs.

## Quality of Service

**QoS** manages a network's limited capacity by treating traffic differently instead of equally. It exists because some applications tolerate degradation and others do not.

The measures that define what an application needs, and what a QoS investigation looks at:

- **Bandwidth** — capacity available to the flow; **throughput** (bit rate) is what is actually achieved, which is always less.
- **Latency** — delay end to end, of which **transmission delay** is the part spent putting bits on the wire.
- **Jitter** — **variation** in latency, which destroys real-time audio and video even when average latency is fine.
- **Packet loss** — dropped packets; TCP retransmits, real-time traffic cannot.
- **Interference** and **signal-to-noise ratio** — on wireless and on poorly shielded copper, the physical causes behind loss and retransmission (see [[Transmission Media]]).
- **Availability** — the link being there at all.

Voice and video need low latency, low jitter, and low loss but little bandwidth; a backup job needs huge bandwidth but tolerates any delay. QoS lets both share one link. When users report dropped connections and data loss, these are the measures to investigate — not system uptime, OS versions, or which application protocol is in use.

**Mechanisms**: **classification and marking** of packets (DSCP at layer 3, CoS at layer 2), **queuing and prioritization** per class, **traffic shaping** (buffering to smooth a flow to a rate) and **policing** (dropping what exceeds it), **congestion avoidance**, and **bandwidth reservation**.

**Why it is a security topic:**

- **Availability is part of security**, and QoS is the control that keeps critical traffic working under contention — including a partial denial-of-service condition.
- **Markings are trust-based**: a host can mark its own traffic as highest priority, so an attacker (or a user with a misbehaving application) can **starve** others unless the network **re-marks or rejects markings at the edge**. Trust DSCP only from devices you control.
- **Prioritization decisions are policy**: which business functions get capacity in a degraded state belongs with continuity planning, not with whoever configures the switch.

## Key Points

- **A load balancer is an availability and scalability control; a VIP is the single client-facing address that hides and abstracts the real servers.**
- **Active-active uses all nodes (more capacity, must be sized for failure, split-brain risk); active-passive keeps a standby that must detect failure and take over the VIP.**
- **Scheduling: round robin, weighted, least connections, source hashing. Persistence pins a client to one server; health checks remove dead servers.**
- **QoS manages bandwidth, latency, jitter, and packet loss; jitter is what kills voice and video.**
- **Markings are only trustworthy from controlled devices — re-mark at the edge or traffic can be prioritized by the sender.**
