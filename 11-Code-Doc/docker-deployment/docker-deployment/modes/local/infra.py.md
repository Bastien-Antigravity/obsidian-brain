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
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|flush_stdin]] (function: calls) — *Flush pending input characters from console and sys.stdin buffer.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_native_config]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls) — *Dynamically resolve host/IP for a service respecting env and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_service_port]] (function: calls) — *Dynamically get listening port for a service, respecting env overrides and native.yaml.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|is_port_listening]] (function: calls) — *Check if a TCP port is actively listening and accepting connections.*
- [[docker-deployment/docker-deployment/scripts/common.py.md|wait_for_port]] (function: calls) — *Poll a TCP port until it begins accepting connections or timeout expires.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|ensure_nats_available]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|LOCAL_DIR]] (constant: belongs_to) — *Locate directories*
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|check_infrastructure_ports]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|ensure_infrastructure_local]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|print_infrastructure_quick_guide]] (function: belongs_to) — *Print clean, copy-pasteable OS-specific instructions for missing native services.*
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|start_infra_compose]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (imports)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (same_package)
<!-- SYNC:END -->
