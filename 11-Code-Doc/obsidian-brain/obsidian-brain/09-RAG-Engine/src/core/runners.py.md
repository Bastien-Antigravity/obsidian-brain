

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/runners.py`.

> **Essential Process**:
> Standardized asynchronous runners for the RAG Engine CLI operations. Provides classes to handle indexing, watching, and visualization tasks.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_watcher]] (function: calls) — *Stops background file monitoring.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|start_async_server]] (function: calls) — *Starts the uvicorn server for FastAPI with harmonized logging.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|IndexerRunner]] (class: belongs_to) — *Handles workspace indexing operations.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|VisualizerRunner]] (class: belongs_to) — *Starts and manages the RAG visualizer dashboard.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|WatcherRunner]] (class: belongs_to) — *Manages the background file watcher.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|build_index]] (function: belongs_to) — *Helper to run build_index.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|build_index]] (function: belongs_to) — *Triggers full workspace indexing via Facade (Async).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|reset_index]] (function: belongs_to) — *Helper to run reset_index.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|reset_index]] (function: belongs_to) — *Wipes and rebuilds the index via Facade (Async).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|run]] (function: belongs_to) — *Starts file watcher and runs the event loop.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|run]] (function: belongs_to) — *Starts the visualizer web server.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_visualizer]] (function: belongs_to) — *Helper to start visualizer.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_watcher]] (function: belongs_to) — *Helper to start watcher.*
<!-- SYNC:END -->
