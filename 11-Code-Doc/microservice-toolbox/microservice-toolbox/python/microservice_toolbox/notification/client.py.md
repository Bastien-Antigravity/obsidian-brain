---
source: microservice-toolbox/python/microservice_toolbox/notification/client.py
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-10-11T22:43:29.045159
---

# Mirror: client.py

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/notification/client.py`.

> **Essential Process**:
> High-level client facade enabling L2 and L3 Python microservices to send direct, multi-channel notifications to notif-server via the libnotif CGO shared library bridge.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_grpc_listen_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/lib_loader.py.md|lib_loader.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/lib_loader.py.md|load_libnotif]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|DEFAULT_TIMEOUT]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|NotificationClient]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|_dispatch_c_call]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|close]] (function: belongs_to) — *Closes active notification client.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|close_sync]] (function: belongs_to) — *Closes notification client immediately.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|from_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|new_client]] (function: belongs_to) — *Initializes a NotificationClient dynamically from AppConfig (Go NewClient parity).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|new_client_with_target]] (function: belongs_to) — *Initializes a NotificationClient with an explicit target address (Go NewClientWithTarget parity).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|send]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|send_alert]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|send_alert_sync]] (function: belongs_to) — *Synchronous helper dispatching a categorized alert.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|send_sync]] (function: belongs_to) — *Synchronous helper dispatching an untyped notification.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|send_with_attachment]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|send_with_attachment_sync]] (function: belongs_to) — *Synchronous helper dispatching a notification over blocking libnotif bridge.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|set_timeout]] (function: belongs_to) — *Sets default RPC dispatch timeout in seconds.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
