---
source: obsidian-brain/09-RAG-Engine/src/core/config.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-09-17T06:24:01.776908
---

# Mirror: config.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/config.py`.

> **Essential Process**:
> Dynamic configuration accessors for 09-RAG-Engine. Replaces static dataclasses with dynamic accessors that read directly from microservice_toolbox.config.loader.AppConfig and distributed-config, with runtime hyperparameter overrides backed by PostgreSQL schema `09-RAG-Engine.configuration`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_config]] (function: calls) — *Retrieves a configuration value from the configuration loader.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|db_config.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get_db_config_service]] (function: calls) — *Singleton getter for DBConfigService.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|_decrypt_secret_val]] (function: belongs_to) — *Safely decrypts an ENC(...) token using the AppConfig decrypt_secret method if available.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|_is_db_enabled]] (function: belongs_to) — *Checks if database connection capability is configured (guards against auto-specced mocks).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_dashboard_settings]] (function: belongs_to) — *Resolves web dashboard configuration.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_db_settings]] (function: belongs_to) — *Resolves database connection settings with decrypted credentials and target RAG database.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_enrichment_settings]] (function: belongs_to) — *Resolves LLM enrichment configuration with automatic secret decryption.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_mcp_settings]] (function: belongs_to) — *Resolves FastMCP network and protocol configuration.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_query_engine_settings]] (function: belongs_to) — *Resolves hybrid search, fusion, and reranker settings (config file overrides DB defaults).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_rag_setting]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_watch_settings]] (function: belongs_to) — *Resolves filesystem watcher configuration.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
