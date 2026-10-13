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
- None detected

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
<!-- SYNC:END -->
