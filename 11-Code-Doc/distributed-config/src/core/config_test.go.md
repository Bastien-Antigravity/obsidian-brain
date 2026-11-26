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
Automatically generated mirror for `distributed-config/src/core/config_test.go`.

> **Essential Process**:
> Unit and concurrency tests validating atomic pointer swapping (RCU), lock-free read consistency, and capability resolution in the core Config struct.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/src/core/config.go.md|Config.Delete]] (method: calls) — *If keys slice is empty, removes the entire section.*
- [[distributed-config/src/core/config.go.md|Config.GetAddress]] (method: calls)
- [[distributed-config/src/core/config.go.md|Config.GetCapability]] (method: calls)
- [[distributed-config/src/core/config.go.md|Config.GetGRPCAddress]] (method: calls)
- [[distributed-config/src/core/config.go.md|Config.GetRESTAddress]] (method: calls)
- [[distributed-config/src/core/config.go.md|Config.GetVersion]] (method: calls) — *GetVersion returns the last applied configuration revision.*
- [[distributed-config/src/core/config.go.md|Config.Get]] (method: calls) — *Returns an empty string if not found.*
- [[distributed-config/src/core/config.go.md|Config.ResolveCapability]] (method: calls) — *Precedence: dotted LiveConfig ("capabilities.<cap>.<k>") > direct LiveConfig ("<cap>.<k>") > static YAML.*
- [[distributed-config/src/core/config.go.md|Config.SetVersion]] (method: calls) — *SetVersion atomically updates the tracked configuration revision.*
- [[distributed-config/src/core/config.go.md|Config.Set]] (method: calls) — *Performs a thread-safe atomic swap (Read-Copy-Update) serialized by writeMu.*
- [[distributed-config/src/core/config.go.md|Config.ShareConfig]] (method: calls) — *ShareConfig merges the provided configuration updates into the LiveConfig.*
- [[distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: calls)
- [[distributed-config/src/core/config.go.md|config.go]] (same_package)
- [[distributed-config/src/core/defaults.go.md|NewDefaultConfig]] (function: calls)
- [[distributed-config/src/core/defaults.go.md|defaults.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/src/core/config_test.go.md|TestConfig_Concurrency]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_ConcurrentWritersNoLostUpdates]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_DynamicCapabilityGetAddress]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_ResolveCapabilityAndVersion]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_SetAndGet]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_ShadowPort]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_ShareConfig]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_ValidateMandatoryServices]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|TestConfig_WildcardBindPreservedOverLiveConfig]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|iterations]] (constant: belongs_to)
- [[distributed-config/src/core/config_test.go.md|workers]] (constant: belongs_to)
<!-- SYNC:END -->
