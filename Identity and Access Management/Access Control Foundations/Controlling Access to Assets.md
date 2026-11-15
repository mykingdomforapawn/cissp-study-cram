Access control is the practice of deciding which **subjects** may act on which **objects**, and in what way. Everything in this domain is a variation on that sentence.

## Subjects and Objects

- **Subject** — the active entity requesting access: a user, a process, a service, a device.
- **Object** — the passive entity being accessed: a file, a database row, a room, a network segment.

The roles are **relative to the request, not fixed**. A process is a subject when it reads a file; it is an object when a user stops it. A print server is an object to the user and a subject to the printer.

## Assets Worth Protecting

Access control protects **information** (the data itself), **systems** (servers, applications, services), **devices** (endpoints, mobile, removable media), and **facilities** (buildings, floors, cabinets). Controls are selected against the asset's classification — see [[Identifying and Classifying Assets]].

## Physical vs. Logical Access Controls

| | **Physical** | **Logical (technical)** |
|---|---|---|
| Restricts | Movement of people and hardware | Actions of subjects on data and systems |
| Examples | Fences, mantraps, badge readers, locks, guards | Authentication, ACLs, firewalls, encryption, MFA |
| Failure mode | Someone walks in | Someone logs in |
| Detail in | [[Physical Access Controls]], [[Perimeter Security Controls]] | This domain |

The two enforce the **same policy at different layers**, and neither substitutes for the other: full-disk encryption does not stop a stolen server, and a locked cabinet does not stop a stolen password. Physical access generally **wins** — a subject with unrestricted physical access can eventually defeat the logical controls on a device, which is why physical compromise is treated as total compromise.

A third category, **administrative** controls (policies, training, access reviews), directs how the other two are applied. See [[Security Controls]].

## CIA and Access Control

Access control is the primary enforcement of **confidentiality** (only authorized subjects reach the data) and **integrity** (only authorized subjects change it), while over-restriction harms **availability**. See [[CIA Triad]] for the triad itself.

## Key Points

- **Subject is the active requester, object the passive target, and the roles swap with the request.**
- **Physical controls restrict movement, logical controls restrict actions, administrative controls direct both.**
- **Physical access defeats logical controls given time — the layers are complementary, not redundant.**
