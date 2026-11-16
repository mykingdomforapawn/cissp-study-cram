An access control model is the answer to one question: **who decides the rule that grants access?** The owner of the data, a central policy, a job function, a condition, or an attribute set. Everything else about a model follows from that.

## Discretionary Access Control (DAC)

Every object has an **owner**, and the owner decides who may access it, at their own **discretion**. Enforced with ACLs attached to each object.

- The familiar model: NTFS and UNIX file permissions, shared folders, document sharing links.
- Strength: flexible, and the person closest to the data makes the call.
- Weakness: **no central control of the result**. Policy is the sum of thousands of individual decisions, nobody can state it, and it drifts. Malware running as the user inherits that user's discretion and can re-share anything the user owns — the reason DAC is considered unsuitable for highly sensitive environments.

## Nondiscretionary Access Control

Everything that is **not** owner-discretion: the rule comes from a central authority, a classification, a role, or a condition, and a user cannot change it for their own objects. Administration is centralized, so the policy exists in one reviewable place.

### Mandatory Access Control (MAC)

Access is decided by comparing a **label on the subject** (clearance) with a **label on the object** (classification), against a rule enforced by the system. Neither users nor owners can override it.

- Labels form a **lattice**: each subject sits at a level with an upper and lower bound on what it may reach.
- Need-to-know is enforced on top through **compartments** (categories) — clearance alone is not enough if the compartment does not match.

| Environment | Structure |
|---|---|
| **Hierarchical** | Ordered levels only — confidential, secret, top secret; higher includes lower |
| **Compartmentalized** | No ordering; access requires membership in the specific compartment |
| **Hybrid** | Levels *and* compartments — the usual real arrangement: secret clearance plus the "Project A" compartment |

Expensive to run, because every object must be labelled and every subject cleared. Used where confidentiality dominates: military and government systems, and SELinux-style enforcement. The formal rules are in [[Security Model Fundamentals]] (Bell-LaPadula for confidentiality, Biba for integrity).

### Role-Based Access Control (RBAC)

Permissions are granted to **roles** matching job functions, and users receive permissions by being **placed in a role**. Changing jobs means changing roles, not editing permissions.

- Fits organizations with **high turnover** and well-defined functions, which is most of them.
- Makes the intended policy reviewable in one place and makes transfers survivable — the standard defense against **privilege creep** (see [[Identity and Access Provisioning Lifecycle]]).
- Cost: a role is an approximation, so any usable role over-grants somebody. Too many narrow roles ("role explosion") returns to unmanageability.
- Implemented with **groups** in most directory products; group membership is the practical form of a role.

Three mechanics that decide most questions about RBAC:

- **A user may hold several roles at once**, and the effective permission set is their union. Roles are not mutually exclusive — a person can be both "Finance Analyst" and "Fire Warden".
- **Roles are hierarchical**, derived from the organization's own structure: a senior role typically inherits the permissions of the junior roles beneath it, so the hierarchy is defined once rather than re-listed per role.
- **RBAC uses no labels.** Labels are MAC. If a question mentions clearance or classification labels, it has left RBAC behind.

Holding multiple roles over a career is how **privilege creep** (also called **creeping privileges**) happens: roles accumulate at each transfer and the old ones are never removed. The fix is removal at transfer plus periodic access review, not better role design — see [[Identity and Access Provisioning Lifecycle]].

### Rule-Based Access Control

Access is decided by **global rules applied to every subject alike** — typically `if condition then allow/deny`, evaluated in order and ending in implicit deny.

- The firewall ruleset is the canonical example; so is "no logins outside business hours".
- The distinguishing feature: the rule is attached to **the system, not to the identity**. The same rule tests every request.
- An **ACL** is often classified here as well, and the two framings are both correct: an ACL is a column of the access control matrix *and* an ordered set of rules evaluated against each request, ending in implicit deny. Think of the matrix view as what an ACL **describes** and the rule view as how it is **evaluated**.

### Attribute-Based Access Control (ABAC)

The decision is a policy evaluated over **attributes of the subject, the object, the action, and the environment** — a generalization of rule-based control, and the most expressive model.

- "A **nurse** may read a **record** of a patient **on their own ward** during a **rostered shift** from a **managed device**."
- Powers software-defined networking policy and modern cloud authorization, and is the decision style assumed by [[Zero Trust Architecture]].
- Cost: policies are code, and nobody can tell by inspection who actually has access — the answer requires evaluating the policy against real data.

### Risk-Based Access Control

Access depends on a **risk score computed at the moment of the request** — location, device health, time, behavioral deviation, sensitivity of the target. The decision is not binary: allow, step up to MFA, allow read-only, or deny.

- The mechanism behind **adaptive** or **conditional-access** authentication (see [[Multifactor and Passwordless Authentication]]).
- Requires the machine learning or heuristics to be tuned: too sensitive and legitimate users are blocked, too loose and the score means nothing.

## Comparison

| Model | Who sets the rule | Decision based on | Typical use |
|---|---|---|---|
| **DAC** | The object's **owner** | The object's ACL | File systems, collaboration tools |
| **MAC** | A **central authority**, via labels | Clearance vs. classification | Military, government, high-confidentiality systems |
| **RBAC** | Administrators, via **roles** | The subject's job function | Most enterprises |
| **Rule-based** | Administrators, via **global rules** | A condition tested on every request | Firewalls, time and location restrictions |
| **ABAC** | Administrators, via **policies** | Subject, object, action, environment attributes | Cloud, SDN, fine-grained applications |
| **Risk-based** | Administrators, via a **risk model** | A score computed per request | Adaptive authentication |

The discriminator is usually a single phrase: *owner decides* → DAC; *labels or clearance* → MAC; *job function or high turnover* → RBAC; *applies to everyone equally* → rule-based; *combination of conditions* → ABAC.

## Key Points

- **DAC lets the owner decide; everything else is nondiscretionary and set centrally.**
- **MAC compares a subject's clearance label with an object's classification label and cannot be overridden by users.**
- **MAC environments are hierarchical, compartmentalized, or hybrid; compartments enforce need-to-know.**
- **RBAC assigns permissions to job functions and is the answer for high-turnover organizations.**
- **Rule-based control applies the same global rules to every subject; ABAC evaluates subject, object, action, and environment attributes.**
- **Risk-based control scores each request and can step up authentication instead of simply denying.**
