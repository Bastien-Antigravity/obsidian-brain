

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py`.

> **Essential Process**:
> LLM-based metadata enricher for indexed document chunks. Generates concise summaries and hypothetical questions to improve semantic retrieval precision.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_enrichment_settings]] (function: calls) — *Resolves LLM enrichment configuration with automatic secret decryption.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|Enricher]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enricher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|generate_response]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|llm_client.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|get_parent]] (function: calls) — *Retrieves the raw content string associated with a specific chunk ID.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|add_documents]] (function: calls) — *Indexes documents and their corresponding vector embeddings.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|get_all]] (function: calls) — *Retrieves all records currently stored in the vector collection.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|MChunkMetadata]] (class: calls) — *Normalized metadata for a logical chunk.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|LLMEnricher]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|_SYSTEM_PROMPT]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|_USER_PROMPT_TMPL]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|_background_loop]] (function: belongs_to) — *Runs forever, calling enrich_pending() at each tick.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|_call_llm]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|_mock_enrichment]] (function: belongs_to) — *Lightweight template fallback used when the LLM is unavailable or disabled.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|_process_one]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|_reenrich_chunk]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|enrich]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|enrich_pending]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|load_pending_from_store]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|set_stores]] (function: belongs_to) — *Late-bind stores (called by the facade factory after construction).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|start_background_loop]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|stop_background_loop]] (function: belongs_to) — *Cancels the background enrichment loop gracefully.*
<!-- SYNC:END -->
