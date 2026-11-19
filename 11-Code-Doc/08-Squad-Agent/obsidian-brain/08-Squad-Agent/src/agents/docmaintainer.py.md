---
source: obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.572548
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: docmaintainer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py`.

> **Essential Process**:
> DocMaintainer agent daemon specialized in verifying documentation alignment, detecting document drift, and suggesting corrections.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|DocMaintainerAgent]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|_fetch]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|_post]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|_resolve_rag_rest_url]] (function: belongs_to) — *Resolves RAG Engine REST address dynamically from AppConfig (Zero Silent Fallback).*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|check_documentation_drift]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|execute_tool]] (function: belongs_to) — *Dispatches DocMaintainer specialized RAG alignment and doc-sync tools.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|sync_code_documentation]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
