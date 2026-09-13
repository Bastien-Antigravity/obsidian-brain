---
source: docker-deployment/modes/local/ghcr/publisher.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-09-13T19:49:59.586112
---

# Mirror: publisher.py

## 📝 Description
Automatically generated mirror for `docker-deployment/modes/local/ghcr/publisher.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|branch.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|check_develop_branches]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|auth.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|auth.py]] (same_package)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|setup_ghcr_credentials]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|LOCAL_MODE_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|SERVICES_DOCKER]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publish_images_ghcr]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
