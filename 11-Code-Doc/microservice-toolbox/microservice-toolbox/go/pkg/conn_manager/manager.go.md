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
Automatically generated mirror for `microservice-toolbox/go/pkg/conn_manager/manager.go`.

> **Essential Process**:
> Manages polyglot inter-service network connections with lifecycle hooks and circuit breakers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|Trim]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.reconnect]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|NewManagedConnection]] (function: calls) — *NewManagedConnection creates a new connection wrapper with an immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectBlocking]] (method: defines_method) — *EstablishConnection attempts a single connection using the immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectNonBlocking]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectWithRetry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.Connect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.EstablishConnection]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.GetNextDelay]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls) — *production microservices from silently running dark without operational logs.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Warning]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|ConnectionMode]] (struct: belongs_to) — *ConnectionMode defines how the manager handles the initial connection behavior.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|ModeBlocking]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|ModeIndefinite]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|ModeNonBlocking]] (constant: belongs_to) — *ConnectionMode defines how the manager handles the initial connection behavior.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectBlocking]] (method: belongs_to) — *EstablishConnection attempts a single connection using the immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectNonBlocking]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectWithRetry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.Connect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.EstablishConnection]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.GetNextDelay]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager]] (struct: belongs_to) — *NetworkManager handles reliable connection establishment with retries.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager]] (struct: defines_method) — *NetworkManager handles reliable connection establishment with retries.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewCriticalStrategy]] (function: belongs_to) — *NewCriticalStrategy creates a manager configured for critical services with infinite retries.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManagerWithLogger]] (function: belongs_to) — *NewNetworkManagerWithLogger creates a manager with provided retry policies and an explicit logger.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManager]] (function: belongs_to) — *If l is nil and ac is provided, ac.Logger is automatically inherited.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewPerformanceStrategy]] (function: belongs_to) — *NewPerformanceStrategy creates a manager for high-performance services with background reconnection.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewStandardStrategy]] (function: belongs_to) — *NewStandardStrategy creates a manager for standard services with limited retries.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|OnErrorHandler]] (struct: belongs_to) — *msg: a descriptive message providing additional context.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|manager_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|manager_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|strategies_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|strategies_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (calls)
<!-- SYNC:END -->
