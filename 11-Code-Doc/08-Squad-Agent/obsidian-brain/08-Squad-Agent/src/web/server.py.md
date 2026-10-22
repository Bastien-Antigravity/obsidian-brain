---
source: obsidian-brain/08-Squad-Agent/src/web/server.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.502970
---

# Mirror: server.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/web/server.py`.

> **Essential Process**:
> FastAPI Web Server for Squad Control Dashboard and MFE registration. Serves static MFE assets and handles REST API queries.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: calls) — *REST API Handler exposing squad controller capabilities.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|register_routes]] (function: calls) — *Registers the REST routes to the FastAPI application.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|_STATIC_DIR]] (constant: belongs_to) — *Mount static files (MFE script)*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|init_routes]] (function: belongs_to) — *Dynamically initializes and registers squad REST routes.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|register_mfe_with_web_interface]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|start_async_server]] (function: belongs_to) — *Launches the uvicorn web server and starts the auto-registration daemon thread.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
