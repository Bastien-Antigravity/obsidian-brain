---
source: microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-10-11T22:43:29.279691
---

# Mirror: NotificationClient.hpp

## 📝 Description
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp`.

> **Essential Process**:
> High-level client facade enabling C++ microservices to dispatch direct, multi-channel notifications to notif-server via the libtoolbox C ABI bridge.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetGRPCListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/logger/Logger.hpp.md|Logger.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.EnsureLoaded]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnClose]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnFreeString]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnGetLastError]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnSend]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.Instance]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.NotifBridgeLoader]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.Close]] (method: defines_method) — *Marks the client as closed.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.FromConfig]] (method: defines_method) — *Fails fast if the notif_server capability or its gRPC address is unresolvable.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.NotificationClient]] (method: defines_method) — *Initializes a NotificationClient pointing to a specific target address.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.SendAlert]] (method: defines_method) — *(e.g., "TRADE", "CRITICAL", "WARNING", "REPORT", "INFO") and optional tags.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.SendWithAttachment]] (method: defines_method) — *attachment reference, and destination tags.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.Send]] (method: defines_method) — *with optional destination tags (e.g. "telegram", "discord").*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.SetTimeout]] (method: defines_method) — *Sets default RPC dispatch timeout in seconds.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.TargetAddr]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|MICROSERVICE_TOOLBOX_NOTIFICATION_CLIENT_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_NOTIFICATION_CLIENT_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.EnsureLoaded]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnClose]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnFreeString]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnGetLastError]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.FnSend]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.Instance]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader.NotifBridgeLoader]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotifBridgeLoader]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.Close]] (method: belongs_to) — *Marks the client as closed.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.FromConfig]] (method: belongs_to) — *Fails fast if the notif_server capability or its gRPC address is unresolvable.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.NotificationClient]] (method: belongs_to) — *Initializes a NotificationClient pointing to a specific target address.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.SendAlert]] (method: belongs_to) — *(e.g., "TRADE", "CRITICAL", "WARNING", "REPORT", "INFO") and optional tags.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.SendWithAttachment]] (method: belongs_to) — *attachment reference, and destination tags.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.Send]] (method: belongs_to) — *with optional destination tags (e.g. "telegram", "discord").*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.SetTimeout]] (method: belongs_to) — *Sets default RPC dispatch timeout in seconds.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient.TargetAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/notification/NotificationClient.hpp.md|NotificationClient]] (class: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
