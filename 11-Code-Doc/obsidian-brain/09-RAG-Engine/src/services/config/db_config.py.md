---
source: obsidian-brain/09-RAG-Engine/src/services/config/db_config.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-09-17T06:23:59.478240
---

# Mirror: db_config.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/config/db_config.py`.

> **Essential Process**:
> Database-backed runtime configuration service for 09-RAG-Engine. Manages the `09-RAG-Engine.configuration` table for live hyperparameter tuning (similarity thresholds, reranker models, search fusion weights, prompts).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/access_matrix.py.md|access_matrix.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|service.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|codebase_db.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|markdown_analyzer.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/config/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|DBConfigService]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|SECRET_KEY_PATTERNS]] (constant: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_SERVICE_INSTANCE]] (constant: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_encrypt_secret_for_db]] (function: belongs_to) — *Encrypts plaintext with RSA-OAEP SHA-256 for secure database persistence.*
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_get_pool_and_schema]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_get_public_key_pem]] (function: belongs_to) — *Resolves public key PEM string from AppConfig or standard file paths.*
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_is_secret_key]] (function: belongs_to) — *Identifies whether a configuration key represents sensitive credentials.*
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get_all]] (function: belongs_to) — *Returns all runtime hyperparameters currently configured in the database.*
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get_db_config_service]] (function: belongs_to) — *Singleton getter for DBConfigService.*
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|init_table]] (function: belongs_to) — *Ensures the configuration table exists in the repository schema.*
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|llm_expander.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|manager.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/graph/CycleDetector.js.md|CycleDetector.js]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/graph/NodeRenderer.js.md|NodeRenderer.js]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|rag-mcp-inspector.js]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|mfe.js]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
