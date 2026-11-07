---
source: obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-05T22:31:59.693718
---

# Mirror: debloat_audit.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py`.

> **Essential Process**:
> Unified Debloat Sentinel & AST Pattern Engine. Merges structural AST pattern extraction with bottom-up bloat & over-engineering analysis: - Level 1: Hardware & Memory Primitives (atomic types, immutable state, stack values). - Level 2: Runtime Concurrency Models (Go CSP channels, Python single-threaded asyncio). - Level 3: Component & Package Boundaries (1-to-1 interfaces, TOCTOU disk checks). - Level 4: Fleet & Network Boundaries (binary serialization schemas, DB constraints, transport auto-reconnect).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|debloatsentinel.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|debloatsentinel.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|Finding]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|PythonAnalyzer]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|SafeByDesignItem]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|audit_architectural_patterns]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|audit_go_file]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|audit_rust_file]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|generate_safe_by_design_markdown]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|get_default_baseline_path]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|resolve_target_path]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|run_debloat_audit]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|to_dict]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_Assign]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_AsyncFunctionDef]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_AsyncWith]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_ClassDef]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_FunctionDef]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_If]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_ImportFrom]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|visit_Import]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
