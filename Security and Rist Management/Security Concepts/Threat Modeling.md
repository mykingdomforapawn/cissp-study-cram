Threat modeling is a structured process for identifying, analyzing, and prioritizing threats to a system before they can be exploited. It shifts security thinking left — from reactive response to proactive design. See [[CIA Triad]], [[AAA Framework]], [[Defense in Depth]].

## Key Terminology

- **Asset** — anything of value that needs protection (data, systems, reputation).
- **Threat** — a potential event that could cause harm to an asset. Threats come from **threat actors**: nation-states, organized crime, hacktivists, insiders, or opportunists (script kiddies). Each has different motivations, capabilities, and targets.
- **Vulnerability** — a weakness that a threat can exploit.
- **Risk** — the likelihood that a threat exploits a vulnerability and the resulting impact. Risk = Threat × Vulnerability × Impact.
- **Attack Vector** — the path or method used to reach and exploit a vulnerability.

## Reduction Analysis

Before threats can be identified, the system must be decomposed into its components to understand the attack surface. This involves mapping:
- **Trust boundaries** — where data crosses between zones of different trust levels
- **Data flows** — how data moves through the system
- **Entry and exit points** — anywhere input enters or output leaves
- **Privileged code** — components that run with elevated permissions

The output is a clear picture of where the system is exposed, which feeds directly into threat identification.

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

Other methodologies (PASTA, Attack Trees, VAST) exist but are less central — STRIDE is the primary one for CISSP.

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
