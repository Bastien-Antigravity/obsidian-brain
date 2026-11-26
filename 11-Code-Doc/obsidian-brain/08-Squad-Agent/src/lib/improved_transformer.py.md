---
source: obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.680783
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: improved_transformer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py`.

> **Essential Process**:
> Python code transformation engine (CodeTransformer) for the Specialist agent. Refactors and cleans source code to make it compliant with governance. Uses AST-based refactoring for robust import management.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: calls) — *Appends a new turn to the isolated session buffer, capping per-session and total capacity.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|CodeTransformer]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|UsageCollector]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_clean_shebang_and_encoding]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_ensure_class_and_method_docstrings]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_ensure_docstring_empty_line]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_ensure_granular_imports]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_ensure_granular_imports_regex]] (function: belongs_to) — *Original regex fallback (kept for safety).*
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_ensure_logger_formatting]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_ensure_method_dividers]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_ensure_triple_block_docstring]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_log]] (function: belongs_to) — *Delegates logging directly to the UniLog engine.*
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_register_used]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|_to_offset]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|is_internal_module]] (function: belongs_to) — *Returns True if the import targets an internal project/ecosystem local module.*
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|main]] (function: belongs_to) — *CLI runner for format-compliance.*
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|make_camel_alias]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|replace_f]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|replace_s]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|transform]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|transform_file]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|transform_path]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|visit_Attribute]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|visit_Name]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
