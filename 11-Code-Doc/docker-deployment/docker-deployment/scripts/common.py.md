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
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|branch.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|auth.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|health.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_ide.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|infra.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|Colors]] (class: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|EXE_EXT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_LINUX]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_MAC]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_WINDOWS]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|SCRIPT_PATH]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|encrypt_secret_rsa]] (function: belongs_to) — *Encrypt a secret string using the external RSA public key.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: belongs_to) — *Ensure RSA 2048-bit keys exist, respecting BASTIEN_PRIVATE_KEY_PATH, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_loopback_alias]] (function: belongs_to) — *Verify or attempt to configure 127.0.0.2 loopback alias.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_placeholders]] (function: belongs_to) — *Ensure required secret env vars are set, generating temporary placeholders if missing.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|flush_stdin]] (function: belongs_to) — *Flush pending input characters from console and sys.stdin buffer.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|generate_placeholder_secret]] (function: belongs_to) — *Generate a random placeholder secret string.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_env]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_server_version]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_native_config]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_public_key_path]] (function: belongs_to) — *Resolve RSA 2048-bit public key path from env, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_ip]] (function: belongs_to) — *Dynamically resolve host/IP for a service respecting env and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_port]] (function: belongs_to) — *Dynamically get listening port for a service, respecting env overrides and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_docker_active]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_docker_process_present]] (function: belongs_to) — *Check if Docker UI or backend processes are currently running.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_git_tracked_or_unsafe]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_port_listening]] (function: belongs_to) — *Check if a TCP port is actively listening and accepting connections.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|load_env_file]] (function: belongs_to) — *Load key-value pairs from .env into os.environ without overriding explicitly set variables.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|repl]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|resolve_template]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|resolve_workspace_root]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/common.py.md|strip_ansi]] (function: belongs_to) — *Remove ANSI escape sequences from text for clean file logging.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|wait_for_port]] (function: belongs_to) — *Poll a TCP port until it begins accepting connections or timeout expires.*
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (same_package)
<!-- SYNC:END -->
