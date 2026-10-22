---
source: obsidian-brain/10-Agent-Factory/src/memory/memory.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.642891
---

# Mirror: memory.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/memory/memory.py`.

> **Essential Process**:
> Provide a memory storage implementation for the agents. Maintains short-term chat context history.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|MemoryStore]] (class: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|interfaces.py]] (imports)

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|squad_facade.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|ShortTermMemory]] (class: belongs_to) — *Concrete ShortTermMemory implementation of the MemoryStore contract.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|__init__]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|add]] (function: belongs_to) — *Appends a new turn to the short-term buffer.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|clear]] (function: belongs_to) — *Clears the buffer.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves history. For simplicity, returns the entire active buffer.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|planner.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
