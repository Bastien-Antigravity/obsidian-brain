---
source: notif-server/notif/cpp/NotificationClient.hpp
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-11T22:43:29.330479
---

# Mirror: NotificationClient.hpp

## 📝 Description
Automatically generated mirror for `notif-server/notif/cpp/NotificationClient.hpp`.

> **Essential Process**:
> C++ RAII facade and header-only wrapper for notif-server direct alert dispatch, binding to the libnotif CGO shared object.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_FreeString]] (function: calls) — *export Notif_FreeString*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_GetLastError]] (function: calls) — *export Notif_GetLastError*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_SendWithTimeout]] (function: calls) — *export Notif_SendWithTimeout*
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.Close]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.IsClosed]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.LastError]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.NotificationClient]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.SendAlert]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.SendWithAttachment]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.Send]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.SetTimeout]] (method: defines_method)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.TargetAddr]] (method: defines_method)
- [[notif-server/notif-server/notif/libnotif/libnotif.h.md|libnotif.h]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|integration_test.go]] (calls)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NOTIF_NOTIFICATION_CLIENT_HPP]] (macro: belongs_to) — *ifndef NOTIF_NOTIFICATION_CLIENT_HPP*
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.Close]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.IsClosed]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.LastError]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.NotificationClient]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.SendAlert]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.SendWithAttachment]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.Send]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.SetTimeout]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient.TargetAddr]] (method: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient]] (class: belongs_to)
- [[notif-server/notif-server/notif/cpp/NotificationClient.hpp.md|NotificationClient]] (class: defines_method)
- [[notif-server/notif-server/src/server/timeout_test.go.md|timeout_test.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
