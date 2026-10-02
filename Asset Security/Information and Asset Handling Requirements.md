Once an asset is classified (see [[Identifying and Classifying Assets]]), that classification has to translate into concrete rules for how it's handled across its lifecycle — otherwise classification is just a label with no effect.

- **Data maintenance** — keeping data accurate, up to date, and consistent with its classification as it's used and modified over time
- **DLP (Data Loss Prevention)** — the program/process of monitoring and blocking unauthorized movement of sensitive data (e.g., blocking an email with a credit card number from leaving the network); the technical tooling that implements this sits alongside the controls in [[Data Protection Methods]]. Deployed at different points depending on where data needs to be caught:
	- **Network DLP** — inspects traffic leaving the network (email, web uploads) for sensitive content
	- **Endpoint DLP** — runs on the device itself, catching actions like copying data to a USB drive or printing before it ever reaches the network
	- **Cloud DLP** — monitors data moving to/from cloud services and SaaS applications, often delivered through a [[Data Protection Methods|CASB]]
- **Labeling** — marking data (headers, footers, metadata, physical media stickers) with its classification so handlers know what rules apply without needing separate lookup
- **Collection limitations** — only collect the data actually needed for the stated purpose; reduces both handling burden and exposure if a breach occurs. A core privacy principle (echoed in GDPR's data minimization requirement, see [[Laws]])
- **Data location** — where data is stored and processed, particularly across borders; data residency/sovereignty requirements may restrict which countries data can legally be stored or transferred to
- **Storing sensitive data** — storage must meet controls appropriate to the classification tier (encryption, access restriction, physical security for media). This applies to backup copies too: a backup is only as protected as its weakest storage location, so an off-site copy needs a secured, access-controlled facility — not just an unstaffed warehouse — to match the protection the original data has on-site
- **Destruction** — sanitization method must match classification sensitivity:
	- **Erasing** — simply deleting the file; the weakest method, since it typically only removes the pointer/link to the data (e.g., the file table entry) while the underlying data remains recoverable until overwritten
	- **Clear** — overwrite media for reuse within the organization; protects against ordinary recovery tools
	- **Purge** — more intensive sanitization (degaussing, cryptographic erase) for media leaving organizational control. Degaussing only works on magnetic media (HDDs, tapes) — it has no effect on SSDs or other flash media, since there's no magnetic flux to disrupt. Purging flash media instead requires a cryptographic erase or the drive's vendor-specific secure-erase command
	- **Destroy** — physical destruction (shredding, incineration) when the media itself must not survive
- **Retention** — how long data must be kept, driven by legal/regulatory requirements or business need; expired data should be destroyed rather than kept indefinitely, and a **legal hold** suspends normal retention/destruction schedules when litigation or investigation is anticipated
