---
tags:
  - anki
---
Anki cards for the Security Concepts notes. Format: `cards/CLAUDE.md`.

---

## Card 1

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A system requires users to enter a password and then answer a preconfigured security question before access is granted. A reviewer objects to the vendor describing this as multi-factor authentication. Why is the reviewer correct?

**Options**
*A password and a security question are both something the user knows, so only one factor type is in use — MFA requires factors drawn from different types.
Security questions are too easily researched to count as an authentication factor — a real weakness, but the classification problem is the factor type.
Multi-factor authentication requires at least three factors — two factors of different types is sufficient.
Multi-factor authentication requires a biometric factor — any two distinct factor types qualify.

**Source**
[[AAA Framework]]

## Card 2

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
Two analysts hold identical security clearances. One works on Project A and one on Project B, and neither can open the other's files. Which principle is being enforced?

**Options**
*Need-to-know — clearance grants eligibility, while need-to-know limits access to the data relevant to the current role or task.
Least privilege — grants the minimum permissions required for a job; the restriction between equally cleared subjects is specifically need-to-know.
Separation of duties — splits a sensitive process across people so no one can complete it alone.
Mandatory access control — an enforcement model that might implement this, not the principle being described.

**Source**
[[AAA Framework]]

## Card 3

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
After an incident, an employee denies having deleted a production file. The organization wants to be able to prove otherwise in future disputes. Which property must its controls provide, and which AAA step primarily supports it?

**Options**
*Non-repudiation, supported primarily through auditing — a detailed, attributable event trail prevents a subject denying an action.
Confidentiality, supported through authentication — verifying identity restricts access but proves nothing about what a subject did.
Integrity, supported through authorization — authorization determines what is permitted, not what actually occurred.
Availability, supported through accounting — accounting reviews logs for compliance and has no bearing on availability.

**Source**
[[AAA Framework]]

## Card 4

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A payment processor requires that transaction records cannot be altered undetected, and accepts added latency in its approval workflow to achieve it. Which pillar is being prioritized, and at whose expense?

**Options**
*Integrity, at the expense of availability — approval workflows and write locks protect accuracy while adding friction and delay.
Confidentiality, at the expense of availability — the stated concern is alteration of records, not disclosure of them.
Availability, at the expense of integrity — the trade-off is described in the opposite direction.
Integrity, at the expense of confidentiality — the added latency affects timely access, not secrecy.

**Source**
[[CIA Triad]]

## Card 5

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
An attacker exfiltrates a customer database and publishes it online. The data itself was not modified or deleted. In DAD terms, which failure has occurred, and which CIA pillar failed to hold?

**Options**
*Disclosure, from a failure of confidentiality — confidentiality is the pillar that prevents disclosure.
Alteration, from a failure of integrity — nothing indicates the data was modified.
Destruction, from a failure of availability — the data was copied, not made unavailable.
Disclosure, from a failure of integrity — integrity prevents alteration; confidentiality is what prevents disclosure.

**Source**
[[CIA Triad]]

## Card 6

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
To improve resilience, an architecture team proposes replicating a sensitive dataset into three additional regions. What is the <b>PRIMARY</b> security trade-off?

**Options**
*Improved availability enlarges the attack surface for disclosure — every additional copy is another location where the data must be protected.
Improved availability weakens integrity because replicas will inevitably diverge — a consistency design problem rather than the primary security trade-off.
Improved confidentiality reduces availability because each replica must be separately access-controlled — the direction of the trade-off is reversed.
There is no security trade-off, since replication only adds redundancy — every additional copy is an additional exposure to manage.

**Source**
[[CIA Triad]]

## Card 7

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
An organization runs the same vendor's firewall product at both its internet perimeter and its internal segmentation boundary, on the grounds that a single vendor simplifies operations. What is the <b>PRIMARY</b> security concern?

