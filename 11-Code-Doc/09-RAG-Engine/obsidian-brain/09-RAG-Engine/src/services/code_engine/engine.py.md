---
source: obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.341786
---

# Mirror: engine.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py`.

> **Essential Process**:
> Core analysis engine for the Codebase Visualizer. Orchestrates file scanning, multi-language parsing, symbol resolution, and graph data export.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/models.py.md|models.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|CppParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|GoParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|HtmlParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|html_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|parse_definitions]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|parse_references]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|JavaScriptParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|PythonParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|RustParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|PostgresCodebaseDB]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|clear]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|get_edges]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|get_nodes]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_edge]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_edges_batch]] (function: calls) — *Batch inserts codebase edges using execute_values within a single transaction.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_node]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_nodes_batch]] (function: calls) — *Batch inserts codebase nodes using execute_values within a single transaction.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|PostgresGraphDB]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|export_unified_graph]] (function: calls) — *Exports the combined view of nodes and edges from all tables to a JSON file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (imports)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|CodebaseAnalyzer]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|_export_results]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|_scan_workspaces]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|add_edge]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|add_node]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|register_symbol]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|resolve_symbol_reference]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|run_analysis]] (function: belongs_to) — *Main entry point for analysis.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
