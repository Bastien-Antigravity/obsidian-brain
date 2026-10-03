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
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.GetLastMessage]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.Stop]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.acceptLoop]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.handleConnection]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|InitWithOptions]] (function: calls) — *It supports dependency injection (ExistingConfig) and specialized metadata.*
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls) — *existingConfig: OPTIONAL. If provided, the logger will use this configuration instance instead of creating a new one.*
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (same_package)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.GetLastMessage]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.Stop]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.acceptLoop]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.handleConnection]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer]] (struct: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|NewMockServerOnPort]] (function: belongs_to) — *NewMockServerOnPort creates a MockServer bound to a specific port.*
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|NewMockServer]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|TestFullEcosystemResilience]] (function: belongs_to)
<!-- SYNC:END -->
