A **security model** is a formal, abstract description of how a security policy is enforced: it states the rules for which subjects may do what to which objects, so that a design can be reasoned about and checked before it is built. Models do not prescribe technology.

A model is not the same as a **policy**, which states what an organization requires. The model is the framework for implementing that policy, giving designers something to map the policy to and measure the design against. The policy the system actually enforces, the **system security policy**, is the enforceable form of the organization's policy: organizational policy, then system policy, then model, then mechanisms (the TCB and reference monitor below). Evaluating a finished system is a fourth thing (see [[Security Evaluation and Authorization]]). Each one captures one concern, such as confidentiality, integrity, or conflict of interest, and real systems combine them. The vocabulary of subjects and objects is in [[Secure Design Principles]], and the mechanisms the models rely on are in [[Techniques for Ensuring CIA]].

> [!info] Tokens, capabilities, and labels
> Three ways of attaching security information to the access decision:
> - **Token** — a data structure holding a subject's security attributes (identity, group memberships, privileges), presented when access is requested.
> - **Capability** — an unforgeable reference that names an object and the rights the holder has on it. Possessing it is the authority to use it (subject-centric).
> - **Label** — a security attribute attached to an object, such as its classification, that is compared with the subject's clearance (object-centric).

## Trusted Computing Base

The **trusted computing base (TCB)** is the combination of hardware, firmware, and software that enforces the security policy. Everything outside it is untrusted and relies on it. A flaw inside the TCB can undermine the whole policy, so it is kept as small as practical.

- **Reference monitor** — the abstract concept: a component that mediates *every* access by a subject to an object. It must be tamper-proof, always invoked, and small enough to be verified.
- **Security kernel** — the TCB components that actually implement the reference monitor.
- **Security perimeter** — the (imaginary) boundary separating the TCB from everything else. In physical security the same term means the boundary of the physically secure area around a system.
- **Trusted path** — a protected channel between the user and the TCB, so that, for example, a password entry cannot be intercepted by untrusted code.

## State Machine Model

Describes a system as a set of **states** and the **transitions** between them. A state is a snapshot of the system (who holds which access, what is in memory), and a transition is an operation that moves it to another state.

A system is **secure** if it starts in a secure state and every possible transition leads only to another secure state. **Bell-LaPadula** and **Biba** are built on it, and they differ in what they define as a "secure state". Take-Grant and Clark-Wilson are not directly based on it. It is also the reasoning behind failing securely: even a crash must land in a secure state.

## Information Flow Model

Instead of asking who may *access* an object, it controls **how information may move** between levels of sensitivity or between objects. Flows are only allowed in directions the policy permits, for example from low to high, and never the reverse.

- It addresses leaks that bypass direct access, since information can move indirectly through a process that reads one object and writes another.
- Flow rules between security levels are typically described with a **lattice**.
- Bell-LaPadula (confidentiality) and Biba (integrity) are both information flow models, with opposite flow directions.

## Noninterference Model

Activity by a subject at a **high** security level must have **no visible effect** on what a **low**-level subject sees. The low-level user cannot tell, from the system's behavior, whether the high-level activity happened at all.

- It prevents **inference** and **covert channels**, where low-level subjects deduce secrets from changes in behavior, timing, or resources.
- It is stronger than information flow rules alone, because it covers indirect effects and not just direct data movement.

## Composition Theories

Secure systems are rarely built from a single component, and joining individually secure components does not guarantee a secure whole. Composition theories study how information flows between interconnected systems:

- **Cascading** — the output of one system is the input of the next, in a chain.
- **Feedback** — one system's output feeds another, whose output returns to the first, creating a loop.
- **Hookup** — a system's output goes to another system while it also interacts with external entities, as in a shared link.

Each pattern creates paths that none of the individual models saw, which is why interconnections need to be assessed as well as components.

## Take-Grant Model

Represents the system as a **directed graph** of subjects and objects, with edges that are rights. A small set of rules defines how rights can spread:

- **Take** — a subject takes a right that another node holds.
- **Grant** — a subject gives one of its rights to another node.
- **Create** and **Remove** — add a new node with rights, or delete rights.

Its purpose is analysis: given an initial graph, which subjects can eventually **acquire** which rights? It shows how rights propagate and whether a given configuration can lead to an unintended privilege.

## Access Control Matrix

A table with **subjects as rows** and **objects as columns**, where each cell, an **access control entry (ACE)**, holds the operations that subject may perform on that object (read, write, execute, own). It assembles the ACLs of many objects into a single table.

