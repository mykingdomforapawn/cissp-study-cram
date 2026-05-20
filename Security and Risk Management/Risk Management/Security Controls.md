Controls are selected after risk response decisions to treat identified risks. They are classified by *category* (what the control is) and *function* (what it does). Most real-world controls span multiple functions. See [[Risk Response]] for how treatment decisions drive control selection and [[Defense in Depth]] for how controls layer together.

## Categories

- **Administrative** — policies, procedures, standards, training, background checks, separation of duties, job rotation. Management-level controls that govern behavior.
- **Technical/Logical** — access control systems, encryption, firewalls, IDS/IPS, MFA. Implemented in hardware or software.
- **Physical** — locks, guards, fences, cameras, badge readers, mantraps. Protect physical access to facilities and assets.

## Functional Types

Apply across all three categories — the same control can serve multiple functions.

| Function | Purpose |
|---|---|
| **Preventive** | Stop an incident before it occurs |
| **Detective** | Identify an incident in progress or after the fact |
| **Corrective** | Reduce the impact of an incident and restore normal operations |
| **Deterrent** | Discourage threat agents from attempting an attack |
| **Recovery** | Restore systems and operations after an incident |
| **Compensating** | Substitute for a primary control that cannot be implemented |
| **Directive** | Guide behavior through policy or instruction |

## Security Control Assessment (SCA)

A formal evaluation of security infrastructure and individual mechanisms against a baseline or reliability expectation. SCA verifies that controls are implemented correctly, operating as intended, and producing the desired outcome. It is distinct from selecting controls — selection decides what to implement; assessment determines whether what was implemented actually works.

## Monitoring and Measurement

Controls must be monitored continuously after implementation to quantify their benefit and detect degradation. Monitoring answers whether a control is still effective over time — not just at the point of deployment. Metrics feed back into risk assessments and support decisions about whether to adjust, replace, or add controls.
