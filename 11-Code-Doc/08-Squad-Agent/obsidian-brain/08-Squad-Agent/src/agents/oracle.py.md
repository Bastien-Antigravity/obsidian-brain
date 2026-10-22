---
source: obsidian-brain/08-Squad-Agent/src/agents/oracle.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.594945
---

# Mirror: oracle.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/oracle.py`.

> **Essential Process**:
> Oracle agent daemon specialized in long-term chronological log auditing, historical analysis, and querying temporal knowledge vaults.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|OracleAgent]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|_check_anti_backlog_impl]] (function: belongs_to) — *Searches the Anti-Backlog for previously settled/rejected architectural topics.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|_query_strategic_decisions_impl]] (function: belongs_to) — *Queries 01-Strategic-Nexus.strategic_decisions in PostgreSQL.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|_record_strategic_milestone_impl]] (function: belongs_to) — *Records a strategic milestone into PostgreSQL and broadcasts over NATS.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|check_anti_backlog]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|db_insert]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|db_query]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|execute_tool]] (function: belongs_to) — *Dynamic tool execution handler for Oracle strategic capabilities.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|query_strategic_decisions]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|record_strategic_milestone]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
