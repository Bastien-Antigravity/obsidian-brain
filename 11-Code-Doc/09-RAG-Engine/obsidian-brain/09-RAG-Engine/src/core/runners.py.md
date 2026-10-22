---
source: obsidian-brain/09-RAG-Engine/src/core/runners.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.005798
---

# Mirror: runners.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/runners.py`.

> **Essential Process**:
> Asynchronous runner for the RAG Engine visualizer dashboard. Manages the lifecycle and event loop of the visualizer web server.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|start_async_server]] (function: calls) — *Starts the uvicorn server for FastAPI with harmonized logging.*

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|VisualizerRunner]] (class: belongs_to) — *Starts and manages the RAG visualizer dashboard.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|run]] (function: belongs_to) — *Starts the visualizer web server.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_visualizer]] (function: belongs_to) — *Helper to start visualizer.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
