The processor (CPU) executes instructions and is the component every other protection mechanism ultimately relies on. How it schedules work, how it separates privileged from unprivileged code, and what state a process is in at any moment all have security consequences. The abstract ideas (bounds, isolation, user vs kernel mode) are in [[Techniques for Ensuring CIA]], and this note covers how the hardware implements them.

## Execution Types

These terms describe how a system runs more than one piece of work. They are easy to confuse, so it helps to separate *what is being shared* from *what is doing the work*.

| Type                 | What it means                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Multitasking**     | One operating system runs several tasks (processes) by switching the processor between them quickly, so they appear to run at the same time                                                                                                                                                                                                                                                                                                    |
| **Multiprogramming** | Several programs are loaded into memory and the processor switches between them when one has to wait (for I/O, for example). An older, simpler form of sharing the processor, typical of batch and mainframe systems, and it usually requires programs written with it in mind                                                                                                                                                                 |
| **Multithreading**   | A single process is split into several **threads**, each a separate path of execution inside the same process and sharing its memory, so one process can do several things at once                                                                                                                                                                                                                                                             |
| **Multicore**        | One processor chip contains several independent **cores**, each able to execute instructions                                                                                                                                                                                                                                                                                                                                                   |
| **Multiprocessing**  | A system uses two or more processors (or cores) to run work truly in parallel. In **symmetric multiprocessing (SMP)** the processors share memory and are treated equally by one OS and the load is balanced across them. In **asymmetric multiprocessing (AMP)** processors are assigned specific tasks. **Massively parallel processing (MPP)** uses many processors, each with its own memory and OS, working on parts of one large problem |

Multitasking, multiprogramming, and multithreading *interleave* work, so on a single core they only look simultaneous. Multicore and multiprocessing give real parallelism.

Security issues come from sharing: threads inside one process share its memory, so timing becomes a problem. If two threads touch the same data without coordination, the result depends on who gets there first (a **race condition**), and a check can become stale between the moment it is made and the moment it is used (**time-of-check to time-of-use**). Separate processes are kept apart by the memory protection in [[Security Capabilities of Information Systems]], but threads are not.

## Processing Types

A processor can be built to handle one level of data sensitivity or several.

- **Single-state** processors handle only one security level at a time, and the system is protected by being dedicated to that level.
- **Multistate** processors can handle data of several classification levels at once, and rely on the hardware and OS to keep the levels separated. They need strong protection mechanisms and a high degree of assurance (see [[Security Evaluation and Authorization]]).

## Kernel

The **kernel** is the core of the operating system. It is loaded at boot, stays in memory, and runs in the most privileged mode (ring 0). It manages the processor, memory, and devices, schedules processes, and mediates every request for those resources, so it enforces the access decisions of the **reference monitor** (the kernel's security-enforcing part is the **security kernel**, see [[Security Model Fundamentals]]).

- A **monolithic kernel** runs nearly everything (scheduling, memory, file systems, drivers) in kernel mode. It is fast, but a flaw in any part, including a driver, gives full control.
- A **microkernel** keeps only the minimum in kernel mode (basic scheduling, memory, and message passing) and runs the rest, such as drivers and file systems, as ordinary user-mode services. It is slower because of the extra communication, but the trusted part is smaller and easier to verify.

## Protection Rings

Protection rings arrange code in concentric levels of privilege. The innermost ring is the most trusted and has the most direct access to hardware.

| Ring | Typical contents |
|---|---|
| **0** | The OS **kernel**, with full access to hardware and memory |
| **1** | Other parts of the operating system |
| **2** | Device drivers and I/O services |
| **3** | Applications and user processes, the least privileged |

- Code at an outer ring cannot directly use inner-ring resources. It asks the kernel through a controlled interface (a **system call**), and the kernel decides whether to do it.
- Most modern operating systems use only two rings in practice, **kernel mode** (ring 0) and **user mode** (ring 3), because the hardware distinction between the middle rings is little used.
- Rings are a **layering** model: a flaw in an inner ring undermines everything outside it, so inner layers should be small and carefully verified.
- Virtualization adds privilege below the kernel: a **hypervisor** runs at a more privileged level than the guest OS kernels (sometimes described informally as ring -1), and firmware such as system management mode runs more privileged still. Compromising these is correspondingly more serious.

## Process States

A **process** is a program in execution. The OS tracks which state each process is in, and moves it between states as it runs.

| State | Meaning |
|---|---|
| **Ready** | Loaded and able to run, waiting for the processor to be assigned to it |
| **Running** | Being executed by the processor, using its allotted time slice |
| **Waiting** (blocked) | Cannot continue until something it needs happens, such as I/O or a resource becoming free |
| **Supervisory** | Executing an action that needs a higher privilege level than normal user code, such as a kernel function, so it runs in privileged mode |
| **Stopped** (terminated) | Finished or ended, and its resources are released |

A process normally cycles between ready, running, and waiting, and enters the supervisory state when it needs privileged work done. Entry to that state must be tightly controlled, and when a process stops its resources must be cleared before reuse (see [[Memory]]).

## Key Points

- **Interleaving vs parallelism.** Multitasking, multiprogramming, and multithreading share a processor over time, while multicore and multiprocessing run work at the same time on separate processing units.
- **Threads share memory, processes do not.** Shared memory is why threading brings race conditions and TOCTOU problems.
- **Single-state vs multistate** is about how many classification levels one processor may handle.
- **The kernel** is the ring 0 core of the OS. A microkernel keeps it small, a monolithic kernel does not.
- **Rings put the most trusted code at the center.** Crossing a ring goes through a controlled gate, and the hypervisor and firmware sit even below ring 0.
- **Process states** are ready, running, waiting, supervisory, and stopped.
