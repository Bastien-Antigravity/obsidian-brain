---
source: docker-deployment/modes/production/run.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-09-13 19:49:59.588881
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: run.py

## 📝 Description
Automatically generated mirror for `docker-deployment/modes/production/run.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls) — *Ensure RSA 2048-bit keys exist, respecting BASTIEN_PRIVATE_KEY_PATH, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_placeholders]] (function: calls) — *Ensure required secret env vars are set, generating temporary placeholders if missing.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run_preflight]] (function: calls) — *Convenience functional entry point for mode runners.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls) — *Inspect and report ecosystem status.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_all]] (function: calls) — *Terminate all services across Docker and Native.*

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|MODES_DIR]] (constant: belongs_to) — *Locate root directory*
- [[docker-deployment/docker-deployment/modes/production/run.py.md|PROD_MODE_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|run_mode_production]] (function: belongs_to) — *Deploy production containerized fleet on public interfaces (0.0.0.0) with Watchtower.*
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/mode_production.py.md|mode_production.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
