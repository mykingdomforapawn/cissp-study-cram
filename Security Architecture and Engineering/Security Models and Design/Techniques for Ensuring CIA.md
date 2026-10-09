The principles in [[Secure Design Principles]] say how a system should be shaped. The techniques here are the mechanisms that make the [[CIA Triad]] hold *inside* a running system: they stop one process, user, or component from reading, corrupting, or starving another. Confinement, bounds, and isolation are about containing subjects, access control is about deciding what they may touch, and trust and assurance are about how much to believe that all of it works.

## Confinement

**Confinement** restricts a process so it can read and write only the memory locations and resources it has been allocated, and cannot reach outside them. A confined process cannot read another process's data (confidentiality), alter it (integrity), or interfere with it (availability).

- Typical implementations are sandboxes, containers, chroot-style jails, and virtual machines.
- It limits the damage of a compromised or malicious program, since the program can only affect what it was given.
- It also limits **leakage**. A confined process should not be able to pass information out through side routes, such as **covert channels** (using shared resources, timing, or storage to signal data in ways the system was never designed to allow). Preventing those is the hard part of confinement.

## Bounds

The **bounds** of a process are the limits on the resources it may use: the lower and upper memory addresses it may access, and the level of privilege it runs with. Every process gets its own bounds, and the operating system enforces them.

- **Memory bounds** — the process gets an address range and any attempt to go outside it is blocked.
- **Privilege bounds** — processors separate **user mode** (restricted) from **kernel/supervisor mode** (full hardware access). Layered models, such as protection rings, place the most trusted code at the center and the least trusted at the outside. A process gets only the privilege its job requires and must pass through controlled gates (system calls) to cross a ring.

Confinement says *where* a process is held, while bounds say *how far* it may reach within that. Bounds are what make least privilege enforceable at the system level.

## Isolation

**Isolation** keeps a process or component in its own separate space, running without being able to see or influence others. It is the outcome that confinement and bounds work together to create, and also a technique in its own right at several levels.

| Level | Example |
|---|---|
| **Process** | Each process has its own virtual address space and cannot read another's memory |
| **Application** | Sandboxed apps and containers share a kernel but not each other's resources |
| **System** | Virtual machines each run a complete OS on virtualized hardware under a hypervisor |
| **Network** | Segmentation, VLANs, and DMZs keep traffic from moving freely between zones |
| **Physical** | Air-gapped systems with no connection to other networks |

The trade-off is between separation and cooperation. The stronger the isolation, the more deliberate, mediated, and sometimes slow communication has to be. Isolation is also only as strong as the layer enforcing it: a flaw in the kernel or hypervisor breaks the isolation of everything above it. See [[Defense in Depth]] for the layering and segmentation vocabulary.

## Access Controls

**Access controls** decide which subjects may perform which actions on which objects, and enforce that decision. Where confinement and isolation limit what a process can reach by construction, access control grants and denies permissions explicitly. Every request is mediated, ideally by a **reference monitor** that cannot be bypassed, and permissions follow **least privilege**.

The subject and object vocabulary is in [[Secure Design Principles]], and authentication, authorization, and accountability are in [[AAA Framework]]. Access control models are not covered further here.

## Trust and Assurance

These two terms are easily confused, because both are about security in a system but describe different things.

| | Trust | Assurance |
|---|---|---|
| **Question** | Does the system have the security capabilities it needs? | How confident can we be that they work as intended? |
| **Established by** | Design: security built into the architecture and enforced by its components | Evidence: testing, evaluation, verification, and independent review |
| **Nature** | A property of the system | A level of confidence about the system |

- A **trusted system** has protection mechanisms that can reliably enforce its security policy. The set of hardware, firmware, and software that must function correctly for that policy to hold is the **trusted computing base (TCB)**, and the smaller it is, the easier it is to verify (the same reasoning as keeping the design small).
- **Assurance** is the degree of confidence that the security mechanisms are correctly implemented and behave as expected. It grows with rigor: more thorough design review, testing, and formal evaluation yield higher assurance.
- Trust without assurance is only a claim. A system can have strong controls on paper and still be unproven, which is why higher-sensitivity environments demand formal evaluation of products and not just feature lists.
