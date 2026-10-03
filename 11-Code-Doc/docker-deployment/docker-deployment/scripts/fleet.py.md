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
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|run_mode_docker]] (function: calls) — *Run containerized Docker fleet bound to isolated loopback 127.0.0.2.*
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|check_develop_branches]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|setup_ghcr_credentials]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publish_images_ghcr]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_antigravity_ide]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run_mode_local]] (function: calls)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|run_mode_production]] (function: calls) — *Deploy production containerized fleet on public interfaces (0.0.0.0) with Watchtower.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_WINDOWS]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run_preflight]] (function: calls) — *Convenience functional entry point for mode runners.*
- [[docker-deployment/docker-deployment/scripts/mode_docker.py.md|mode_docker.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/mode_local.py.md|mode_local.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/mode_production.py.md|mode_production.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_docker]] (function: calls) — *Build Docker container images from local sources.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_native]] (function: calls) — *Compile missing or all native binaries, build FFI libraries, and setup Python venvs.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|ensure_fleet_cloned]] (function: calls) — *Check and clone missing ecosystem repositories into WORKSPACE_ROOT.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_doctor]] (function: calls) — *Verify prerequisites across the toolchain.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_guide]] (function: calls) — *Display native infrastructure setup guide.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_secrets]] (function: calls) — *Sovereign secret encryption, key security audit, and database credentials management.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls) — *Inspect and report ecosystem status.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_all]] (function: calls) — *Terminate all services across Docker and Native.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_docker]] (function: calls) — *Stop all Docker containers (compose fleet, local databases, and standalone infra).*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_native]] (function: calls) — *Stop all native processes cleanly with full per-service visibility.*

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|build_cli_parser]] (function: belongs_to) — *Construct strict, modular CLI parser with dedicated subparsers.*
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|dispatch_command]] (function: belongs_to) — *Execute the validated command.*
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|interactive_menu]] (function: belongs_to) — *Display clean, structured interactive CLI selection menu.*
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|main]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (same_package)
<!-- SYNC:END -->
