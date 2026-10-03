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
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_DECRYPTION_FAILED]] (macro: belongs_to) — *define DISTCONF_ERR_NETWORK_FAILURE     5*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_GENERIC]] (macro: belongs_to) — *define DISTCONF_SUCCESS                0*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_INVALID_HANDLE]] (macro: belongs_to) — *define DISTCONF_ERR_GENERIC            1*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_INVALID_INPUT]] (macro: belongs_to) — *define DISTCONF_ERR_DECRYPTION_FAILED   6*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_KEY_NOT_FOUND]] (macro: belongs_to) — *define DISTCONF_ERR_INVALID_HANDLE      2*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_NETWORK_FAILURE]] (macro: belongs_to) — *define DISTCONF_ERR_VALIDATION_FAILED   4*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_ERR_VALIDATION_FAILED]] (macro: belongs_to) — *define DISTCONF_ERR_KEY_NOT_FOUND       3*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|DISTCONF_SUCCESS]] (macro: belongs_to) — *Standardized Error Codes*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|GO_CGO_EXPORT_PROLOGUE_H]] (macro: belongs_to) — *ifndef GO_CGO_EXPORT_PROLOGUE_H*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|GO_CGO_PROLOGUE_H]] (macro: belongs_to) — *ifndef GO_CGO_PROLOGUE_H*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|call_config_update_cb]] (function: belongs_to) — *C helper to call the callback*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|call_distconf_update_cb]] (function: belongs_to) — *Helper to safely execute a C callback from Go*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|call_notif_callback]] (function: belongs_to) — *Helper to safely execute a C callback from Go*
- [[universal-logger/universal-logger/libunilog/libunilog.h.md|set_last_error]] (function: belongs_to)
<!-- SYNC:END -->
