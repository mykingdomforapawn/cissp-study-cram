Authentication establishes **who** a subject is; authorization decides **what** that subject may do. This note covers the vocabulary and the mechanisms that implement the decision — the models that choose *who sets the rules* are in [[Access Control Models]].

## Permissions, Rights, and Privileges

The three words are used loosely in practice, but the distinction is precise:

| Term | Means | Example |
|---|---|---|
| **Permission** | Access granted to an **object** — what a subject may do to a resource | Read and write on a file, select on a database table |
| **Right** | The ability to take an **action on the system** itself, independent of any one object | Change the system time, install a driver, shut down the server |
| **Privilege** | The **combination** of permissions and rights a subject holds | An administrator's full set of file permissions plus system rights |

**Permissions are about objects, rights are about actions, privileges are the sum of both.** A user can hold wide permissions and almost no rights (a data analyst reading every report but unable to change a setting), or the reverse.

## Authorization Mechanisms

These are the building blocks a system uses to arrive at an allow-or-deny decision. Several usually operate together.

- **Implicit deny** — anything not **explicitly** allowed is denied. The default rule at the bottom of every firewall ruleset and ACL. Its value is that a gap in the policy fails closed; a system that defaults to allow grants access nobody ever decided to give. See [[Secure Design Principles]] on secure defaults.
- **Access control matrix** — subjects as rows, objects as columns, allowed operations in the cells. It describes a policy rather than enforcing one. The full table and its two slices are in [[Security Model Fundamentals]].
  - A **column** is an **access control list** — everyone who may touch one object (**object-centric**). Answers "who can open this file?"
  - A **row** is a **capability list** — everything one subject may touch (**subject-centric**). Answers "what can this user reach?" A **capability ticket** carried by the subject is the implementation.
- **Constrained interface** — the application shows or enables **only the functions the subject may use**: menu items are hidden or greyed out, commands are absent from the shell, fields are read-only. It reduces errors and probing, but it is an interface restriction and **not a substitute for enforcing the permission server-side** — a crafted request bypasses a hidden button.
- **Content-dependent control** — the decision depends on **the data inside the object**. A database view that returns only the rows for the user's own department; an email filter that blocks messages containing card numbers. Expensive, because every access requires inspecting content.
- **Context-dependent control** — the decision depends on the **circumstances of the request**, not its content: time of day, location, device posture, the sequence of prior actions. A payroll clerk allowed to run reports only during business hours from an office workstation. Transaction sequencing (no checkout without a prior add-to-cart) is the same idea.

**Content-dependent asks what is in the object; context-dependent asks what is going on around the request.**

## Principles Governing Authorization

These constrain how much authority is granted, and are covered in full elsewhere:

- **Need-to-know** — access only to the specific information required for a task. Clearance grants eligibility, need-to-know grants the actual access. See [[AAA Framework]].
- **Least privilege** — the minimum permissions *and* rights needed to do the job, for no longer than needed. Need-to-know is about data; least privilege is the broader rule covering rights and duration.
- **Separation of duties** — split a sensitive process so that no one person can complete it alone, forcing collusion. See [[Organizational Roles and Responsibilities]] and [[Personnel Security Lifecycle]].

The tension to recognize: role-based grouping (see Abstraction in [[AAA Framework]]) makes authorization administrable but necessarily over-grants, because a role is an approximation of what its members need.

## Defining Requirements with a Security Policy

The **security policy** is the document that states what the organization requires — which assets matter, who may reach them, and under what conditions. It is the authority the mechanisms above implement:

- It defines the requirement; models, ACLs, and interfaces are the **implementation** of that requirement.
- Without it, access decisions are made ad hoc by whoever administers each system, and there is no standard against which an access review can find anything wrong (see [[Identity and Access Provisioning Lifecycle]]).
- It also determines what "correct" means for an audit — a configuration can only be judged against a stated intent.

## Key Points

- **Permissions apply to objects, rights apply to system actions, privileges are the combination of both.**
- **Implicit deny means anything not explicitly granted is denied — the policy fails closed.**
- **An ACL is an object's column of the access control matrix; a capability list is a subject's row.**
- **A constrained interface hides unavailable functions but must not be the only enforcement.**
- **Content-dependent control inspects the data; context-dependent control inspects the circumstances.**
- **The security policy states the requirement that every access control mechanism implements.**
