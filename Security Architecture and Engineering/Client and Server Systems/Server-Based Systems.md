Servers hold the data and run the services that clients use. Because they concentrate both, a server is a more valuable target than any one client, and the security question is how to protect them when the work is spread over many machines. Three distributed designs are the topic here: large-scale parallel systems, grid computing, and peer-to-peer. They differ mainly in how tightly coupled the nodes are and who controls them.

## Large-Scale Parallel Data Systems

A **large-scale parallel system** splits one big problem over many processors or **nodes** that work on it at the same time, then combines the results. Examples are **clusters**, **massively parallel processing (MPP)** systems (see [[Processors]]), supercomputers, and big-data frameworks such as Hadoop and Spark.

- Nodes are usually owned by one organization, close together, and connected by a fast network.
- Data and processing are distributed and often replicated, so it is hard to say where a piece of data is at any moment (see [[Data Localization and Sovereignty]]).

**Security concerns:**
- **Integrity and consistency.** Many nodes updating shared data need synchronization, or results become inconsistent (race conditions).
- **Large attack surface.** A flaw or weak node exposes the data it holds, and compromised nodes can corrupt results.
- **Authentication and trust between nodes.** Nodes and the jobs sent to them must be authenticated, and the internal traffic protected.
- **Aggregated data.** Big pools of data combine into more sensitive information, and are an attractive target.
- **Access control and logging at scale** are harder than on a single system, and encryption adds overhead.
- **Availability.** Node failures are expected, so the system must tolerate them (see [[Security Capabilities of Information Systems]]).

## Grid Computing

**Grid computing** links many computers into a loosely coupled virtual supercomputer, using their **spare processing capacity**. The nodes are heterogeneous, geographically scattered, often owned by different organizations or volunteers, and connected over the internet. A coordinator divides a task into **work units**, sends them to nodes, and collects the results. Examples are SETI@home and Folding@home.

Unlike a cluster, there is **no single owner or administrative domain**, and nodes can join and leave at will.

**Security concerns:**
- **Untrusted nodes.** A node can return false results, and can see the data in its work unit.
- **Loss of data privacy.** Grid members can usually read the work segments they are given, so sensitive data should not be sent to nodes the organization does not control. Grid computing copes with latency, duplicate work, and fluctuating capacity, but not with this.
- **Integrity of results.** There is no guarantee a returned result is correct.
- **No central policy enforcement.** Participants' systems may be insecure or compromised.
- **Availability.** Nodes are unreliable, and may drop out mid-task.

**Controls:** send the same work unit to several nodes and compare the results, sign work units and results, authenticate participants, run work inside sandboxes or VMs, and keep sensitive data out of the grid.

## Peer-to-Peer (P2P)

In a **peer-to-peer** network, every participant is both client and server, sharing resources directly with the others, with **no central server**. Examples are BitTorrent file sharing and blockchain networks. Legitimate uses include software distribution and content delivery, and some botnets use P2P for command and control.

**Security concerns:**
- **Malware** hidden in shared files, and no authority vouches for what is downloaded.
- **Data leakage.** Misconfigured clients share folders, and sensitive files leave the organization.
- **Illegal content and copyright** violations, with the organization's network and liability involved.
- **Bandwidth use** and unmanaged inbound connections that bypass perimeter controls.
- **No central control or logging**, so it is hard to monitor or take down.

**Controls:** policy prohibiting unapproved P2P software, blocking protocols and ports at the firewall, application allow lists, DLP and egress monitoring, and verifying downloads against published hashes (see [[Hashing Algorithms]]).

## Comparison

| | Parallel system / cluster | Grid | Peer-to-peer |
|---|---|---|---|
| **Coupling** | Tight, fast local network | Loose, over the internet | Loose, over the internet |
| **Ownership** | One organization | Many owners or volunteers | Many individual participants |
| **Nodes** | Usually uniform | Heterogeneous | Heterogeneous |
| **Control** | Central | A coordinator, but nodes are not controlled | None |
| **Purpose** | One large computation or dataset | Borrowed computing power for a task | Direct sharing of files or resources |
| **Main risk** | Scale, integrity, aggregated data | Untrusted nodes and results | Malware, leakage, no control |

## Key Points

- **Parallel systems share work across nodes you own.** The risks are scale, consistency, and concentrated data.
- **Grid computing borrows spare capacity from nodes you don't control.** The key problem is trusting the nodes and their results, handled by redundancy and keeping sensitive data out.
- **P2P has no server and no central control**, so the risks are malware, leakage, and legal exposure.
- **The less control over the nodes, the less you can trust them.**
