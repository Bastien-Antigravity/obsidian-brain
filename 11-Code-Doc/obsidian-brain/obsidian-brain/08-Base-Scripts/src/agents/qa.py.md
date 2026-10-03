---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/agents/qa.py`.

> **Essential Process**:
> QA Engineer agent daemon specialized in verifying logic implementation, auditing unit tests, and reporting verification reports.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/qa.py.md|QAAgent]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/qa.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/qa.py.md|execute_tool]] (function: belongs_to) — *Executes a function call requested by the model.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/qa.py.md|run_squad_tests]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->
