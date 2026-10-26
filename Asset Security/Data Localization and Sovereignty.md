Data stored or processed in another country can fall under that country's laws. **Data sovereignty** and **data localization** are two related but different ideas about that, and a third term, **data residency**, often sits between them. **Data portability** is the counterweight: the ability to move data.

## Sovereignty vs Localization

| | Data sovereignty | Data localization |
|---|---|---|
| **Focus** | *Whose law* governs the data, and who has legal authority and access to it | *Where* the data physically is stored or processed |
| **Nature** | A principle: data is subject to the laws of the country where it is located or collected | A requirement: a law that data must stay within the country's borders |
| **Scope** | Applies to any data under the jurisdiction, and some laws reach beyond borders (the GDPR follows EU residents' data wherever the organization is based) | Usually limited to named categories, such as citizens' personal data, financial, health, or government data; may require storage only, or storage and processing |
| **Drivers** | National security, protection of citizens' privacy, control over government access, and reluctance to depend on foreign legal systems | Easier law enforcement and regulator access, privacy and security concerns, protection of critical infrastructure, and promotion of the local economy and data industry |
| **Implications** | Conflicts between laws (a provider may be compelled by its home country to disclose data stored abroad); cross-border transfer restrictions; the provider's country of origin matters as well as the storage location | Higher cost and duplicated infrastructure, less freedom to use global cloud regions, reduced resilience if backups cannot leave, a fragmented internet, and barriers to cross-border services |

**Data residency** is the plain location of the data, often a choice (selecting a cloud region) rather than a legal mandate. Residency is where the data sits, sovereignty is whose law applies to it, and localization is the law that forces it to stay.

Localization is one way a state asserts sovereignty, but sovereignty does not require localization: a country can allow data to leave while still imposing its law on it or restricting transfers to places without adequate protection (see [[Laws]]).

## Why It Is Hard in Practice

Distributed and cloud systems hide location. Data is replicated across regions, backups land elsewhere, content delivery networks cache copies near users, and support staff in other countries may reach the data through remote access. Any of these can move regulated data across a border, or expose it to a foreign legal process, without anyone deciding to.

## Data Portability

**Data portability** is the ability to move data from one service, provider, or system to another in a usable form.

- **Individual right.** Under the GDPR, a data subject can obtain their personal data in a structured, commonly used, machine-readable format and transfer it to another controller (see [[Data Roles]]).
- **Organizational concern.** Portability avoids **vendor lock-in**: if data is held in a proprietary format, leaving a provider is costly or impossible, which affects exit planning and resilience (see [[Supply Chain Risk Management]]).
- **Tension with localization.** Portability is about being free to move data, while localization restricts where it may go. A portable format is useful, but the destination must still satisfy residency and transfer rules.

## Controls

- **Data mapping and inventory.** Know what data is where, including backups and replicas, before deciding what is permitted (see [[Identifying and Classifying Assets]] and [[Information and Asset Handling Requirements]]).
- **Region selection.** Pin storage and processing to approved locations, and constrain cross-region replication and backup for restricted data.
- **Contract terms.** Require the provider to state data locations, forbid relocation without consent, disclose subprocessors, and notify the customer of government access requests (see [[Contracting and Procurement]]). Include exit terms and open export formats for portability.
- **Customer-held encryption keys.** Keys kept under the customer's control in an approved location leave a foreign provider or authority with only ciphertext. This reduces exposure but does not satisfy a mandate that the data itself stay in-country. See [[Symmetric Key Management]].
- **Access restrictions.** Limit remote administrative and support access to personnel in approved locations.

## Key Points

- **Residency, sovereignty, localization.** Where the data is, whose law governs it, and the law requiring it to stay.
- **Sovereignty is about authority, localization is about place.**
- **Location and provider origin both matter.** The storage country's law and the provider's home-country law can conflict.
- **Localization trades resilience, cost, and performance for control.** Apply it where classification and law require it, not everywhere.
- **Portability pulls the other way.** It frees data to move, so it needs to be bounded by the same location rules.
