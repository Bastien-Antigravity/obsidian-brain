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
Automatically generated mirror for `universal-logger/scripts/parity-audit.py`.

> **Essential Process**:
> Automated cross-language parity audit script verifying that all exported CGO symbols from libunilog.h are implemented across Python, Rust, C++, and VBA.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|EXPECTED_LEVELS]] (constant: belongs_to)
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|FACADES]] (constant: belongs_to)
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|ROOT_DIR]] (constant: belongs_to)
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|SOURCE_OF_TRUTH]] (constant: belongs_to)
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|check_facade_parity]] (function: belongs_to) — *Check which exported functions are implemented in the given facade.*
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|check_level_parity]] (function: belongs_to) — *Check if all 11 log levels are defined in the facade.*
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|get_exported_functions]] (function: belongs_to) — *Extract UniLog_* and DistConf_* exports from the C header.*
- [[universal-logger/universal-logger/scripts/parity-audit.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->
