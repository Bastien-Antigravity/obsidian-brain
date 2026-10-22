---
source: obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.296590
---

# Mirror: tools.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py`.

> **Essential Process**:
> Decoupled Model Context Protocol (MCP) tools for the Obsidian Brain RAG Engine. Defines all RAG search, filesystem, security/context, and graph tools as portable Python functions, completely independent of the server/transport framework.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|is_path_excluded]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_now]] (function: calls) — *Triggers an immediate enrichment pass on all pending chunks.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|get_caller_client]] (function: calls) — *Resolve the client ID requesting the MCP tool (e.g. CursorIDE, VSCodeIDE, AntigravityIDE, SquadAgent).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|ALL_TOOLS]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|MAX_FILES]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_check_permission]] (function: belongs_to) — *Strictly enforces Access Control Matrix (ACM) and write protections.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_find]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_find_symbol_db]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_fold_generic_code]] (function: belongs_to) — *Folds braced language function bodies (JS/TS/Go/Rust/C++).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_fold_python_code]] (function: belongs_to) — *Folds python function/class bodies to show only signatures and docstrings.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_get_generic_live_outline]] (function: belongs_to) — *Generate a regex-based fallback outline for non-python code files.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_get_mode]] (function: belongs_to) — *Retrieves the active squad mode from environment.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_get_python_live_outline]] (function: belongs_to) — *Generate high-fidelity outline of Python classes and functions using AST.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_list]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_merge_contiguous_chunks]] (function: belongs_to) — *Merges contiguous chunks from the same file to save context tokens.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_query]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_query_nodes_or_edges]] (function: belongs_to) — *Helper to query codebase relational graph DB in PostgreSQL.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_query_symbols]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_run]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_run_cmd]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_scan_concepts]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_scan_dir]] (function: belongs_to) — *Sub-function for recursive listing respecting firewalls*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_search_walk]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|_traverse]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|audit_documentation]] (function: belongs_to) — *Perform a system-wide audit to find all broken links (orphans).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|check_documentation_drift]] (function: belongs_to) — *Check if docs linked to a code chunk are out of sync.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|enrich_brain]] (function: belongs_to) — *Trigger an immediate LLM enrichment pass on all pending chunks.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|find_dependency_path]] (function: belongs_to) — *Finds the shortest relational path connecting start_node and end_node in the ecosystem graph.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_architecture_standard]] (function: belongs_to) — *Retrieve authoritative architectural standards for a specific ecosystem category (ports, config, networking, docker, ...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_brain_stats]] (function: belongs_to) — *Retrieve statistics about the RAG index.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_codebase_relations]] (function: belongs_to) — *Query the codebase dependency graph database for relationships.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_coding_standard]] (function: belongs_to) — *Retrieve authoritative, unabridged coding standards for a specific programming language (go, rust, python, cpp, vba).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_file_dependencies]] (function: belongs_to) — *Get imports and outbound/inbound dependencies for a workspace file using the codebase graph.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_file_outline]] (function: belongs_to) — *Retrieve a compact outline of a file. For code files, returns defined symbols with line numbers. For Markdown, return...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_fleet_status]] (function: belongs_to) — *Audit Git status, branch, clean/dirty state, and ahead/behind commit counts across the fleet or for a target repo.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_session_context]] (function: belongs_to) — *Exposes current squad mode settings, ACM rules, write protections, and folder/file exclusions.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_subgraph]] (function: belongs_to) — *Retrieve the immediate subgraph neighborhood of a specific node by its ID. Supports depth-based recursive traversals.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|get_symbol_source]] (function: belongs_to) — *Directly fetch the exact source code block of a class, function, or method across the codebase, respecting ACM permis...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|index_workspace_files]] (function: belongs_to) — *Triggers indexing pipeline updates for specific file paths.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|list_concepts]] (function: belongs_to) — *Lists all available high-level design documents and microservice MOC hubs. High-performance cache-backed scanner. Use...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|list_drifted_documents]] (function: belongs_to) — *Lists all documentation markdown files that have drifted (become out-of-sync) with the active codebase.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|list_workspace_directory]] (function: belongs_to) — *List contents of a directory with security enforcement. Supports recursive lists (depth parameter) and regex/glob mat...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_brain]] (function: belongs_to) — *Search the knowledge base for relevant context. Supports verbosity overrides ('full', 'signatures').*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_ecosystem_graph]] (function: belongs_to) — *Search the ecosystem knowledge graph. Performs hybrid vector search to find seed nodes, traverses neighborhood to dep...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_strategic_decisions]] (function: belongs_to) — *Retrieve active architectural decisions, Anti-Backlog constraints, or strategic patterns from the database. Provide a...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|read_workspace_file]] (function: belongs_to) — *Read a file in the workspace, with optional start/end line boundaries (1-indexed). Output is prefixed with line numbe...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|register_documentation_link]] (function: belongs_to) — *Registers a link between a code chunk and a doc note.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|reset_and_rebuild_index]] (function: belongs_to) — *Clears all stores and rebuilds the full workspace index.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|resolve_documentation_drift]] (function: belongs_to) — *Resolves documentation drift by writing updated content and re-aligning hashes.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|search_code]] (function: belongs_to) — *Perform a high-speed keyword or regex search across files in the workspace (ripgrep-like), respecting ACM permissions...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|search_symbols]] (function: belongs_to) — *Search for code symbols (functions, classes, methods) in the codebase graph matching a query.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|sort_key]] (function: belongs_to) — *Sort results by source_path, then start_line*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|suggest_doc_rewrite]] (function: belongs_to) — *Generate a self-healing prompt for the AI to rewrite drifted documentation.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|sync_code_doc]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|sync_fleet]] (function: belongs_to) — *Perform atomic pull, submodule updates, and push across the fleet or for a target repo.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|validate_code_compliance]] (function: belongs_to) — *Mechanically audits a source code file or directory against ecosystem invariants (Triple-Block header, section divide...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|validate_code_syntax]] (function: belongs_to) — *Run a fast, non-destructive compile or syntax validation check on a file in the workspace, returning syntax/type erro...*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|vault_sync]] (function: belongs_to) — *Perform an atomic sync of obsidian-brain submodules and parent pointer.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|write_workspace_file]] (function: belongs_to) — *Create or overwrite a file.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
