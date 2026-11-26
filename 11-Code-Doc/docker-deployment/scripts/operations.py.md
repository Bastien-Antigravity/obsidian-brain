---
microservice: docker-deployment
type: note
status: active
tags:
- '#service/docker-deployment'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/operations.py`.

> **Essential Process**:
> Operational and Lifecycle Utilities for Bastien-Antigravity Fleet Orchestrator. Includes: compile, rebuild, status, stop, doctor, guide, and secrets management.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/scripts/common.py.md|EXE_EXT]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|IS_LINUX]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|IS_MAC]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|IS_WINDOWS]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|common.py]] (imports)
- [[docker-deployment/scripts/common.py.md|common.py]] (same_package)
- [[docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls) — *Ensure RSA 2048-bit keys exist, respecting BASTIEN_PRIVATE_KEY_PATH, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: calls)
- [[docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/scripts/common.py.md|get_public_key_path]] (function: calls) — *Resolve RSA 2048-bit public key path from env, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls) — *Dynamically resolve host/IP for a service respecting env and native.yaml.*
- [[docker-deployment/scripts/common.py.md|get_service_port]] (function: calls) — *Dynamically get listening port for a service, respecting env overrides and native.yaml.*
- [[docker-deployment/scripts/common.py.md|is_docker_active]] (function: calls)
- [[docker-deployment/scripts/common.py.md|is_git_tracked_or_unsafe]] (function: calls)
- [[docker-deployment/scripts/common.py.md|is_port_listening]] (function: calls) — *Check if a TCP port is actively listening and accepting connections.*
- [[docker-deployment/scripts/fleet.py.md|DEPLOY_DIR]] (constant: calls)
- [[docker-deployment/scripts/fleet.py.md|fleet.py]] (same_package)
- [[docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/scripts/setup_nats.py.md|download_and_install_nats]] (function: calls)
- [[docker-deployment/scripts/setup_nats.py.md|find_existing_nats]] (function: calls) — *Check system PATH and workspace directories for nats-server.*
- [[docker-deployment/scripts/setup_nats.py.md|setup_nats.py]] (imports)
- [[docker-deployment/scripts/setup_nats.py.md|setup_nats.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/modes/docker/run.py.md|run.py]] (calls)
- [[docker-deployment/modes/local/ide/setup_ide.py.md|setup_ide.py]] (calls)
- [[docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/modes/production/run.py.md|run.py]] (calls)
- [[docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/scripts/fleet.py.md|fleet.py]] (imports)
- [[docker-deployment/scripts/fleet.py.md|fleet.py]] (same_package)
- [[docker-deployment/scripts/operations.py.md|WORKSPACE_REPOSITORIES]] (constant: belongs_to)
- [[docker-deployment/scripts/operations.py.md|_add_if_dir]] (function: belongs_to)
- [[docker-deployment/scripts/operations.py.md|_detect_go_version]] (function: belongs_to) — *Detect Go toolchain version from existing go.work or active 'go' binary.*
- [[docker-deployment/scripts/operations.py.md|_discover_workspace_python_sdks]] (function: belongs_to) — *Dynamically discover all local Python SDK directories present inside workspace_root.*
- [[docker-deployment/scripts/operations.py.md|_ffi_needs_rebuild]] (function: belongs_to) — *Return True if a CGO shared library is missing, forced, or older than its Go sources.*
- [[docker-deployment/scripts/operations.py.md|_is_rust_library_crate]] (function: belongs_to) — *Return True if crate_dir contains a Cargo.toml defining a Rust library crate.*
- [[docker-deployment/scripts/operations.py.md|_sync_cargo_config]] (function: belongs_to) — *Discover local Rust library crates on disk and synchronize .cargo/config.toml paths.*
- [[docker-deployment/scripts/operations.py.md|_sync_go_work]] (function: belongs_to) — *Discover local Go modules on disk and synchronize root go.work (missing modules fall back to GitHub).*
- [[docker-deployment/scripts/operations.py.md|_write_venv_workspace_pth]] (function: belongs_to) — *Write _bastien_workspace.pth inside site-packages of venv_dir for local-first SDK resolution.*
- [[docker-deployment/scripts/operations.py.md|check_compilation_prerequisites]] (function: belongs_to) — *Check if toolchains required for compilation exist on host and display actionable guidance.*
- [[docker-deployment/scripts/operations.py.md|check_debloat_prerequisites]] (function: belongs_to)
- [[docker-deployment/scripts/operations.py.md|compile_docker]] (function: belongs_to) — *Build Docker container images from local sources across all compose modes [DD-01].*
- [[docker-deployment/scripts/operations.py.md|compile_native]] (function: belongs_to) — *Compile native binaries incrementally (or clean rebuild when force=True), build FFI libraries, and setup Python venvs.*
- [[docker-deployment/scripts/operations.py.md|ensure_fleet_cloned]] (function: belongs_to) — *Check and clone missing ecosystem repositories into WORKSPACE_ROOT.*
- [[docker-deployment/scripts/operations.py.md|install_debloat_tools]] (function: belongs_to) — *Install missing Debloat Sentinel and static analysis tools across Go, Rust, and Python.*
- [[docker-deployment/scripts/operations.py.md|load_fleet_inventory]] (function: belongs_to) — *Load ecosystem repositories strictly scoped to the active workspace and execution mode.*
- [[docker-deployment/scripts/operations.py.md|run_doctor]] (function: belongs_to) — *Verify prerequisites across the toolchain.*
- [[docker-deployment/scripts/operations.py.md|run_guide]] (function: belongs_to) — *Display native infrastructure setup guide.*
- [[docker-deployment/scripts/operations.py.md|run_secrets]] (function: belongs_to) — *Sovereign secret encryption, key security audit, and database credentials management.*
- [[docker-deployment/scripts/operations.py.md|run_status]] (function: belongs_to) — *Inspect and report ecosystem status.*
- [[docker-deployment/scripts/operations.py.md|stop_all]] (function: belongs_to) — *Terminate all services across Docker and Native.*
- [[docker-deployment/scripts/operations.py.md|stop_docker]] (function: belongs_to) — *Stop all Docker containers (compose fleet across modes, local databases, and standalone infra) [DD-01].*
- [[docker-deployment/scripts/operations.py.md|stop_native]] (function: belongs_to) — *Stop all native processes cleanly with full per-service visibility.*
- [[docker-deployment/scripts/operations.py.md|sync_workspace_local_resolvers]] (function: belongs_to) — *Synchronize workspace-local Go (go.work), Rust (.cargo/config.toml), and Python (.pth) resolvers.*
- [[docker-deployment/scripts/operations.py.md|update_native_yaml_secret]] (function: belongs_to) — *Update a secret field in docker-deployment/modes/local/config/native.yaml directly.*
<!-- SYNC:END -->
