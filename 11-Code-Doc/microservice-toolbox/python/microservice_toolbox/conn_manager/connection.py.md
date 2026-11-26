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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py`.

> **Essential Process**:
> ManagedConnection wraps a connection and handles automatic reconnection. Provides a 'self-healing' interface that triggers background recovery upon failure.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|MaxRetriesReachedError]] (class: calls) — *Raised when the network manager gives up after the configured number of attempts.*
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|WriteFailedError]] (class: calls) — *Raised when data could not be sent over the socket.*
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|errors.py]] (imports)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|errors.py]] (same_package)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|establish_connection]] (function: calls)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|get_next_delay]] (function: calls)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (imports)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|Endpoint]] (class: belongs_to) — *Immutable destination coordinates holding pre-formatted Address.*
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|ManagedConnection]] (class: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|_current_endpoint]] (function: belongs_to) — *Returns the active Endpoint, refreshing from AppConfig if bound to a capability.*
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|close]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|get_endpoint]] (function: belongs_to) — *Returns current target coordinates.*
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|reconnect]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|update_endpoint]] (function: belongs_to) — *Atomically updates the connection target coordinates.*
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|write]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (calls)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (imports)
- [[microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (same_package)
<!-- SYNC:END -->