**Options**
*One vulnerability in that product bypasses both layers at once — the layers are not independent, so the defence is far shallower than the architecture suggests.
Running two instances of the same product doubles the licensing and patching workload — an operational cost, not a security weakness.
Perimeter and internal boundaries require fundamentally different filtering technologies — the same class of product can legitimately serve both.
Attackers preferentially target the most widely deployed firewall vendors — market share affects likelihood but is not the structural flaw.

**Source**
[[Defense in Depth]]

## Card 8

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A security architect insists that a customer database be encrypted at rest and require its own authentication, even though it already sits behind a firewall, a segmented network, and hardened endpoints. Which principle <b>BEST</b> supports this position?

**Options**
*Assume breach — each inner layer is designed as though every outer layer has already failed, so no single layer is trusted to hold.
Least privilege — concerns the permissions granted to subjects rather than the layering of controls.
Separation of duties — splits a process across people and is unrelated to control layering.
Vendor diversity — avoids a shared flaw across layers, a different aspect of defence in depth.

**Source**
[[Defense in Depth]]

## Card 9

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A critical vulnerability is disclosed in a widely used logging library. Days later the security team still cannot say which of its several hundred applications include the affected component. What would <b>MOST</b> directly address this?

**Options**
*Maintaining a software bill of materials for each application — a component inventory is what makes rapid exposure assessment possible.
Increasing the frequency of vulnerability scanning — scanners find what they have signatures for and routinely miss embedded library versions.
Requiring vendors to warrant that their software is free of vulnerabilities — an unenforceable warranty that produces no inventory.
Deploying a web application firewall to virtually patch the flaw — mitigates exploitation but still does not reveal where the component is.

**Source**
[[Supply Chain Risk Management]]

## Card 10

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
Two organizations want to record a shared intention to collaborate on a research initiative. Neither wants enforceable obligations at this stage. Which instrument fits?

**Options**
*A memorandum of understanding — records shared intent and expectations without being binding.
A service level agreement — binding, and defines measurable service levels and remedies.
A business partnership agreement — binding, and sets out formal partnership terms.
An interconnection security agreement — binding, and governs the security of directly interconnected systems.

**Source**
[[Supply Chain Risk Management]]

## Card 11

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A government agency and a contractor are establishing a permanent dedicated network link between their environments. Which agreement specifically governs the security requirements of that connection?

**Options**
*An interconnection security agreement — governs the security requirements for systems that directly interconnect.
A service level agreement — defines expected service levels rather than the security of an interconnection.
A master services agreement — governs the overall commercial relationship between the parties.
A non-disclosure agreement — protects the confidential information exchanged, not the security of the link itself.

**Source**
[[Supply Chain Risk Management]]

## Card 12

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A device manufacturer needs assurance that firmware has not been tampered with between manufacturing and boot, verified before the operating system loads. Which mechanism provides this?

**Options**
*A silicon root of trust — a hardware-anchored mechanism that validates firmware integrity before the operating system loads.
A physically unclonable function — derives a unique hardware fingerprint to verify chip authenticity, addressing counterfeiting rather than boot integrity.
A software bill of materials — inventories software components and plays no part in boot-time verification.
Full-disk encryption — protects data at rest and does not validate the boot chain.

**Source**
[[Supply Chain Risk Management]]

## Card 13

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
During threat modelling, a team finds that a user could perform a high-value transaction and later credibly deny having done so, because the application's logs do not attribute actions to individual accounts. Which STRIDE category is this?

**Options**
*Repudiation — the threat that a user denies performing an action, countered by non-repudiation controls such as attributable audit logs.
Spoofing — impersonating another identity, which violates authentication.
Tampering — unauthorized modification of data, which violates integrity.
Information disclosure — exposure of sensitive data, which violates confidentiality.

**Source**
[[Threat Modeling]]

## Card 14

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A team has agreed the scope of a threat model: a new payment service and its integrations. Before enumerating threats with STRIDE, what should they do <b>FIRST</b>?

