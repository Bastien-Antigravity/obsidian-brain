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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: calls)
- [[log-server/log-server/src/config/config.rs.md|config.rs]] (imports)
- [[log-server/log-server/src/core/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (imports)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.name]] (method: defines_method) — *Get server name*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.new]] (method: defines_method) — *Create new gRPC bridge gateway*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.run]] (method: defines_method) — *Run the gRPC server*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.log_message]] (method: defines_method) — *Handle incoming gRPC log message*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.new]] (method: defines_method) — *Create new gRPC bridge implementation*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogEntry.from]] (method: defines_method) — *Use the renamed types*
- [[log-server/log-server/src/transport/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls) — *Formats and prints an internal server log message (visual alignment only)*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.name]] (method: belongs_to) — *Get server name*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.new]] (method: belongs_to) — *Create new gRPC bridge gateway*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.run]] (method: belongs_to) — *Run the gRPC server*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway]] (struct: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway]] (struct: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.log_message]] (method: belongs_to) — *Handle incoming gRPC log message*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.new]] (method: belongs_to) — *Create new gRPC bridge implementation*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl]] (struct: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl]] (struct: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogEntry.from]] (method: belongs_to) — *Use the renamed types*
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogEntry]] (struct: defines_method) — *Conversion from protobuf to internal type*
<!-- SYNC:END -->
