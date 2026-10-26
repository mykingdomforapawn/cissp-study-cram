**Virtualization** uses software to present a computer, or part of one, as several independent virtual ones sharing the same physical hardware. A **virtual machine (VM)** is a complete system (a **guest** OS with its applications) running on a **host**, with a **hypervisor** dividing the hardware among the guests. The isolation and VM-escape basics are in [[Security Capabilities of Information Systems]], and this note covers the technology around them.

## Benefits

- **Consolidation.** Many workloads share a few physical servers, which cuts hardware, power, and space costs.
- **Isolation.** Each VM is separated from the others, so one can be compromised or fail without taking the rest down.
- **Speed and recovery.** VMs are provisioned in minutes from a template, and **snapshots** and image copies make rollback and disaster recovery quick.
- **Portability.** A VM is just files, so it can be moved or copied between hosts.

## Hypervisor Types

| | Type 1 (bare metal) | Type 2 (hosted) |
|---|---|---|
| **Runs** | Directly on the hardware, with no OS underneath | As an application on top of a host OS |
| **Examples** | VMware ESXi, Microsoft Hyper-V, Xen, KVM | VirtualBox, VMware Workstation |
| **Performance** | Better, with fewer layers | Lower, since requests pass through the host OS |
| **Security** | Smaller attack surface | Larger: a compromised host OS exposes every VM |
| **Typical use** | Data centers and cloud platforms | Desktops, development, and testing |

## Elasticity and Scalability

- **Scalability** is the ability to handle growth by adding resources. It is a capability that is exercised on request or by plan.
- **Elasticity** (also called **dynamic resource allocation**) is the ability to **automatically add and release resources** (compute, memory, storage, network) as demand rises and falls, so capacity follows load in both directions and cost follows use.

Virtualization is what makes both possible, because VMs can be started, stopped, resized, and moved quickly. Elasticity is a defining feature of the cloud. Security consequences are that instances appear and disappear without manual steps, so protection (hardening, monitoring, agents, patching) has to be built into the image and the automation (see [[Microservices, IaC, and Immutable Architecture]]).

## Virtual Software

- **Virtual desktop infrastructure (VDI)** runs users' desktops as VMs in the data center, and users connect from **thin clients** (low-capability devices or virtual interfaces that only display the session) or any device. Data stays on central servers instead of endpoints. A **non-persistent** (static) desktop keeps no changes: it resets to a clean image at logoff, which removes malware and leftovers and defeats users' attempts to install software or alter security tools. A **persistent** desktop keeps the user's changes.
- **Virtual mobile infrastructure (VMI)** is the mobile equivalent: a mobile operating system runs on a server and the user reaches it remotely, so no data stays on the phone.
- **Application virtualization** delivers an application to the user without installing it on the local OS, either streamed or run in an isolated bundle. It simplifies deployment and keeps applications from conflicting with each other.
- **Virtual servers** are the ordinary VM case: a server OS and its services running on a hypervisor.

## Key Points

- **Type 1 sits on the hardware, Type 2 sits on an OS.** Type 1 is faster and has the smaller attack surface.
- **Elasticity is automatic scaling in both directions.** Scalability is only the ability to grow.
- **VDI keeps data central**, and a non-persistent desktop returns to a clean state each session. The endpoint becomes a **thin client**, a low-capability device or virtual interface that only displays the session and runs and stores nothing locally.
- **Security groups** are collections of users, applications, or devices that are allowed or denied access to specific resources, and are a main cloud access control (see [[Virtual Networking and Software-Defined Everything]]).
- **Security must be built into the image**, because instances are created and destroyed automatically.
