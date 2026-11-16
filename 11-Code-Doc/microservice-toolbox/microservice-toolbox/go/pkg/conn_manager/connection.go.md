---
microservice: microservice-toolbox
type: note
status: active
tags:
- '#service/microservice-toolbox'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/conn_manager/connection.go`.

> **Essential Process**:
> Represents a resilient, auto-reconnecting network connection with exponential backoff.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Close]] (method: defines_method) — *Close terminates the connection and stops the reconnection loop.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Endpoint]] (method: defines_method) — *Endpoint returns the current immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.GetEndpoint]] (method: defines_method) — *GetEndpoint returns the current IP and Port destination coordinates lock-free.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.UpdateEndpoint]] (method: defines_method) — *UpdateEndpoint atomically updates the target destination IP and Port.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Write]] (method: defines_method) — *Write sends data over the connection, lock-free on the hot path.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.currentEndpoint]] (method: defines_method) — *currentEndpoint returns the active Endpoint, refreshing from AppConfig's atomic LiveConfig if bound to a capability.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.isClosing]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.reconnect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.EstablishConnection]] (method: calls) — *Zero temporary variables, zero defensive nil-checks, and zero string formatting overhead.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.GetNextDelay]] (method: calls) — *attempt is 0-indexed.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|Endpoint]] (struct: belongs_to) — *Precalculates Address on the cold path to eliminate hot-path formatting and parsing.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Close]] (method: belongs_to) — *Close terminates the connection and stops the reconnection loop.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Endpoint]] (method: belongs_to) — *Endpoint returns the current immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.GetEndpoint]] (method: belongs_to) — *GetEndpoint returns the current IP and Port destination coordinates lock-free.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.UpdateEndpoint]] (method: belongs_to) — *UpdateEndpoint atomically updates the target destination IP and Port.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Write]] (method: belongs_to) — *Write sends data over the connection, lock-free on the hot path.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.currentEndpoint]] (method: belongs_to) — *currentEndpoint returns the active Endpoint, refreshing from AppConfig's atomic LiveConfig if bound to a capability.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.isClosing]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.reconnect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection]] (struct: belongs_to) — *ManagedConnection wraps a connection and handles automatic reconnection lock-free.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection]] (struct: defines_method) — *ManagedConnection wraps a connection and handles automatic reconnection lock-free.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|NewEndpoint]] (function: belongs_to) — *NewEndpoint builds an immutable Endpoint on the cold path.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|NewManagedConnectionRaw]] (function: belongs_to) — *NewManagedConnectionRaw creates a ManagedConnection from string pointers (backwards compatibility).*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|NewManagedConnection]] (function: belongs_to) — *NewManagedConnection creates a new connection wrapper with an immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|manager_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|manager_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|strategies_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|strategies_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/spec/spec_test.go.md|spec_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/matrix_gen.go.md|matrix_gen.go]] (calls)
<!-- SYNC:END -->
