---
microservice: obsidian-brain
type: session-state
status: active
tags:
- '#service/obsidian-brain'
- '#type/session-state'
- '#state/active'
- '#zone/3-fleet'
---

# AI Session State: obsidian-brain

Mission-ID: MISSION-AUTONOMOUS-001
Trace-ID: TRACE-AUTONOMOUS-001
Status: Active / Ready

## Latest Changes (2026-08-05)
- **ChromaDB Purge**: Completely purged all obsolete ChromaDB references, `.chroma_db` directory, `chromadb` pip requirement, gitignore rules, BDD specs, and documentation across the codebase.
- **Standards Alignment**: Standardized all RAG vector store references on PostgreSQL + pgvector.
- **99-Humans Refactoring & RAG Sync**: Relocated technical specs to `03-Tech-Stack/02-Project-Architecture/`, archived scratch notes to `01-Strategic-Nexus/archive/`, verified 1,187 markdown files with Sovereignty Engine, and re-indexed the RAG engine.
- **RAG Seed Export & Import Tooling (Option 1)**: Added `export-seed` and `import-seed` CLI commands in `09-RAG-Engine/main.py`, implemented secret/path sanitization in `SeedService`, created `docker-compose.db.yml`, and generated the official `data/seed` dataset package.
- **RAG Data Exclusion & README Fix**: Added `"data"` to `GLOBAL_EXCLUDES` in `09-RAG-Engine/src/core/constants.py` to exclude seed/data folders from indexing, and restored `sync-docs` documentation in `09-RAG-Engine/README.md`.
- **RAG-Engine Phase 1 Optimization & Real-Time Deletion (2026-10-12)**:
  - Deduplicated PostgreSQL startup check in `09-RAG-Engine/src/facade/__init__.py`, removing 46 lines of redundant raw `psycopg2` connects and letting `src/utils/pg_pool.py` serve as single authoritative database/extension/schema check.
  - Implemented missing key negative caching with TTL in `DBConfigService` (`src/services/config/db_config.py`) to prevent leasing connections for missing hyperparameters during file-change indexing.
  - Applied granular functional imports (`[module][FunctionName]`) across `db_config.py`.
  - Audited ecosystem scripts for runner callers; verified zero callers for `IndexerRunner` and `WatcherRunner`, cleaned dead runners from `src/core/runners.py` while preserving `VisualizerRunner` and `start_visualizer`.
  - Implemented real-time chunk removal on file deletion/move: wired `UnifiedWatcher.on_deleted` and `on_moved` through `delete_callback` -> `RAGFacade.delete_file` -> `StandardIndexingPipeline.delete_file`, pruning records across pgvector (`vector_store`), BM25 (`lexical_store`), `parent_store`, and `graph_db`.
  - Added unit tests in `tests/test_pipeline.py` and `tests/test_db_config.py`; all 83 test cases passing.
- **RAG-Engine Phase 2 Indexing Acceleration (2026-10-12)**:
  - **Codebase AST Analysis Batching**: Added `insert_nodes_batch` and `insert_edges_batch` to `ICodebaseDB` and `PostgresCodebaseDB` using `psycopg2.extras.execute_values`. Updated `CodeEngine.run_analysis()` to buffer AST nodes and edges across Pass 1 & 2, flushing in a single batch transaction instead of ~25,000 individual queries.
  - **Vector Store Multi-Row Batching**: Replaced single-row cursor loops in `PgVectorStore.add_documents()` with `execute_values(cursor, sql, batch_data, page_size=200)` and set `batch_size=32` on `SentenceTransformer.encode()`.
  - **Lexical Store Multi-Row Batching**: Replaced single-row cursor loops in `PostgresLexicalStore.add_documents()` with `execute_values(cursor, sql, batch_data, template="(%s, %s, %s, to_tsvector('english', %s))", page_size=200)`.
  - **Parent Store Multi-Row Batching**: Replaced single-row cursor loops in `PostgresParentStore.store_parents_batch()` with `execute_values(cursor, sql, batch_data, page_size=200)`.
  - **Validation & Stability**: Verified full test suite; all 83 test cases passed with zero regressions. Single-file watcher event behavior remains 100% guarded and operational.
- **RAG-Engine Phase 3 Startup Acceleration, Memory Efficiency & Lightweight Pruning (2026-10-12)**:
  - **Fast CLI Bootstrap**: Removed eager `import torch` and `import sentence_transformers` from `src/bootstrap/__init__.py`. Reduced `main.py` CLI invocation latency from 10.85s to 0.53s (~20x faster).
  - **Lazy & Shared Model Loading**: Implemented `PgVectorStore._shared_model` singleton and `@property def model`, deferring model weight loading until first embedding call and sharing weights across all tenant schemas to eliminate 2.2GB memory duplication.
  - **Lightweight Orphan Pruning**: Added `get_all_source_paths()` to `PgVectorStore` and `MultiTenantVectorStoreProxy`, replacing memory-heavy `get_all()` text extraction with a <15ms distinct SQL query.
  - **RAG-Engine Ecosystem Coding Standards Sweep & Code-Doc Alignment (2026-10-12)**:
  - **100% Repository Compliance**: Audited all 106 `.py` files across `09-RAG-Engine` (`src/`, `main.py`, and `tests/`) against the `pythonspecialist` mandate.
  - **Triple-Block Headers**: Verified each file features `ESSENTIAL PROCESS:`, `DATA FLOW:`, and `KEY PARAMETERS:`.
  - **Execution Shebang**: Standardized `#!/usr/bin/env python` and `# coding:utf-8` with exactly one empty line before docstrings.
  - **Granular Imports & CamelCase Aliasing**: Removed unaliased imports (`import os`, `import sys`, `import json`, `import re`, `import time`, `import asyncio`, etc.) outside bootstrap entrypoints; converted to granular camelCase imports (`from time import time as timeTime`, `from json import dumps as jsonDumps`, `from re import split as reSplit`, `from typing import List as typingList`).
  - **Dead Import Elimination**: Purged vestigial and unused modules across all services (`pg_pool.py`, `graph/postgres_db.py`, `postgres_alignment.py`, `seed_service.py`, `tools.py`, `fastmcp.py`).
  - **Code-Doc Comment Separators**: Enforced exactly 95-dash horizontal rule dividers (`# -----------------------------------------------------------------------------------------------`) between classes, methods, and major sections.
  - **Verification**: Complete test suite executed; all 85 unit and integration tests passing with 100% success rate.


