

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py`.

> **Essential Process**:
> Provides the REST API endpoints wrapping the RAGController. Supports querying/updating config variables and checking system health via HTTP.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|RAGRESTHandler]] (class: belongs_to) — *REST API Handler mapping config and status queries to RAGController.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_config]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_status]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|list_config]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|register_routes]] (function: belongs_to) — *Registers the REST routes to the FastAPI application mux.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|set_config]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
