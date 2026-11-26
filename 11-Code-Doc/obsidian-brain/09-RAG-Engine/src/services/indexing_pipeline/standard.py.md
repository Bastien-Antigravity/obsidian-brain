

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py`.

> **Essential Process**:
> Standard indexing pipeline coordinating the transformation of files into RAG chunks. Handles file reading, exclusion checking, chunking, enrichment, and storage.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_rag_setting]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|has_meaningful_codedoc_notes]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|get_workspace_registry]] (function: calls) — *Returns the process-wide WorkspaceRegistry singleton.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_brain_for_path]] (function: calls) — *Resolves the owning brain_id for an absolute filesystem path via deepest prefix match.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_workspace_root]] (function: calls) — *Resolves the workspace root directory for the given brain_id (defaults to primary).*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|analyze]] (function: calls) — *Analyzes file content and returns a list of logical chunks/entities.*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|analyzer.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enrich]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enricher.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|IndexingPipeline]] (class: calls)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|indexing_pipeline.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|add_documents]] (function: calls) — *Populates the lexical index with a corpus of documents.*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|delete_by_source]] (function: calls) — *Deletes all data records associated with a source file path.*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|get_all_file_hashes]] (function: calls) — *Retrieves all stored file hashes from the database as a dictionary {source_path: file_hash}.*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|is_file_changed]] (function: calls) — *Checks if a file's hash differs from the stored version (Differential Indexing).*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|store_parents_batch]] (function: calls) — *Persists a batch of chunks in a single database transaction.*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|update_file_hash]] (function: calls) — *Updates the stored hash for a file after successful indexing.*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|get_all]] (function: calls) — *Retrieves all records currently stored in the vector collection.*
- [[obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|MChunk]] (class: calls) — *Represents a logical chunk of a document/code.*
- [[obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|chunk.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|MChunkMetadata]] (class: calls) — *Normalized metadata for a logical chunk.*
- [[obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|FileResult]] (class: belongs_to) — *Container for parsed file results before batching.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|StandardIndexingPipeline]] (class: belongs_to) — *Coordinates the multi-stage indexing process for files.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_batch_flusher_loop]] (function: belongs_to) — *Background task that aggregates FileResults and flushes them in batches.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_enrich_one]] (function: belongs_to) — *1. Enrich (in parallel, leveraging LLMEnricher's internal semaphore)*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_ensure_loop_primitives]] (function: belongs_to) — *Rebinds asyncio Queue and Lock if the pipeline is invoked on a new/different event loop.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_flush_batch]] (function: belongs_to) — *Atomically enriches and stores a batch of files.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_get_supported_extensions]] (function: belongs_to) — *Returns set of normalized file extensions (e.g. {'.py', '.md', '.txt'}) supported by pipeline & analyzers.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_has_meaningful_codedoc_notes]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_lazy_init_graph_helpers]] (function: belongs_to) — *Lazy loads inventory.json and maps note stems if not already loaded.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_load_inventory_and_map_notes]] (function: belongs_to) — *Loads inventory.json and builds a mapping of note stem names to file paths.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_resolve_service_for_path]] (function: belongs_to) — *Determines which microservice a file belongs to based on the repository registry.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|build_full_index]] (function: belongs_to) — *Performs a full workspace scan and index rebuild.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|delete_file]] (function: belongs_to) — *Removes all chunks and records associated with a deleted file.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|ensure_batcher]] (function: belongs_to) — *Starts the batch flusher loop if not already running, tracking active concurrent callers.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|process_file]] (function: belongs_to) — *Indexes a single file into the RAG system.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|release_batcher]] (function: belongs_to) — *Decrements the active indexer count and flushes/stops the batcher only when all callers finish.*
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|worker]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (calls)
<!-- SYNC:END -->
