## Distributed Systems

A **distributed system** is a set of independent computers, connected by a network, that cooperate so as to appear as one system. Web applications, distributed databases, cloud platforms, and the grid and peer-to-peer designs in [[Server-Based Systems]] are all examples.

They share no memory and coordinate by passing messages, so work is concurrent and **parts can fail independently**.

**Concerns:**
- **Network exposure.** All coordination crosses a network, so it needs authentication and encryption between nodes.
- **Consistency.** Several nodes holding copies of data must stay in sync, and a trade-off arises between consistency and availability when nodes cannot reach each other.
- **Interconnectedness.** The tight linkage of components is the defining concern of a distributed computing environment (DCE): an error or malware spreads easily, and an attacker who compromises one component can pivot and move laterally to the others. Unlike authentication or access weaknesses, it cannot be designed away without abandoning the distributed design, so it is contained with segmentation and least privilege between nodes.
- **Many trust boundaries.** Each node and link is a potential entry point, and compromise of one must not give access to all.
- **Visibility.** Logs are scattered, so they need central collection and consistent time.

**Controls:** mutual authentication, encryption in transit, least privilege per node, centralized logging, and redundancy to remove single points of failure.

## High-Performance Computing (HPC)

**HPC** combines the power of many processors, typically in a cluster or supercomputer, with fast interconnects and shared storage to solve very large problems such as weather and climate modeling, scientific simulation, genomics, and AI training. It is the most demanding form of the large-scale parallel systems in [[Server-Based Systems]].

**Concerns:**
- **Valuable data and research**, which attracts attackers, including state-backed ones.
- **Performance over security.** Encryption and monitoring cost speed, so internal controls are often relaxed.
- **Many users with broad access.** Researchers share the system and run their own code, so jobs and users must be isolated from each other.
- **Misuse of resources**, such as cryptomining on a compromised account.
- **Patching is disruptive** when jobs run for days or weeks.

**Controls:** separate management, compute, and storage networks, MFA on the login nodes, job and user isolation, monitoring for unusual usage, and least-privilege access to data.

## Key Points

- **Distributed systems** are independent nodes acting as one. The main risk is interconnectedness (malware propagation and lateral movement), along with network trust, consistency, and scattered visibility.
- **HPC** is parallel computing at the largest scale, where the security tension is performance versus protection.
