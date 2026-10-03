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
Automatically generated mirror for `microservice-toolbox/rust/src/conn_manager/manager.rs`.

> **Essential Process**:
> Manages polyglot inter-service network connections with lifecycle hooks and circuit breakers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: calls) — *Synchronize with the Config Server*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: calls) — *Send data, reconnecting if necessary*
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|OnErrorHandler]] (struct: calls) — *msg: a descriptive message providing additional context.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.reconnect]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.set_stream]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.write]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|connection.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|connection.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|Error]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|errors.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|errors.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect_blocking]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect_non_blocking]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect_with_retry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.establish_connection]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.get_next_delay]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_critical]] (method: defines_method) — *Infinite retries, aggressive backoff.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_performance]] (method: defines_method) — *Short timeouts, low delay, background reconnection.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_standard]] (method: defines_method) — *Limited retries, moderate backoff.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_with_all]] (method: defines_method) — *across the polyglot ecosystem.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls) — *Logger trait defines the standard interface for structured logging across the toolbox.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|ensure_safe_logger]] (function: calls) — *In strict mode (STRICT_LOGGER=true), panics to prevent microservices from running dark.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|connection.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|connection.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|connection.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|ConnectionMode]] (enum: belongs_to) — *ConnectionMode defines how the manager handles the initial connection.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect_blocking]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect_non_blocking]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.connect_with_retry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.establish_connection]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.get_next_delay]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_critical]] (method: belongs_to) — *Infinite retries, aggressive backoff.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_performance]] (method: belongs_to) — *Short timeouts, low delay, background reconnection.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_standard]] (method: belongs_to) — *Limited retries, moderate backoff.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.new_with_all]] (method: belongs_to) — *across the polyglot ecosystem.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager]] (struct: belongs_to) — *Strategies*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager]] (struct: defines_method) — *Strategies*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|OptionalHandler]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|new_network_manager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|new_network_manager_with_all]] (function: belongs_to) — *NOTE: Matches NetworkManager::new_with_all argument count for polyglot parity.*
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|test_connect_non_blocking_returns_immediately]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|test_managed_connection_reconnect_max_retries]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|test_on_error_unified_hook]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|test_strategies_presets]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|test_unified_connect]] (function: belongs_to)
<!-- SYNC:END -->
