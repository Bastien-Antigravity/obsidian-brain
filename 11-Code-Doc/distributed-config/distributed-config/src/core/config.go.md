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
Automatically generated mirror for `distributed-config/src/core/config.go`.

> **Essential Process**:
> Core configuration model defining the unified Config struct, atomic LiveConfig snapshot pointer swaps (RCU), and typed capability extraction helpers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Apply]] (method: defines_method) — *Use this in conjunction with PreviewSet to avoid redundant calculations.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetAddress]] (method: defines_method) — *It looks for "ip" and "port" keys in the capability configuration.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetCapability]] (method: defines_method) — *GetCapability extracts a specific capability dictionary and unmarshals it into the target struct.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetGRPCAddress]] (method: defines_method) — *Requires explicit 'grpc_port' (and 'grpc_ip' falling back to 'ip').*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetRESTAddress]] (method: defines_method) — *Requires explicit 'rest_port'.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Get]] (method: defines_method) — *Returns an empty string if not found.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.PreviewSet]] (method: defines_method) — *before committing locally.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Set]] (method: defines_method) — *Performs a thread-safe atomic swap (Read-Copy-Update).*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.ShareConfig]] (method: defines_method)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: defines_method)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.getAddr]] (method: defines_method)
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|LogServerCap.Validate]] (method: calls) — *Validate ensures all mandatory fields are present.*
- [[distributed-config/distributed-config/src/core/service_schemas.go.md|service_schemas.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|logger.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/core/config.go.md|CommonConfig]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Apply]] (method: belongs_to) — *Use this in conjunction with PreviewSet to avoid redundant calculations.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetAddress]] (method: belongs_to) — *It looks for "ip" and "port" keys in the capability configuration.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetCapability]] (method: belongs_to) — *GetCapability extracts a specific capability dictionary and unmarshals it into the target struct.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetGRPCAddress]] (method: belongs_to) — *Requires explicit 'grpc_port' (and 'grpc_ip' falling back to 'ip').*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetRESTAddress]] (method: belongs_to) — *Requires explicit 'rest_port'.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Get]] (method: belongs_to) — *Returns an empty string if not found.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.PreviewSet]] (method: belongs_to) — *before committing locally.*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Set]] (method: belongs_to) — *Performs a thread-safe atomic swap (Read-Copy-Update).*
- [[distributed-config/distributed-config/src/core/config.go.md|Config.ShareConfig]] (method: belongs_to)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: belongs_to)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.getAddr]] (method: belongs_to)
- [[distributed-config/distributed-config/src/core/config.go.md|Config]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/core/config.go.md|Config]] (struct: defines_method)
- [[distributed-config/distributed-config/src/core/config.go.md|ParseSharePayload]] (function: belongs_to) — *Supports map[string]map[string]string, map[string]string, and map[string]interface{}.*
- [[distributed-config/distributed-config/src/core/config_test.go.md|config_test.go]] (calls)
- [[distributed-config/distributed-config/src/core/config_test.go.md|config_test.go]] (same_package)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (imports)
- [[distributed-config/distributed-config/src/interfaces/config_strategy.go.md|config_strategy.go]] (imports)
- [[distributed-config/distributed-config/src/loader/env_loader.go.md|env_loader.go]] (imports)
- [[distributed-config/distributed-config/src/loader/loader.go.md|loader.go]] (imports)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (calls)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (imports)
- [[distributed-config/distributed-config/src/loader/validator.go.md|validator.go]] (imports)
- [[distributed-config/distributed-config/src/loader/validator_test.go.md|validator_test.go]] (imports)
- [[distributed-config/distributed-config/src/network/backoff.go.md|backoff.go]] (imports)
- [[distributed-config/distributed-config/src/network/client.go.md|client.go]] (imports)
- [[distributed-config/distributed-config/src/network/network_resilience_test.go.md|network_resilience_test.go]] (imports)
- [[distributed-config/distributed-config/src/network/network_test.go.md|network_test.go]] (calls)
- [[distributed-config/distributed-config/src/network/network_test.go.md|network_test.go]] (imports)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (imports)
- [[distributed-config/distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (calls)
- [[distributed-config/distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|standalone.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/test.go.md|test.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/test.go.md|test.go]] (imports)
<!-- SYNC:END -->
