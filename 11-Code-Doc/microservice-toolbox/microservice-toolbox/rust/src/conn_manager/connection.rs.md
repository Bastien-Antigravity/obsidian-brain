

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/conn_manager/connection.rs`.

> **Essential Process**:
> Represents a resilient, auto-reconnecting network connection with exponential backoff.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.drop]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|Endpoint.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.close]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.current_endpoint]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.endpoint]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.get_endpoint]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.new_with_endpoint]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.reconnect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.set_stream]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.swap_endpoint]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.update_endpoint]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.write]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|Error]] (enum: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|errors.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|errors.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.establish_connection]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.get_next_delay]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager]] (struct: calls) — *- Context-Aware Recovery: Unified error reporting via on_error.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|manager.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|Endpoint.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|Endpoint]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|Endpoint]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.close]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.current_endpoint]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.endpoint]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.get_endpoint]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.new_with_endpoint]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.reconnect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.set_stream]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.swap_endpoint]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.update_endpoint]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.write]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection]] (struct: belongs_to) — *background reconnections if a network failure is detected during use.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection]] (struct: defines_method) — *background reconnections if a network failure is detected during use.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->
