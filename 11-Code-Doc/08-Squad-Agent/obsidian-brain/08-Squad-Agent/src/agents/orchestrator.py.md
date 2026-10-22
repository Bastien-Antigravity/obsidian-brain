---
source: obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.575539
---

# Mirror: orchestrator.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py`.

> **Essential Process**:
> Orchestrator agent daemon responsible for decomposing user goals, delegating tasks to specific agents, and reporting progress.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|OrchestratorAgent]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|_record_strategic_milestone_impl]] (function: belongs_to) — *Records an epic/mission milestone in PostgreSQL and broadcasts over NATS.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|db_insert]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|execute_tool]] (function: belongs_to) — *Dynamic tool execution handler for Orchestrator.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
