Storage devices hold data over the long term. Their security concerns are persistent data and who can reach the media. Disposal is covered in [[Information and Asset Handling Requirements]] and [[Data Protection Methods]].

## Classifying Storage

| Dimension | Types |
|---|---|
| **Primary vs secondary** | **Primary** storage is memory the CPU addresses directly, namely RAM and ROM (see [[Memory]]), and is fast and small. **Secondary** storage is larger, slower, persistent storage that the CPU cannot address directly, such as hard disks, SSDs, tape, optical discs, and USB drives |
| **Volatile vs nonvolatile** | **Volatile** storage loses its content without power (RAM). **Nonvolatile** storage keeps it (ROM, flash, disks, tape, optical) |
| **Random vs sequential** | **Random access** devices reach any location directly and about equally fast (RAM, disks, SSDs). **Sequential access** devices must be read in order from the start (magnetic tape), so reaching data far along is slow. Tape is cheap and dense, so it remains common for backup and archive |

## Common Media

- **Magnetic hard disk drives (HDDs)** store data magnetically on spinning platters.
- **Solid state drives (SSDs)** store data in flash memory with no moving parts, and are faster. They spread writes evenly across cells (**wear leveling**) and keep spare capacity, so data may remain in cells the operating system cannot address.
- **Magnetic tape** is sequential and used for backup and archive.
- **Optical discs** (CD, DVD, Blu-ray) are written by a laser. Many are write-once, and they must be physically destroyed to be sanitized.
- **Removable media**, such as USB flash drives and memory cards, is small, easy to lose, and a route for both data theft and malware.
- **Network storage**, such as SAN and NAS, puts storage behind a network and so adds the usual network access controls to the concerns.

## Storage Media Security

- **Data remanence.** Deleting a file only removes its reference. The data stays on the media until overwritten, and sometimes even then. Sanitization must match the media and its sensitivity: overwriting works for magnetic disks, **degaussing** works only on magnetic media, and **SSDs** need cryptographic erase or the drive's secure-erase command because of wear leveling. Optical media and others where nothing else works get physically destroyed.
- **Theft and loss.** Portable and removable media is the most common source of exposure. **Encryption** (full-disk or file-level) makes a lost device a lesser incident, as it protects the data at rest (see [[Portable Devices and TPM]]).
- **Unauthorized access.** Storage needs access controls and physical security, and backups need the same protection as the originals, including off-site copies.
- **Malware and data exfiltration.** Removable media can carry malware in or data out, which is why organizations restrict or control USB ports.
- **Integrity and availability.** Media fails, so redundancy (such as RAID) and tested backups protect availability, and checksums or hashes can detect corrupted or altered data.
- **End of life.** Media leaving the organization, or being reused, must be sanitized to the sensitivity of the data it held, and the method recorded.

## Key Points

- **Primary** is directly addressed by the CPU, **secondary** is persistent bulk storage.
- **Tape is sequential**, while disks and flash are random access.
- **Deleted is not erased.** Remanence is the core storage risk, and the sanitization method must fit the media type.
- **SSDs break the old assumptions** about overwriting and degaussing, so cryptographic erase is the usual answer.
- **Encryption at rest** reduces the impact of lost or stolen media.
