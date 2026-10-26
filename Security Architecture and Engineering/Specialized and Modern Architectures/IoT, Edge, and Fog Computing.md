## Internet of Things (IoT)

**IoT** devices are network-connected everyday objects with sensors, such as cameras, thermostats, wearables, smart-home gear, and medical monitors, that collect and exchange data. They are embedded devices (see [[Embedded and Cyber-Physical Systems]]) built cheaply, in large numbers, and often with little security.

**Concerns:**
- Default or hard-coded credentials, and no way to update firmware.
- Insecure or unencrypted communication, and weak vendor support.
- Scale and poor visibility: many devices, some unknown to IT (shadow IoT).
- **Botnets:** compromised devices are used for DDoS attacks (Mirai).
- **Privacy:** devices collect personal data, such as video, audio, location, and health.

**Controls:** the most effective single measure is keeping devices **updated**. Do not give them public IP addresses (that exposes them to the internet), and do not simply cut their internet access, because that blocks updates, cloud features, and app control. Put them on a separate network segment, change default credentials, keep an inventory, apply updates where available, disable unused features, and buy from vendors that commit to security support.

## Edge Computing

**Edge computing** processes data **close to where it is generated**, on the device or a nearby gateway, instead of sending everything to a central cloud. It cuts latency and bandwidth use, and keeps working if the connection to the cloud is lost.

A **content delivery network** is a familiar example: many small servers placed close to users (for instance inside ISPs) serve common content locally and fall back to the central servers only for what they lack.

**Concerns:** many scattered locations are hard to secure physically and to patch, and each edge node is another place where data lives and attacks can start.

## Fog Computing

**Fog computing** adds an **intermediate layer** between the edge and the cloud: local nodes such as gateways, routers, or on-site servers that gather and process data from many edge devices before passing results on.

| Layer | Where | Role |
|---|---|---|
| **Edge** | On or beside the device | Immediate local processing |
| **Fog** | Local network, between devices and cloud | Aggregation and processing for many devices |
| **Cloud** | Central data centers | Heavy analysis and long-term storage |

The terms are used loosely, and some sources treat fog as a form of edge computing. The security concerns are the same as for the edge: more distributed nodes to protect and update, and the need to protect data moving between the layers.

## Key Points

- **IoT devices are weakly secured by default**, so segmentation, inventory, and removing defaults come first.
- **Edge is processing at the device, fog is the layer in between, cloud is central.**
- **Distribution brings benefits (speed, bandwidth) and costs a larger, harder-to-manage attack surface.**
