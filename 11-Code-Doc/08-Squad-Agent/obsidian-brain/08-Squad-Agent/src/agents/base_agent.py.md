---
source: obsidian-brain/08-Squad-Agent/src/agents/base_agent.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20T15:13:14.796244
---

# Mirror: base_agent.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/base_agent.py`.

> **Essential Process**:
> Autonomous Agent Base Class and Tool Execution Engine for the AI Squad. Provides unified LLM prompt compilation, tool calling, memory history retrieval, and reactive event bus message processing for all persona roles.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|RAGMemoryStore]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: calls) — *Retrieves active conversation history buffer.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fetch_history]] (function: belongs_to) — *Queries postgres squad_chat_logs for history turns.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fold_generic_code]] (function: belongs_to) — *Folds braced language function bodies (JS/TS/Go/Rust/C++).*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fold_python_code]] (function: belongs_to) — *Folds python function/class bodies to show only signatures and docstrings.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_init_genai_client]] (function: belongs_to) — *Initialises or updates the Google GenAI Client with active credentials.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_load_system_prompt]] (function: belongs_to) — *Reads the agent role's system instruction from KMS files.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_refresh_llm_config]] (function: belongs_to) — *Dynamically re-reads LLM configuration from config capability or environment for live hot-reload.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_run_mock_think_and_respond]] (function: belongs_to) — *Generates a simulated role-specific mock response for testing offline.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_save_log]] (function: belongs_to) — *Saves a conversation turn to squad_chat_logs.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|db_insert]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|db_query]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|execute_shell_command]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|execute_tool]] (function: belongs_to) — *Dynamic tool execution handler.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|msg_cb]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|on_chat_message]] (function: belongs_to) — *Callback invoked when a new message arrives in the room.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|query_rag_engine]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|read_workspace_file]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|start]] (function: belongs_to) — *Registers the agent message consumer loop.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|stop]] (function: belongs_to) — *Clean shut down.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|think_and_respond]] (function: belongs_to) — *Queries Gemini using conversation logs database history and broadcasts response.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|write_workspace_file]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
