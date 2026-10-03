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

## 📝 Description
Automatically generated mirror for `distributed-config/src/loader/path_resolver.go`.

> **Essential Process**:
> Multi-tier configuration file path resolver evaluating explicit environment variables (CONFIG_PATH), caller stack heuristics, working directories, and binary names.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/loader/path_resolver.go.md|ResolveConfigPath]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/path_resolver.go.md|getCallerDir]] (function: belongs_to) — *This provides an extremely robust anchor for 'go run' where os.Executable is in /tmp/.*
- [[distributed-config/distributed-config/src/loader/path_resolver_test.go.md|path_resolver_test.go]] (calls)
- [[distributed-config/distributed-config/src/loader/path_resolver_test.go.md|path_resolver_test.go]] (same_package)
<!-- SYNC:END -->
