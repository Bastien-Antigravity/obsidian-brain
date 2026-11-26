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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/scripts/common.py.md|EXE_EXT]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|IS_LINUX]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|IS_MAC]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/scripts/common.py.md|audit_timescale_container_volume]] (function: calls)
- [[docker-deployment/scripts/common.py.md|ensure_docker_daemon]] (function: calls)
- [[docker-deployment/scripts/common.py.md|flush_stdin]] (function: calls) — *Flush pending input characters from console and sys.stdin buffer.*
- [[docker-deployment/scripts/common.py.md|get_docker_compose_cmd]] (function: calls)
- [[docker-deployment/scripts/common.py.md|get_docker_env]] (function: calls)
- [[docker-deployment/scripts/common.py.md|get_native_config]] (function: calls)
- [[docker-deployment/scripts/common.py.md|get_service_ip]] (function: calls) — *Dynamically resolve host/IP for a service respecting env and native.yaml.*
- [[docker-deployment/scripts/common.py.md|get_service_port]] (function: calls) — *Dynamically get listening port for a service, respecting env overrides and native.yaml.*
- [[docker-deployment/scripts/common.py.md|is_port_listening]] (function: calls) — *Check if a TCP port is actively listening and accepting connections.*
- [[docker-deployment/scripts/common.py.md|wait_for_port]] (function: calls) — *Poll a TCP port until it begins accepting connections or timeout expires.*
- [[docker-deployment/scripts/fleet_guard/crypto_validator.py.md|IS_WINDOWS]] (constant: calls)
- [[docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (imports)
- [[docker-deployment/scripts/fleet_guard/crypto_validator.py.md|decrypt_rsa]] (function: calls) — *Decrypt an ENC(...) ciphertext string using the RSA private key.*
- [[docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/scripts/setup_nats.py.md|ensure_nats_available]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/modes/local/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/modes/local/infra.py.md|LOCAL_DIR]] (constant: belongs_to) — *Locate directories*
- [[docker-deployment/modes/local/infra.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/modes/local/infra.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/modes/local/infra.py.md|_find_psql_binary]] (function: belongs_to) — *Locate psql executable on PATH or standard OS-specific PostgreSQL installation paths.*
- [[docker-deployment/modes/local/infra.py.md|_run_psql_query]] (function: belongs_to)
- [[docker-deployment/modes/local/infra.py.md|check_infrastructure_ports]] (function: belongs_to)
- [[docker-deployment/modes/local/infra.py.md|ensure_infrastructure_local]] (function: belongs_to)
- [[docker-deployment/modes/local/infra.py.md|print_infrastructure_quick_guide]] (function: belongs_to) — *Print clean, copy-pasteable OS-specific instructions for missing native services.*
- [[docker-deployment/modes/local/infra.py.md|start_infra_compose]] (function: belongs_to)
- [[docker-deployment/modes/local/infra.py.md|verify_database_extensions]] (function: belongs_to)
- [[docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/modes/local/run.py.md|run.py]] (imports)
- [[docker-deployment/modes/local/run.py.md|run.py]] (same_package)
<!-- SYNC:END -->
