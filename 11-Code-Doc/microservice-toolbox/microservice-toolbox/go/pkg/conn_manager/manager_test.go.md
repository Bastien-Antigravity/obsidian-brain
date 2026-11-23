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
Automatically generated mirror for `microservice-toolbox/go/pkg/conn_manager/manager_test.go`.

> **Essential Process**:
> Manages polyglot inter-service network connections with lifecycle hooks and circuit breakers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.New]] (method: calls) — *Unified Factory Method combining AppConfig and Logger in one function with pointers*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|Endpoint]] (struct: calls) — *Precalculates Address on the cold path to eliminate hot-path formatting and parsing.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.GetEndpoint]] (method: calls) — *GetEndpoint returns the current IP and Port destination coordinates lock-free.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.UpdateEndpoint]] (method: calls) — *UpdateEndpoint atomically updates the target destination IP and Port.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.reconnect]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|NewEndpoint]] (function: calls) — *NewEndpoint builds an immutable Endpoint on the cold path.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|NewManagedConnection]] (function: calls) — *NewManagedConnection creates a new connection wrapper with an immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectCapability]] (method: calls) — *and establishes a lock-free ManagedConnection bound to AppConfig. On 3 failed attempts, it automatically syncs AppCon...*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectEndpoint]] (method: calls) — *ConnectEndpoint establishes a connection using the specified mode with an immutable Endpoint pointer.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectNonBlocking]] (method: calls) — *ConnectNonBlocking immediately returns a ManagedConnection and attempts to connect in background (backwards compatibi...*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.ConnectWithRetry]] (method: calls) — *ConnectWithRetry attempts to connect and returns a ManagedConnection wrapper.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.WithPolicy]] (method: calls) — *WithPolicy configures custom retry policy parameters on NetworkManager.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManagerWithConfig]] (function: calls) — *NewNetworkManagerWithConfig creates a resilient NetworkManager pre-bound to the ecosystem AppConfig.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManagerWithPolicy]] (function: calls) — *NewNetworkManagerWithPolicy creates a manager with explicit retry policies (durations in milliseconds).*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManager]] (function: calls) — *If l is nil and ac is provided, ac.Logger is automatically inherited.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|trackingWriteCloser.Close]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|trackingWriteCloser.Write]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestConnectNonBlocking]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestManagedConnection_CloseDuringDial_ClosesNewSocketAndLeavesCurrentConnNil]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestManagedConnection_ConcurrentClose_NoPanic]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestNetworkManager_ConnectCapability_LiveConfigRefresh]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestNetworkManager_ConnectCapability_Resolution]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestNetworkManager_UnifiedConstructor_And_LockFreeEndpoint]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestNetworkManager_WithPolicy_ClampingAndConnectEndpointFailure]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestOnErrorUnifiedHook]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|TestRealWorld_DynamicFailover_And_3TryReload]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|goroutines]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|trackingWriteCloser.Close]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|trackingWriteCloser.Write]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|trackingWriteCloser]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|trackingWriteCloser]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|strategies_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|strategies_test.go]] (same_package)
<!-- SYNC:END -->
