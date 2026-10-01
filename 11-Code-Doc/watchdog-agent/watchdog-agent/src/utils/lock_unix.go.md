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
Automatically generated mirror for `watchdog-agent/src/utils/lock_unix.go`.

> **Essential Process**:
> Unix-specific single-instance filesystem locking implementation using flock. Prevents duplicate watchdog-agent instances from executing concurrently.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/utils/lock_unix.go.md|AcquireLock]] (function: belongs_to) — *AcquireLock opens and locks the lock file exclusively on Unix-like systems.*
<!-- SYNC:END -->
