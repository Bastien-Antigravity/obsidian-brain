---
source: obsidian-brain/10-Agent-Factory/src/factory/factory.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.839463
---

# Mirror: factory.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/factory/factory.py`.

> **Essential Process**:
> Implements the Factory pattern that creates a fully-wired `Agent` instance from a single configuration dictionary. The factory hides the complex wiring (identity -> memory -> skills -> planner -> safety).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|Agent]] (class: calls) — *Concrete, reusable agent instance.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|info]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|interfaces.py]] (imports)

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|squad_facade.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|squad_facade.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|AgentFactory]] (class: belongs_to) — *Factory responsible for assembling a complete `Agent`.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|__init__]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|create_from_file]] (function: belongs_to) — *Read a JSON config file, instantiate the Agent and return it.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
