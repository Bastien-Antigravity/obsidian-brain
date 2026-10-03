---
source: config-server/src/server/server_test.go
workspace: config-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.512901
---

# Mirror: server_test.go

## 📝 Description
Automatically generated mirror for `config-server/src/server/server_test.go`.

> **Essential Process**:
> Unit tests for server.Server lifecycle, listener management, collision avoidance, controller accessors with baseline fallbacks, and health telemetry.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: calls) — *DeleteConfig deletes a configuration key atomically and broadcasts the change.*
- [[config-server/config-server/src/server/controller.go.md|Server.GetConfig]] (method: calls) — *GetConfig returns a specific configuration value from the dynamic store.*
- [[config-server/config-server/src/server/controller.go.md|Server.GetStatus]] (method: calls) — *GetStatus returns the health status, active client counts, and client names.*
- [[config-server/config-server/src/server/controller.go.md|Server.SetConfig]] (method: calls) — *SetConfig updates a configuration value atomically and broadcasts the change.*
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (same_package)
- [[config-server/config-server/src/server/server.go.md|NewServer]] (function: calls) — *NewServer creates a new Config Server.*
- [[config-server/config-server/src/server/server.go.md|Server.GetActiveClients]] (method: calls) — *GetActiveClients returns the current number of connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.addListener]] (method: calls) — *addListener adds a client mailbox to the broadcast list.*
- [[config-server/config-server/src/server/server.go.md|Server.removeListener]] (method: calls) — *removeListener removes a client from the broadcast list only if it's the same instance.*
- [[config-server/config-server/src/server/server.go.md|server.go]] (same_package)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Error]] (method: defines_method)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Info]] (method: defines_method)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Warning]] (method: defines_method)
- [[config-server/config-server/src/store/persistence.go.md|NewPersistenceManager]] (function: calls) — *NewPersistenceManager creates a new manager for the given file path.*
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|NewStore]] (function: calls) — *NewStore initializes a new Store with an empty config.*

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (calls)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (same_package)
- [[config-server/config-server/src/server/server.go.md|server.go]] (calls)
- [[config-server/config-server/src/server/server.go.md|server.go]] (same_package)
- [[config-server/config-server/src/server/server_test.go.md|TestServer_AddAndRemoveListener]] (function: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|TestServer_GetConfig_StoreOnly]] (function: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|TestServer_GetStatus]] (function: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|createTestServer]] (function: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger]] (struct: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
