---
microservice: obsidian-brain
type: task
status: active
priority: high
tags:
- '#service/obsidian-brain'
- '#type/task'
- '#state/active'
- '#zone/3-fleet'
---
# TODO: obsidian-brain (Governance & Meta-Logic)

## 🏗️ Architecture & Refactoring
- [x] Consolidate common BDD templates into a centralized `00-AI-Orchestration/Templates/` folder.
- [x] **Persona Extractor — ENABLED**: Patched and enabled as a background process in `squad-agent`.
- [x] **Mode Guardrail**: Added a mandatory "Current Mode" check to the AI-Session-State handshake to ensure the previous mode is "parked."
- [x] **Knowledge Compression Script**: Implemented an automated way to distill old session logs into fresh patterns to keep the context window clean.
- [ ] **Ecosystem Logger Fallback & Strict Mode Evolution**:
  - Review `STRICT_LOGGER=true` opt-in mechanism across base repositories (`microservice-toolbox`, `safe-socket`, `distributed-config`).
  - When `STRICT_LOGGER` is unset, `EnsureSafeLogger(nil)` currently falls back to `NoOpLogger` / test stub. While safe for isolated unit tests, uninitialized production microservices could run dark without warning.
  - Design a robust daemon/headless-aware logger fallback or warning mechanism that works seamlessly for microservices without UI interfaces, eliminating silent discard without fragile environment variable dependencies.

## 📡 Autonomous Fleet Error Shipping & Real-Time Auto-Repair

### 📊 Global Synthesis of Current Functionality
An asynchronous, zero-loss operational observability and real-time self-healing pipeline has been engineered across `watchdog-agent`, `obsidiandb` (TimescaleDB + pgvector), and `08-Squad-Agent`:
- **Per-Service Log Harvesting & Volume Isolation**: Tails native `*/logs/*.log` (filtering forwarded client rows out of `_main.log`) or Docker `fleet-logs:/var/log/fleet/<service>/<service>.log` while keeping `log-server` isolated on `log-server-logs:/var/log/log-server`.
- **Dual Text + Cloud JSON Parser**: Parses standard 8-column text lines and `flexible-logger` `JSONSerializer` cloud logs with UTF-8 / NUL-byte poison-pill sanitization, restricted strictly to `ERROR` (`10`) and `CRITICAL` (`11`).
- **Durable Checkpointing**: Thread-safe cursor management in `.shipper_offsets.json` with file truncation, inode rotation detection, and missing-file pruning.
- **Option B TimescaleDB Schema (`watchdog_agent`)**: Partitioned `watchdog_agent.fleet_error_logs` and `watchdog_agent.fleet_incidents` inside `obsidiandb` with startup DDL verification (`EnsureSchema` & `ensure_fleet_error_schema`) plus `docker-deployment` extension & `pgdata` layout audits.
- **Resilient Offset Freeze & Backoff**: Offsets freeze during DB outages with `conn_manager.NewCriticalStrategy` exponential backoff and replay idempotently via `event_hash`.
- **Real-Time AutoRepair Coordinator (`08-Squad-Agent/src/agents/autorepair.py`)**: Brain-partitioned NATS subscriber (`<prefix>[.<brain>].fleet.incident`), signature coalescing, 3-strike circuit breaker, isolated `/tmp` `git worktree` verification, dirty-worktree guard, REST/Telegram 1-click approval, and on-the-fly Enable/Disable toggle.

### 🛡️ Deepening Roadmap (Hardening, Behavior, Architecture & Testing)
- [ ] **Hardening & Resilience**:
  - [x] Implemented `.shipper_offsets.json` state pruning, UTF-8/NUL sanitization, `conn_manager` DB backoff, diff safety bounds (`validate_proposed_diff`), and dirty-worktree blocking.
  - [ ] Tune PostgreSQL `statement_timeout` & run stress chaos tests under continuous log rotation.
- [ ] **Behavior & Functionality Definition**:
  - [x] Cross-language canonical 12-level severity + Cloud JSON ingestion + AutoRepair runtime toggle (`GET/POST /api/v1/squad/autorepair/*`) & Telegram menu controls.
  - [ ] Implement moving-average error burst detection (`BURST` tagging >10 errors/min) and automated TimescaleDB retention policy (`INTERVAL '30 days'`).
- [ ] **Architecture & Multi-Node Topology**:
  - [ ] Specify mutual TLS (mTLS) configuration for remote containerized log shippers connecting across public networks.
  - [ ] Author BDD specification `FEAT-010-Autonomous-Error-Log-Shipping.md` in `02-Business-BDD`.
  - [ ] Extend OpenMFE dashboard in `web-interface` to stream real-time errors and display auto-repair remediation logs.
- [ ] **Testing & Verification Matrix**:
  - [x] Unit test suites passing across `watchdog-agent/src/shipper`, `flexible-logger/src/helpers`, `log-server`, `docker-deployment/scripts/tests`, and `08-Squad-Agent/tests/test_autorepair.py`.
  - [ ] Add high-throughput Go benchmarks (`BenchmarkParseLogLine`), DB network-partition chaos tests, and live containerized `timescale-db` end-to-end integration tests.

## ✅ Completed
- [x] Initial structure for `02-Business-BDD`. (Now `business-bdd-brain`)
- [x] Creation of `03-Tech-Stack/06-Role-Wisdom/`. (Now in `tech-stack-brain`)
- [x] Multi-Mode Switching Framework via `MODE-MANUAL.md` and `squad-agent`.
- [x] Fleet Operations Brain (`fleet-operation-brain`) for fleet-wide action logs.
- [x] Labs Brain (`rapid-prototyping-brain`) for experimental/rapid-proto work.
- [x] Updated `Daily-AI-Playbook.md` with mode-specific "Rules of Engagement."
- [x] Python Ecosystem Standardization (18 scripts, headers, aliasing, docstrings).
- [x] Submodule URL correction (`.gitmodules` → new repo names).
- [x] Integrated Preflight Check system (`Preflight-Check.py`).
- [x] Standardized Business Data Models (MarketEvent, OHLCV, Signal) and migrated business services.
- [x] Repair squad-agent & Workflow Governance (Mission COMPLETED).
