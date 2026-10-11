Security models say what a system must enforce, and these are the capabilities built into hardware and software that actually enforce it. They are the implementation counterpart to [[Security Model Fundamentals]] and the mechanisms in [[Techniques for Ensuring CIA]]. Several are only introduced here, with the detail covered elsewhere.

## Memory Protection

Memory is shared by every process, so the system has to stop one from reading or corrupting another, or the operating system itself. It is the implementation of the **bounds** and **isolation** ideas in [[Techniques for Ensuring CIA]], enforced by the hardware and the operating system. It has to be enforced regardless of which programs are running. Without it the typical results are instability, integrity violations between applications, local denial of service, and information disclosure between processes.

## Virtualization

Virtualization runs several **virtual machines (VMs)** on one physical host, each behaving like a complete system, with a **hypervisor** allocating the hardware. It gives strong **isolation** between workloads, easy snapshots and rebuilds from a clean image, and better use of hardware. Its main risk is that the hypervisor becomes a single point of compromise, and a **VM escape** breaks the isolation of everything on the host.

## Trusted Platform Module (TPM)

A **TPM** is a hardware chip that acts as a **root of trust** for a device: a component whose behavior is assumed correct because everything else is built on it. It stores keys and measurements in tamper-resistant hardware. The device-encryption use and the comparison to an HSM are in [[Portable Devices and TPM]].

- **Secure and measured boot** — each boot stage is measured (hashed) and recorded, so changes to firmware or the bootloader are detectable.
- **Remote attestation** — the device can prove its measured state to another party.
- **Sealed storage** — keys and data are released only if the platform is in the expected state.
- **Key generation and protection** — keys are created and kept in hardware and never leave it.

## Interfaces

A **constrained (restricted) interface** limits what a user can see or do to what their role permits, instead of relying only on blocking forbidden actions behind the scenes. It limits the actions of both authorized and unauthorized users. It is not authentication (verifying identity) and not auditing (tracking events).

- **Menus and shells** that offer only permitted commands, and **greyed-out or hidden** options for functions the user cannot use.
- **Database views** that expose only certain columns or rows.
- **Physical limits**, such as a keypad that allows no more than the function it was built for.

This implements least privilege at the point of use. Interfaces also include APIs, where **input validation** and authentication are what prevent a well-formed but malicious request from reaching the system.

## Fault Tolerance

**Fault tolerance** is the ability to keep operating when a component fails, with no interruption. It supports **availability** in the [[CIA Triad]] by removing **single points of failure** through redundancy, such as redundant disks, power, and servers with failover. It is not the same as a backup: redundancy keeps the system running through a failure, while backups restore it afterwards. It is related to the fail-secure choice in [[Secure Design Principles]], which is about the *state* a system fails into.

## Encryption and Decryption

Encryption protects the **confidentiality** of data at rest, in transit, and in use, and its strength depends on **key management**. The algorithms and mechanisms are in [[Symmetric Key Algorithms]], [[Asymmetric Key Algorithms]], and [[Network Encryption]], and device encryption is in [[Portable Devices and TPM]].
