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
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|branch.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|check_develop_branches]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|auth.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|auth.py]] (same_package)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|setup_ghcr_credentials]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)

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
