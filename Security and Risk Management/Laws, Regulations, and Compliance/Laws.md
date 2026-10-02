A survey of the major legal areas that intersect with security. See [[Categories of Law]] for how these are classified and enforced, and [[State Privacy Laws]] for the US state-level layer on top of the federal laws below.

## Intellectual Property

Protects the products of intellectual effort. Each type protects something different and lasts for a different length of time:

- **Copyright** — protects the expression of an idea (source code, documentation, media); automatic on creation, lasts 70 years after the death of the last surviving author
- **Trademark** — protects brand identifiers (names, logos, slogans) that distinguish a company's goods/services; use ™ while registration is pending, ® once it's granted
- **Patent** — protects inventions and novel processes, but not abstract ideas or mathematical algorithms themselves; requires registration, lasts 20 years from the application date, then enters the public domain
- **Trade secret** — protects confidential business information (formulas, algorithms) that derives value from secrecy; protected only as long as it stays secret, no registration or expiration — and no protection at all once the information is voluntarily published

## Computer Crime Law

Laws written specifically to address unauthorized computer access and misuse, rather than general criminal/civil law applied to computers:

- **Computer Fraud and Abuse Act (CFAA)** — the primary US federal computer crime statute; criminalizes unauthorized access to protected computers
- Most countries have an equivalent statute; the common thread is criminalizing *unauthorized access* itself, separate from whatever damage follows
- **Federal Information Security Management Act (FISMA)** — governs information security at US federal agencies; authority over classified systems sits with the NSA, authority over all other federal systems sits with NIST
- **Federal Cybersecurity Laws of 2014** — a package of US laws (including FISMA 2014) that formalized NIST's role in setting federal information security standards, tying the legal requirement directly to the NIST frameworks in [[Security Control Frameworks]]
- **Communications Assistance for Law Enforcement Act (CALEA)** — requires communications carriers (phone and network providers, not financial, healthcare, or general web businesses) to build in the ability to assist law enforcement in executing lawful wiretaps

## Software Licensing

Using software also means being bound by its license terms, and failure to comply carries legal exposure similar to other IP violations. The main risk to manage is running unlicensed, under-licensed, or counterfeit software — organizations are subject to license compliance audits by vendors, and violations can mean significant fines. The detailed license types (open source, proprietary, etc.) aren't worth memorizing individually for the exam — the key point is that a license is a legal contract, and using software outside its terms is a compliance failure.

## Privacy Laws (Federal / International)

Regulate how personal data is collected, used, and protected. Each targets a specific sector or jurisdiction:

- **GDPR (General Data Protection Regulation)** — EU regulation; broad scope, applies to any organization processing EU residents' data regardless of where the organization is based; strong individual rights (access, erasure, portability). Transferring personal data outside the EU requires a lawful mechanism — **standard contractual clauses** (the default choice between two separate companies), **binding corporate rules** (for transfers within a single corporate group), or an adequacy decision; the EU/US Privacy Shield that used to serve this purpose is no longer valid
- **HIPAA (Health Insurance Portability and Accountability Act)** — US; protects health information (PHI). A covered entity may only share PHI with a third-party service provider under a **business associate agreement (BAA)**, which extends HIPAA liability to that provider
- **GLBA (Gramm-Leach-Bliley Act)** — US; protects financial information held by financial institutions
- **SOX (Sarbanes-Oxley Act)** — US; financial reporting integrity and controls for public companies, not privacy per se, but drives a lot of IT control and audit requirements (ties into [[Security Control Frameworks]] via COBIT)
- **COPPA (Children's Online Privacy Protection Act)** — US; requires parental consent before collecting personal information from children under 13 online
- **FERPA (Family Educational Rights and Privacy Act)** — US; protects student education records
- **Privacy Act of 1974** — US; restricts how federal government agencies may use and disclose personal information that individuals provide to them

## Constitutional Protections

- **Fourth Amendment** — restricts government search and seizure of private property; sets the "probable cause" standard and generally requires a warrant before law enforcement can gain involuntary access to a residence or facility. Distinct from the Privacy Act above, which constrains how agencies handle information people voluntarily give them, not physical searches.

## Import/Export Controls

Restrict the cross-border movement of technology, particularly strong encryption, treated similarly to controlled goods:

- **EAR (Export Administration Regulations)** — controls export of dual-use items (commercial + military applications)
- **ITAR (International Traffic in Arms Regulations)** — controls export of defense-related articles and technical data
- **BIS (Bureau of Industry and Security)** — the Department of Commerce agency that administers and enforces EAR, including the export of encryption products

Encryption software has historically been treated as a controlled munition under these regimes, so exporting or open-sourcing strong cryptography can carry legal restrictions depending on jurisdiction and destination.
