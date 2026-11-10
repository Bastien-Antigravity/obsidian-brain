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
An asynchronous, zero-loss operational observability and real-time self-healing pipeline has been engineered across `watchdog-agent`, TimescaleDB, and `squad-agent`:
- **Log Harvesting**: Multi-file tailer scans native workspaces (`*/logs/*.log`) or Docker volumes (`/var/log/fleet/*.log`).
- **Zero-Allocation Parser**: Fixed-width 8-column parser extracting errors (`level >= ERROR`) with regex fallback.
- **Durable Checkpointing**: Thread-safe cursor management in `.shipper_offsets.json` with file truncation and inode rotation detection.
- **TimescaleDB Hypertable**: Partitioned `fleet_error_logs` storage with automatic DDL startup verification (`EnsureSchema`).
- **Resilient Offset Freeze**: Database outage handling where offsets remain frozen during downtime and replay without data loss.
- **Orchestrator Decoupling**: Modular operational switches (`--mode=shipper`, `--supervise=false`) ensuring zero conflict with Docker daemon.
- **Real-Time SRE Triage**: Event dispatching over NATS (`bastien-antigravity.fleet.incident`) with a 60s signature-based throttler to trigger **Role 15: Fleet Healer & Auto-Repair Sentinel** (`Prompt-Fleet-AutoRepair.md`).

### 🛡️ Deepening Roadmap (Hardening, Behavior, Architecture & Testing)
- [ ] **Hardening & Resilience**:
  - Implement `.shipper_offsets.json` state compaction (purge deleted log file keys).
  - Add binary garbage and non-UTF8 sanitization to protect database transactions from malformed log input.
  - Tune TimescaleDB client pool with statement timeouts and jittered exponential reconnection backoff.
- [ ] **Behavior & Functionality Definition**:
  - Define canonical cross-language log severity mapping (Go, Rust, Python, C++).
  - Implement moving-average error burst detection and anomaly tagging (>10 errors/min).
  - Configure automated chunk drop retention policies on TimescaleDB (`INTERVAL '30 days'`).
  - Implement NATS incident acknowledgment and resolution status synchronization with `squad-agent`.
- [ ] **Architecture & Multi-Node Topology**:
  - Specify mutual TLS (mTLS) configuration for remote containerized log shippers connecting across public networks.
  - Author BDD specification `FEAT-010-Autonomous-Error-Log-Shipping.md` in `02-Business-BDD`.
  - Extend OpenMFE dashboard in `web-interface` to stream real-time errors and display auto-repair remediation logs.
- [ ] **Testing & Verification Matrix**:
  - High-throughput micro-benchmarks (`BenchmarkParseLogLine`) verifying 0 heap allocations under 100k lines/sec.
  - Automated chaos test simulating database network partitions mid-batch to guarantee zero data loss and offset freezing.
  - Multi-service end-to-end integration test with live PostgreSQL/TimescaleDB container.
  - Mock NATS drill simulating auto-repair agent responses to verify incident payload contracts.

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
