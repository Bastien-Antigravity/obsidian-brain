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
Automatically generated mirror for `config-server/cmd/config-server/main.go`.

> **Essential Process**:
> Boots and initializes the config-server microservice, establishing dynamic capabilities discovery and REST management ports.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|NewGRPCService]] (function: calls) — *NewGRPCService creates a new GRPCService instance*
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[config-server/config-server/src/rest/mfe.js.md|mfe.js]] (imports)
- [[config-server/config-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: calls) — *NewRESTHandler creates a new RESTHandler instance*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: calls) — *StartServer starts a HTTP server for the REST API on the specified address (e.g. "127.0.0.1:3308" or ":3308").*
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Close]] (method: calls)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/server/server.go.md|NewServer]] (function: calls) — *NewServer creates a new Config Server.*
- [[config-server/config-server/src/store/persistence.go.md|NewPersistenceManager]] (function: calls) — *NewPersistenceManager creates a new manager for the given file path.*
- [[config-server/config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: calls) — *If the file does not exist, it returns an empty ConfigMap and no error.*
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|NewStore]] (function: calls) — *NewStore initializes a new Store with an empty config.*
- [[config-server/config-server/src/store/store.go.md|Store.Replace]] (method: calls) — *Ensures the store "owns" the data by performing a deep copy.*
- [[config-server/config-server/src/telegram/manager_test.go.md|manager_test.go]] (imports)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Critical]] (method: calls)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Error]] (method: calls)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Info]] (method: calls)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Warning]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
