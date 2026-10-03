---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|config.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|config.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|UniLog_RegisterVBAWindow]] (function: belongs_to) — *export UniLog_RegisterVBAWindow*
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump_stub.go.md|dispatchConfigurationUpdate]] (function: belongs_to) — *update on non-Windows platforms (Standard FFI Callback only).*
<!-- SYNC:END -->
