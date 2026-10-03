---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/web/server.py`.

> **Essential Process**:
> FastAPI Web Server for Squad Control Dashboard and MFE registration. Serves static MFE assets and handles REST API queries.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: calls) — *REST API Handler exposing squad controller capabilities.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|register_routes]] (function: calls) — *Registers the REST routes to the FastAPI application.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|_STATIC_DIR]] (constant: belongs_to) — *Mount static files (MFE script)*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|init_routes]] (function: belongs_to) — *Dynamically initializes and registers squad REST routes.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|register_mfe_with_web_interface]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|start_async_server]] (function: belongs_to) — *Launches the uvicorn web server and starts the auto-registration daemon thread.*
<!-- SYNC:END -->
