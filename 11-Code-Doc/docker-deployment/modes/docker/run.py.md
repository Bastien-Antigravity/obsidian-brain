---
microservice: docker-deployment
type: note
status: active
tags:
- '#service/docker-deployment'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|audit_timescale_container_volume]] (function: calls)
- [[docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls) — *Ensure RSA 2048-bit keys exist, respecting BASTIEN_PRIVATE_KEY_PATH, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/scripts/common.py.md|ensure_loopback_alias]] (function: calls) — *Verify or attempt to configure 127.0.0.2 loopback alias.*
- [[docker-deployment/scripts/common.py.md|ensure_placeholders]] (function: calls)
- [[docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: calls)
- [[docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/scripts/fleet_guard/engine.py.md|run_preflight]] (function: calls) — *Convenience functional entry point for mode runners.*
- [[docker-deployment/scripts/operations.py.md|run_status]] (function: calls) — *Inspect and report ecosystem status.*
- [[docker-deployment/scripts/operations.py.md|stop_docker]] (function: calls) — *Stop all Docker containers (compose fleet across modes, local databases, and standalone infra) [DD-01].*

### 🔌 Consumers (Inbound)
- [[docker-deployment/modes/docker/run.py.md|DOCKER_MODE_DIR]] (constant: belongs_to)
- [[docker-deployment/modes/docker/run.py.md|MODES_DIR]] (constant: belongs_to) — *Locate root directory*
- [[docker-deployment/modes/docker/run.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/modes/docker/run.py.md|run_mode_docker]] (function: belongs_to) — *Run containerized Docker fleet bound to isolated loopback 127.0.0.2.*
- [[docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/scripts/mode_docker.py.md|mode_docker.py]] (calls)
<!-- SYNC:END -->
