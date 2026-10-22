---
source: obsidian-brain/08-Squad-Agent/src/agents/docindexer.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20T15:13:14.816130
---

# Mirror: docindexer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/docindexer.py`.

> **Essential Process**:
> DocIndexer agent daemon specialized in documentation indexing, formatting, and metadata cataloging. Provides capabilities to scan local markdown files in any satellite brain and index or purge them remotely in the central partitioned RAG Engine.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|DocIndexerAgent]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|_index_document_remote]] (function: belongs_to) — *Sends document to central RAG REST endpoint for indexing with resilient retry.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|_purge_brain_remote]] (function: belongs_to) — *Sends purge request to central RAG REST endpoint with resilient retry.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|_resolve_rag_rest_url]] (function: belongs_to) — *Dynamically resolves RAG Engine REST endpoint from ecosystem configuration.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|_scan_and_index_directory]] (function: belongs_to) — *Walks local directory and indexes all markdown files.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|execute_tool]] (function: belongs_to) — *Dispatches DocIndexer specific tools with fallback to BaseAgent.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|index_brain_document]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|purge_brain_index]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|scan_and_index_local_vault]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
