---
source: notif-server/cmd/libnotif/main.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-11T22:43:29.304811
---

# Mirror: main.go

## 📝 Description
Automatically generated mirror for `notif-server/cmd/libnotif/main.go`.

> **Essential Process**:
> CGO shared library bridge exporting C ABI functions for dispatching direct, multi-channel notifications to notif-server over gRPC (Port 1027).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service.pb.go.md|notif_service.pb.go]] (imports)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|NewNotifServiceClient]] (function: calls)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_Close]] (function: belongs_to) — *export Notif_Close*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_FreeString]] (function: belongs_to) — *export Notif_FreeString*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_GetLastError]] (function: belongs_to) — *export Notif_GetLastError*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_SendWithTimeout]] (function: belongs_to) — *export Notif_SendWithTimeout*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_Send]] (function: belongs_to) — *export Notif_Send*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|getOrInitClient]] (function: belongs_to)
- [[notif-server/notif-server/cmd/libnotif/main.go.md|main]] (function: belongs_to)
- [[notif-server/notif-server/cmd/libnotif/main.go.md|setLastError]] (function: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.hpp]] (calls)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|__init__.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
