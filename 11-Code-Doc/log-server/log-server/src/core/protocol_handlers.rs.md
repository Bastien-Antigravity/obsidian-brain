---
microservice: log-server
type: note
status: active
tags:
- '#service/log-server'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader]] (struct: calls)
- [[log-server/log-server/src/protocols/capnp/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|handle_grpc_message]] (function: belongs_to) — *Handle gRPC log message*
- [[log-server/log-server/src/core/protocol_handlers.rs.md|handle_tcp_message]] (function: belongs_to) — *Handle incoming TCP client connection*
- [[log-server/log-server/src/core/protocol_handlers.rs.md|identify_client_from_handshake]] (function: belongs_to) — *without needing to manually link or re-generate safe-socket schemas in Rust.*
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
<!-- SYNC:END -->
