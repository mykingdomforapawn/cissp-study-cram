Choosing controls starts from what the system must achieve, and the confidence that a product or system actually achieves it is established by **evaluation** and then formal **authorization**. This is the evidence side of the trust and assurance distinction in [[Techniques for Ensuring CIA]]: the design supplies the trust, and evaluation supplies the assurance.

## Common Criteria

The **Common Criteria (ISO/IEC 15408)** is the international standard for evaluating the security of IT products. It replaced earlier national schemes such as the US TCSEC ("Orange Book") and European ITSEC, and results are mutually recognized across participating countries, so a product evaluated once is accepted in many places.

It separates *what is required*, *what is claimed*, and *how thoroughly it was checked*:

| Term | Meaning | Written by |
|---|---|---|
| **Target of Evaluation (TOE)** | The product or system being evaluated | |
| **Protection Profile (PP)** | A reusable set of security requirements for a category of product (a firewall, an operating system) | The customer or a community of users |
| **Security Target (ST)** | The specific security claims and functions of one TOE | The vendor |
| **Evaluation Assurance Level (EAL)** | The depth and rigor of the evaluation | Set by the evaluation |

An independent, accredited lab checks the ST against the TOE, and the product is then certified at an EAL.

### Evaluation Assurance Levels

| Level | Description |
|---|---|
| **EAL1** | Functionally tested |
| **EAL2** | Structurally tested |
| **EAL3** | Methodically tested and checked |
| **EAL4** | Methodically designed, tested, and reviewed |
| **EAL5** | Semi-formally designed and tested |
| **EAL6** | Semi-formally verified design and tested |
| **EAL7** | Formally verified design and tested |

A higher EAL means **more rigorous** evaluation, not stronger security features. It is more confidence that the claimed features work, with a bigger cost and time to obtain. Most commercial products land in the middle, and the top levels are reserved for the highest-risk environments. The EAL also says nothing about whether the product's claims fit a given need, which is why the Protection Profile and Security Target matter as much as the level.

## Authorization to Operate

Evaluating a product says little about whether it is acceptable in a particular environment. **Authorization to operate (ATO)** is the decision, made by a responsible official, to let a specific system run in a specific environment, and to **accept the residual risk** that remains. The concept itself is covered in [[Organizational Security Processes]].

Two steps are commonly distinguished:

- **Certification** — a technical evaluation of whether the system meets its security requirements and which controls are in place.
- **Accreditation (authorization)** — the management decision to approve operation, based on the certification results and the risk the organization is willing to take.

In US federal practice both are part of the NIST Risk Management Framework (see [[Risk Frameworks]]), which uses "authorization" and ends with a continuing-monitoring phase, as an ATO is not permanent. A new authorization has to be obtained when:

- **The ATO expires** — it is granted for a limited period, so it lapses unless renewed.
- **A security breach occurs** — the evidence the authorization rested on can no longer be trusted.
- **The security posture changes** — a significant change to the system, its environment, or its controls means the earlier assessment no longer describes what is running.

## How They Fit Together

| | Common Criteria | Authorization to operate |
|---|---|---|
| **Scope** | A product, in the abstract | A system, in its actual environment |
| **Question** | Does it do what it claims, and how sure are we? | Is the remaining risk acceptable to run it here? |
| **Decision by** | Independent evaluation lab | The organization's authorizing official |

An evaluated product is an input to authorization, not a replacement for it: a high-EAL product can still be deployed insecurely or in an environment it was not evaluated for.
