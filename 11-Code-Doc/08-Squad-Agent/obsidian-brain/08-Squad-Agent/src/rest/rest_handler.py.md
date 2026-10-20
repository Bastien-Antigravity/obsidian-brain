---
source: obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20T18:09:59.717411
---

# Mirror: rest_handler.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py`.

> **Essential Process**:
> Provides the REST API endpoints wrapping the Squad Command Controller. Allows external clients (like web-interface) to query status, switch modes, list commands, and run commands via SSE stream.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_mode_details]] (function: calls) — *Returns name and description for a mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|list_commands]] (function: calls) — *Returns a list of available subcommands and their descriptions.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|publish_user_message]] (function: calls) — *Saves a user message and publishes it to EventBus to trigger agents.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: belongs_to) — *REST API Handler exposing squad controller capabilities.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|event_generator]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|get_active_mode]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|get_chat_history]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|get_commands]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|get_github_user]] (function: belongs_to) — *Returns the configured GitHub user handle or default organization.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|get_status]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|is_github_configured]] (function: belongs_to) — *Verifies if a valid GitHub personal access token is configured in environment or capability config.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|msg_cb]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|post_chat_message]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|register_routes]] (function: belongs_to) — *Registers the REST routes to the FastAPI application.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|run_command_stream]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|stream_chat_messages]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|switch_mode]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|server.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
