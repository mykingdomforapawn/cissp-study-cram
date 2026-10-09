Secure design principles are the guidelines applied while a system is being architected, before any specific control is chosen. They decide the system's default posture: what it exposes, how it behaves when something breaks, and who it trusts. They complement the layered strategy in [[Defense in Depth]] and the objectives in [[CIA Triad]].

## Objects and Subjects

- **Subject** — the *active* entity that requests access to a resource. A user, a process, a service account, or a program acting on a user's behalf.
- **Object** — the *passive* entity that is accessed. A file, database, device, memory region, or network resource.

The roles are relative to the interaction, not fixed. A program is a subject when it opens a file, and an object when a user launches it. Every access control decision is the same question: *may this subject perform this action on this object?* Access control models, [[AAA Framework]], and later the formal security models are all built on this pairing.

### Transitive Trust

**Transitive trust** means trust that passes along a chain: if A trusts B, and B trusts C, then A ends up trusting C, even though A never made that decision. The trust extends to subjects A has never evaluated.

- It is convenient, because one relationship gives access across many domains (for example, trusts between domains or forests in a directory service, or a certificate chain back to a root CA).
- It is risky, because access can be granted indirectly and unintentionally. A compromise of C, or a weak link in the chain, reaches A.
- **Non-transitive** trust limits the relationship to the two parties directly involved, so each additional trust must be created deliberately.
- Zero trust rejects the idea outright, since every request is verified rather than inherited from a relationship.

## Closed and Open Systems

| | Open system | Closed system |
|---|---|---|
| **Built on** | Published, industry-standard interfaces | Proprietary interfaces and designs |
| **Interoperability** | High, components from many vendors work together | Limited, tied to one vendor or ecosystem |
| **Strength** | Flexibility, vendor choice, broad scrutiny of the standards | Smaller external surface, tighter control over every component |
| **Weakness** | Wider exposure and a larger pool of known attack techniques | Lock-in, and security that rests on few reviewers |

This is a separate axis from **open source vs closed source**, which is about whether the code is available for inspection. A system can be open (standards-based) yet built from closed-source components, or closed (proprietary) yet publish parts of its code.

Neither is inherently more secure. The related principle is that secrecy of design is not a control: **security through obscurity** is a weak foundation, and a design should remain secure even when an attacker knows how it works. This is the same reasoning as Kerckhoffs's principle for algorithms in [[Core Crypto Concepts]].

## Secure Defaults

Out of the box, a system should be in its most restrictive reasonable configuration, with users deliberately opting *in* to extra exposure rather than having to opt out.

- No default or well-known credentials; first use forces a new one.
- Unneeded services, ports, and features are off.
- Least privilege is the starting point for new accounts.
- Strong encryption and logging are on without being asked.

The reasoning is that most users never change defaults, so the default *is* the deployed configuration for most installations. A convenience-first default scales the same weakness across every customer. It is often summarized as **secure by design, secure by default, secure in deployment**.

## Fail Securely

When a system hits an error, crash, or unexpected state, it should end up in a secure state rather than an exposed one. Failure is inevitable, so what matters is which way the system falls.

| Mode | Behavior on failure | Priority | Example |
|---|---|---|---|
| **Fail-closed** (fail-secure) | Denies access, locks down | Confidentiality and integrity | A firewall that blocks all traffic when it crashes; a vault door that stays locked on power loss |
| **Fail-open** | Permits access, stays available | Availability | A network bypass that keeps a link up when the inspection device dies |
| **Fail-safe** | Moves to whatever state protects people from harm | Human safety | A fire exit that unlocks on power loss; equipment that shuts down rather than overheating |

No mode is always right. Where **human life** is at stake, safety wins, which usually means failing open for doors and exits (fail-safe). Where assets and data are at stake, the mechanism should fail closed. Fail-safe is a goal (nobody gets hurt) while fail-open and fail-closed describe the resulting access state, and the two can coincide. Sources use *fail-safe* and *fail-secure* loosely and sometimes interchangeably, so the context matters. Related practices are not leaking sensitive detail in error messages and not letting an exception skip an authorization check.

## Keep It Simple and Small

Also called **economy of mechanism** or **KISS**. Every added feature, line of code, and interaction is more to review, test, and defend.

- A smaller design has a smaller **attack surface**.
- Simple designs are easier to reason about, verify, and audit.
- Complexity hides flaws, and interactions between components are a common source of vulnerabilities.
- The approach is to include only what is needed, and to reduce or remove what is not (hardening, disabling unused features).

The trade-off is against functionality and flexibility: the secure choice is often the less featureful one.

