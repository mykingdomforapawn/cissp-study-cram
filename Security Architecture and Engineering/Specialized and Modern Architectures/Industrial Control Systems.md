**Industrial control systems (ICS)** monitor and control physical processes such as power generation, water treatment, pipelines, manufacturing lines, and building systems. They belong to the wider category of cyber-physical systems (see [[Embedded and Cyber-Physical Systems]]). In the **operational technology (OT)** world, a failure means a physical event, not just lost data.

## Components

| Component | Role |
|---|---|
| **PLC** (programmable logic controller) | A rugged, special-purpose computer that reads **sensors**, runs control logic, and drives **actuators** such as valves and motors |
| **HMI** (human-machine interface) | The operator's screen for viewing and controlling the process |
| **DCS** (distributed control system) | Controllers spread through **one site** (a refinery or plant) under central supervision, for continuous processes. Control is distributed, while the network is local |
| **SCADA** (supervisory control and data acquisition) | Central monitoring and control of **geographically dispersed** assets (pipelines, power grids) over wide-area links, using remote units at each site and a control center with a data **historian** |

## Security Concerns

- **Safety and availability come first.** The usual IT priority of confidentiality, integrity, availability reverses: the process must keep running safely, so patching and rebooting are often not allowed.
- **Legacy and long lifespans.** Equipment runs for decades, on old operating systems and unpatchable firmware (see [[Firmware]]).
- **Insecure protocols.** Industrial protocols such as Modbus were designed for closed networks and have no authentication or encryption.
- **IT/OT convergence.** Connecting plant networks to the corporate network or internet for efficiency exposes them. The air gap is largely gone, and where it exists it is breached by USB drives and vendor laptops (Stuxnet did this).

## Controls

- **Segmentation.** Separate the OT network from IT with firewalls and a DMZ, and divide it into zones with controlled **conduits** (the Purdue model layers the plant this way).
- **Restrict remote access** to vendors and engineers with MFA and monitoring.
- **Passive monitoring** of OT traffic, since active scanning can disrupt fragile devices.
- **Compensating controls** where patching is impossible: allow lists, isolation, and virtual patching.
- **Physical security** of controllers and strict change management. NIST SP 800-82 is the reference guide.

## Key Points

- **PLC** controls a machine, **DCS** controls one plant, **SCADA** controls widely dispersed assets.
- **Safety and availability outrank confidentiality** in OT.
- **Segmentation is the main defense** because the devices themselves cannot be easily hardened or patched.
