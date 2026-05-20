Risk management is a continuous process with four activities: *risk assessment* (identifying assets, threats, and vulnerabilities), *risk analysis* (quantifying or qualifying the resulting risk), *risk response* (deciding what to do about it), and *risk awareness* (keeping stakeholders informed so decisions are grounded in shared understanding of exposure). See [[Threat Modeling]] for the foundational vocabulary these build on.

## Terminology

- **Asset** — anything of value to the organization (data, systems, reputation, people).
- **Asset Valuation** — quantifying that value: replacement cost, revenue impact, regulatory consequence.
- **Threat** — a potential event that could cause harm to an asset.
- **Threat Agent** — the actor behind a threat (person, group, system, or natural force).
- **Threat Event** — a specific instance of a threat materializing.
- **Threat Vector** — the path or method a threat agent uses to reach a target.
- **Vulnerability** — a weakness that a threat can exploit.
- **Exposure** — the condition of being open to loss if a threat materializes.
- **Risk** — the probability that a threat exploits a vulnerability, combined with the resulting impact.
- **Safeguard** — a control that reduces risk; also called countermeasure or control.
- **Attack** — a deliberate act that attempts to exploit a vulnerability.
- **Breach** — a successful unauthorized access or data loss event.
- **Hazard** — a condition that increases the likelihood or impact of a threat (e.g., running unpatched software).

## Asset Valuation

Before risk can be assessed, assets must be valued — this determines what gets protected and how much investment is justified. Valuation factors:

- **Replacement/purchase cost** — what it costs to rebuild or rebuy
- **Productivity impact** — revenue or output lost if the asset is unavailable
- **Competitive advantage** — value of proprietary data, IP, or processes
- **Legal and regulatory liability** — fines, penalties, or litigation exposure if the asset is compromised
- **Reputation** — customer trust and brand damage (hard to quantify but often the largest consequence)

Tangible assets (hardware, data) can often be valued directly. Intangible assets (reputation, trade secrets) require estimation. The output doesn't need to be a precise dollar figure — it needs to be consistent enough to prioritize one asset over another.

## Identifying Threats and Vulnerabilities

Once assets are valued, build a comprehensive list of what could threaten them. Cover both axes:

- **Source**: internal (employees, misconfiguration) vs. external (attackers, partners, regulators)
- **Nature**: human/deliberate, human/accidental, and natural/environmental

For threats, NIST SP 800-30 provides structured threat-source and threat-event tables — a useful starting point rather than building from scratch. MITRE ATT&CK covers adversary techniques in more detail when the threat landscape is well-defined.

Vulnerabilities are identified in parallel: patch levels, configuration gaps, process weaknesses, and physical exposures. The goal at this stage is completeness — a threat or vulnerability missed here never gets assessed or treated.

## The Risk Cycle

Threat agents exploit vulnerabilities in assets → creating risk → if unaddressed, risk materializes as an attack → leading to breach or loss → safeguards are applied → reducing risk to a residual level → new threats and environmental changes restart the cycle.

The cycle never terminates. Risk management is an ongoing program, not a one-time assessment. This is the principle of **continuous improvement** — the threat landscape, business environment, and control effectiveness all change over time, so assessments and treatments must be revisited regularly. A risk accepted last year may be unacceptable today.

## Asset-Focused vs. Threat-Focused Approaches

Both approaches converge on the same output — a prioritized risk picture — but the starting point shapes what you find.

**Asset-focused**: inventory and value assets first, then identify what threatens each one. Suits organizations protecting specific high-value targets (e.g., a financial institution protecting customer data).

**Threat-focused**: profile threat agents and events first, then determine which assets they would target. Suits environments with a well-defined threat landscape (e.g., critical infrastructure facing sector-specific adversaries).
