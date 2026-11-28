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
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_DECRYPTION_FAILED]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_GENERIC]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_INVALID_HANDLE]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_INVALID_INPUT]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_KEY_NOT_FOUND]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_NETWORK_FAILURE]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_VALIDATION_FAILED]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|DISTCONF_SUCCESS]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|GO_CGO_EXPORT_PROLOGUE_H]] (macro: belongs_to) — *ifndef GO_CGO_EXPORT_PROLOGUE_H*
- [[universal-logger/libunilog/libunilog.h.md|GO_CGO_PROLOGUE_H]] (macro: belongs_to) — *line 1 "cgo-gcc-export-header-prolog"*
- [[universal-logger/libunilog/libunilog.h.md|THREAD_LOCAL]] (macro: belongs_to)
- [[universal-logger/libunilog/libunilog.h.md|call_config_update_cb]] (function: belongs_to) — *C helper to call the callback*
- [[universal-logger/libunilog/libunilog.h.md|call_distconf_update_cb]] (function: belongs_to) — *Helper to safely execute a C callback from Go*
- [[universal-logger/libunilog/libunilog.h.md|call_notif_callback]] (function: belongs_to) — *Helper to safely execute a C callback from Go*
- [[universal-logger/libunilog/libunilog.h.md|get_last_error]] (function: belongs_to) — *line 1 "cgo-generated-wrapper"*
- [[universal-logger/libunilog/libunilog.h.md|get_last_error_code]] (function: belongs_to) — *include <stdlib.h>*
- [[universal-logger/libunilog/libunilog.h.md|get_vba_buffer]] (function: belongs_to) — *line 13 "distconf_bridge.go"*
- [[universal-logger/libunilog/libunilog.h.md|set_last_error]] (function: belongs_to)
- [[universal-logger/src/cgo_bridge/config.go.md|config.go]] (calls)
- [[universal-logger/src/cgo_bridge/distconf_bridge.go.md|distconf_bridge.go]] (calls)
<!-- SYNC:END -->
