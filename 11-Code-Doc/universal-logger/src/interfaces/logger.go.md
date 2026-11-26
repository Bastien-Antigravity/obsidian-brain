---
microservice: universal-logger
type: note
status: active
tags:
- '#service/universal-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/interfaces/logger.go.md|Logger]] (interface: belongs_to) — *It is a facade that ensures microservices remain decoupled from the underlying logging engine.*
<!-- SYNC:END -->
