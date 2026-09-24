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
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|IsPortListening]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogError]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/postgres_launcher.go.md|LaunchPostgresAttempt]] (function: belongs_to)
<!-- SYNC:END -->
