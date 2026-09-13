

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_loopback_alias]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_placeholders]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_all]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|DOCKER_MODE_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|run_mode_docker]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/mode_docker.py.md|mode_docker.py]] (calls)
<!-- SYNC:END -->
