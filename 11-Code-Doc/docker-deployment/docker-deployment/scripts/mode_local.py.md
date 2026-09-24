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
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run_mode_local]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/mode_local.py.md|MODES_DIR]] (constant: belongs_to)
<!-- SYNC:END -->
