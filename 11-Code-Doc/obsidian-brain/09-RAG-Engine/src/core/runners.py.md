

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/runners.py`.

> **Essential Process**:
> Asynchronous runner for the RAG Engine visualizer dashboard. Manages the lifecycle and event loop of the visualizer web server.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|start_async_server]] (function: calls) — *Starts the uvicorn server for FastAPI with harmonized logging.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|VisualizerRunner]] (class: belongs_to) — *Starts and manages the RAG visualizer dashboard.*
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|run]] (function: belongs_to) — *Starts the visualizer web server.*
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_visualizer]] (function: belongs_to) — *Helper to start visualizer.*
<!-- SYNC:END -->
