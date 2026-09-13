

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_MAC]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_WINDOWS]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|encrypt_secret_rsa]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|get_stored_credentials]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|login_docker_ghcr]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|save_credentials_to_native_yaml]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|save_permanent_os_env]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|setup_ghcr_credentials]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
<!-- SYNC:END -->
