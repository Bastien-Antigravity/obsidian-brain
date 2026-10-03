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
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: defines_method) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Reset]] (method: defines_method) — *Reset clears the LogEntry for reuse.*
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Retain]] (method: defines_method) — *Must be called when passing the entry to an additional async consumer.*

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|log_engine.go]] (calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: belongs_to) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Reset]] (method: belongs_to) — *Reset clears the LogEntry for reuse.*
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Retain]] (method: belongs_to) — *Must be called when passing the entry to an additional async consumer.*
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry]] (struct: belongs_to) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry]] (struct: defines_method) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/flexible-logger/src/models/entry_test.go.md|entry_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/models/entry_test.go.md|entry_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|async.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|multi.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (calls)
<!-- SYNC:END -->
