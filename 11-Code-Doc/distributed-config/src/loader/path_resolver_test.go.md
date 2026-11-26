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
Automatically generated mirror for `distributed-config/src/loader/path_resolver_test.go`.

> **Essential Process**:
> Unit test suite verifying configuration path resolution priority across CWD, config/ subdirectory, executable directory, and fallback binary names.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/src/loader/loader.go.md|LoadConfigFromFileSafe]] (function: calls) — *config tags like CF_IP/CF_PORT are provided via ENV variables.*
- [[distributed-config/src/loader/loader.go.md|loader.go]] (same_package)
- [[distributed-config/src/loader/path_resolver.go.md|ResolveConfigPath]] (function: calls)
- [[distributed-config/src/loader/path_resolver.go.md|path_resolver.go]] (same_package)
- [[distributed-config/src/utils/logger.go.md|EnsureSafeLogger]] (function: calls) — *In strict mode (STRICT_LOGGER=true), it panics immediately.*
- [[distributed-config/src/utils/logger.go.md|logger.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/src/loader/path_resolver_test.go.md|TestResolveConfigPath]] (function: belongs_to)
<!-- SYNC:END -->
