---
microservice: distributed-config
type: note
status: active
tags:
- '#service/distributed-config'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `distributed-config/src/cgo_bridge/errors.c`.

> **Essential Process**:
> Thread-local and fallback fixed-buffer error storage for the distributed-config CGO C ABI bridge.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distconf/libdistconf/helpers.h.md|helpers.h]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/cmd/libdistconf/main.go.md|main.go]] (calls)
- [[distributed-config/src/cgo_bridge/errors.c.md|DISTCONF_ERR_BUF_SIZE]] (macro: belongs_to) — *include <stdio.h>*
- [[distributed-config/src/cgo_bridge/errors.c.md|get_last_error]] (function: belongs_to)
- [[distributed-config/src/cgo_bridge/errors.c.md|get_last_error_code]] (function: belongs_to)
- [[distributed-config/src/cgo_bridge/errors.c.md|res]] (constant: belongs_to)
- [[distributed-config/src/cgo_bridge/errors.c.md|set_last_error]] (function: belongs_to)
<!-- SYNC:END -->
