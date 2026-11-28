---
microservice: config-server
type: note
status: active
tags:
- '#service/config-server'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `config-server/src/server/server.go`.

> **Essential Process**:
> Implements the central Config Server TCP network daemon, managing client mailboxes, broadcast channels, registry notifications, and background state saves.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/src/server/connection.go.md|Server.handleConnection]] (method: calls)
- [[config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.BroadcastFullRefresh]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.GetActiveClients]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.GetClientNames]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.ReloadConfig]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.SaveSync]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.SetOnUpdate]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.Start]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.Stop]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.TriggerSave]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.addListener]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.broadcastRegistry]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.broadcastUpdate]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.flushDirtyOnce]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.persistenceWorker]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.removeListener]] (method: defines_method)
- [[config-server/src/server/server.go.md|clientMailbox.Close]] (method: defines_method)
- [[config-server/src/server/server.go.md|clientMailbox.ensureInit]] (method: defines_method)
- [[config-server/src/server/server_test.go.md|mockLogger.Error]] (method: calls)
- [[config-server/src/server/server_test.go.md|mockLogger.Info]] (method: calls)
- [[config-server/src/server/server_test.go.md|mockLogger.Warning]] (method: calls)
- [[config-server/src/server/server_test.go.md|server_test.go]] (same_package)
- [[config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: calls)
- [[config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: calls)
- [[config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/src/store/store.go.md|Store.Get]] (method: calls) — *Callers MUST treat the returned map as immutable.*
- [[config-server/src/store/store.go.md|Store.Replace]] (method: calls) — *the matching monotonic version under a consistent lock.*
- [[config-server/src/store/store.go.md|Store]] (struct: calls) — *100% lock-free reads while maintaining atomic, side-effect-free updates.*

### 🔌 Consumers (Inbound)
- [[config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (calls)
- [[config-server/src/server/connection.go.md|connection.go]] (calls)
- [[config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/src/server/controller.go.md|controller.go]] (calls)
- [[config-server/src/server/controller.go.md|controller.go]] (same_package)
- [[config-server/src/server/server.go.md|NewServer]] (function: belongs_to) — *NewServer creates a new Config Server.*
- [[config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.BroadcastFullRefresh]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.GetActiveClients]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.GetClientNames]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.ReloadConfig]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.SaveSync]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.SetOnUpdate]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.Start]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.Stop]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.TriggerSave]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.addListener]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.broadcastRegistry]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.broadcastUpdate]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.flushDirtyOnce]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.persistenceWorker]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server.removeListener]] (method: belongs_to)
- [[config-server/src/server/server.go.md|Server]] (struct: belongs_to) — *Server represents the Config Server.*
- [[config-server/src/server/server.go.md|Server]] (struct: defines_method) — *Server represents the Config Server.*
- [[config-server/src/server/server.go.md|clientMailbox.Close]] (method: belongs_to)
- [[config-server/src/server/server.go.md|clientMailbox.ensureInit]] (method: belongs_to)
- [[config-server/src/server/server.go.md|clientMailbox]] (struct: belongs_to)
- [[config-server/src/server/server.go.md|clientMailbox]] (struct: defines_method)
- [[config-server/src/server/server.go.md|newClientMailbox]] (function: belongs_to)
- [[config-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[config-server/src/server/server_test.go.md|server_test.go]] (same_package)
<!-- SYNC:END -->
