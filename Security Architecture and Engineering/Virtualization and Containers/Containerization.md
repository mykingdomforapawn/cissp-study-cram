**Containerization** (OS-level virtualization) packages an application with its libraries and dependencies into a **container**, which runs as an isolated process on a shared host operating system. Containers are built from **images**, and **Docker** is the common format, with **Kubernetes** commonly **orchestrating** (deploying, scaling, and healing) many containers.

## Containers vs VMs

|                         | Virtual machine                              | Container                                                             |
| ----------------------- | -------------------------------------------- | --------------------------------------------------------------------- |
| **What is virtualized** | The hardware, so each VM has its own full OS | The operating system, so containers share the host's **kernel**       |
| **Size and start-up**   | Gigabytes, and starts in minutes             | Megabytes, and starts in seconds                                      |
| **Density**             | Fewer per host                               | Many more per host                                                    |
| **Isolation**           | Stronger, enforced by the hypervisor         | Weaker, enforced by the shared kernel (namespaces and control groups) |
| **Portability**         | Moderate                                     | High: the same image runs the same way anywhere                       |

Because containers do not each carry a full guest OS, the same hardware can run many more workloads, which is the answer when capacity is short and no new hardware can be bought. Containers trade isolation for efficiency and speed. They are the natural runtime for microservices and fit immutable deployments (see [[Microservices, IaC, and Immutable Architecture]]), and the application sandboxing in [[Techniques for Ensuring CIA]] is this idea.

## Security Concerns

- **Shared kernel.** A kernel vulnerability, or a container escape, can expose the host and every other container on it.
- **Vulnerable or malicious images.** Images include outdated libraries, and public images may be untrusted or contain malware.
- **Secrets in images.** Credentials baked into an image or its build history leak to everyone who can pull it.
- **Excess privilege.** Containers run as root or with extra capabilities (**privileged** containers) greatly widen the impact of a compromise.
- **Orchestrator misconfiguration.** An exposed or poorly secured Kubernetes API or dashboard gives control of the cluster.
- **Flat networking.** By default, containers can often talk to each other freely.

## Controls

- **Scan images** for vulnerabilities, build from minimal trusted base images, and pull only **signed** images from trusted registries.
- **Run with least privilege:** non-root users, no privileged mode, read-only file systems, and limited capabilities.
- **Keep secrets out of images,** and supply them at runtime through a secrets manager.
- **Patch the host kernel** and the orchestrator, and secure the orchestrator's API and access control.
- **Segment containers** with network policies, and monitor them at runtime.
- **Treat containers as disposable:** rebuild and redeploy to update instead of patching in place.

## Key Points

- **Containers share the host kernel**, so they are lighter than VMs and less strongly isolated.
- **The image is the unit of trust.** Scan it, sign it, and keep secrets out of it.
- **Least privilege and kernel patching** limit the impact of an escape.
