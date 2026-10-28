Barriers only delay, so they need **detection** and **response**. Sensors detect events, **alarms** announce them, and **verification** confirms them before costly response. These are **detective** controls (see [[Security Controls]], [[Defense in Depth]]).

## Intrusion Detection Systems

A physical IDS has **sensors**, a **control panel**, and **alerting** to guards or a monitoring center.

**Perimeter breach detection** senses an attempt to cross or open a boundary:

- **Door and window contacts** (magnetic switches).
- **Glass-break sensors** (sound or vibration).
- **Vibration and shock sensors** on walls, fences, and safes.
- **Fence sensors** and **buried or microwave beams** across open ground (PIDAS).
**Motion detectors** sense movement **inside** a space:

| Type | How it detects |
|---|---|
| **Passive infrared (PIR)** | Body **heat** against the background. Most common, emits nothing |
| **Wave pattern** | Transmits a steady **ultrasonic** or **microwave** signal and detects disturbances in the reflected pattern. Microwave can pass through some walls, so may false-alarm |
| **Photoelectric** | Senses changes in **visible light** levels. Used in dark, windowless interior rooms (a broken light beam works similarly) |
| **Capacitance** | Senses changes in the **electric or magnetic field** around a monitored object, such as a safe |
| **Dual-technology** | Needs **two** methods to trigger, cutting false alarms |

**Intrusion alarms:**

- **Local:** sounds on site, deters, needs someone to respond.
- **Central station / proprietary:** signals a **monitoring center** that dispatches guards or police.
- **Auxiliary:** connects directly to police or fire stations.
- **Deterrent/repellent** alarms (loud, bright) scare intruders off. **Silent notification** alarms alert staff.
- **Protect the alarm itself:** **tamper protection**, **backup power**, and secure signaling (such as cellular backup if lines are cut). It should fail in a way that raises an alert.

**Tuning:** poorly tuned sensors give **false positives** that teach staff to ignore alarms, or **false negatives** that miss real events.

## Secondary Verification Mechanisms

An alarm alone is not proof: it may be an animal, a draft, or a fault. **Secondary verification** confirms it before dispatch, reducing false responses.

- **Cameras** to view the area.
- **Two-sensor confirmation**, or dual-technology detectors.
- **Audio** monitoring or two-way audio.
- **Guard dispatch** to inspect.
- **Call-back** to the authorized person.

## Cameras and CCTV

**CCTV** provides **detection, verification, deterrence,** and **evidence**. Visible cameras deter, and recordings support investigation.

- **Coverage:** clear sight lines to entry and exit points, all exterior walls, and interior hallways, plus valuable assets and public areas such as parking structures and walkways.
- **Overt vs hidden:** visible cameras give a **deterrent** benefit, concealed ones mainly **detect**.
- **Types:** **fixed** (single view, reliable), **PTZ** (pan-tilt-zoom, covers wide areas), **dome** (hides lens direction), **infrared/low-light**, and **IP** cameras (flexible, but with the convergence risks in [[Facility Planning and Design]]).
- **Lens:** a wide angle covers more area, a longer lens gives detail at distance, and **resolution** must suffice to identify people.
- **Placement:** cover entrances, perimeters, and sensitive areas, avoiding blind spots, glare, and backlight (see [[Perimeter Security Controls]]).
- **Live monitoring** allows real-time response, while **recording** alone only helps afterwards. Recordings need adequate retention, secure storage, and **integrity protection** to serve as evidence.
- **Embedded intelligence:** some cameras have a **system on a chip (SoC)** that adds time-lapse, tracking, facial recognition, object detection, or infrared and color-filtered recording. These reduce operator load but raise accuracy and **privacy** questions. Simple **motion-triggered** cameras can be fooled by animals, birds, insects, weather, or foliage.
- **Privacy:** notify people, do not film where privacy is expected (restrooms, changing rooms), and limit access to footage (see [[Laws]]).
- Protect cameras with tamper protection, backup power, and patching and segmentation.

## Key Points

- A physical IDS = **sensors, panel, alerting**. Sensors cover **perimeter breach** (contacts, glass break, vibration, beams) and **motion** (**PIR**, ultrasonic, microwave, dual-technology).
- **PIR** senses heat. **Ultrasonic and microwave** emit energy and detect change. **Dual-technology** cuts false alarms.
- Alarms: **local**, **central station**, **auxiliary**, with tamper protection, backup power, secure signaling.
- **Secondary verification** (cameras, second sensor, guard check) confirms alarms before response.
- **CCTV** deters, detects, and records. **Live monitoring** gives response, **recording** gives evidence, and both need privacy compliance and cybersecurity.
