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
Automatically generated mirror for `config-server/src/server/server.go`.

> **Essential Process**:
> Implements the central Config Server TCP network daemon, managing client mailboxes, broadcast channels, registry notifications, and background state saves.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/server/connection.go.md|Server.handleConnection]] (method: calls)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: defines_method) — *BroadcastConfig sends a full configuration update to all connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.GetActiveClients]] (method: defines_method) — *GetActiveClients returns the current number of connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.GetClientNames]] (method: defines_method) — *GetClientNames returns the names of all currently connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.ReloadConfig]] (method: defines_method) — *ReloadConfig reloads the configuration from the base YAML file.*
- [[config-server/config-server/src/server/server.go.md|Server.Start]] (method: defines_method) — *Start listens for incoming TCP connections.*
- [[config-server/config-server/src/server/server.go.md|Server.Stop]] (method: defines_method) — *Stop signals the server to shutdown.*
- [[config-server/config-server/src/server/server.go.md|Server.TriggerSave]] (method: defines_method) — *TriggerSave marks the state as dirty to trigger background persistence.*
- [[config-server/config-server/src/server/server.go.md|Server.addListener]] (method: defines_method) — *addListener adds a client mailbox to the broadcast list.*
- [[config-server/config-server/src/server/server.go.md|Server.broadcastRegistry]] (method: defines_method) — *broadcastRegistry sends the list of all connected active clients.*
- [[config-server/config-server/src/server/server.go.md|Server.broadcastUpdate]] (method: defines_method) — *broadcastUpdate sends configuration updates to all connected client mailboxes.*
- [[config-server/config-server/src/server/server.go.md|Server.persistenceWorker]] (method: defines_method) — *persistenceWorker periodically saves the configuration to disk if dirty.*
- [[config-server/config-server/src/server/server.go.md|Server.removeListener]] (method: defines_method) — *removeListener removes a client from the broadcast list only if it's the same instance.*
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Error]] (method: calls)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Info]] (method: calls)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Warning]] (method: calls)
- [[config-server/config-server/src/server/server_test.go.md|server_test.go]] (same_package)
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Save]] (method: calls) — *prevent file corruption in case of crashes during the write process.*
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls) — *Callers MUST treat the returned map as immutable.*
- [[config-server/config-server/src/store/store.go.md|Store]] (struct: calls) — *remains untouched (Atomicity/Rollback).*

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (calls)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (calls)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (same_package)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (same_package)
- [[config-server/config-server/src/server/server.go.md|NewServer]] (function: belongs_to) — *NewServer creates a new Config Server.*
- [[config-server/config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: belongs_to) — *BroadcastConfig sends a full configuration update to all connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.GetActiveClients]] (method: belongs_to) — *GetActiveClients returns the current number of connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.GetClientNames]] (method: belongs_to) — *GetClientNames returns the names of all currently connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.ReloadConfig]] (method: belongs_to) — *ReloadConfig reloads the configuration from the base YAML file.*
- [[config-server/config-server/src/server/server.go.md|Server.Start]] (method: belongs_to) — *Start listens for incoming TCP connections.*
- [[config-server/config-server/src/server/server.go.md|Server.Stop]] (method: belongs_to) — *Stop signals the server to shutdown.*
- [[config-server/config-server/src/server/server.go.md|Server.TriggerSave]] (method: belongs_to) — *TriggerSave marks the state as dirty to trigger background persistence.*
- [[config-server/config-server/src/server/server.go.md|Server.addListener]] (method: belongs_to) — *addListener adds a client mailbox to the broadcast list.*
- [[config-server/config-server/src/server/server.go.md|Server.broadcastRegistry]] (method: belongs_to) — *broadcastRegistry sends the list of all connected active clients.*
- [[config-server/config-server/src/server/server.go.md|Server.broadcastUpdate]] (method: belongs_to) — *broadcastUpdate sends configuration updates to all connected client mailboxes.*
- [[config-server/config-server/src/server/server.go.md|Server.persistenceWorker]] (method: belongs_to) — *persistenceWorker periodically saves the configuration to disk if dirty.*
- [[config-server/config-server/src/server/server.go.md|Server.removeListener]] (method: belongs_to) — *removeListener removes a client from the broadcast list only if it's the same instance.*
- [[config-server/config-server/src/server/server.go.md|Server]] (struct: belongs_to) — *broadcastUpdate sends configuration updates to all connected client mailboxes.*
- [[config-server/config-server/src/server/server.go.md|Server]] (struct: defines_method) — *broadcastUpdate sends configuration updates to all connected client mailboxes.*
- [[config-server/config-server/src/server/server.go.md|clientMailbox]] (struct: belongs_to) — *clientMailbox represents a dedicated outgoing queue for a client.*
- [[config-server/config-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[config-server/config-server/src/server/server_test.go.md|server_test.go]] (same_package)
<!-- SYNC:END -->
