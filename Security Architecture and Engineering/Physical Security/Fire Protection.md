Fire threatens life first and assets second, and damages through smoke, heat, and suppression agents as well as flames. Protection combines **prevention**, **detection**, and **suppression**, with building design that limits spread. Life safety always comes first (see [[Physical Security Management]]).

## Fire Triangle and Classes

A fire needs **fuel, oxygen, and heat** plus a sustaining reaction. Removing one element puts it out:

| Method | Element removed |
|---|---|
| **Water** | Heat |
| **Gas / CO2** | Oxygen |
| **Dry powder / soda acid** | Fuel (or the reaction) |

The extinguisher must match the fire class:

| Class | Fuel | Suitable agents |
|---|---|---|
| **A** | Common combustibles (wood, paper) | Water, soda acid |
| **B** | Flammable liquids | Gas (CO2, halon replacements), soda acid |
| **C** | Electrical | Gas, non-conductive agents. **Never water** |
| **D** | Combustible metals | Dry powder |
| **K** | Cooking oils and fats | Wet chemicals |

## Stages of Fire

A fire develops through four stages, and earlier detection gives more time to respond:

| Stage | What happens | Detected by |
|---|---|---|
| **1. Incipient** | Air ionizes, but there is no visible smoke or flame | Ionization and air-sampling detectors |
| **2. Smoke** | Smoke becomes visible in the air | Smoke detectors |
| **3. Flame** | Flames become visible | Flame detectors |
| **4. Heat** | Intense heat and rapidly rising temperature | Heat detectors |

Suppression is most effective and least damaging in the first stages, so the earlier stages are the best place to detect.

## Prevention

- **Training** in the fire plan, evacuation routes, and extinguisher use.
- **Control fuel and ignition:** limit combustibles in sensitive rooms, restrict open flames, maintain electrical systems.
- **Fire-resistant construction:** fire-rated walls, doors, and floors form compartments, and openings are sealed. **Plenum-rated** cabling is used in air spaces.
- **Regular inspection** of alarms, extinguishers, suppression, and exits.

## Extinguishers

First response for small fires. They are class-labeled, visible, near exits, inspected on schedule, and staff are trained. Evacuate if the fire is not quickly controlled.

## Detection

| Type | Detects by |
|---|---|
| **Fixed temperature** | Reaching a set temperature (e.g., sprinkler fusible link) |
| **Rate of rise** | Rapid temperature increase. Faster than fixed |
| **Flame** | Infrared or ultraviolet energy |
| **Smoke: ionization** | Smoke disturbing an ionized air current |
| **Smoke: photoelectric** | Smoke scattering or blocking a light beam |
| **Air sampling** | Draws air to a sensor for **very early** detection (data centers) |

Place detectors above and below ceilings and raised floors, and connect them to a monitoring station. Smoke detection reacts earlier. Heat detection has fewer false alarms. Detectors **only** in a drop ceiling miss fires in the room below (**false negatives**).

## Water Suppression

| System        | How it works                                                                  | Notes                                                           |
| ------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Wet pipe**  | Pipes **always filled**. A heat-triggered head opens                          | Fast and simple. Leak and **freeze** risk                       |
| **Dry pipe**  | Pipes hold **pressurized air**. Water enters after a head opens               | No freezing, but **slower**                                     |
| **Preaction** | Dry pipe with **two triggers**: a detector fills the pipes, then a head opens | Time to stop accidental release. **Preferred for data centers** |
| **Deluge**    | **Open heads**, all discharge at once                                         | High-hazard areas, not equipment rooms                          |

Water protects life and structure cheaply but damages electronics. Preaction mitigates this with its delay and double trigger. The most common cause of an unwanted discharge (false positive) is **human error**: a pulled alarm with no fire, or a water supply left shut off after a fire and never reopened.

## Gas Discharge

Gas suppresses fire by removing oxygen, without residue or water damage, so it does the **least damage to computer systems** and can act faster than water. It suits **data centers and equipment rooms**, but because it removes oxygen it is usable only where **human presence is minimal**, not facility-wide.

- **Halon** **depletes the ozone layer** and is banned under the **Montreal Protocol**.
- **Replacements:** **FM-200**, **Novec 1230**, and inert gases (argon, nitrogen, Inergen).
- **CO2** removes oxygen, so it is **dangerous to people** and used only in unoccupied areas or with safeguards.
- Needs a **sealed room** to hold concentration, a **pre-discharge delay and alarm** so people can leave or abort, and regular recharge and maintenance. It is costlier than water.

## Damage

- **Smoke** is often the biggest source of loss. It spreads far and harms equipment, media, and people.
- **Heat** damages media at about **100°F (38°C)**, hardware at about **175°F (79°C)**, and paper at about **350°F (177°C)**. Media needs a media-rated safe.
- **Suppression:** water causes electrical damage and corrosion, so power off and dry equipment.
- **Secondary:** HVAC spreads smoke, and corrosive combustion by-products keep damaging after the fire.

Recovery is covered in [[BCP vs DRP]].

## Key Points

- Four stages: **incipient** (ionization, no smoke), **smoke**, **flame**, **heat**. Detect early.
- Fire needs **fuel, oxygen, heat**. **Match extinguisher to class (A, B, C, D, K)**. Never water on class C.
- **Detection:** heat (fixed, rate of rise), flame, smoke (ionization, photoelectric), air sampling.
- **Wet** fastest, **dry** avoids freezing, **preaction** (two triggers) suits data centers, **deluge** floods.
- **Halon** is banned, replaced by **FM-200**, Novec 1230, inert gases. **CO2** endangers people.
- **Smoke and suppression** often damage more than flames. **Life safety** first.
