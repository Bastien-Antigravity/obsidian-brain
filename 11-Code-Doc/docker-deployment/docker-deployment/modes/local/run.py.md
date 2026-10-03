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
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|branch.py]] (same_package)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|check_develop_branches]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|DEPLOY_DIR]] (constant: calls)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|health.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|health.py]] (same_package)
- [[docker-deployment/docker-deployment/modes/local/health.py.md|wait_for_fleet_readiness]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_antigravity_ide]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_ide.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|ensure_infrastructure_local]] (function: calls)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|infra.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|infra.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/common.py.md|EXE_EXT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_keys_exist]] (function: calls) — *Ensure RSA 2048-bit keys exist, respecting BASTIEN_PRIVATE_KEY_PATH, /etc/bastien/, or ~/.bastien/keys/.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|flush_stdin]] (function: calls) — *Flush pending input characters from console and sys.stdin buffer.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_native_config]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls) — *Dynamically resolve host/IP for a service respecting env and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run_preflight]] (function: calls) — *Convenience functional entry point for mode runners.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|compile_native]] (function: calls) — *Compile missing or all native binaries, build FFI libraries, and setup Python venvs.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|ensure_fleet_cloned]] (function: calls) — *Check and clone missing ecosystem repositories into WORKSPACE_ROOT.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|run_status]] (function: calls) — *Inspect and report ecosystem status.*
- [[docker-deployment/docker-deployment/scripts/operations.py.md|stop_native]] (function: calls) — *Stop all native processes cleanly with full per-service visibility.*

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|LOCAL_DIR]] (constant: belongs_to) — *Locate root directories*
- [[docker-deployment/docker-deployment/modes/local/run.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run_mode_local]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/mode_local.py.md|mode_local.py]] (calls)
<!-- SYNC:END -->
