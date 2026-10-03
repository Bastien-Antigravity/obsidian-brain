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
Automatically generated mirror for `distributed-config/distributed_config.go`.

> **Essential Process**:
> Top-level entrypoint package and alias facade for the distributed-config library, exporting constructors, profile factories, and helper utilities.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|NewConfig]] (function: calls)
- [[distributed-config/distributed-config/src/facade/config_facade_test.go.md|config_facade_test.go]] (imports)
- [[distributed-config/distributed-config/src/loader/validator.go.md|validator.go]] (imports)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|crypto.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/config-cli/main.go.md|main.go]] (calls)
- [[distributed-config/distributed-config/cmd/config-cli/main.go.md|main.go]] (imports)
- [[distributed-config/distributed-config/distributed_config.go.md|Decrypt]] (function: belongs_to) — *Decrypt decrypts a single ENC(...) ciphertext string.*
- [[distributed-config/distributed-config/distributed_config.go.md|New]] (function: belongs_to) — *- "standalone": Local YAML only, No network connection.*
- [[distributed-config/distributed-config/distributed_config.go.md|ProcessConfigSecrets]] (function: belongs_to) — *ProcessConfigSecrets is a helper that decrypts all ENC(...) blocks in a raw byte slice.*
- [[distributed-config/distributed-config/distributed_config.go.md|ProcessNode]] (function: belongs_to) — *ProcessNode is a helper that expands environment variables in a YAML node.*
- [[distributed-config/distributed-config/distributed_config.go.md|ResolveConfigPath]] (function: belongs_to) — *ResolveConfigPath returns the absolute path to the configuration file based on platform search rules.*
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
- [[distributed-config/distributed-config/src/cgo_bridge/security.go.md|security.go]] (imports)
<!-- SYNC:END -->
