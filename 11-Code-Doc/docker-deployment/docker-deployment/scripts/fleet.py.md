

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|run_mode_docker]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|check_develop_branches]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|setup_ghcr_credentials]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publish_images_ghcr]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_antigravity_ide]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run_mode_local]] (function: calls)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|run_mode_production]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/mode_docker.py.md|mode_docker.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/mode_local.py.md|mode_local.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/mode_production.py.md|mode_production.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_docker]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_native]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|ensure_fleet_cloned]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_doctor]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_guide]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_secrets]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_all]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|interactive_menu]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|main]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (same_package)
<!-- SYNC:END -->
