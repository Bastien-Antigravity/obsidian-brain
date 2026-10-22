---
source: obsidian-brain/10-Agent-Factory/src/run_fleet.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.629790
---

# Mirror: run_fleet.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/run_fleet.py`.

> **Essential Process**:
> Async entry point that assembles a squad of agents and runs a demo goal.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|SquadFacade]] (class: calls) — *Facade for managing and orchestrating a squad of agents.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|run_goal]] (function: calls) — *Runs the high-level goal sequentially across the squad, passing context.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|squad_facade.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|Logger]] (class: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|interfaces.py]] (imports)

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|SimpleLogger]] (class: belongs_to) — *Thin wrapper around the standard library logger to satisfy the `Logger` interface.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|__init__]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|error]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|info]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|main]] (function: belongs_to) — *Bootstrap the demo squad and run a single high-level goal.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|warning]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
