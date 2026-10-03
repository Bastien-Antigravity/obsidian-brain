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
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls) — *existingConfig: OPTIONAL. If provided, the logger will use this configuration instance instead of creating a new one.*
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (imports)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.GetConfig]] (method: calls) — *Get returns a configuration value for a given section and key.*
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.OnConfigUpdate]] (method: calls) — *OnConfigUpdate registers a callback for configuration updates.*
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.SetConfig]] (method: calls) — *Subsystems monitoring updates via OnConfigUpdate will be notified.*
- [[universal-logger/universal-logger/src/utils/levels.go.md|GetLogLevel]] (function: calls) — *GetLogLevel converts string to Level.*
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
