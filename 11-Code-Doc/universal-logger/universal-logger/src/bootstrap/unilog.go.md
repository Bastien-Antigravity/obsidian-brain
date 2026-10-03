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
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.OnConfigUpdate]] (method: calls) — *OnConfigUpdate registers a callback for configuration updates.*
- [[universal-logger/universal-logger/src/config/config_handler.go.md|NewDistributedConfig]] (function: calls) — *NewDistributedConfig initializes a new configuration service.*
- [[universal-logger/universal-logger/src/config/config_handler.go.md|config_handler.go]] (imports)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|NewUniLog]] (function: calls) — *when the logger instance is about to be garbage collected.*
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|logger_handler_test.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.SetLevel]] (method: calls)
- [[universal-logger/universal-logger/src/utils/levels.go.md|GetLogLevel]] (function: calls) — *GetLogLevel converts string to Level.*
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (same_package)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|resilience_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|resilience_test.go]] (same_package)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|BootstrapOptions]] (struct: belongs_to) — *BootstrapOptions defines the configuration parameters for initializes the subsystems.*
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|InitService]] (function: belongs_to) — *selecting the appropriate config and logger profiles automatically.*
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|InitWithOptions]] (function: belongs_to) — *It supports dependency injection (ExistingConfig) and specialized metadata.*
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: belongs_to) — *existingConfig: OPTIONAL. If provided, the logger will use this configuration instance instead of creating a new one.*
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (calls)
<!-- SYNC:END -->
