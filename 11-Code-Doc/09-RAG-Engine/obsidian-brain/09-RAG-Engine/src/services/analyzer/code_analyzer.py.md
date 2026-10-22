---
source: obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.445021
---

# Mirror: code_analyzer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py`.

> **Essential Process**:
> Advanced multi-language analyzer that bridges the RAG system with the deep structural parsing logic of the CodeEngine.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|Analyzer]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|RAGCaptureBridge]] (class: calls) — *Helper to capture CodeEngine definitions as RAG-compatible chunks.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|capture_bridge.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|capture_bridge.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|CppParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|GoParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|HtmlParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|html_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|parse_definitions]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|JavaScriptParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|PythonParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|RustParser]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|CodeEngineAnalyzerBridge]] (class: belongs_to) — *Bridge analyzer that uses CodeEngine's AST-based parsers for structural chunking.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|analyze]] (function: belongs_to) — *Analyzes code files using AST parsers to extract symbols as chunks.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
