---
source: obsidian-brain/08-Squad-Agent/src/agents/base_agent.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.591662
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: base_agent.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/base_agent.py`.

> **Essential Process**:
> Autonomous Agent Base Class and Tool Execution Engine for the AI Squad. Provides unified LLM prompt compilation, tool calling, memory history retrieval, cross-brain task_context handoffs, and reactive event bus message processing.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|ComplianceAuditor]] (class: calls) — *Mechanical compliance scanner for code files.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_file]] (function: calls) — *Audits a single source file and returns a list of detected violations.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|RAGMemoryStore]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: calls) — *Appends a new turn to the isolated session buffer, capping per-session and total capacity.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: calls) — *Retrieves active conversation history strictly for the requested session.*
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py.md|task_decomposer.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_AUDITED_EXTENSIONS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_AUDITED_FILENAMES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_BLOCKED_IN_WORKTREE_TOOLS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_BLOCKED_WORKSPACE_ROOTS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_LIST_EXCLUDED_DIRS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_MAX_LISTED_FILES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_MAX_TOOL_OUTPUT_CHARS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_MUTATING_TOOL_NAMES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_PROTECTED_SANDBOX_FILENAMES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_READ_ONLY_ROLES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_RESERVED_PRIMARY_BRAINS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_SANDBOX_SHELL_META_CHARS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_SCRUBBED_SUBPROCESS_SECRETS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_audit_written_file]] (function: belongs_to) — *Runs ComplianceAuditor on newly written/edited source and manifest files and formats feedback.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_compile_active_instruction]] (function: belongs_to) — *Compiles system instruction with dynamic task_context details when active.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_execute_sandboxed_command]] (function: belongs_to) — *Executes strictly allowlisted test/check binaries with shell=False inside the worktree jail.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fetch_history]] (function: belongs_to) — *Queries postgres squad_chat_logs for history turns.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fold_generic_code]] (function: belongs_to) — *Folds braced language function bodies (JS/TS/Go/Rust/C++).*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_fold_python_code]] (function: belongs_to) — *Folds python function/class bodies to show only signatures and docstrings.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_get_effective_tools]] (function: belongs_to) — *Returns active LLM tools filtered by read_only or worktree_sandbox_mode policy.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_get_squad_capability]] (function: belongs_to) — *Reads squad_agent capability settings from AppConfig data or accessor.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_infer_domain_vault_path]] (function: belongs_to) — *Infers the Obsidian vault root inside a registered domain workspace.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_init_genai_client]] (function: belongs_to) — *Initialises or updates the Google GenAI Client with active credentials.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_is_valid_domain_workspace]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_load_system_prompt]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_parse_extra_workspaces_env]] (function: belongs_to) — *Splits EXTRA_WORKSPACES supporting both comma and colon entry delimiters.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_publish_agent_response]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_read_optional_text]] (function: belongs_to) — *Directly reads an optional text file without a TOCTOU pre-check.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_refresh_llm_config]] (function: belongs_to) — *Dynamically re-reads LLM configuration from config capability or environment for live hot-reload.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_register]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_resolve_active_workspace_root]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_resolve_guarded_workspace_root]] (function: belongs_to) — *Resolves active workspace root for tool calls, failing fast if explicit target_workspace_path is invalid.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_run_mock_think_and_respond]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_save_log]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_validate_mutation_target]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_write_atomic_synced]] (function: belongs_to) — *Atomically persists file contents via .tmp write + fsync + os.replace with guaranteed cleanup.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|current_source_brain]] (function: belongs_to) — *Task-isolated active source brain identifier (race-free across concurrent async turns).*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|current_task_context]] (function: belongs_to) — *Task-isolated active cross-brain context dictionary (race-free across concurrent async turns).*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|db_insert]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|db_query]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|discover_registered_domain_workspaces]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|edit_workspace_file]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|enable_readonly_mode]] (function: belongs_to) — *Enforces strict read-only tool permissions on this agent instance.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|enable_worktree_sandbox_mode]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|execute_shell_command]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|execute_tool]] (function: belongs_to) — *Dynamic tool execution handler.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|list_workspace_files]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|msg_cb]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|on_chat_message]] (function: belongs_to) — *Callback invoked when a new message arrives in the room.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|query_rag_engine]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|read_workspace_file]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|slugify_role_name]] (function: belongs_to) — *Normalizes a prompt stem or role label into a canonical lowercase slug.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|start]] (function: belongs_to) — *Registers the agent message consumer loop.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|stop]] (function: belongs_to) — *Clean shut down.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|think_and_respond]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|write_workspace_file]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|debloatsentinel.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|debloatsentinel.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|debloatsentinel.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|eval_agent.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|eval_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|agent_dispatcher.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|agent_dispatcher.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
