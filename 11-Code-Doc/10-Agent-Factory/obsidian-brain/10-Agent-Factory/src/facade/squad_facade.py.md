---
source: obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.699019
---

# Mirror: squad_facade.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py`.

> **Essential Process**:
> Provides the SquadFacade orchestrator class. It coordinates a squad of autonomous agents, running them to accomplish a high-level goal.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|chat]] (function: calls) — *Public façade – the only method a caller should invoke.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|AgentFactory]] (class: calls) — *Factory responsible for assembling a complete `Agent`.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|create_from_file]] (function: calls) — *Read a JSON config file, instantiate the Agent and return it.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|factory.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|add]] (function: calls) — *Appends a new turn to the short-term buffer.*

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|SquadFacade]] (class: belongs_to) — *Facade for managing and orchestrating a squad of agents.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|__init__]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|run_goal]] (function: belongs_to) — *Runs the high-level goal sequentially across the squad, passing context.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|run_fleet.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|run_fleet.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
