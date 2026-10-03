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
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|InitWithOptions]] (function: calls) — *It supports dependency injection (ExistingConfig) and specialized metadata.*
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls) — *existingConfig: OPTIONAL. If provided, the logger will use this configuration instance instead of creating a new one.*
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (same_package)
- [[universal-logger/universal-logger/src/config/config_handler.go.md|DistConfig.SetConfig]] (method: calls) — *Subsystems monitoring updates via OnConfigUpdate will be notified.*
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|LogWithMetadata]] (function: calls) — *It delegates directly to LogWithCaller on the Logger interface for maximum performance.*
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|TestConfigInjection]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|TestDynamicLogLevelFiltering_ConfigurationSync]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|TestLocalNotification_LevelThresholdAndPayload]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|TestLocalNotification_NonBlockingOnSaturation]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|TestLogLevelSynchronization]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|TestManualNotifierBinding]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|TestMetadataInjection]] (function: belongs_to)
<!-- SYNC:END -->
