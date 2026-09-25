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
- [x] **Persona Extractor — ENABLED**: Patched and enabled as a background process in `start_squad.py`.
- [x] **Mode Guardrail**: Added a mandatory "Current Mode" check to the AI-Session-State handshake to ensure the previous mode is "parked."
- [x] **Knowledge Compression Script**: Implemented an automated way to distill old session logs into fresh patterns to keep the context window clean.
- [ ] **Ecosystem Logger Fallback & Strict Mode Evolution**:
  - Review `STRICT_LOGGER=true` opt-in mechanism across base repositories (`microservice-toolbox`, `safe-socket`, `distributed-config`).
  - When `STRICT_LOGGER` is unset, `EnsureSafeLogger(nil)` currently falls back to `NoOpLogger` / test stub. While safe for isolated unit tests, uninitialized production microservices could run dark without warning.
  - Design a robust daemon/headless-aware logger fallback or warning mechanism that works seamlessly for microservices without UI interfaces, eliminating silent discard without fragile environment variable dependencies.

## ✅ Completed
- [x] Initial structure for `02-Business-BDD`. (Now `business-bdd-brain`)
- [x] Creation of `03-Tech-Stack/06-Role-Wisdom/`. (Now in `tech-stack-brain`)
- [x] Multi-Mode Switching Framework via `MODE-MANUAL.md` and `start_squad.py`.
- [x] Fleet Operations Brain (`fleet-operation-brain`) for fleet-wide action logs.
- [x] Labs Brain (`rapid-prototyping-brain`) for experimental/rapid-proto work.
- [x] Updated `Daily-AI-Playbook.md` with mode-specific "Rules of Engagement."
- [x] Python Ecosystem Standardization (18 scripts, headers, aliasing, docstrings).
- [x] Submodule URL correction (`.gitmodules` → new repo names).
- [x] Integrated Preflight Check system (`Preflight-Check.py`).
- [x] Standardized Business Data Models (MarketEvent, OHLCV, Signal) and migrated business services.
- [x] Repair start_squad.py & Workflow Governance (Mission COMPLETED).
