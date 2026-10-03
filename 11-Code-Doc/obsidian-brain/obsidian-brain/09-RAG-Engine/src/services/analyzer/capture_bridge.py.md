

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py`.

> **Essential Process**:
> Helper bridge to capture CodeEngine definitions as RAG-compatible chunks. Used by the CodeEngineAnalyzerBridge to intercept parser output.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|RAGCaptureBridge]] (class: belongs_to) — *Helper to capture CodeEngine definitions as RAG-compatible chunks.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|_extract_segment]] (function: belongs_to) — *Simple heuristic to extract a code block starting at start_line.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|add_edge]] (function: belongs_to) — *Edges are ignored for basic RAG chunking.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|add_node]] (function: belongs_to) — *Intercepts 'add_node' from CodeEngine parsers to create RAG chunks.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|register_symbol]] (function: belongs_to) — *Registering symbols is handled by the add_node interception.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (same_package)
<!-- SYNC:END -->
