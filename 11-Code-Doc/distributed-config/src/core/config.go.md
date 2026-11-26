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
Automatically generated mirror for `distributed-config/src/core/config.go`.

> **Essential Process**:
> Core configuration model defining the unified Config struct, atomic LiveConfig snapshot pointer swaps (RCU), and typed capability extraction helpers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/src/core/config.go.md|Config.Delete]] (method: defines_method) — *If keys slice is empty, removes the entire section.*
- [[distributed-config/src/core/config.go.md|Config.GetAddress]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.GetCapability]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.GetGRPCAddress]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.GetRESTAddress]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.GetVersion]] (method: defines_method) — *GetVersion returns the last applied configuration revision.*
- [[distributed-config/src/core/config.go.md|Config.Get]] (method: defines_method) — *Returns an empty string if not found.*
- [[distributed-config/src/core/config.go.md|Config.PreviewSet]] (method: defines_method) — *before committing locally. Supports "__DELETED__" sentinel values to remove keys.*
- [[distributed-config/src/core/config.go.md|Config.ReplaceLive]] (method: defines_method) — *ReplaceLive atomically replaces the entire live configuration snapshot under writeMu.*
- [[distributed-config/src/core/config.go.md|Config.ResolveCapability]] (method: defines_method) — *Precedence: dotted LiveConfig ("capabilities.<cap>.<k>") > direct LiveConfig ("<cap>.<k>") > static YAML.*
- [[distributed-config/src/core/config.go.md|Config.SetVersion]] (method: defines_method) — *SetVersion atomically updates the tracked configuration revision.*
- [[distributed-config/src/core/config.go.md|Config.Set]] (method: defines_method) — *Performs a thread-safe atomic swap (Read-Copy-Update) serialized by writeMu.*
- [[distributed-config/src/core/config.go.md|Config.ShareConfig]] (method: defines_method) — *ShareConfig merges the provided configuration updates into the LiveConfig.*
- [[distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.getAddr]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.getCapabilityField]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.getListenHostField]] (method: defines_method)
- [[distributed-config/src/core/config.go.md|Config.getStaticCapabilityField]] (method: defines_method)
- [[distributed-config/src/core/service_schemas.go.md|LogServerCap.Validate]] (method: calls) — *Validate ensures all mandatory fields are present.*
- [[distributed-config/src/core/service_schemas.go.md|service_schemas.go]] (same_package)
- [[distributed-config/src/utils/logger.go.md|logger.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/src/core/config.go.md|CommonConfig]] (struct: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.Delete]] (method: belongs_to) — *If keys slice is empty, removes the entire section.*
- [[distributed-config/src/core/config.go.md|Config.GetAddress]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.GetCapability]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.GetGRPCAddress]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.GetRESTAddress]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.GetVersion]] (method: belongs_to) — *GetVersion returns the last applied configuration revision.*
- [[distributed-config/src/core/config.go.md|Config.Get]] (method: belongs_to) — *Returns an empty string if not found.*
- [[distributed-config/src/core/config.go.md|Config.PreviewSet]] (method: belongs_to) — *before committing locally. Supports "__DELETED__" sentinel values to remove keys.*
- [[distributed-config/src/core/config.go.md|Config.ReplaceLive]] (method: belongs_to) — *ReplaceLive atomically replaces the entire live configuration snapshot under writeMu.*
- [[distributed-config/src/core/config.go.md|Config.ResolveCapability]] (method: belongs_to) — *Precedence: dotted LiveConfig ("capabilities.<cap>.<k>") > direct LiveConfig ("<cap>.<k>") > static YAML.*
- [[distributed-config/src/core/config.go.md|Config.SetVersion]] (method: belongs_to) — *SetVersion atomically updates the tracked configuration revision.*
- [[distributed-config/src/core/config.go.md|Config.Set]] (method: belongs_to) — *Performs a thread-safe atomic swap (Read-Copy-Update) serialized by writeMu.*
- [[distributed-config/src/core/config.go.md|Config.ShareConfig]] (method: belongs_to) — *ShareConfig merges the provided configuration updates into the LiveConfig.*
- [[distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.getAddr]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.getCapabilityField]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.getListenHostField]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config.getStaticCapabilityField]] (method: belongs_to)
- [[distributed-config/src/core/config.go.md|Config]] (struct: belongs_to)
- [[distributed-config/src/core/config.go.md|Config]] (struct: defines_method)
- [[distributed-config/src/core/config.go.md|ParseSharePayload]] (function: belongs_to) — *Supports map[string]map[string]string, map[string]string, and map[string]interface{}.*
- [[distributed-config/src/core/config.go.md|isWildcardBindIP]] (function: belongs_to)
- [[distributed-config/src/core/config_test.go.md|config_test.go]] (calls)
- [[distributed-config/src/core/config_test.go.md|config_test.go]] (same_package)
- [[distributed-config/src/facade/config_facade.go.md|config_facade.go]] (calls)
- [[distributed-config/src/facade/config_facade.go.md|config_facade.go]] (imports)
- [[distributed-config/src/interfaces/config_strategy.go.md|config_strategy.go]] (imports)
- [[distributed-config/src/loader/env_loader.go.md|env_loader.go]] (imports)
- [[distributed-config/src/loader/loader.go.md|loader.go]] (imports)
- [[distributed-config/src/loader/loader_test.go.md|loader_test.go]] (calls)
- [[distributed-config/src/loader/loader_test.go.md|loader_test.go]] (imports)
- [[distributed-config/src/loader/path_resolver_test.go.md|path_resolver_test.go]] (imports)
- [[distributed-config/src/loader/validator.go.md|validator.go]] (imports)
- [[distributed-config/src/loader/validator_test.go.md|validator_test.go]] (imports)
- [[distributed-config/src/network/backoff.go.md|backoff.go]] (imports)
- [[distributed-config/src/network/client.go.md|client.go]] (calls)
- [[distributed-config/src/network/client.go.md|client.go]] (imports)
- [[distributed-config/src/network/network_resilience_test.go.md|network_resilience_test.go]] (imports)
- [[distributed-config/src/network/network_test.go.md|network_test.go]] (calls)
- [[distributed-config/src/network/network_test.go.md|network_test.go]] (imports)
- [[distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (calls)
- [[distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (imports)
- [[distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (calls)
- [[distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (imports)
- [[distributed-config/src/strategies/cloud.go.md|cloud.go]] (calls)
- [[distributed-config/src/strategies/cloud.go.md|cloud.go]] (imports)
- [[distributed-config/src/strategies/standalone.go.md|standalone.go]] (calls)
- [[distributed-config/src/strategies/standalone.go.md|standalone.go]] (imports)
- [[distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (calls)
- [[distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (imports)
- [[distributed-config/src/strategies/test.go.md|test.go]] (calls)
- [[distributed-config/src/strategies/test.go.md|test.go]] (imports)
<!-- SYNC:END -->
