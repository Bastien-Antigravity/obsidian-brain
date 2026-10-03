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
Automatically generated mirror for `microservice-toolbox/go/pkg/conn_manager/strategies_test.go`.

> **Essential Process**:
> Core microservice-toolbox module: strategies_test.go.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|ManagedConnection.Close]] (method: calls) — *Close terminates the connection and stops the reconnection loop.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/connection.go.md|connection.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NetworkManager.Connect]] (method: calls) — *Connect establishes a connection using the specified mode.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewCriticalStrategy]] (function: calls) — *NewCriticalStrategy creates a manager configured for critical services with infinite retries.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewNetworkManager]] (function: calls) — *NewNetworkManager creates a manager with provided retry policies (durations in milliseconds).*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewPerformanceStrategy]] (function: calls) — *NewPerformanceStrategy creates a manager for high-performance services with background reconnection.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|NewStandardStrategy]] (function: calls) — *NewStandardStrategy creates a manager for standard services with limited retries.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|TestStrategies]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/strategies_test.go.md|TestUnifiedConnect]] (function: belongs_to)
<!-- SYNC:END -->
