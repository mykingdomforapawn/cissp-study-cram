Virtualization adds a layer, the hypervisor and its management tools, that sits beneath every guest, so protecting it matters more than protecting any single VM. See [[Virtualization and Hypervisors]] for the technology.

## Main Risks

- **VM escape.** An attacker breaks out of a guest to reach the hypervisor or other guests, which defeats the isolation that virtualization depends on. A flaw in the hypervisor affects every VM on the host.
- **VM sprawl.** VMs are so easy to create that they multiply without planning or tracking, so there is no layout of what runs where and the host hardware becomes overcommitted. Systems past their **end of service life (EOSL)** make it worse. Forgotten VMs go unpatched, unmonitored, and unowned, and become an entry point.
- **Dormant and offline VMs.** A VM that is powered off or stored as an image misses patches and security updates, and returns vulnerable when started.
- **Snapshots and images.** They contain the full state of a system, including memory, credentials, and data, and need the same protection as the live VM. Restoring an old snapshot can bring back vulnerabilities or revert security settings.
- **Management plane compromise.** Whoever controls the hypervisor console or management APIs controls every VM.
- **Resource contention and side channels.** A busy VM can starve its neighbors (**denial of service**), and shared processor and memory resources can leak information between VMs.
- **VM mobility.** Live migration moves a running VM between hosts, and its memory contents cross the network and are exposed if not encrypted.
- **Mixed sensitivity.** Placing VMs of very different classification on the same host raises the impact of an escape.

## Controls

- **Harden and patch the hypervisor** and keep it current, and minimize the services it runs.
- **Protect the management plane:** a separate, restricted management network, strong authentication with MFA, least privilege, and logging of administrator actions.
- **Control VM lifecycle:** an inventory with owners, approval to create VMs, expiry or review dates, and decommissioning with data removal.
- **Build from hardened gold images,** and keep the images integrity-protected. Patch offline VMs and images, or rebuild them (see [[Microservices, IaC, and Immutable Architecture]]).
- **Segment** VMs by sensitivity and function, and monitor virtual network traffic.
- **Encrypt** VM disks, snapshots, backups, and migration traffic, and control access to the stored images.
- **Limit resource use** with quotas so one VM cannot starve others.

## Key Points

- **The hypervisor and management plane are the critical assets.** Compromising them compromises every guest.
- **Sprawl and dormant VMs are management failures** that turn into security gaps.
- **Snapshots are sensitive data** as well as backups.
