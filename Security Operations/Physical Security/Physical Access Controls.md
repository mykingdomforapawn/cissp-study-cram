Physical access controls follow the [[AAA Framework]]: **identify**, **authenticate**, **authorize** entry, and **log** it, with least privilege and need-to-know.

## Badges and Smartcards

- **ID badges** show identity visually (photo, name) and often use **color coding** for access level or visitor status. They support challenge culture but are easy to forge alone.
- **Smartcards** carry a **chip** that stores credentials or a certificate and can perform cryptography. The card is **something you have**, and pairing it with a **PIN** or **biometric** gives multifactor access.
- **Magnetic stripe** cards are old and easy to clone.
- **Lost or stolen** cards must be revoked quickly, so issuance follows identity verification and cards are returned on departure (see [[Personnel Security Lifecycle]]).

## Proximity Devices

**Proximity cards and fobs** use **RFID** and open a door when held near a reader.

| Type | Description |
|---|---|
| **Passive** | No battery, powered by the **reader's field**, very short range |
| **Semi-passive** | Battery powers the circuit, reader field powers the response |
| **Active** | **Battery**, transmits on its own, **longer range** (vehicle gates, tracking) |

They are convenient, but legacy cards can be **cloned** by a nearby reader (skimming) and work for any finder. Encrypted exchanges are more secure, and sensitive areas should add a **PIN or biometric**.

## Locks, Keys, and Combination Logs

- **Preset (mechanical)** locks (key locks, deadbolts, padlocks) are cheap, but keys can be copied and lost, and there is **no record** of use.
- **Programmable** locks (keypad, cipher, electronic) can be **re-keyed instantly**, and keep **audit logs** and schedules.
- **Biometric** locks authenticate by a physical trait (see [[AAA Framework]]).
- Frames, hinges, and deadbolts matter as much as the lock.

**Key and combination management:**

- Keep a **key inventory and log** with sign-out for shared keys. Use **master keys** sparingly, since a lost master compromises many locks.
- **Change combinations and codes** when someone leaves, when compromised, and on a schedule.
- **Rekey** after lost keys, and limit duplication.
- **Review logs** regularly (see [[Intrusion Detection and Monitoring]]).

## Access Abuses

- **Tailgating:** following an authorized person through a door **without** their knowledge.
- **Piggybacking:** entering **with** their knowledge or help, such as a held door.
- **Credential sharing**, borrowed or lent badges, **propped doors**, disabled alarms.
- **Forged or cloned badges**, lock picking, and bypassing via windows or loading docks.
- **Insider misuse:** entering areas without need.
- **Social engineering:** posing as delivery, vendor, or maintenance staff (see [[Social Engineering]]).

**Countermeasures:**

- **Person traps and turnstiles** admitting one person at a time (see [[Perimeter Security Controls]]), and guards at critical entrances.
- **Anti-passback:** a card that entered must exit before re-entering, so it cannot be passed back.
- **Door-held-open and forced-door alarms**, with camera review (see [[Intrusion Detection and Monitoring]]).
- **Awareness training** so staff challenge unbadged people and report lost badges (see [[Security Awareness, Training, and Education]]).
- **Access reviews** and logging.

## Key Points

- **Smartcards** (chip, cryptography) beat plain badges and magnetic stripe. Add a **PIN or biometric** for multifactor.
- **Proximity:** **passive** (no battery, short range), **active** (battery, longer range). Cloning is the main risk.
- **Programmable locks** allow quick re-keying and logs. Preset locks leave **no record**. Keep key and combination logs, and rekey or change codes after loss or departures.
- **Tailgating** is **without** the authorized person's knowledge, **piggybacking** **with** it.
- Counter abuse with **person traps, anti-passback, alarms, and trained staff**.
