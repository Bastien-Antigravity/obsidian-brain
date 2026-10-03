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
- [[docker-deployment/docker-deployment/scripts/common.py.md|EXE_EXT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_LINUX]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_MAC]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_WINDOWS]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls) — *Ensure RSA 2048-bit keys exist, respecting BASTIEN_PRIVATE_KEY_PATH, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_public_key_path]] (function: calls) — *Resolve RSA 2048-bit public key path from env, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls) — *Dynamically resolve host/IP for a service respecting env and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_port]] (function: calls) — *Dynamically get listening port for a service, respecting env overrides and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_docker_active]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_git_tracked_or_unsafe]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_port_listening]] (function: calls) — *Check if a TCP port is actively listening and accepting connections.*
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|DEPLOY_DIR]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|download_and_install_nats]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|find_existing_nats]] (function: calls) — *Check system PATH, workspace watchdog-agent/nats, and standard user paths for nats-server.*
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|setup_nats.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|setup_nats.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|WORKSPACE_REPOSITORIES]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|check_compilation_prerequisites]] (function: belongs_to) — *Check if toolchains required for compilation exist on host and display actionable guidance.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_docker]] (function: belongs_to) — *Build Docker container images from local sources.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_native]] (function: belongs_to) — *Compile missing or all native binaries, build FFI libraries, and setup Python venvs.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|ensure_fleet_cloned]] (function: belongs_to) — *Check and clone missing ecosystem repositories into WORKSPACE_ROOT.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|load_fleet_inventory]] (function: belongs_to) — *Load ecosystem repositories strictly scoped to the active workspace and execution mode.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_doctor]] (function: belongs_to) — *Verify prerequisites across the toolchain.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_guide]] (function: belongs_to) — *Display native infrastructure setup guide.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_secrets]] (function: belongs_to) — *Sovereign secret encryption, key security audit, and database credentials management.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: belongs_to) — *Inspect and report ecosystem status.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_all]] (function: belongs_to) — *Terminate all services across Docker and Native.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_docker]] (function: belongs_to) — *Stop all Docker containers (compose fleet, local databases, and standalone infra).*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_native]] (function: belongs_to) — *Stop all native processes cleanly with full per-service visibility.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|update_native_yaml_secret]] (function: belongs_to) — *Update a secret field in docker-deployment/modes/local/config/native.yaml directly.*
<!-- SYNC:END -->
