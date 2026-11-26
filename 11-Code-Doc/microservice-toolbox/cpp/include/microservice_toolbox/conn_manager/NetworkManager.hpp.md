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
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp`.

> **Essential Process**:
> Core microservice-toolbox module: NetworkManager.hpp.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|Endpoint.Endpoint]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.GetNextDelay]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NetworkManager]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewCritical]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewPerformance]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewStandard]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewWithConfig]] (method: defines_method) — *Static Factory Methods for Strategies*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.New]] (method: defines_method) — *Unified Factory Method combining AppConfig and Logger in one function with pointers*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/logger/Logger.hpp.md|Logger.hpp]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.hpp]] (same_package)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|AppConfig]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|Endpoint.Endpoint]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|Endpoint]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|Endpoint]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|MICROSERVICE_TOOLBOX_CONN_MANAGER_NETWORK_MANAGER_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_CONN_MANAGER_NETWORK_MANAGER_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|ManagedConnection]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.GetNextDelay]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NetworkManager]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewCritical]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewPerformance]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewStandard]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewWithConfig]] (method: belongs_to) — *Static Factory Methods for Strategies*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.New]] (method: belongs_to) — *Unified Factory Method combining AppConfig and Logger in one function with pointers*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/errors.go.md|errors.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager_test.go.md|manager_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/notification/client_test.go.md|client_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|client_test.go]] (calls)
<!-- SYNC:END -->
