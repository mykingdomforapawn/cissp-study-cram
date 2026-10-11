Security is cheaper and more effective when it is part of the system's whole life rather than something added near the end. The **systems lifecycle** (as in ISO/IEC/IEEE 15288 and NIST SP 800-160) divides that life into stages, and each stage has its own security activity. It applies the proactive stance of [[Secure Design Principles]] (including privacy by design) to the whole system. Stage names vary between standards, and the order may repeat when a system is iterated.

| Stage | Purpose | Security focus |
|---|---|---|
| **Stakeholder needs and requirements** | Identify what the system must do and who it serves | Business objectives, regulatory and compliance needs, risk appetite, data sensitivity |
| **Requirements analysis** | Turn needs into specific, testable requirements | Explicit security and privacy requirements, with controls selected from the requirements (see [[Security Evaluation and Authorization]]) |
| **Architectural design** | Define the structure and how components interact | Apply the design principles (least privilege, secure defaults, defense in depth), threat modeling, boundaries, and trust relationships |
| **Development and implementation** | Build the components | Secure coding, code review, dependency and supply chain control, and protection of the build pipeline |
| **Integration** | Combine components into the working system | Check the interfaces and interconnections (see composition in [[Security Model Fundamentals]]), and ensure the integrated whole behaves securely |
| **Verification and validation** | Confirm it was built right and is the right system | Security testing, penetration testing, and evaluation, which supply the assurance for authorization |
| **Transition and deployment** | Move into the production environment | Secure configuration and hardening, baselines, change control, and the authorization to operate |
| **Operations and maintenance (sustainment)** | Run, monitor, and support it | Patching, monitoring, incident response, and continual assessment, with reauthorization when things change |
| **Retirement and disposal** | Decommission it | Secure data sanitization and destruction, key and account revocation, and archiving of what must be retained |

## Key Points

- **Verification vs validation.** Verification asks whether the system meets its specified requirements (built right). Validation asks whether it meets the stakeholders' actual needs (the right thing built).
- **Early is cheaper.** A flaw found in requirements or design costs far less to correct than one found in operation, which is why security requirements and threat modeling come at the start.
- **Requirements drive traceability.** Each control should trace back to a requirement and each requirement to a stakeholder need, so that nothing is built without a reason and nothing needed is missing.
- **The end is part of the lifecycle.** Disposal is often neglected, but data left on retired hardware is a common exposure. See [[Data Protection Methods]] and [[Information and Asset Handling Requirements]] for sanitization and handling.
- **It is continuous.** Operations feeds back into earlier stages: new threats, changes, and incidents prompt revised requirements and design.
