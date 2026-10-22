---
source: obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.595628
---

# Mirror: indexing_pipeline.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py`.

> **Essential Process**:
> Defines the abstract interface for the document indexing pipeline. Coordinates the transformation of raw files into searchable RAG chunks.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|IndexingPipeline]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|build_full_index]] (function: belongs_to) — *Scans the entire workspace and performs a comprehensive re-index.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|delete_file]] (function: belongs_to) — *Removes all chunks and records associated with a deleted file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|process_file]] (function: belongs_to) — *Processes and indexes a single file based on its path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
