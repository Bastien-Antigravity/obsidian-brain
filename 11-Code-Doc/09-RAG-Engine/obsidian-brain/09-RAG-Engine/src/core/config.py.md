---
source: obsidian-brain/09-RAG-Engine/src/core/config.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.995616
---

# Mirror: config.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/config.py`.

> **Essential Process**:
> Dynamic configuration accessors for 09-RAG-Engine. Replaces static dataclasses with dynamic accessors that read directly from microservice_toolbox.config.loader.AppConfig and distributed-config, with runtime hyperparameter overrides backed by PostgreSQL schema `09-RAG-Engine.configuration`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_config]] (function: calls) — *Retrieves a configuration value from the configuration loader.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|db_config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get_db_config_service]] (function: calls) — *Singleton getter for DBConfigService.*

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|_decrypt_secret_val]] (function: belongs_to) — *Safely decrypts an ENC(...) token using the AppConfig decrypt_secret method if available.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|_is_db_enabled]] (function: belongs_to) — *Checks if database connection capability is configured (guards against auto-specced mocks).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_dashboard_settings]] (function: belongs_to) — *Resolves web dashboard configuration.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_db_settings]] (function: belongs_to) — *Resolves database connection settings with decrypted credentials and target RAG database.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_enrichment_settings]] (function: belongs_to) — *Resolves LLM enrichment configuration with automatic secret decryption.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_mcp_settings]] (function: belongs_to) — *Resolves FastMCP network and protocol configuration.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_query_engine_settings]] (function: belongs_to) — *Resolves hybrid search, fusion, and reranker settings (config file overrides DB defaults).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_rag_setting]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_watch_settings]] (function: belongs_to) — *Resolves filesystem watcher configuration.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