Several named ideas express the same instinct:

- **DRY (Don't Repeat Yourself)** — each piece of logic lives in one place. A security check or fix is written once and reused, so there is no second copy to forget to patch.
- **YAGNI (You Aren't Gonna Need It)** — don't build features for hypothetical future needs. Unused code is attack surface that delivers no value.
- **Computing minimalism** — use the smallest set of components, services, and software that does the job, such as minimal OS installs and stripped-down containers.
- **New Jersey style ("worse is better")** — favor simplicity of design and implementation over completeness. A simple system that covers most needs and can be understood and fixed beats a complete but intricate one. It is named in contrast to the "do the right thing" approach, which prizes correctness and completeness even at the cost of complexity.

## Zero Trust

**Zero trust** removes the idea of a trusted internal network. The slogan is **"never trust, always verify"**. Location on the network grants nothing; every request is evaluated on its own.

- **Assume breach** — design as if the attacker is already inside, the same philosophy as in [[Defense in Depth]].
- **Verify explicitly** — authenticate and authorize every request using identity, device health, location, and context, not network position.
- **Least privilege** — grant only what the task needs, often just in time.
- **Micro-segmentation** — small isolated zones so a compromise cannot move laterally.
- **Continuous evaluation** — trust is re-assessed during a session, not granted once at login.

Architecturally it is described as a **control plane**, where a policy decision point decides based on identity and context, and a **data plane**, where a policy enforcement point allows or blocks the actual traffic. Zero trust is a strategy, not a single product.

An **air gap** is the opposite end of the spectrum: a system or network physically isolated, with no connection to other networks, so there is no path to verify or filter. It is used for the most sensitive systems (industrial control, classified networks). Zero trust assumes connectivity and controls it request by request, while an air gap removes the connectivity. An air gap is not absolute, since removable media, insiders, and side channels can still cross it.

## Trust but Verify

The older, perimeter-oriented posture. Entities inside the boundary (or those already vetted) are **trusted by default**, and verification happens afterward through monitoring, auditing, and logging to catch misuse.

| | Trust but verify | Zero trust |
|---|---|---|
| **Starting point** | Trusted unless shown otherwise | Untrusted until verified |
| **Verification** | After the fact (audit, review) | At every request |
| **Trust basis** | Network location, prior vetting | Identity, device, context |
| **Failure mode** | One breach of the perimeter exposes everything inside | A breach is contained to what the compromised identity can reach |

It still has a place where constant checking is impractical, such as dealing with a vetted partner or contractor, supported by detective controls ([[Vendor, Consultant, and Contractor Agreements]]). It is weak where the perimeter has dissolved through cloud, remote work, and mobile devices.

## Privacy by Design

Privacy is built into the system from the start rather than added afterward. It is associated with Ann Cavoukian, and its seven foundational principles are:

1. **Proactive, not reactive** — prevent privacy harm, don't remediate it after the fact.
2. **Privacy as the default** — personal data is protected without the individual taking action (the privacy equivalent of secure defaults).
3. **Privacy embedded into design** — part of the architecture, not a bolt-on.
4. **Full functionality** — positive-sum, not a trade of privacy against security or usability.
5. **End-to-end security** — protection across the whole data lifecycle, from collection to destruction.
6. **Visibility and transparency** — practices are open and verifiable.
7. **Respect for user privacy** — user-centric, with strong notice and choice.

It is applied through the **software development life cycle (SDLC)**: privacy requirements are set at the start, the design is reviewed through a privacy impact assessment, privacy is verified in testing, and retention and disposal are handled in maintenance and retirement. Raising it only at release is the reactive approach that the first principle rejects.

In practice it shows up as **data minimization**, purpose limitation, retention limits, and anonymization or pseudonymization. It underlies the "data protection by design and by default" obligation in GDPR (see [[Laws]]).

## Secure Access Service Edge (SASE)

**SASE** (pronounced "sassy") is a cloud-delivered architecture that converges **networking** and **network security** into one service, enforced close to the user or device wherever they are, rather than at a central data center.

- **Networking:** SD-WAN, for connectivity between sites, users, and clouds.
- **Security services:** secure web gateway (SWG), cloud access security broker (CASB), firewall as a service (FWaaS), and zero trust network access (ZTNA).

It exists because traffic no longer flows through one corporate perimeter: users are remote and applications sit in the cloud, so backhauling everything through a data center is slow and hard to protect. SASE moves the policy enforcement point out to the edge and ties access decisions to identity and context. In that sense it is the delivery model for [[#Zero Trust]].
