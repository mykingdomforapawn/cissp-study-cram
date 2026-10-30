## General Wireless Concepts

Wireless communication sends data over electromagnetic radiation, usually radio, by **modulating** a carrier. **Spectrum** is divided into bands licensed for specific uses or left unlicensed (2.4 GHz, 5 GHz, 6 GHz ISM bands, where Wi-Fi, Bluetooth, and many consumer devices coexist).

**Spread spectrum** techniques spread a signal over a wider band than strictly needed, which improves resistance to interference and makes casual interception harder:

| Technique | How | Where |
|---|---|---|
| **FHSS** (frequency hopping) | The signal hops rapidly between many frequencies in a sequence known to both ends; narrow interference affects only a few hops | Bluetooth (classic, 1600 hops per second), early 802.11, military radios |
| **DSSS** (direct sequence) | Each bit is multiplied by a high-rate "chipping code", spreading it across the band; the receiver recovers the signal and rejects noise | 802.11b, GPS, CDMA cellular |
| **OFDM** (orthogonal frequency-division multiplexing) | Data is split across many closely spaced orthogonal sub-carriers transmitted in parallel; high spectral efficiency and resilience to multipath | 802.11a/g/n/ac/ax, LTE, 5G, DSL |

Points that recur: unlicensed bands mean **interference** from other users is normal; **range** is a function of frequency, power, and antenna; and encryption at the protocol or application layer is the only real confidentiality control, since radio reception cannot be prevented.

## Bluetooth

**Bluetooth (IEEE 802.15)** is a short-range **personal area network (PAN)** technology in the 2.4 GHz band using FHSS, with a nominal range of about 10 m (class 2) to 100 m (class 1), and **Bluetooth Low Energy (BLE)** for battery-powered devices and beacons. Devices **pair** by exchanging keys; legacy pairing used a 4-digit PIN (often 0000 or 1234), modern **Secure Simple Pairing** and BLE Secure Connections use elliptic-curve exchange with numeric comparison.

Attacks (names matter):

| Attack | What it does |
|---|---|
| **Bluejacking** | Sending unsolicited messages or contacts to a nearby device; a nuisance, no data theft |
| **Bluesnarfing** | **Unauthorized access to data** on the device (contacts, calendar, files) over Bluetooth |
| **Bluebugging** | **Taking control** of the device: placing calls, sending messages, listening in; the most severe |
| **Bluesmacking** | Denial of service with oversized L2CAP packets |
| **BlueBorne**, **KNOB** and similar | Protocol-stack exploits that allow takeover without pairing, or that negotiate a key down to one byte of entropy |
| **Tracking** | Persistent device identifiers in advertising frames allow following a person |

Range is the attacker's limit, but directional antennas extend "short range" to over a kilometer. Defenses: keep Bluetooth **off or non-discoverable** when not needed, patch devices, use modern pairing with numeric comparison, refuse unexpected pairing requests, do not transfer sensitive data over Bluetooth, and in secure areas prohibit it through MDM policy (see [[Mobile Device Security Features]]).

## RFID

**Radio frequency identification** uses a reader that energizes and queries a **tag**. **Passive** tags have no battery and are powered by the reader's field (short range, centimeters to a few meters); **active** tags have a battery and transmit on their own (tens of meters or more). Frequencies range from low frequency (animal tags, older access cards) through 13.56 MHz (smart cards, NFC) to UHF (supply chain, toll tags).

Uses: inventory and supply chain tracking, asset tags, **physical access cards** (proximity cards), passports, toll collection. Security issues:

- **Unauthorized reading** (skimming) of a tag from a distance, since many tags reply to any reader.
- **Cloning** of simple tags, including many legacy access cards (125 kHz proximity cards have no cryptography at all).
- **Tracking** of people or goods through their tags.
- **Eavesdropping** on the reader-to-tag exchange, and **replay**.

Controls: tags with mutual authentication and encryption (modern smart cards), shielded sleeves and wallets, limiting read range, and not using cloneable cards for access to anything sensitive (see [[Physical Access Controls]]).

## NFC

**Near-field communication** is a subset of RFID at 13.56 MHz with a range of a few centimeters, designed for deliberate, touch-like interaction: **contactless payments**, transit cards, pairing devices by tapping, and reading tags in posters or products. It supports active-active mode (two devices), reader mode, and card emulation (a phone acting as a payment card).

The short range is the main defense, but it is not a guarantee: relay attacks, skimming with amplified readers, and eavesdropping at a short distance have been demonstrated. Payment implementations therefore add **tokenization** (a one-time card number per transaction), cryptograms, transaction limits, and device unlock requirements. Malicious NFC tags can trigger URLs or actions on a phone that automatically reads them, so phones should prompt before acting on a tag.

## Key Points

- **FHSS hops frequencies (Bluetooth), DSSS spreads with a chipping code (802.11b, GPS), OFDM uses parallel sub-carriers (modern Wi-Fi, LTE, 5G).**
- **Bluejacking = unsolicited messages; bluesnarfing = data theft; bluebugging = device takeover.**
- **Bluetooth defenses: off or non-discoverable, patched, modern pairing, no sensitive data over it.**
- **RFID tags often answer any reader: skimming, cloning, and tracking are the risks; legacy proximity cards are cloneable.**
- **NFC's centimeter range is the main control; payments add tokenization and cryptograms; relay and skimming attacks still exist.**
