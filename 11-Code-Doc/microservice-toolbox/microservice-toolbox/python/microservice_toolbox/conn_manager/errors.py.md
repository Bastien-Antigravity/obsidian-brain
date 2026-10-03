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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py`.

> **Essential Process**:
> Domain-specific exception hierarchy for network connection management, retries, and write failures.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|ConnectionManagerError]] (class: belongs_to) — *Base class for connection manager errors.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|ConnectionRefusedError]] (class: belongs_to) — *Raised when the target address actively rejects the connection.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|MaxRetriesReachedError]] (class: belongs_to) — *Raised when the network manager gives up after the configured number of attempts.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|NoConnectionError]] (class: belongs_to) — *Raised when an operation is attempted on a nil or closed connection.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|WriteFailedError]] (class: belongs_to) — *Raised when data could not be sent over the socket.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (same_package)
<!-- SYNC:END -->
