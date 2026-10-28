Some spaces hold more value or risk than the rest of a facility. They get stricter controls, access limited to need-to-know, and logging of entries, following [[Defense in Depth]] and least privilege.

## Wiring Closets

A **wiring closet** (IDF) holds the switches, patch panels, and cabling for an area of the building. The **main distribution frame (MDF)** is the primary equipment room where external connections enter.

- Physical access lets an attacker tap or cut cables, plug in rogue devices, or take down a whole floor, yet closets are often neglected.
- Treat them like small server rooms: **locked** (card reader or MFA, fail-secure lock), limited and logged access, a **two-person rule** for sensitive ones, and never shared with janitorial or storage use.
- Keep them **climate-controlled and clutter-free**, add door alarms and cameras, and keep cabling labeled so tampering is visible.
- Secure cable paths with conduit and locked trays.

**Cable plant management** maps and labels every cabling element, so changes and tampering can be spotted:

| Element | Role |
|---|---|
| **Entrance facility** | Where external service enters, including the **demarcation point** |
| **Equipment room** | Houses the main network and telecom equipment (the MDF) |
| **Backbone distribution system** | Cabling between entrance facility, equipment room, and telecommunications rooms |
| **Telecommunications room** | Per-floor closet (IDF) connecting to the horizontal cabling |
| **Horizontal distribution system** | Cabling from the telecommunications room out to work areas |

## Server Rooms and Data Centers

The most protected space in the facility.

- **Location:** building core, no windows, no signage (see [[Facility Planning and Design]]).
- **Access control:** multiple factors, a **person trap** at the entrance (see [[Perimeter Security Controls]]), logged entry, and escorted visitors. See [[Physical Access Controls]].
- **Monitoring:** cameras and intrusion detection inside and at the door (see [[Intrusion Detection and Monitoring]]).
- **Environment:** dedicated cooling, redundant conditioned power, and clean-agent fire suppression (see [[Utilities and Equipment Failure]], [[Fire Protection]]).
- **Emanations:** shielding or a Faraday cage for the most sensitive systems (see [[Emanations and Input Output Devices]]).
- **Rack-level locks** so room access does not mean access to every system.
- No food, drink, or unneeded combustibles, and rules on bringing in or removing media and cameras.
- It is built for **equipment, not people**: security and equipment needs (non-water suppression, cooling, few visitors) outrank worker comfort, and every entry and exit is logged.

## Media Storage Facilities

Media needs protection as strong as its data, often in a separate location.

- A **secure, access-controlled area** with locked safes for the most sensitive items. A **media librarian or custodian** runs a **check-in/check-out** process that logs who removes and returns media, and **sanitization tools** wipe returned reusable media. Hashing is not part of this: reusable media should be cleaned, not preserved.
- **Off-site backups**, far enough away to avoid the same disaster and secured as well as the primary (see [[BCP vs DRP]]).
- Controlled **temperature, humidity**, and protection from magnetic fields, dust, fire, and water. Media-rated safes, since media tolerates less heat than paper.
- **Encrypt** media in transit and use trusted couriers.
- **Inventory and label** media, and sanitize or destroy it at end of life (see [[Data Storage Devices]], [[Information and Asset Handling Requirements]]).

## Evidence Storage

Evidence must stay both secure and **admissible**.

- A **separate, locked, access-limited** area, away from regular media and from those involved in the case.
- **Chain of custody:** a documented record of everyone who handled the evidence, when, and why. Any gap weakens it.
- **Integrity:** keep evidence unaltered (for digital evidence, work from forensic copies and verify hashes). Use **tamper-evident seals** on containers, label it, and protect it from damage.
- Log every access, and keep it for a defined retention period.

## Work Area Security

Work areas are exposed mainly through visibility, outsiders, and carelessness.

- **Restricted areas** for sensitive work, with need-to-know access.
- **Visitors** are signed in, badged distinctively, **escorted**, and kept out of sensitive areas. Staff challenge anyone without a badge.
- **Clean desk policy:** lock away sensitive papers and media, and lock screens.
- **Screen privacy:** privacy filters and screen placement away from windows.
- **Secure printing and disposal:** shred bins, **cross-cut** shredders, and prompt collection of printouts.
- **Equipment:** cable locks on laptops, and controls on removable media and personal devices.
- Clear **whiteboards and meeting rooms** after use. Control reception, mail rooms, and loading docks, where outsiders enter.
- These controls depend on people, so see [[Security Awareness, Training, and Education]] and [[Social Engineering]].

## Key Points

- **Wiring closets** are neglected but give network access, so lock and monitor them.
- A **data center** layers location, access control, monitoring, environment, and rack locks.
- **Backups** go off-site, secured, climate-controlled, and encrypted in transit.
- **Evidence** needs a locked store and an unbroken **chain of custody**.
- **Work areas** rely on visitor control, clean desks, screen privacy, and secure disposal.
