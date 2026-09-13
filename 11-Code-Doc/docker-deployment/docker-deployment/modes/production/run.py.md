---
source: docker-deployment/modes/production/run.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-09-13T19:49:59.588881
---

# Mirror: run.py

## 📝 Description
Automatically generated mirror for `docker-deployment/modes/production/run.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_placeholders]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_all]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|PROD_MODE_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|run_mode_production]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/mode_production.py.md|mode_production.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
