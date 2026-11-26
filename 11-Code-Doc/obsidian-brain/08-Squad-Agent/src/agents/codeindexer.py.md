---
source: obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.580540
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: codeindexer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py`.

> **Essential Process**:
> CodeIndexer agent daemon specialized in code symbol parsing, cross-referencing, and semantic dependency indexing.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|CodeIndexerAgent]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|_fetch]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|_resolve_rag_rest_url]] (function: belongs_to) — *Resolves RAG Engine REST address dynamically from AppConfig (Zero Silent Fallback).*
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|execute_tool]] (function: belongs_to) — *Dispatches CodeIndexer AST symbol search and dependency graph tools via RAG REST API.*
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|get_file_dependency_graph]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|search_code_symbols]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
