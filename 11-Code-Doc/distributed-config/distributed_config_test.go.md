---
source: distributed-config/distributed_config_test.go
workspace: distributed-config
type: code-mirror
status: auto-generated
last_sync: 2026-11-16 15:02:39.336828
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: distributed_config_test.go

## 📝 Description
Automatically generated mirror for `distributed-config/distributed_config_test.go`.

> **Essential Process**:
> Top-level entrypoint test suite validating facade constructors, node processing, path resolution, and secret decryption helpers.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed_config.go.md|Decrypt]] (function: calls) — *Decrypt decrypts a single ENC(...) ciphertext string.*
- [[distributed-config/distributed_config.go.md|New]] (function: calls) — *- "standalone": Local YAML only, No network connection.*
- [[distributed-config/distributed_config.go.md|ProcessConfigSecrets]] (function: calls) — *ProcessConfigSecrets is a helper that decrypts all ENC(...) blocks in a raw byte slice.*
- [[distributed-config/distributed_config.go.md|ProcessNode]] (function: calls) — *ProcessNode is a helper that expands environment variables in a YAML node.*
- [[distributed-config/distributed_config.go.md|ResolveConfigPath]] (function: calls) — *ResolveConfigPath returns the absolute path to the configuration file based on platform search rules.*
- [[distributed-config/distributed_config.go.md|distributed_config.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed_config_test.go.md|TestTopLevel_EnvironmentOverride]] (function: belongs_to)
- [[distributed-config/distributed_config_test.go.md|TestTopLevel_New]] (function: belongs_to)
- [[distributed-config/distributed_config_test.go.md|TestTopLevel_ProcessNode]] (function: belongs_to)
- [[distributed-config/distributed_config_test.go.md|TestTopLevel_ResolveConfigPath]] (function: belongs_to)
- [[distributed-config/distributed_config_test.go.md|TestTopLevel_Secrets]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
