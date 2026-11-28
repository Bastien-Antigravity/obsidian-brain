---
source: config-server/src/server/server_test.go
workspace: config-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-01 01:10:01.512901
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: server_test.go

## 📝 Description
Automatically generated mirror for `config-server/src/server/server_test.go`.

> **Essential Process**:
> Unit tests for server.Server lifecycle, listener management, collision avoidance, controller accessors with baseline fallbacks, and health telemetry.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: calls)
- [[config-server/src/server/controller.go.md|Server.GetConfig]] (method: calls)
- [[config-server/src/server/controller.go.md|Server.GetStatus]] (method: calls)
- [[config-server/src/server/controller.go.md|Server.SetConfigWithOCC]] (method: calls)
- [[config-server/src/server/controller.go.md|Server.SetConfig]] (method: calls)
- [[config-server/src/server/controller.go.md|controller.go]] (same_package)
- [[config-server/src/server/server.go.md|NewServer]] (function: calls) — *NewServer creates a new Config Server.*
- [[config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: calls)
- [[config-server/src/server/server.go.md|Server.BroadcastFullRefresh]] (method: calls)
- [[config-server/src/server/server.go.md|Server.GetActiveClients]] (method: calls)
- [[config-server/src/server/server.go.md|Server.GetClientNames]] (method: calls)
- [[config-server/src/server/server.go.md|Server.ReloadConfig]] (method: calls)
- [[config-server/src/server/server.go.md|Server.SaveSync]] (method: calls)
- [[config-server/src/server/server.go.md|Server.SetOnUpdate]] (method: calls)
- [[config-server/src/server/server.go.md|Server.TriggerSave]] (method: calls)
- [[config-server/src/server/server.go.md|Server.addListener]] (method: calls)
- [[config-server/src/server/server.go.md|Server.broadcastRegistry]] (method: calls)
- [[config-server/src/server/server.go.md|Server.flushDirtyOnce]] (method: calls)
- [[config-server/src/server/server.go.md|Server.removeListener]] (method: calls)
- [[config-server/src/server/server.go.md|newClientMailbox]] (function: calls)
- [[config-server/src/server/server.go.md|server.go]] (same_package)
- [[config-server/src/server/server_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[config-server/src/server/server_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[config-server/src/server/server_test.go.md|mockLogger.Error]] (method: defines_method)
- [[config-server/src/server/server_test.go.md|mockLogger.Info]] (method: defines_method)
- [[config-server/src/server/server_test.go.md|mockLogger.Warning]] (method: defines_method)
- [[config-server/src/store/persistence.go.md|NewPersistenceManager]] (function: calls) — *NewPersistenceManager creates a new manager for the given file path.*
- [[config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: calls)
- [[config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: calls)
- [[config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/src/store/store.go.md|NewStore]] (function: calls) — *NewStore initializes a new Store with an empty config.*

### 🔌 Consumers (Inbound)
- [[config-server/src/server/connection.go.md|connection.go]] (calls)
- [[config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/src/server/controller.go.md|controller.go]] (calls)
- [[config-server/src/server/controller.go.md|controller.go]] (same_package)
- [[config-server/src/server/server.go.md|server.go]] (calls)
- [[config-server/src/server/server.go.md|server.go]] (same_package)
- [[config-server/src/server/server_test.go.md|TestServer_AddAndRemoveListener]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_BroadcastFullRefreshOnDelete]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_ConcurrentBroadcastAndDisconnectNoPanic]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_ConcurrentOnUpdateAndBroadcast]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_DeterministicRegistrySorting]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_GetConfig_StoreOnly]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_GetStatus]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_OverflowElevatesToFullRefresh]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_PersistenceRetryAndReloadErrorPropagation]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_SaveSyncAndVersionIncrement]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|TestServer_SuperseededListenerClosesMailbox]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|createTestServer]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[config-server/src/server/server_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[config-server/src/server/server_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[config-server/src/server/server_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[config-server/src/server/server_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[config-server/src/server/server_test.go.md|mockLogger]] (struct: belongs_to)
- [[config-server/src/server/server_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
