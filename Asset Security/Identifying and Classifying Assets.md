Before anything can be protected, it has to be found and rated. This starts with an **asset inventory** — a catalog of the information and systems the organization holds — since a classification scheme is meaningless applied to an incomplete list. Classification is then assigned by the **Asset Owner** (see [[Organizational Roles and Responsibilities]]), based on criteria like value, sensitivity, criticality to operations, and any regulatory requirement that mandates a specific level.

## Classification Tiers

Two common tier sets show up in study material, and it's worth knowing both exist rather than treating either as *the* standard — classification labels are not standardized across organizations or sources:

- **Commercial** — Confidential/Proprietary, Private, Sensitive, Public (highest to lowest)
- **Government/Military** — Top Secret, Secret, Confidential, Unclassified

The exact labels matter less than the underlying idea: every tier maps to a defined set of handling rules (see [[Information and Asset Handling Requirements]]), and higher tiers mean stricter rules.

## Special Data Categories

Some data types carry classification requirements independent of an organization's general scheme, usually because a specific law or regulation applies to them directly:

- **PII (Personally Identifiable Information)** — data that can identify a specific individual (name, SSN, address); triggers privacy law obligations (see [[Laws]], [[State Privacy Laws]])
- **PHI (Protected Health Information)** — health-related data tied to an individual; regulated specifically under HIPAA
- **Proprietary data** — information that gives the organization a competitive edge (formulas, source code, business processes); overlaps with the trade secret protections in [[Laws]]

## Data States

Classification and handling requirements apply differently depending on where data currently sits — this is the dimension the protection methods in [[Data Protection Methods]] are built around:

- **At rest** — stored on disk, in a database, or on backup media
- **In transit** — moving across a network
- **In use** — actively being processed in memory, the hardest state to protect since it must be readable to be useful
