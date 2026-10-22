---
source: obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.364881
---

# Mirror: base_parser.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py`.

> **Essential Process**:
> Defines the base interface for language-specific parsers. Enforces a consistent API for symbol definition extraction and reference resolution across all languages.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|BaseParser]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|parse_definitions]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|parse_references]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|html_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|html_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|html_parser.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
