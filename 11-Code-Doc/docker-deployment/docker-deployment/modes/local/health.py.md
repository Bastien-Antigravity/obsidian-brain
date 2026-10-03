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
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls) — *Dynamically resolve host/IP for a service respecting env and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_port]] (function: calls) — *Dynamically get listening port for a service, respecting env overrides and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_port_listening]] (function: calls) — *Check if a TCP port is actively listening and accepting connections.*

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|LOCAL_DIR]] (constant: belongs_to) — *Locate directories*
- [[docker-deployment/docker-deployment/modes/local/health.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|print_readiness_diagnostics]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|probe_http_service]] (function: belongs_to) — *Probe an HTTP endpoint dynamically. Return True if response code is received (< 500).*
- [[docker-deployment/docker-deployment/modes/local/health.py.md|query_watchdog_status]] (function: belongs_to) — *Query watchdog-agent status endpoint dynamically at http://<host>:<port>/api/v1/status.*
- [[docker-deployment/docker-deployment/modes/local/health.py.md|tail_watchdog_log]] (function: belongs_to) — *Print the last N lines of watchdog.log for crash or panic diagnostics.*
- [[docker-deployment/docker-deployment/modes/local/health.py.md|wait_for_fleet_readiness]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (same_package)
<!-- SYNC:END -->