**Options**
*Decompose the system through reduction analysis — mapping trust boundaries, data flows, entry and exit points, and privileged code is what makes per-component threat enumeration possible.
Score the known threats with DREAD to establish priority — prioritization comes after threats have been identified.
Reuse the threat list from a comparable service already in production — skips the analysis specific to this system's attack surface.
Define the security requirements the service must meet — requirements follow from understanding the threats, not the other way round.

**Source**
[[Threat Modeling]]

## Card 15

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
Twenty-three threats have been identified for a system and the team can only address a subset before release. Which technique is designed to establish the order in which they are addressed?

**Options**
*DREAD — rates each threat on damage, reproducibility, exploitability, affected users, and discoverability to produce a priority ordering.
STRIDE — categorizes threats by type and does not rank them.
Reduction analysis — decomposes the system to map the attack surface, before threats are identified at all.
An attack tree — models the paths towards a single goal rather than prioritizing a set of threats.

**Source**
[[Threat Modeling]]

## Card 16

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A user types their email address into a login form and the system displays a password prompt. At this point in the sequence, what has the user actually done?

**Options**
*Made an identity claim through identification — the claim has been asserted but nothing has yet been proven.
Completed authentication — authentication is the subsequent step, where the claim is verified against something the user knows, has, or is.
Received authorization — authorization determines permitted actions and only follows successful authentication.
Generated an accounting record — accounting reviews logged activity to hold subjects accountable, well after this point.

**Source**
[[AAA Framework]]

## Card 17

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A network team needs a AAA protocol for administrative access to routers and switches, and specifically wants authentication, authorization, and accounting handled as independent steps so that command-level authorization can be controlled separately. Which protocol fits?

**Options**
*TACACS+ — separates authentication, authorization, and accounting into independent steps, which supports granular command authorization for device administration.
RADIUS — combines authentication and authorization, and is oriented towards network access such as VPN and wireless.
Kerberos — an authentication protocol for network services rather than a device administration AAA protocol.
LDAP — a directory access protocol used as an identity source, not a AAA protocol in itself.

**Source**
[[AAA Framework]]

## Card 18

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
An intelligence agency and a hospital emergency department each ask which pillar of the triad their architecture should favour when a trade-off is unavoidable. What is the correct answer for each?

**Options**
*Confidentiality for the agency and availability for the hospital — disclosure of secrets causes the greatest harm in intelligence work, while emergency systems must be reachable when lives depend on them.
Integrity for the agency and availability for the hospital — integrity dominates in financial systems, where altered transaction data is the catastrophic outcome.
Confidentiality for both — a hospital holds sensitive records, but an unreachable emergency system is the more severe failure.
Availability for both — an intelligence system that stays up while leaking secrets has failed at its primary purpose.

**Source**
[[CIA Triad]]

## Card 19

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A manufacturer sources a specialized component from a single supplier at a favourable price. The security team raises a supply chain concern that has nothing to do with the component's technical integrity. What is it?

**Options**
*Single-source dependency creates a single point of failure — a disruption at that one supplier halts production with no alternative available.
The supplier may insert a hardware implant during manufacturing — a genuine supply chain risk, but one concerning the component's integrity.
The component may be counterfeit and fail prematurely — again an integrity concern rather than a dependency concern.
The supplier's firmware may not support a silicon root of trust — a technical integrity property of the component itself.

**Source**
[[Supply Chain Risk Management]]

## Card 20

**Domain**
1 — Security and Risk Management / Security Concepts

**Question**
A defence contractor must be able to confirm that chips arriving from a distributor are genuine and not cloned substitutes, using a property that cannot be copied even by a sophisticated counterfeiter. Which mechanism provides this?

**Options**
*A physically unclonable function — exploits unique manufacturing variations in silicon to produce a hardware fingerprint that cannot be cloned.
A silicon root of trust — validates firmware integrity before the operating system loads, addressing boot integrity rather than chip authenticity.
A software bill of materials — inventories software components and says nothing about the authenticity of hardware.
A tamper-evident shipping seal — reveals interference in transit but cannot establish that the chip inside was genuine to begin with.

**Source**
[[Supply Chain Risk Management]]
