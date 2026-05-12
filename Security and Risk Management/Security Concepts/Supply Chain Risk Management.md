Supply Chain Risk Management (SCRM) is the process of identifying, assessing, and mitigating security risks introduced through third-party vendors, suppliers, hardware manufacturers, and service providers. The core concern: every external dependency is a potential attack vector outside your direct control. See [[Organizational Security Processes]], [[Security Control Frameworks]], [[Security Governance & Management]].

## Key Risks

**Hardware Risks**
- **Counterfeit components** — fake hardware that may fail prematurely or contain backdoors
- **Firmware/BIOS tampering** — malicious code inserted during manufacturing or shipping
- **Hardware implants** — physical modifications to intercept or manipulate data
- **Silicon Root of Trust** — a hardware-anchored verification mechanism (typically a dedicated chip) that validates firmware integrity before the OS loads, ensuring the boot chain hasn't been tampered with
- **Physically Unclonable Function (PUF)** — exploits unique manufacturing variations in silicon to create a hardware "fingerprint" that cannot be cloned, used to verify chip authenticity and counter counterfeiting

**Software Risks**
- **Compromised open source libraries** — malicious code injected into widely-used dependencies (e.g., Log4Shell)
- **Malicious updates** — legitimate update mechanisms hijacked to distribute malware (e.g., SolarWinds)
- **Backdoors in commercial software** — intentional or coerced vulnerabilities introduced by the vendor
- **SBOM (Software Bill of Materials)** — a complete inventory of all components, libraries, and dependencies in a software product. Enables rapid exposure assessment when a vulnerability is disclosed in a component. Increasingly required by regulation (US Executive Order 14028).

**Vendor Access Risks**
- Third parties with privileged access to internal systems are an extension of your attack surface
- A breach at a vendor can cascade directly into your environment

## Vendor Agreements

Formal agreements define security expectations with third parties. Knowing which applies in which scenario is heavily tested:

| Agreement | Binding? | Purpose |
|---|---|---|
| **SLA** (Service Level Agreement) | Yes | Defines expected service levels, uptime, and security requirements |
| **MOU** (Memorandum of Understanding) | No | Documents shared intent and expectations between parties |
| **NDA** (Non-Disclosure Agreement) | Yes | Protects confidential information shared with the vendor |
| **ISA** (Interconnection Security Agreement) | Yes | Governs security requirements for systems that directly interconnect |
| **BPA** (Business Partnership Agreement) | Yes | Formal terms of a business partnership, may include security obligations |

## Risk Controls

- **Due diligence in vendor selection** — vet vendors before engagement: review security posture, certifications, audit history. See [[Organizational Security Processes]].
- **Minimum security requirements** — define a baseline (see [[Security Governance & Management]]) that all vendors must meet as a condition of engagement
- **Third-party audits and SOC reports** — independent verification that vendor controls work as claimed
- **End-of-life management** — unsupported hardware or software in the supply chain introduces unpatched vulnerabilities with no remediation path; must be tracked and replaced
- **Single-source dependency** — relying on one supplier creates a single point of failure; diversification reduces supply chain disruption risk
