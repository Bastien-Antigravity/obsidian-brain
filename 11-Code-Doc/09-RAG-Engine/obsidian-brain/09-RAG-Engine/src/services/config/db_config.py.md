---
source: obsidian-brain/09-RAG-Engine/src/services/config/db_config.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.256788
---

# Mirror: db_config.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/config/db_config.py`.

> **Essential Process**:
> Database-backed runtime configuration service for 09-RAG-Engine. Manages the `09-RAG-Engine.configuration` table for live hyperparameter tuning (similarity thresholds, reranker models, search fusion weights, prompts).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|lab_manager.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|ensure_frontmatter.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|discord_client.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|agent_dispatcher.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/build_inventory.py.md|build_inventory.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|close_mission.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|fleet_commander.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_init_update.py.md|fleet_init_update.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|fleet_refresh.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|fleet_version.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|service.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|interfaces.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|pg_pool.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|joint_audit_purger.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|manager.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|server.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|mfe.js]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/access_matrix.py.md|access_matrix.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|service.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|codebase_db.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|markdown_analyzer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|DBConfigService]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|SECRET_KEY_PATTERNS]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_SERVICE_INSTANCE]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_encrypt_secret_for_db]] (function: belongs_to) — *Encrypts plaintext with RSA-OAEP SHA-256 for secure database persistence.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_get_pool_and_schema]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_get_public_key_pem]] (function: belongs_to) — *Resolves public key PEM string from AppConfig or standard file paths.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|_is_secret_key]] (function: belongs_to) — *Identifies whether a configuration key represents sensitive credentials.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get_all]] (function: belongs_to) — *Returns all runtime hyperparameters currently configured in the database.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get_db_config_service]] (function: belongs_to) — *Singleton getter for DBConfigService.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|init_table]] (function: belongs_to) — *Ensures the configuration table exists in the repository schema.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|llm_expander.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|manager.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.js]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/graph/CycleDetector.js.md|CycleDetector.js]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|squad_facade.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|planner.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|safety.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|summarize.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/web_search.py.md|web_search.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
