

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py`.

> **Essential Process**:
> Defines the abstract interface for AI-driven metadata enrichment of chunks. Enrichment runs in two modes: - On-demand  : `enrich(chunk)` called inline during indexing. - Background : `start_background_loop()` drains a queue of unenriched chunks and re-writes their metadata in the vector + parent stores. `enrich_pending()` can be called at any time to trigger an immediate enrichment pass without waiting for the next loop tick.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|Enricher]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enrich]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enrich_pending]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|start_background_loop]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|stop_background_loop]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
<!-- SYNC:END -->
