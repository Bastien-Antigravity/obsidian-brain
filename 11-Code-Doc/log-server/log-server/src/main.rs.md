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
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.new]] (method: calls) — *Create new log server instance*
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.run]] (method: calls) — *Run the log server with all components*
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: calls) — *Split into its component halves*
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls) — *Formats and prints an internal server log message (visual alignment only)*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/main.rs.md|main]] (function: belongs_to)
- [[log-server/log-server/src/main.rs.md|run_server]] (function: belongs_to) — *Main server execution function*
<!-- SYNC:END -->
