

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py`.

> **Essential Process**:
> Defines the abstract interface for the document indexing pipeline. Coordinates the transformation of raw files into searchable RAG chunks.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|IndexingPipeline]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|build_full_index]] (function: belongs_to) — *Scans the entire workspace and performs a comprehensive re-index.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|process_file]] (function: belongs_to) — *Processes and indexes a single file based on its path.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
<!-- SYNC:END -->
