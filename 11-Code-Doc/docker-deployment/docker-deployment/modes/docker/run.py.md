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
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls) — *Ensure RSA 2048-bit keys exist, respecting BASTIEN_PRIVATE_KEY_PATH, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_loopback_alias]] (function: calls) — *Verify or attempt to configure 127.0.0.2 loopback alias.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_placeholders]] (function: calls) — *Ensure required secret env vars are set, generating temporary placeholders if missing.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run_preflight]] (function: calls) — *Convenience functional entry point for mode runners.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls) — *Inspect and report ecosystem status.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_all]] (function: calls) — *Terminate all services across Docker and Native.*

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|DOCKER_MODE_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|MODES_DIR]] (constant: belongs_to) — *Locate root directory*
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|run_mode_docker]] (function: belongs_to) — *Run containerized Docker fleet bound to isolated loopback 127.0.0.2.*
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/mode_docker.py.md|mode_docker.py]] (calls)
<!-- SYNC:END -->
