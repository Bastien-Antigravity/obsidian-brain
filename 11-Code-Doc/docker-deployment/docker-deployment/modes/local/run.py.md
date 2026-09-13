---
source: docker-deployment/modes/local/run.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-09-13T19:49:59.559982
---

# Mirror: run.py

## 📝 Description
Automatically generated mirror for `docker-deployment/modes/local/run.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|branch.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|branch.py]] (same_package)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|check_develop_branches]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|health.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|health.py]] (same_package)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|wait_for_fleet_readiness]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_antigravity_ide]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_ide.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|ensure_infrastructure_local]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|infra.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|infra.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/common.py.md|EXE_EXT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_native_config]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_native]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|ensure_fleet_cloned]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_native]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|LOCAL_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run_mode_local]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/mode_local.py.md|mode_local.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
