---
microservice: flexible-logger
type: note
status: active
tags:
- '#service/flexible-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/src/models/entry.go.md|LogEntry.Reset]] (method: calls) — *Reset clears the LogEntry for reuse.*
- [[flexible-logger/src/models/entry.go.md|LogEntry.Retain]] (method: calls) — *Must be called when passing the entry to an additional async consumer.*
- [[flexible-logger/src/models/entry.go.md|entry.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/src/models/entry_test.go.md|TestEntryPool_Reuse]] (function: belongs_to)
- [[flexible-logger/src/models/entry_test.go.md|TestLogEntry_Reset]] (function: belongs_to)
- [[flexible-logger/src/models/entry_test.go.md|TestLogEntry_RetainRelease]] (function: belongs_to)
<!-- SYNC:END -->
