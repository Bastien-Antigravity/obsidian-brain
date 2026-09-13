---
source: docker-deployment/modes/local/health.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-09-13T21:20:15.797201
---

# Mirror: health.py

## 📝 Description
Automatically generated mirror for `docker-deployment/modes/local/health.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_port]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_port_listening]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|LOCAL_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|print_readiness_diagnostics]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|probe_http_service]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|query_watchdog_status]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|tail_watchdog_log]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|wait_for_fleet_readiness]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