| | File A | File B | Printer |
|---|---|---|---|
| **Alice** | read, write | read | print |
| **Bob** | read | none | none |

- A **column** is an **access control list (ACL)**, which lists everyone with access to one object (object-centric).
- A **row** is a **capability list**, which lists everything one subject can access (subject-centric).

It is a simple model that describes a policy but does not say how it should be enforced or how rights change, which is where Take-Grant and the other models come in.

## Bell-LaPadula Model

A **confidentiality** model built on the state machine and information flow ideas, designed for military and government settings with classification levels (the basis of mandatory access control). It prevents information from flowing to subjects without the right clearance.

- **Simple Security Property** — **no read up**: a subject may not read an object at a higher classification than its clearance.
- **\* (Star) Security Property** — **no write down**: a subject may not write to a lower classification, so secrets cannot leak downward.
- **Strong Star Property** — a subject that can both read and write may do so only at its own level.
- **Discretionary Security Property** — an access control matrix is also used, so need to know applies within a level.
- **Tranquility principle** — labels do not change while in use (strong tranquility: never; weak: only in ways that do not violate the policy).

A **trusted subject** is allowed to violate the wording of the star property and write an object to a lower level. The legitimate case is **declassification**: moving an object to a lower classification once it no longer justifies the higher one. It breaks the letter of the rule but not its intent, which is preventing unauthorized disclosure, and it is why only trusted subjects may do it.

It protects only confidentiality and says nothing about integrity. It also does not address covert channels, or how access control is managed in practice.

## Biba Model

An **integrity** model with a lattice of integrity levels. Like Bell-LaPadula it is built on the state machine model, is based on information flow, and is multilevel. It protects data from being modified by lower-integrity subjects, and so it is the mirror image of Bell-LaPadula's confidentiality rules: the direction of the rules is reversed. What is forbidden implies what is allowed: read up and write down.

- **Simple Integrity Axiom** — **no read down**: a subject may not read data at a lower integrity level, so unreliable data cannot contaminate it.
- **\* (Star) Integrity Axiom** — **no write up**: a subject may not write to a higher integrity level, so it cannot corrupt trusted data.
- **Invocation property** — a subject may not call on a subject of higher integrity.

It covers only one integrity goal, preventing modification by **unauthorized subjects**. It does not deal with insider errors, internal consistency, or separation of duties.

## Clark-Wilson Model

An **integrity** model aimed at commercial systems, where subjects are not allowed to touch data directly. Instead of defining a formal state machine, it defines each data item and the allowed transformations of it. Access is mediated by approved programs, in the access triple **subject → program → object**, where the program is also called the **interface** (see constrained interfaces in [[Security Capabilities of Information Systems]]).

- **Constrained data items (CDIs)** — protected data whose integrity is enforced.
- **Unconstrained data items (UDIs)** — data not yet validated, such as raw user input.
- **Transformation procedures (TPs)** — the only approved operations that may change a CDI, written as **well-formed transactions**.
- **Integrity verification procedures (IVPs)** — checks that CDIs are still valid and consistent.

By forcing every change through a TP, it enforces **separation of duties** and **auditing**. It addresses all three integrity goals (preventing unauthorized changes, preventing authorized subjects from making improper changes, and keeping data internally and externally consistent), where Biba covers only the first.

## Brewer and Nash Model

Also called the **Chinese Wall** model. It prevents **conflicts of interest** by making access rights **dynamic**: what a subject has already accessed changes what it may access next.

- Data is grouped into **conflict-of-interest classes**, such as competing companies in the same sector.
- Once a subject accesses data of one company in a class, access to the data of its competitors in that class is blocked.
- A consultant can work for any client, but only for one of two competitors at a time.

It is unusual because the rules depend on the subject's *history* and not on a fixed classification.

## Comparison

| Model | Primary concern | Key idea |
|---|---|---|
| **State machine** | General security | Secure state, and only secure transitions |
| **Information flow** | Confidentiality, integrity | Control where information may move |
| **Noninterference** | Confidentiality | High-level activity is invisible to low-level subjects |
| **Take-Grant** | Rights propagation | Graph rules show how rights can spread |
| **Access control matrix** | Policy description | Subjects × objects table of permissions |
| **Bell-LaPadula** | Confidentiality | No read up, no write down |
| **Biba** | Integrity | No read down, no write up |
| **Clark-Wilson** | Integrity | Subject → program → object, well-formed transactions |
| **Brewer and Nash** | Conflict of interest | Access history changes what is allowed |
