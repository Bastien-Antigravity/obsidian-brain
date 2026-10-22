---
source: obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.487423
---

# Mirror: query_engine.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py`.

> **Essential Process**:
> Defines the abstract interface for the hybrid search query engine. Coordinates high-level search requests across multiple retrieval strategies.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/request.py.md|request.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/result.py.md|result.py]] (imports)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|QueryEngine]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|query]] (function: belongs_to) — *Executes a unified search operation across the entire brain.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
