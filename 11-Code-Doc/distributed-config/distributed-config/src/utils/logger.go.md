---
microservice: distributed-config
type: note
status: active
tags:
- '#service/distributed-config'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `distributed-config/src/utils/logger.go`.

> **Essential Process**:
> Standardized logging abstraction compatible with universal-logger and microservice-toolbox, providing fallback no-op and console sinks.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Critical]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Debug]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Info]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Logon]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Logout]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Report]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Schedule]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Stream]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Trade]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (imports)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (calls)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (imports)
- [[distributed-config/distributed-config/src/loader/path_resolver_test.go.md|path_resolver_test.go]] (calls)
- [[distributed-config/distributed-config/src/loader/path_resolver_test.go.md|path_resolver_test.go]] (imports)
- [[distributed-config/distributed-config/src/network/network_resilience_test.go.md|network_resilience_test.go]] (calls)
- [[distributed-config/distributed-config/src/network/network_resilience_test.go.md|network_resilience_test.go]] (imports)
- [[distributed-config/distributed-config/src/utils/logger.go.md|EnsureSafeLogger]] (function: belongs_to) — *In strict mode (STRICT_LOGGER=true), it panics immediately.*
- [[distributed-config/distributed-config/src/utils/logger.go.md|Logger]] (interface: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Critical]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Debug]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Info]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Logon]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Logout]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Report]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Schedule]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Stream]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Trade]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Warning]] (method: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger]] (struct: defines_method)
- [[distributed-config/distributed-config/src/utils/logger_test.go.md|logger_test.go]] (calls)
- [[distributed-config/distributed-config/src/utils/logger_test.go.md|logger_test.go]] (same_package)
<!-- SYNC:END -->
