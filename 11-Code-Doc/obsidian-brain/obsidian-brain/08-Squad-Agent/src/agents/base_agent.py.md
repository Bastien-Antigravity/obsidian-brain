---
source: obsidian-brain/08-Squad-Agent/src/agents/base_agent.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.591662
---

# Mirror: base_agent.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/base_agent.py`.

> **Essential Process**:
> Autonomous Agent Base Class and Tool Execution Engine for the AI Squad. Provides unified LLM prompt compilation, tool calling, memory history retrieval, and reactive event bus message processing for all persona roles.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|RAGMemoryStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: calls) — *Retrieves active conversation history buffer.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls) — *Resolves public key PEM string from AppConfig or standard file paths.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fetch_history]] (function: belongs_to) — *Queries postgres squad_chat_logs for history turns.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fold_generic_code]] (function: belongs_to) — *Folds braced language function bodies (JS/TS/Go/Rust/C++).*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fold_python_code]] (function: belongs_to) — *Folds python function/class bodies to show only signatures and docstrings.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_load_system_prompt]] (function: belongs_to) — *Reads the agent role's system instruction from KMS files.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_run_mock_think_and_respond]] (function: belongs_to) — *Generates a simulated role-specific mock response for testing offline.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_save_log]] (function: belongs_to) — *Saves a conversation turn to squad_chat_logs.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|db_insert]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|db_query]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|execute_shell_command]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|execute_tool]] (function: belongs_to) — *Dynamic tool execution handler.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|msg_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|on_chat_message]] (function: belongs_to) — *Callback invoked when a new message arrives in the room.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|query_rag_engine]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|read_workspace_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|start]] (function: belongs_to) — *Registers the agent message consumer loop.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|stop]] (function: belongs_to) — *Clean shut down.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|think_and_respond]] (function: belongs_to) — *Queries Gemini using conversation logs database history and broadcasts response.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|write_workspace_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
