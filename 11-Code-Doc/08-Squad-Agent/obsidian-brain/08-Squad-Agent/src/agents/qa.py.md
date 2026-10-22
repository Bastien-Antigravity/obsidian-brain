---
source: obsidian-brain/08-Squad-Agent/src/agents/qa.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.613751
---

# Mirror: qa.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/qa.py`.

> **Essential Process**:
> QA Engineer agent daemon specialized in verifying logic implementation, auditing unit tests, and reporting verification reports.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|QAAgent]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|execute_tool]] (function: belongs_to) — *Executes a function call requested by the model.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|run_squad_tests]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
