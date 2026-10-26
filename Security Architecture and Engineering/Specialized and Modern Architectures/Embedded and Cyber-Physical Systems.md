## Embedded Devices

An **embedded device** is a computer built into a larger product to do one dedicated job: appliances, vehicles' control units, medical devices, printers, routers, ATMs, smart TVs, and PLCs. It runs fixed software stored as [[Firmware]] and usually has limited processing power, memory, and power.

### Building Blocks

- **Microcontroller:** a small, cheap chip (or board, such as an Arduino) that combines a processor, memory, and input/output pins and runs a simple fixed program, for example switching a light or a pump on a schedule. It suits tasks with minimal computing needs and no required networking, and is usually not robust enough for mission-critical real-time work.
- **System on a chip (SoC):** a whole computer system (processor, memory, graphics, communications, and more) integrated onto one chip. It is compact and power efficient, and is common in phones and IoT devices.
- **Field-programmable gate array (FPGA):** a chip whose hardware logic can be reprogrammed by the customer after manufacture. It is flexible and fast, and is used in industrial and network equipment, but it is harder to program and costs more than a simple microcontroller.
- **Multifunction printer (MFP)** and similar office devices are embedded systems too (see [[Emanations and Input Output Devices]]).

The right choice follows the need: a microcontroller for simple cheap automation, an RTOS for critical timing, an FPGA for custom high-speed logic.

## Static Systems

A **static system** (or static environment) is configured once and then deliberately left unchanged: embedded devices, kiosks, medical equipment, and industrial controllers. Changes risk breaking certification or safe operation, so they are rarely patched and often run outdated software. They are protected by **isolation and compensating controls** such as network segmentation, allow lists, and monitoring, rather than by keeping them up to date.

## Cyber-Physical Systems

A **cyber-physical system (CPS)** tightly integrates computing and networking with physical processes. Sensors measure the physical world, software decides, and actuators act on it, in a feedback loop. Examples are smart grids, autonomous vehicles, robots, medical devices, and building automation. [[Industrial Control Systems]] are a CPS, and IoT devices (see [[IoT, Edge, and Fog Computing]]) often are.

## Real-Time Operating Systems

A **real-time operating system (RTOS)** guarantees that tasks complete within strict, predictable time limits, so timing matters as much as correct output.

- **Hard real-time:** missing a deadline is a failure with possible physical harm (airbags, flight control, pacemakers).
- **Soft real-time:** a missed deadline lowers quality but is tolerable (audio and video streaming).

An RTOS is typically stored in ROM or other firmware and runs on embedded hardware, in contrast to a microcontroller program on a flash chip. It is small and minimal, as in VxWorks, FreeRTOS, and QNX, so it often lacks memory protection, user separation, and room for security features. Security overhead such as encryption or heavy logging can itself break the timing guarantees.

## Security Concerns

- **Physical consequences.** An attack can cause injury, damage, or loss of life, so safety is the primary concern.
- **Hard to patch.** Updates may be impossible, risky, or unsupported by the vendor, and lifespans are long.
- **Limited resources.** Little capacity for encryption, authentication, or monitoring, and timing constraints in real-time systems.
- **Weak defaults.** Hard-coded or default credentials, unneeded services, and unauthenticated protocols.
- **Physical access.** Devices sit in the field where attackers can reach them.
- **Supply chain.** The components and firmware come from many vendors (see [[Supply Chain Risk Management]]).

**Controls:** segment and isolate, remove default credentials and unneeded services, require signed firmware and secure boot, monitor, keep an inventory, plan for replacement at end of support, and build security in at design time (see [[Secure Design Principles]]).

## Key Points

- **Embedded** means a dedicated computer inside a product, **static** means deliberately unchanging, and **CPS** means software controlling a physical process.
- **Microcontroller, SoC, and FPGA** are common embedded building blocks. A simple, non-critical task needs only a microcontroller.
- **RTOS** means predictable timing, hard (failure) or soft (degraded), and security must not break the deadlines.
- **Isolation substitutes for patching** when the system cannot be updated.
