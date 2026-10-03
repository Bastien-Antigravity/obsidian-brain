

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|is_path_excluded]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_now]] (function: calls) — *Triggers an immediate enrichment pass on all pending chunks.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|get_caller_client]] (function: calls) — *Resolve the client ID requesting the MCP tool (e.g. CursorIDE, VSCodeIDE, AntigravityIDE, SquadAgent).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|run]] (function: calls) — *Start the MCP SSE server on the specified or current event loop.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|ALL_TOOLS]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|MAX_FILES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_check_permission]] (function: belongs_to) — *Strictly enforces Access Control Matrix (ACM) and write protections.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_find]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_find_symbol_db]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_fold_generic_code]] (function: belongs_to) — *Folds braced language function bodies (JS/TS/Go/Rust/C++).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_fold_python_code]] (function: belongs_to) — *Folds python function/class bodies to show only signatures and docstrings.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_get_generic_live_outline]] (function: belongs_to) — *Generate a regex-based fallback outline for non-python code files.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_get_mode]] (function: belongs_to) — *Retrieves the active squad mode from environment.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_get_python_live_outline]] (function: belongs_to) — *Generate high-fidelity outline of Python classes and functions using AST.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_list]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_merge_contiguous_chunks]] (function: belongs_to) — *Merges contiguous chunks from the same file to save context tokens.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_query]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_query_nodes_or_edges]] (function: belongs_to) — *Helper to query codebase relational graph DB in PostgreSQL.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_query_symbols]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_run]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_run_cmd]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_scan_concepts]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_scan_dir]] (function: belongs_to) — *Sub-function for recursive listing respecting firewalls*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_search_walk]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_traverse]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|audit_documentation]] (function: belongs_to) — *Perform a system-wide audit to find all broken links (orphans).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|check_documentation_drift]] (function: belongs_to) — *Check if docs linked to a code chunk are out of sync.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|enrich_brain]] (function: belongs_to) — *Trigger an immediate LLM enrichment pass on all pending chunks.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|find_dependency_path]] (function: belongs_to) — *Finds the shortest relational path connecting start_node and end_node in the ecosystem graph.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_architecture_standard]] (function: belongs_to) — *Retrieve authoritative architectural standards for a specific ecosystem category (ports, config, networking, docker, ...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_brain_stats]] (function: belongs_to) — *Retrieve statistics about the RAG index.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_codebase_relations]] (function: belongs_to) — *Query the codebase dependency graph database for relationships.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_coding_standard]] (function: belongs_to) — *Retrieve authoritative, unabridged coding standards for a specific programming language (go, rust, python, cpp, vba).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_file_dependencies]] (function: belongs_to) — *Get imports and outbound/inbound dependencies for a workspace file using the codebase graph.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_file_outline]] (function: belongs_to) — *Retrieve a compact outline of a file. For code files, returns defined symbols with line numbers. For Markdown, return...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_fleet_status]] (function: belongs_to) — *Audit Git status, branch, clean/dirty state, and ahead/behind commit counts across the fleet or for a target repo.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_session_context]] (function: belongs_to) — *Exposes current squad mode settings, ACM rules, write protections, and folder/file exclusions.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_subgraph]] (function: belongs_to) — *Retrieve the immediate subgraph neighborhood of a specific node by its ID. Supports depth-based recursive traversals.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_symbol_source]] (function: belongs_to) — *Directly fetch the exact source code block of a class, function, or method across the codebase, respecting ACM permis...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|index_workspace_files]] (function: belongs_to) — *Triggers indexing pipeline updates for specific file paths.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|list_concepts]] (function: belongs_to) — *Lists all available high-level design documents and microservice MOC hubs. High-performance cache-backed scanner. Use...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|list_drifted_documents]] (function: belongs_to) — *Lists all documentation markdown files that have drifted (become out-of-sync) with the active codebase.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|list_workspace_directory]] (function: belongs_to) — *List contents of a directory with security enforcement. Supports recursive lists (depth parameter) and regex/glob mat...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_brain]] (function: belongs_to) — *Search the knowledge base for relevant context. Supports verbosity overrides ('full', 'signatures').*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_ecosystem_graph]] (function: belongs_to) — *Search the ecosystem knowledge graph. Performs hybrid vector search to find seed nodes, traverses neighborhood to dep...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_strategic_decisions]] (function: belongs_to) — *Retrieve active architectural decisions, Anti-Backlog constraints, or strategic patterns from the database. Provide a...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|read_workspace_file]] (function: belongs_to) — *Read a file in the workspace, with optional start/end line boundaries (1-indexed). Output is prefixed with line numbe...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|register_documentation_link]] (function: belongs_to) — *Registers a link between a code chunk and a doc note.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|reset_and_rebuild_index]] (function: belongs_to) — *Clears all stores and rebuilds the full workspace index.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|resolve_documentation_drift]] (function: belongs_to) — *Resolves documentation drift by writing updated content and re-aligning hashes.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|search_code]] (function: belongs_to) — *Perform a high-speed keyword or regex search across files in the workspace (ripgrep-like), respecting ACM permissions...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|search_symbols]] (function: belongs_to) — *Search for code symbols (functions, classes, methods) in the codebase graph matching a query.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|sort_key]] (function: belongs_to) — *Sort results by source_path, then start_line*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|suggest_doc_rewrite]] (function: belongs_to) — *Generate a self-healing prompt for the AI to rewrite drifted documentation.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|sync_code_doc]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|sync_fleet]] (function: belongs_to) — *Perform atomic pull, submodule updates, and push across the fleet or for a target repo.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|validate_code_compliance]] (function: belongs_to) — *Mechanically audits a source code file or directory against ecosystem invariants (Triple-Block header, section divide...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|validate_code_syntax]] (function: belongs_to) — *Run a fast, non-destructive compile or syntax validation check on a file in the workspace, returning syntax/type erro...*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|vault_sync]] (function: belongs_to) — *Perform an atomic sync of obsidian-brain submodules and parent pointer.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|write_workspace_file]] (function: belongs_to) — *Create or overwrite a file.*
<!-- SYNC:END -->
