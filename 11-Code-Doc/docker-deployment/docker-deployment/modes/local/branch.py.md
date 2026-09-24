---
source: docker-deployment/modes/local/branch.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-09-13 19:49:59.568334
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: branch.py

## 📝 Description
Automatically generated mirror for `docker-deployment/modes/local/branch.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|WORKSPACE_REPOSITORIES]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|check_develop_branches]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
