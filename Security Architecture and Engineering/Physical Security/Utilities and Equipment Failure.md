Systems depend on utilities (power, cooling, water) and on equipment continuing to work. Failures are availability events (see [[CIA Triad]]), handled with redundancy, monitoring, and replacement planning.

## Equipment Failure

| Metric | Meaning |
|---|---|
| **MTTF** (mean time to failure) | Expected lifetime of a device that is replaced, **not repaired** |
| **MTBF** (mean time between failures) | Expected time between failures of a **repairable** system |
| **MTTR** (mean time to repair) | Average time to restore a failed system |

- Use MTTF and MTBF to replace gear **before** expected end of life and to decide where redundancy is needed. Low MTTR shortens downtime.
- **SLAs** with vendors set maximum repair or replacement time and must match the recovery objectives from the [[Business Impact Analysis]].
- Keep **spares**, remove **single points of failure** with redundant components and failover (see [[Techniques for Ensuring CIA]]), and monitor health, since aging hardware is the main source of failures.

## Power

| Event                 | Description                                       |
| --------------------- | ------------------------------------------------- |
| **Blackout**          | Complete loss of power (a **fault** is momentary) |
| **Brownout / sag**    | **Low** voltage                                   |
| **Surge / spike**     | **High** voltage                                  |
| **Inrush**            | Surge when equipment is switched on               |
| **Noise / transient** | Interference on the line                          |

- **UPS** bridges outages with batteries until the generator starts or systems shut down cleanly. **Online (double-conversion)** gives the cleanest power. **Standby** and **line-interactive** switch to battery on a problem.
- **Generators** give long-term power and need fuel, regular testing, and an automatic transfer switch.
- **Surge protectors** and **line conditioners** smooth spikes and noise.
- **Redundant feeds** from separate sources, and dedicated circuits for critical gear.
- **Emergency power off (EPO)** switches need protection from accidental use.

## Noise (EMI and RFI)

Motors, fluorescent lights, power lines, and transmitters create **EMI/RFI** that can corrupt data. Countermeasures: shielded cable or fiber, **separating** data cables from power lines, **grounding**, and shielded rooms. See also [[Emanations and Input Output Devices]].

## Temperature, Humidity, and Static

HVAC is a security control as well as a comfort one.

- **Temperature:** **59-89.6°F (15-32°C)** is the acceptable range, and operators often hold it tighter (about 60-75°F). Overheating shortens equipment life, so cooling needs redundancy and monitoring.
- **Humidity:** **20-80% relative humidity** is acceptable (about 40-60% is a common tighter target). Above 80% causes **condensation and corrosion**, below 20% causes **static**.
- **Static (ESD)** can damage components at levels people cannot feel. Use humidity control, anti-static flooring, grounding, and wrist straps.
- **Airflow:** hot aisle/cold aisle layouts. **Positive pressure** pushes air out, keeping dust and smoke out.
- HVAC can spread fire and smoke, so ducts have **fire dampers** and shut down on alarm (see [[Fire Protection]]).

## Water Issues

Leaks, burst pipes, flooding, condensation, and sprinkler discharge all threaten equipment.

- Keep critical gear **away from water pipes** and out of basements.
- **Leak detection** under raised floors and near cooling gear.
- **Drainage** and raised equipment where water could collect.
- Known, accessible, tested **shut-off valves**.
- Account for flood risk in site selection (see [[Facility Planning and Design]]).

## Key Points

- **MTTF** non-repairable, **MTBF** repairable, **MTTR** repair time. SLAs and spares support recovery objectives.
- **Blackout** = loss, **sag/brownout** = low, **spike/surge** = high. A **UPS** bridges to a **generator**.
- **Shielding, separation, grounding** reduce EMI/RFI.
- **59-89.6°F and 20-80% humidity** are the acceptable ranges. Low humidity means static, high means corrosion.
- **Hot aisle/cold aisle** layout fixes heat buildup from densely stacked, unorganized equipment.
- Keep equipment away from water pipes, with leak detection and accessible shut-offs.
