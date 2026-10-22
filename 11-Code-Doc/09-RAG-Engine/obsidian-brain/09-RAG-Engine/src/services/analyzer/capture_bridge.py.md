---
source: obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.439782
---

# Mirror: capture_bridge.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py`.

> **Essential Process**:
> Helper bridge to capture CodeEngine definitions as RAG-compatible chunks. Used by the CodeEngineAnalyzerBridge to intercept parser output.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|RAGCaptureBridge]] (class: belongs_to) — *Helper to capture CodeEngine definitions as RAG-compatible chunks.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|_extract_segment]] (function: belongs_to) — *Simple heuristic to extract a code block starting at start_line.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|add_edge]] (function: belongs_to) — *Edges are ignored for basic RAG chunking.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|add_node]] (function: belongs_to) — *Intercepts 'add_node' from CodeEngine parsers to create RAG chunks.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|register_symbol]] (function: belongs_to) — *Registering symbols is handled by the add_node interception.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
