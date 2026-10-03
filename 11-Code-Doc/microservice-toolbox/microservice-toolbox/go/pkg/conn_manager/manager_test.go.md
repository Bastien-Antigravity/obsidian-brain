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
Automatically generated mirror for `microservice-toolbox/go/pkg/conn_manager/manager_test.go`.

> **Essential Process**:
> Manages polyglot inter-service network connections with lifecycle hooks and circuit breakers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Close]] (method: calls) — *Close terminates the connection and stops the reconnection loop.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectNonBlocking]] (method: calls) — *ConnectNonBlocking immediately returns a ManagedConnection and attempts to connect in the background.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectWithRetry]] (method: calls) — *ConnectWithRetry attempts to connect and returns a ManagedConnection wrapper.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManager]] (function: calls) — *NewNetworkManager creates a manager with provided retry policies (durations in milliseconds).*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestConnectNonBlocking]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestOnErrorUnifiedHook]] (function: belongs_to)
<!-- SYNC:END -->
