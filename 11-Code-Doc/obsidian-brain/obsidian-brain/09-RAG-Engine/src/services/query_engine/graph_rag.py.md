

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py`.

> **Essential Process**:
> Graph-RAG Query Engine that extends the Hybrid search engine. Retrieves semantic vector search seeds, traverses their 1/2-hop graph neighborhoods, and injects relational context maps directly into RAG results.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|chunk.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/request.py.md|request.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/result.py.md|result.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|HybridQueryEngine]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|GraphRAGQueryEngine]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|_format_subgraph_markdown]] (function: belongs_to) — *Formats nodes and edges list into a highly readable markdown map for the LLM.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|query]] (function: belongs_to) — *Performs hybrid search and enriches each result with its graph neighborhood.*
<!-- SYNC:END -->
