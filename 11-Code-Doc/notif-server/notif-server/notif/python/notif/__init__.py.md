---
source: notif-server/notif/python/notif/__init__.py
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-11T22:43:29.324057
---

# Mirror: __init__.py

## 📝 Description
Automatically generated mirror for `notif-server/notif/python/notif/__init__.py`.

> **Essential Process**:
> Standalone Python client wrapper for notif-server via libnotif CGO bridge.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_FreeString]] (function: calls) — *export Notif_FreeString*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_GetLastError]] (function: calls) — *export Notif_GetLastError*
- [[notif-server/notif-server/cmd/libnotif/main.go.md|Notif_SendWithTimeout]] (function: calls) — *export Notif_SendWithTimeout*

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|NotifClient]] (class: belongs_to)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|NotifError]] (class: belongs_to) — *Exception raised when notification dispatch fails.*
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|__init__]] (function: belongs_to)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|_dispatch]] (function: belongs_to)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|_load_lib]] (function: belongs_to)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|close]] (function: belongs_to)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|send]] (function: belongs_to)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|send_alert]] (function: belongs_to)
- [[notif-server/notif-server/notif/python/notif/__init__.py.md|send_with_attachment]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
