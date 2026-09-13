A survey of the major legal areas that intersect with security. See [[Categories of Law]] for how these are classified and enforced, and [[State Privacy Laws]] for the US state-level layer on top of the federal laws below.

## Intellectual Property

Protects the products of intellectual effort. Each type protects something different and lasts for a different length of time:

- **Copyright** — protects the expression of an idea (source code, documentation, media); automatic on creation, long duration
- **Trademark** — protects brand identifiers (names, logos, slogans) that distinguish a company's goods/services
- **Patent** — protects inventions and novel processes; requires registration, limited term, then enters the public domain
- **Trade secret** — protects confidential business information (formulas, algorithms) that derives value from secrecy; protected only as long as it stays secret, no registration or expiration

## Computer Crime Law

Laws written specifically to address unauthorized computer access and misuse, rather than general criminal/civil law applied to computers:

- **Computer Fraud and Abuse Act (CFAA)** — the primary US federal computer crime statute; criminalizes unauthorized access to protected computers
- Most countries have an equivalent statute; the common thread is criminalizing *unauthorized access* itself, separate from whatever damage follows
- **Federal Cybersecurity Laws of 2014** — a package of US laws (including FISMA 2014) that formalized NIST's role in setting federal information security standards, tying the legal requirement directly to the NIST frameworks in [[Security Control Frameworks]]

## Software Licensing

Using software also means being bound by its license terms, and failure to comply carries legal exposure similar to other IP violations. The main risk to manage is running unlicensed, under-licensed, or counterfeit software — organizations are subject to license compliance audits by vendors, and violations can mean significant fines. The detailed license types (open source, proprietary, etc.) aren't worth memorizing individually for the exam — the key point is that a license is a legal contract, and using software outside its terms is a compliance failure.

## Privacy Laws (Federal / International)

Regulate how personal data is collected, used, and protected. Each targets a specific sector or jurisdiction:

- **GDPR (General Data Protection Regulation)** — EU regulation; broad scope, applies to any organization processing EU residents' data regardless of where the organization is based; strong individual rights (access, erasure, portability)
- **HIPAA (Health Insurance Portability and Accountability Act)** — US; protects health information (PHI)
- **GLBA (Gramm-Leach-Bliley Act)** — US; protects financial information held by financial institutions
- **SOX (Sarbanes-Oxley Act)** — US; financial reporting integrity and controls for public companies, not privacy per se, but drives a lot of IT control and audit requirements (ties into [[Security Control Frameworks]] via COBIT)
- **COPPA (Children's Online Privacy Protection Act)** — US; protects data of children under 13 online
- **FERPA (Family Educational Rights and Privacy Act)** — US; protects student education records

## Import/Export Controls

Restrict the cross-border movement of technology, particularly strong encryption, treated similarly to controlled goods:

- **EAR (Export Administration Regulations)** — controls export of dual-use items (commercial + military applications)
- **ITAR (International Traffic in Arms Regulations)** — controls export of defense-related articles and technical data

Encryption software has historically been treated as a controlled munition under these regimes, so exporting or open-sourcing strong cryptography can carry legal restrictions depending on jurisdiction and destination.
