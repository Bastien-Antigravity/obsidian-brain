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
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py`.

> **Essential Process**:
> Provides the REST API endpoints wrapping the Squad Command Controller. Allows external clients (like web-interface) to query status, switch modes, list commands, and run commands via SSE stream.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_mode_details]] (function: calls) — *Returns name and description for a mode.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|list_commands]] (function: calls) — *Returns a list of available subcommands and their descriptions.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|publish_user_message]] (function: calls) — *Saves a user message and publishes it to EventBus to trigger agents.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: belongs_to) — *REST API Handler exposing squad controller capabilities.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|event_generator]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_active_mode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_chat_history]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_commands]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_github_user]] (function: belongs_to) — *Returns the configured GitHub user handle or default organization.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_status]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|is_github_configured]] (function: belongs_to) — *Verifies if a valid GitHub personal access token is configured in environment or capability config.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|msg_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|post_chat_message]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|register_routes]] (function: belongs_to) — *Registers the REST routes to the FastAPI application.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|run_command_stream]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|stream_chat_messages]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|switch_mode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
