---
source: obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.453859
---

# Mirror: rest_handler.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py`.

> **Essential Process**:
> Provides the REST API endpoints wrapping the RAGController. Supports querying/updating config variables and checking system health via HTTP.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|RAGRESTHandler]] (class: belongs_to) — *REST API Handler mapping config and status queries to RAGController.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_config]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_status]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|index_document]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|list_config]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|purge_vault]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|query_rag]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|register_routes]] (function: belongs_to) — *Registers the REST routes to the FastAPI application mux.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|set_config]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
