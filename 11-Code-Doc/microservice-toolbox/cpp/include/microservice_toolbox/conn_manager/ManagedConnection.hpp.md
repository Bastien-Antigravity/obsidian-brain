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
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp`.

> **Essential Process**:
> Core microservice-toolbox module: ManagedConnection.hpp.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetListenAddr]] (method: calls)
- [[microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetProfile]] (method: calls)
- [[microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetPublicIP]] (method: calls)
- [[microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Close]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.CurrentEndpoint]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.EnsureConnected]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.GetEndpointPtr]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.GetEndpoint]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.ManagedConnection]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Receive]] (method: defines_method) — *Receive data*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Reconnect]] (method: defines_method) — *Reconnect logic mirroring Go/Python/Rust*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: defines_method) — *Send data, reconnecting if necessary*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.UpdateEndpoint]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.ConnectBlocking]] (method: defines_method) — *NetworkManager implementation of high-level API*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.ConnectCapability]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.ConnectNonBlocking]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.Connect]] (method: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.GetNextDelay]] (method: calls)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.hpp]] (imports)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.hpp]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|MICROSERVICE_TOOLBOX_CONN_MANAGER_MANAGED_CONNECTION_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_CONN_MANAGER_MANAGED_CONNECTION_HPP*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Close]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.CurrentEndpoint]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.EnsureConnected]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.GetEndpointPtr]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.GetEndpoint]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.ManagedConnection]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Receive]] (method: belongs_to) — *Receive data*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Reconnect]] (method: belongs_to) — *Reconnect logic mirroring Go/Python/Rust*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: belongs_to) — *Send data, reconnecting if necessary*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.UpdateEndpoint]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection]] (class: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection]] (class: defines_method)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.ConnectBlocking]] (method: belongs_to) — *NetworkManager implementation of high-level API*
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.ConnectCapability]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.ConnectNonBlocking]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager.Connect]] (method: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|NetworkManager]] (class: defines_method) — *NetworkManager implementation of high-level API*
<!-- SYNC:END -->
