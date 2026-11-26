---
microservice: universal-logger
type: note
status: active
tags:
- '#service/universal-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump.go.md|UniLog_RegisterVBAWindow]] (function: belongs_to) — *export UniLog_RegisterVBAWindow*
- [[universal-logger/universal-logger/src/cgo_bridge/vba_message_pump.go.md|dispatchConfigurationUpdate]] (function: belongs_to) — *update to the correct destination (VBA Message Pump and/or Standard FFI Callback).*
<!-- SYNC:END -->
