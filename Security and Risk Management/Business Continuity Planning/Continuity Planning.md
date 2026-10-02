The third element of BCP (see [[BCP vs DRP]]) turns BIA priorities into actual recovery capability. It has two parts: **strategy development** — deciding, for each critical function, whether to mitigate the risk, accept it, or build a continuity strategy to meet its RTO/MTD (see [[Business Impact Analysis]]) — and **provisions and processes** — implementing the people, facilities, and technology needed to execute that strategy.

Common continuity strategies:

- **Alternate sites** — facilities to fail over to when a primary site is unavailable:
	- **Hot site** — fully equipped and near-live, fastest to activate, most expensive
	- **Warm site** — partially equipped, requires some setup and data restoration
	- **Cold site** — bare facility with power/space only, cheapest but slowest to activate
- **Personnel continuity** — succession planning and cross-training so critical roles aren't single points of failure
- **Communications continuity** — backup channels to reach staff, customers, and partners when primary systems are down
- **Alternative systems** — redundant components (e.g., a second communications circuit) that take over when the primary fails; one of several general provision categories alongside hardening a system or reducing its exposure

This is also where DRP-specific technical recovery procedures (backups, system restoration, failover) plug into the broader plan — DRP delivers the "how" for the systems a continuity strategy depends on.
