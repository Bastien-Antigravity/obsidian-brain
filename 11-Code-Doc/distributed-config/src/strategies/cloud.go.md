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
Automatically generated mirror for `distributed-config/src/strategies/cloud.go`.

> **Essential Process**:
> Unified cloud configuration strategy implementation for Staging and Production, connecting over safe-socket to config-server for dynamic LiveConfig sync.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/src/core/config.go.md|Config.Delete]] (method: calls) — *If keys slice is empty, removes the entire section.*
- [[distributed-config/src/core/config.go.md|Config.GetCapability]] (method: calls)
- [[distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: calls)
- [[distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/src/loader/env_loader.go.md|LoadCommonFromEnv]] (function: calls)
- [[distributed-config/src/loader/loader.go.md|LoadConfigFromFileSafe]] (function: calls) — *config tags like CF_IP/CF_PORT are provided via ENV variables.*
- [[distributed-config/src/loader/loader.go.md|LoadYAML]] (function: calls) — *consistent string-typing (except for booleans) natively on the node tree.*
- [[distributed-config/src/loader/validator.go.md|CheckProductionIPs]] (function: calls)
- [[distributed-config/src/loader/validator.go.md|validator.go]] (imports)
- [[distributed-config/src/network/backoff_test.go.md|backoff_test.go]] (imports)
- [[distributed-config/src/network/client.go.md|Client.GetConfig]] (method: calls) — *GetConfig fetches configuration from the server.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfigMapWithOCC]] (method: calls) — *Returns ErrVersionConflict if the server version does not match expectedVersion.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfig]] (method: calls) — *UpdateConfig sends the entire current live configuration to the server.*
- [[distributed-config/src/network/client.go.md|Client.Watch]] (method: calls) — *Watch starts a background goroutine to handle asynchronous updates (BROADCASTs).*
- [[distributed-config/src/network/client.go.md|NewClient]] (function: calls) — *NewClient creates a new Config Client and connects to the server.*
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Close]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.DeleteKeysWithOCC]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.DeleteKeys]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.GetHandler]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Load]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Name]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.SetWithOCC]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Set]] (method: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Sync]] (method: defines_method)
- [[distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (same_package)
- [[distributed-config/src/strategies/strategies_test.go.md|strategyTestLogger.Error]] (method: calls)
- [[distributed-config/src/strategies/strategies_test.go.md|strategyTestLogger.Info]] (method: calls)
- [[distributed-config/src/strategies/strategies_test.go.md|strategyTestLogger.Warning]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/src/factory/config_factory.go.md|config_factory.go]] (imports)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Close]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.DeleteKeysWithOCC]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.DeleteKeys]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.GetHandler]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Load]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Name]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.SetWithOCC]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Set]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy.Sync]] (method: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy]] (struct: belongs_to)
- [[distributed-config/src/strategies/cloud.go.md|CloudStrategy]] (struct: defines_method)
- [[distributed-config/src/strategies/cloud.go.md|hydrateCapabilitiesFromLiveConfig]] (function: belongs_to) — *from LiveConfig into cfg.Capabilities before the local YAML override pass.*
- [[distributed-config/src/strategies/cloud.go.md|isWildcardBindIP]] (function: belongs_to) — *overwrite peer-routable DNS addresses in config-server's shared LiveConfig store.*
- [[distributed-config/src/strategies/cloud.go.md|syncCapabilitiesToLiveConfig]] (function: belongs_to) — *into a map[string]map[string]string delta and merges them into cfg.LiveConfig via cfg.Set.*
- [[distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (calls)
- [[distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (same_package)
- [[distributed-config/src/strategies/test.go.md|test.go]] (calls)
- [[distributed-config/src/strategies/test.go.md|test.go]] (same_package)
<!-- SYNC:END -->
