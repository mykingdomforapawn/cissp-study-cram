Physical security protects people, facilities, and equipment, and underpins every logical control: an attacker with physical access can usually bypass technical protections. It is the outermost layer of [[Defense in Depth]], and it works best when designed in from the start rather than retrofitted.

## Secure Facility Plan

The plan starts from what must be protected, not from the building.

- **Critical path analysis** identifies mission-critical processes and maps the assets, systems, people, and facilities each depends on. It shows which locations need the strongest protection and where one failure stops the business. It is the physical counterpart to the [[Business Impact Analysis]].
- **Technology convergence** is the tendency of technologies, solutions, and utilities to merge over time, so that formerly separate systems perform similar functions on shared infrastructure. The main example here is physical security (badge readers, cameras, alarms, HVAC, building controls) moving onto the same IP network as IT. This is efficient and centrally manageable, but it creates **single points of failure**: one network outage or compromise can disable physical and logical security together, and physical controls become attackable over the network. Converged systems need the same patching, segmentation, and monitoring as any other networked system, and IT and physical security teams must coordinate (see [[Industrial Control Systems]]).
- **Layered defense.** Concentric layers (property boundary, building exterior, interior, sensitive rooms) serve six functions, **in this order**:

| Function | Purpose | Example |
|---|---|---|
| **Deter** | Discourage the attempt | Signs, visible cameras, lighting |
| **Deny** | Keep unauthorized people out | Locks, fences, badge doors |
| **Detect** | Notice an attempt | Alarms, cameras, motion sensors |
| **Delay** | Buy time for responders | Multiple barriers, reinforced doors |
| **Determine** | Judge what happened | Guard verifying an alarm |
| **Decide** | Choose the response | Dispatch police, lock down, stand down |

## CPTED

**Crime Prevention Through Environmental Design** shapes the environment so legitimate use is natural and intrusion is conspicuous. The first generation focuses on the physical setting, and the second adds the social setting.

**First generation (physical design):**

- **Natural access control:** walkways, fences, bollards, landscaping, lighting, and door placement subtly guide people to intended entrances.
- **Natural surveillance:** windows, lighting, and sight lines raise the chance of being observed, so intruders feel uneasy.
- **Territorial reinforcement (control):** signs, fences, and maintained grounds make ownership clear, so the area feels like a cared-for community and strangers stand out.
- **Image / milieu management:** keep the site's image positive (clean, repaired, no graffiti, activity supported) so it does not attract crime.

**Second generation (social factors):**

- **Social cohesion:** build relationships among the people who use the space, so they look out for each other.
- **Community culture:** shared identity, pride, and activities that give people a stake in the place.
- **Connectivity:** links to outside groups, agencies, and resources (police, local businesses, neighboring communities).
- **Threshold capacity:** limit the concentration of activities or land uses in one area, since too much of one kind (or too many people) can tip a place into becoming a crime attractor.

## Site Selection

Location is the first security decision, and controls cannot fully fix a poor site.

- **Visibility:** how exposed the site is and how much it advertises its contents. A data center is better unmarked.
- **Surroundings:** crime rate, neighbors, and risky neighbors (chemical plants, airports, military targets).
- **Accessibility:** roads, transit, and airports help staff and attackers alike, and traffic affects evacuation.
- **Natural disasters:** flood, earthquake, hurricane, and wildfire exposure (see [[BCP vs DRP]] for alternate sites).
- **Emergency services:** distance to police, fire, and medical response.
- **Utilities:** reliable, redundant power, water, and telecom (see [[Utilities and Equipment Failure]]).
- **Shared buildings:** in leased or multi-tenant space, others control parts of the environment.

## Facility Design

- **Construction:** fire-rated walls and doors, load capacity for heavy equipment, and resistance to forced entry.
- **Sensitive rooms:** in the building **core**, away from exterior walls, public areas, and loading docks. Avoid the ground floor and basement (access, flooding) and the top floor (roof and storm exposure). No signage revealing them, and **industrial camouflage** (making a facility look ordinary so its purpose is hidden) for the building as a whole.
- **Access proportional to value:** restriction rises with the importance and confidentiality of an area. Equal access everywhere is never a security design. Work and visitor areas are separate.
- **Walls:** run floor to true ceiling, not just to a drop ceiling.
- **Doors:** strong frames, hinge pins inside, outward-opening alarmed emergency exits, and few controlled entrances.
- **Windows:** avoid in sensitive rooms. Otherwise use shatter-resistant or translucent glass, and remember windows allow shoulder-surfing and emanation leakage (see [[Emanations and Input Output Devices]]).
- **Floors and ceilings:** raised floors must be grounded and load-rated. The spaces above and below a secure room are part of its perimeter.
- **Separation:** keep public, visitor, employee, and restricted areas apart, and shipping and receiving away from sensitive rooms.

**Fail-safe vs fail-secure.** On power or lock failure a door either **unlocks** (fail-safe) or **stays locked** (fail-secure). Where lives are at stake, such as exits, safety wins and the door fails open. See [[Secure Design Principles]] and [[Physical Security Management]].

## Key Points

- **Critical path analysis** finds what matters most. **Convergence** merges systems onto shared infrastructure: efficient, but a **single point of failure**.
- Functions in order: **deter, deny, detect, delay, determine, decide**.
- **CPTED** first generation: access control, natural surveillance, territorial reinforcement, image/milieu. Second generation (social): social cohesion, community culture, connectivity, threshold capacity.
- Site selection weighs **visibility, surroundings, accessibility, disasters, emergency services, utilities**.
- Sensitive rooms go in the **core**, behind floor-to-true-ceiling walls, unmarked.
- **Life safety overrides asset protection** in how doors fail.
