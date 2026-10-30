## Network Access Control

**Network access control (NAC)** decides **whether and how a device may join the network**, based on who it is and what state it is in. The goal is to prevent unauthorized or unhealthy devices from reaching internal resources, and to automate the response when one appears.

The two questions a NAC solution asks:

1. **Identity**: is this a known device or user? Verified through **802.1X** (port-based authentication, see [[Wireless Security Protocols]] for the EAP mechanics), certificates, MAC address lists, or a captive portal login.
2. **Posture** (health): does the device meet policy? Patched OS, running endpoint protection with current signatures, disk encryption on, no forbidden software.

Based on the answers, NAC enforces by **assigning the port or session to a VLAN** (production, guest, or a **quarantine / remediation** VLAN that only reaches patch servers), by applying ACLs, or by refusing the connection.

| Design choice | Options |
|---|---|
| **When** it checks | **Pre-admission** (check before granting access) vs **post-admission** (monitor behavior after connection and revoke on violation); most products do both |
| **How** it checks | **Agent-based** (software on the endpoint reports posture; deeper visibility) vs **agentless** (network-side scanning, DHCP fingerprinting, 802.1X alone; needed for printers, IoT, guest devices) |
| **Where** it enforces | **Inline** (NAC device in the traffic path) vs **out-of-band** (NAC instructs switches and wireless controllers) |

NAC is the practical mechanism for policies like "only corporate-managed laptops get the internal VLAN, everything else is guest" and for onboarding BYOD devices into a limited segment. It also discovers unknown devices, which matters for the asset inventory. Limitations: devices that cannot run an agent or do 802.1X fall back to MAC-based exceptions, which are spoofable; and the posture check is a point in time.

## Endpoint Security

Network controls cannot see everything, and a device that leaves the office leaves the perimeter. **Endpoint security** puts controls on the device itself, which is also the principle behind zero trust: trust the device based on its own verified state, not on where it is connected.

The layers typically present on an endpoint:

- **Anti-malware / endpoint protection platform (EPP)**: signature, heuristic, and behavioral detection of malicious code.
- **Endpoint detection and response (EDR)**: continuous recording of process, file, registry, and network activity on the host, with detection of suspicious behavior, investigation tools, and remote containment (isolate the host from the network). **XDR** extends this by correlating endpoint data with network, email, identity, and cloud telemetry.
- **Host-based firewall** and **host IDS/IPS**: filter and monitor the device's own traffic; the building block of microsegmentation.
- **Application allow-listing** (whitelisting): only approved executables run; stronger than block-listing but higher maintenance.
- **Full-disk encryption**, **patch management**, **configuration hardening** against a baseline, and **data loss prevention** agents.
- **Device control**: USB and removable media restrictions.
- **Mobile device management** for phones and tablets (see [[Mobile Device Security Features]]).

Principles: endpoints are managed **centrally** (policy, updates, telemetry to a console or SIEM) so that controls cannot be silently disabled by the user; **least privilege** on the endpoint (users are not local administrators) limits what malware can do; and endpoint telemetry is one of the most valuable sources for detection, since the endpoint sees decrypted content and process context that the network cannot.

NAC and endpoint security connect: the endpoint agent reports posture to NAC, and EDR's "isolate host" is a NAC-style enforcement.

## Key Points

- **NAC answers "who is this device and is it healthy?" and enforces by VLAN assignment, ACLs, or refusal.**
- **Pre-admission checks before access, post-admission monitors after; agent-based sees more, agentless covers devices that cannot run agents.**
- **A quarantine VLAN lets non-compliant devices remediate without reaching production.**
- **EPP detects malware, EDR records and responds to behavior, XDR correlates across sources.**
- **Application allow-listing, host firewalls, least privilege, and central management are the endpoint fundamentals.**
