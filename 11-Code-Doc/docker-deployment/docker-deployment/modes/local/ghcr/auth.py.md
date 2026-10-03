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
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_MAC]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|encrypt_secret_rsa]] (function: calls) — *Encrypt a secret string using the external RSA public key.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|MODES_DIR]] (constant: belongs_to) — *Locate root directory*
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|get_stored_credentials]] (function: belongs_to) — *Retrieve GITHUB_USER and GHCR_TOKEN from OS environment.*
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|login_docker_ghcr]] (function: belongs_to) — *Execute docker login ghcr.io using provided credentials.*
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|save_credentials_to_native_yaml]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|save_permanent_os_env]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|setup_ghcr_credentials]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
<!-- SYNC:END -->
