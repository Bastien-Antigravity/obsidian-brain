---
source: obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.419853
---

# Mirror: graph_rag.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py`.

> **Essential Process**:
> Graph-RAG Query Engine that extends the Hybrid search engine. Retrieves semantic vector search seeds, traverses their 1/2-hop graph neighborhoods, and injects relational context maps directly into RAG results.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|chunk.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/request.py.md|request.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/result.py.md|result.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|HybridQueryEngine]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|GraphRAGQueryEngine]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|_format_subgraph_markdown]] (function: belongs_to) — *Formats nodes and edges list into a highly readable markdown map for the LLM.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|query]] (function: belongs_to) — *Performs hybrid search and enriches each result with its graph neighborhood.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
