---
source: obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.412063
---

# Mirror: hybrid.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py`.

> **Essential Process**:
> Hybrid search engine combining semantic (vector) and lexical (keyword) results. Uses Reciprocal Rank Fusion (RRF) to provide balanced and highly relevant search outcomes. Optionally applies a second-stage Cross-Encoder re-ranking for highest precision.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_query_engine_settings]] (function: calls) — *Resolves hybrid search, fusion, and reranker settings (config file overrides DB defaults).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|QueryEngine]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|query_engine.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|MChunk]] (class: calls) — *Represents a logical chunk of a document/code.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|chunk.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|MChunkMetadata]] (class: calls) — *Normalized metadata for a logical chunk.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/request.py.md|request.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/result.py.md|MQueryResult]] (class: calls) — *Standardized output for a search query.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/result.py.md|result.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|HybridQueryEngine]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|_apply_cross_encoder]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|_apply_rrf]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|_re_rank_sync]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|query]] (function: belongs_to) — *Performs hybrid search and re-ranks results.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
