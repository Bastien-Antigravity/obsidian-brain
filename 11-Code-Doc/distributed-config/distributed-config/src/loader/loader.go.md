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
Automatically generated mirror for `distributed-config/src/loader/loader.go`.

> **Essential Process**:
> YAML configuration loader, file creator, and regex-based ${VAR:default} environment variable expansion engine.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/core/defaults.go.md|NewDefaultConfig]] (function: calls)
- [[distributed-config/distributed-config/src/core/merger.go.md|DeepMerge]] (function: calls) — *Entries in source override entries in target.*
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/loader/loader.go.md|EnsureFileExists]] (function: belongs_to) — *EnsureFileExists checks if a file exists. If it doesn't, it creates it using the provided payload.*
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadConfigFromFileSafe]] (function: belongs_to) — *config tags like CF_IP/CF_PORT are provided via ENV variables.*
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadConfigFromFile]] (function: belongs_to) — *and Test profiles to allow instant "Zero-Config" local bootstrap.*
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadYAML]] (function: belongs_to) — *consistent string-typing (except for booleans) natively on the node tree.*
- [[distributed-config/distributed-config/src/loader/loader.go.md|ProcessNode]] (function: belongs_to) — *It expands env variables and forces all scalars to strings, except for booleans.*
- [[distributed-config/distributed-config/src/loader/loader.go.md|loadPublicKey]] (function: belongs_to) — *loadPublicKey attempts to find and load public.pem into Common.PublicKey*
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (calls)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (same_package)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|standalone.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/test.go.md|test.go]] (calls)
<!-- SYNC:END -->
