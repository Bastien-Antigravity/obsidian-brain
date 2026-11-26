---
source: obsidian-brain/08-Squad-Agent/src/agents/oracle.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.620316
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: oracle.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/oracle.py`.

> **Essential Process**:
> Oracle agent daemon specialized in long-term chronological log auditing, historical analysis, and querying temporal knowledge vaults.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|OracleAgent]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|_check_anti_backlog_impl]] (function: belongs_to) — *Searches the Anti-Backlog for previously settled/rejected architectural topics.*
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|_query_strategic_decisions_impl]] (function: belongs_to) — *Queries 01-Strategic-Nexus.strategic_decisions in PostgreSQL.*
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|_record_strategic_milestone_impl]] (function: belongs_to) — *Records a strategic milestone into PostgreSQL and broadcasts over NATS.*
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|check_anti_backlog]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|db_insert]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|db_query]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|execute_tool]] (function: belongs_to) — *Dynamic tool execution handler for Oracle strategic capabilities.*
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|query_strategic_decisions]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|record_strategic_milestone]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
