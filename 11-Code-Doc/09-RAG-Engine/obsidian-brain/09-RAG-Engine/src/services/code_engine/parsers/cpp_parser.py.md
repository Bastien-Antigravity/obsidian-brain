---
source: obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.368944
---

# Mirror: cpp_parser.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py`.

> **Essential Process**:
> Specialized parser for C/C++ files using Tree-sitter. Extracts classes, structs, methods (both inline and qualified), includes, and references.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|resolve_symbol_reference]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|BaseParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|base_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|base_parser.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|CppParser]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|__getstate__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|__setstate__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_init_tree_sitter]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_resolve_declarator]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_resolve_include]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_resolve_ref]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_walk_definitions]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|_walk_references]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|parse_definitions]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|parse_references]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
