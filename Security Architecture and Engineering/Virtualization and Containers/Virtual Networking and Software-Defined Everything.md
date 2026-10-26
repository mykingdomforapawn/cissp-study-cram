## Virtual Networking

Virtual machines on a host connect through a **virtual switch** in the hypervisor, with **virtual network interfaces (vNICs)**. Whole networks (switches, routers, firewalls, load balancers) can be built in software, either inside one host or across many through **overlay** networks and **VLANs**.

- **Benefit:** networks and segments are created quickly, and **virtual firewalls** and **microsegmentation** can place controls around individual workloads.
- **Visibility problem:** traffic between VMs on the same host (**east-west** traffic) never crosses a physical switch, so physical firewalls and monitoring tools cannot see it. Monitoring and filtering have to be built into the virtual layer.
- **Misconfiguration risk:** a wrong virtual switch or segment setting can silently connect workloads of different sensitivity.

## Security Groups

A **security group** is a collection of entities, usually users but also applications and devices, that can be granted or denied access to particular resources, or allowed particular traffic between workloads. Rules are written once for the group, and membership decides what each member may reach. It is a basic access control in cloud and virtual environments, and it supports controlling which applications may access which assets.

## Software-Defined Everything (SDx)

**Software-defined everything** moves the control of infrastructure out of the individual hardware devices and into software that is managed centrally, through APIs and automation. The key idea is to separate the **control plane** (decisions about where traffic or data goes) from the **data plane** (the forwarding of the traffic itself).

| Term | What becomes software-defined |
|---|---|
| **SDN** (software-defined networking) | Network control: a central controller sets forwarding rules for switches and routers (OpenFlow is a standard protocol for this) |
| **SD-WAN** | Management of wide-area links, steering traffic over the best path between sites and clouds |
| **SDS** (software-defined storage) | Storage pooled and managed through software, independent of the hardware |
| **SDDC** (software-defined data center) | Compute, network, storage, and security all virtualized and managed as software |

**Benefits:** agility, automation, consistent policy, and central visibility. **Concerns:**
- The **controller is a high-value target** and a single point of failure. Compromising it gives control of the whole network.
- **APIs** become the management interface, and need strong authentication and authorization.
- A mistake or malicious change **propagates instantly** to everything the controller manages.
- It depends on the integrity of the software supply chain.

**Controls:** harden and isolate the controller and its management network, strong authentication and role-based access for administrators and APIs, change control and logging, and redundant controllers. The cloud-delivered security model SASE (see [[Secure Design Principles]]) builds on SD-WAN.

## Key Points

- **East-west traffic is invisible to physical security devices**, so controls move into the virtual layer.
- **Software-defined means separating the control plane from the data plane** and managing it centrally.
- **The central controller and its APIs are the new crown jewels.**
