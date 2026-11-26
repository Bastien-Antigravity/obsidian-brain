

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py`.

> **Essential Process**:
> Specialized parser for C/C++ files using Tree-sitter. Extracts classes, structs, methods (both inline and qualified), includes, and references.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|resolve_symbol_reference]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|BaseParser]] (class: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|UTF8Content]] (class: calls) — *Wrapper around UTF-8 bytes so Tree-sitter byte-offset slicing returns decoded str.*
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|base_parser.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|base_parser.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|CppParser]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|__getstate__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|__setstate__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_init_tree_sitter]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_resolve_declarator]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_resolve_include]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_resolve_ref]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_walk_definitions]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_walk_references]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|parse_definitions]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|parse_references]] (function: belongs_to)
<!-- SYNC:END -->
