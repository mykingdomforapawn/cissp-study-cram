Three modern ways of building and running systems. They are related, and are often used together in cloud environments.

## Microservices

A **microservice** architecture builds an application as many small, independent services, each doing one function with its own process and data, and communicating through APIs. It contrasts with a **monolith**, a single deployed unit. Microservices derive from **service-oriented architecture (SOA)**, which builds new applications out of existing, separate software services. Microservices take this further into single-purpose functions that other software calls through a clearly defined API. Because an application assembled from services is new, its combined security is untested, so each service's API must be secured.

- **Benefits:** services can be deployed, scaled, and patched independently, and a compromise or failure can be contained to one service (smaller blast radius).
- **Concerns:** many more APIs and network connections to protect, **service-to-service authentication and authorization**, secrets management, and tracing activity across services for logging and detection.
- **Controls:** an API gateway, mutual TLS between services, least-privilege service identities, segmentation, and scanning of container images (an application of zero trust, see [[Secure Design Principles]]).

## Infrastructure as Code (IaC)

**IaC** defines servers, networks, and configuration in **machine-readable files** (Terraform, CloudFormation, Ansible) that tooling applies automatically, instead of configuring by hand.

- **Benefits:** repeatable, consistent builds, version control and review of every change, and security baselines enforced from the start. Environments can be rebuilt quickly.
- **Concerns:** a mistake or insecure setting is **replicated at scale**, secrets can end up in code repositories, and whoever controls the repository and the pipeline controls the infrastructure.
- **Controls:** code review, automated scanning of templates for misconfiguration, secrets kept in a vault, restricted access to the repository and pipeline, and drift detection to find manual changes (see [[Information System Lifecycle]] for the change-control side).

## Immutable Architecture

In an **immutable** architecture, a deployed component is **never modified**. To change or patch it, a new instance is built from an updated image and **replaces** the old one.

- **Benefits:** no configuration drift, patching means rebuilding, tampering or persistence is wiped out by redeploying, and rollback is simple.
- **Concerns:** the **image and build pipeline** become critical, since a compromised image is replicated everywhere. State must be kept outside the instance, in external storage. Evidence on a replaced instance is lost unless logs are collected first.

## Key Points

- **Microservices** make small independent services, and security shifts to the APIs and the service-to-service trust.
- **IaC** treats infrastructure as code, so it gets code's benefits (review, versioning) and code's risks (errors at scale, leaked secrets).
- **Immutable** means replace, don't repair. Protect the image and pipeline, and keep data and logs outside the instance.
