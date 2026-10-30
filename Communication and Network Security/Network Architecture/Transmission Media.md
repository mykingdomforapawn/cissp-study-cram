## Choosing a Medium

The transmission medium decides **bandwidth, distance, cost, susceptibility to interference, and how easily it can be tapped**. For security the last two matter most: copper radiates and can be tapped with a vampire tap or an inductive clamp; fiber neither radiates nor is tapped without a detectable loss of light.

## Coaxial Cable

A single copper core surrounded by insulation, a braided shield, and an outer jacket. Shielding gives good resistance to **electromagnetic interference (EMI)** and longer runs than early twisted pair, but it is thick, stiff, and expensive, and bus-based coax networks fail entirely when the cable breaks or a terminator is missing.

- **Thinnet (10Base2)**: thinner, about 185 m, BNC connectors.
- **Thicknet (10Base5)**: thicker, about 500 m, vampire taps.

Both are obsolete for LANs; coax survives in cable TV and cable internet (DOCSIS) and in some antenna and video applications.

## Twisted Pair

Pairs of insulated copper wires twisted together; the twisting cancels crosstalk and EMI, and more twists per inch means better resistance. It is cheap, flexible, and easy to install, which is why it is the standard LAN cable, at the cost of a **100 m** maximum run and susceptibility to interference and tapping.

| | Description |
|---|---|
| **UTP** (unshielded) | No shielding; relies on twisting alone; the common office cable |
| **STP** (shielded) | Foil or braid around the pairs or the whole bundle; better EMI resistance, used in noisy environments |

Categories:

| Category | Speed (typical) | Notes |
|---|---|---|
| Cat 3 | 10 Mbps | Voice, legacy 10BaseT |
| Cat 5 | 100 Mbps | Fast Ethernet; superseded |
| **Cat 5e** | 1 Gbps | Minimum for Gigabit Ethernet |
| **Cat 6** | 1 Gbps (10 Gbps to 55 m) | Tighter twisting, often a separator |
| **Cat 6a** | 10 Gbps to 100 m | Standard for new installations |
| Cat 7 | 10 Gbps | Fully shielded; non-standard connectors |
| Cat 8 | 25 to 40 Gbps to 30 m | Data center patching |

Connector: **RJ-45** (8P8C). **RJ-11** is the smaller telephone connector.

## Conductors

Factors limiting copper media, and the reasons fiber was introduced:

- **Attenuation**: signal loss over distance; sets the maximum run length. Repeaters regenerate the signal.
- **EMI and RFI**: interference from motors, fluorescent lights, radio sources; shielding and twisting resist it.
- **Crosstalk**: signal bleeding between adjacent pairs or cables.
- **Emanation**: copper radiates, so the signal can be picked up at a distance (the TEMPEST concern, see [[Emanations and Input Output Devices]]).
- **Fire rating**: **plenum-rated** cable with low-smoke jacketing is required in air-handling spaces; PVC jackets release toxic smoke.
- Cable quality, bend radius, and proper termination all affect reliability.

## Fiber Optic Cable

Transmits **light pulses** through a glass or plastic core. Advantages: very high bandwidth, long distances, **immune to EMI**, **no emanation**, and very hard to tap without being detected (tapping requires bending or splicing and causes measurable loss). Disadvantages: cost, fragility, and the skill needed to terminate and splice.

| | Single-mode (SMF) | Multimode (MMF) |
|---|---|---|
| Core | Very thin (about 9 μm), laser light source, one path | Thicker (50 or 62.5 μm), LED or VCSEL source, many paths |
| Distance | Tens of kilometers | A few hundred meters (up to about 2 km at low speeds) |
| Cost | Higher optics, cheaper cable | Cheaper optics |
| Use | Campus and WAN links, telecom | Inside buildings and data centers |

Connectors: SC, LC (most common today), ST, MTRJ. Fiber is the preferred medium wherever confidentiality or interference is a concern, and for backbone and inter-building links (it also provides electrical isolation between buildings).

## Comparison

| Medium | Max speed | Distance | EMI resistance | Tap resistance | Cost |
|---|---|---|---|---|---|
| Coaxial | Moderate | Hundreds of meters | Good | Low | Moderate |
| UTP | Up to 10 Gbps+ | 100 m | Poor | Low | Low |
| STP | Up to 10 Gbps+ | 100 m | Good | Low | Moderate |
| Fiber | Terabits | Kilometers | Immune | High | High |

## Key Points

- **Fiber: fastest, longest, immune to EMI, no emanations, hardest to tap, most expensive.** Single-mode for distance, multimode for inside buildings.
- **Twisted pair: 100 m limit, Cat 5e for Gigabit, Cat 6a for 10 Gbps to 100 m, STP for noisy environments.**
- **Coax is shielded but obsolete for LANs; a break or missing terminator kills a bus.**
- **Copper can be tapped and radiates; plenum-rated cable is required in air spaces.**
