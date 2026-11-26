---
source: obsidian-brain/08-Squad-Agent/src/web/server.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.511725
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: server.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/web/server.py`.

> **Essential Process**:
> FastAPI Web Server for Squad Control Dashboard and MFE registration. Serves static MFE assets and handles REST API queries.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|build_squad_agent_contracts]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|contracts.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: calls) — *REST API Handler exposing squad controller capabilities.*
- [[obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|register_routes]] (function: calls) — *Registers the REST routes to the FastAPI application.*
- [[obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/web/server.py.md|_STATIC_DIR]] (constant: belongs_to) — *Mount static files (MFE script)*
- [[obsidian-brain/08-Squad-Agent/src/web/server.py.md|init_routes]] (function: belongs_to) — *Dynamically initializes and registers squad REST routes.*
- [[obsidian-brain/08-Squad-Agent/src/web/server.py.md|register_mfe_with_web_interface]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/web/server.py.md|start_async_server]] (function: belongs_to) — *Launches the uvicorn web server and starts the auto-registration daemon thread.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
