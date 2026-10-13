---
source: obsidian-brain/08-Squad-Agent/src/web/server.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.511725
---

# Mirror: server.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/web/server.py`.

> **Essential Process**:
> FastAPI Web Server for Squad Control Dashboard and MFE registration. Serves static MFE assets and handles REST API queries.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: calls) — *REST API Handler exposing squad controller capabilities.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|register_routes]] (function: calls) — *Registers the REST routes to the FastAPI application.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls) — *Resolves public key PEM string from AppConfig or standard file paths.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/web/server.py.md|_STATIC_DIR]] (constant: belongs_to) — *Mount static files (MFE script)*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/web/server.py.md|init_routes]] (function: belongs_to) — *Dynamically initializes and registers squad REST routes.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/web/server.py.md|register_mfe_with_web_interface]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/web/server.py.md|start_async_server]] (function: belongs_to) — *Launches the uvicorn web server and starts the auto-registration daemon thread.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
