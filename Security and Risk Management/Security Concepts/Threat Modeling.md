Threat modeling is a structured process for identifying, analyzing, and prioritizing threats to a system before they can be exploited. It shifts security thinking left — from reactive response to proactive design. See [[CIA Triad]], [[AAA Framework]], [[Defense in Depth]].

## Key Terminology

- **Asset** — anything of value that needs protection (data, systems, reputation).
- **Threat** — a potential event that could cause harm to an asset. Threats come from **threat actors**: nation-states, organized crime, hacktivists, insiders, or opportunists (script kiddies). Each has different motivations, capabilities, and targets.
- **Vulnerability** — a weakness that a threat can exploit.
- **Risk** — the likelihood that a threat exploits a vulnerability and the resulting impact. Risk = Threat × Vulnerability × Impact.
- **Attack Vector** — the path or method used to reach and exploit a vulnerability.

## Reduction Analysis

Before threats can be identified, the system must be decomposed into its components to understand the attack surface. Five things are mapped:

- **Trust boundaries** — where data crosses between zones of different trust levels
- **Dataflow paths** — how data moves through the system
- **Input points** — anywhere data enters, since every input is a place an attacker can reach
- **Privileged operations** — actions that run with elevated permissions, where the consequence of compromise is highest
- **Security stance and approach** — the assumptions the design already makes about what protects what

The last one is easy to skip and matters most. A decomposition that records the components but not the reasoning behind their protection produces a map with no legend — later reviewers cannot tell which exposures were accepted deliberately and which were never considered.

The output is a clear picture of where the system is exposed, which feeds directly into threat identification.

## Proactive and Reactive Modeling

Threat modeling can happen at two very different points in a system's life, and the timing changes what it can achieve.

- **Proactive (defensive)** — performed during design and development, before the system exists. Threats are addressed by changing the design, which is the cheapest point at which a flaw can be removed.
- **Reactive (adversarial)** — performed after a product has been built and deployed, often in response to an incident or a penetration test. The design is now fixed, so the available responses are compensating controls and patches rather than structural change.

Neither replaces the other. Proactive modeling catches design flaws; reactive modeling catches what the design assumptions got wrong once the system meets reality.

## Threat Modeling Process

1. **Define scope** — what system, component, or feature is being modeled?
2. **Decompose** — apply reduction analysis to map the attack surface
3. **Identify threats** — use a methodology (e.g., STRIDE) to enumerate threats per component
4. **Prioritize** — score threats by impact and likelihood (e.g., DREAD)
5. **Respond** — mitigate, transfer, accept, or avoid each threat based on priority

## Methodologies

**STRIDE** (Microsoft) — categorizes threats by type. Applied per component after reduction analysis:

| Threat                     | Violates        | Example                                     |
| -------------------------- | --------------- | ------------------------------------------- |
| **S**poofing               | Authentication  | Attacker impersonates a legitimate user     |
| **T**ampering              | Integrity       | Attacker modifies data in transit           |
| **R**epudiation            | Non-repudiation | User denies performing an action            |
| **I**nformation Disclosure | Confidentiality | Sensitive data exposed in error messages    |
| **D**enial of Service      | Availability    | Flood attack takes down a service           |
| **E**levation of Privilege | Authorization   | User gains admin rights they shouldn't have |

**PASTA** (Process for Attack Simulation and Threat Analysis) — a seven-stage, **risk-centric** methodology. Where STRIDE asks what could go wrong with a component, PASTA asks what is worth protecting and how much protection is proportionate: countermeasures are selected or developed in relation to the *value of the assets* being protected. This makes it the natural fit where security spending has to be justified against business impact.

**VAST** (Visual, Agile, and Simple Threat) — integrates threat and risk management into an Agile development environment on a scalable basis. Its design goal is breadth rather than depth: usable by many teams repeatedly inside an existing workflow, rather than as a separate security exercise a specialist runs occasionally.

**Attack trees** — model the paths to a single attacker goal as a branching structure, with the goal at the root and the means of achieving it below. Useful for reasoning about one high-value target in depth.

The four differ in what they are *for*: STRIDE categorizes, DREAD rates, PASTA weighs against asset value, and VAST scales across an organization.

## Prioritization & Response (DREAD)

DREAD scores each identified threat to determine response priority. Each dimension is rated 1–10:

| Factor | Question |
|---|---|
| **D**amage | How severe is the impact if exploited? |
| **R**eproducibility | How easily can the attack be repeated? |
| **E**xploitability | How much skill or effort does exploitation require? |
| **A**ffected users | How many users or systems are impacted? |
| **D**iscoverability | How easy is it to find the vulnerability? |

Average the five scores — higher total = higher priority. Responses follow the standard risk treatment options: mitigate, transfer, accept, or avoid.

## Non-Repudiation

Repudiation (the R in STRIDE) is countered by non-repudiation controls — ensuring a subject cannot deny an action they performed. Mechanisms: digital signatures, audit logs, timestamps. This is the forward reference from [[CIA Triad]] (Integrity pillar) and [[AAA Framework]] (Auditing step).
