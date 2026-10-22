---
source: obsidian-brain/08-Squad-Agent/src/clients/discord_client.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20T18:09:59.710263
---

# Mirror: discord_client.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/clients/discord_client.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|CommandController]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|publish_user_message]] (function: calls) — *Saves a user message and publishes it to EventBus to trigger agents.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|DiscordClient]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|HAS_DISCORD]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_resolve_channel_id]] (function: belongs_to) — *Resolves the designated Discord channel ID for squad chat monitoring.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_resolve_token]] (function: belongs_to) — *Resolves the Discord bot token from environment or settings file.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_setup_bot]] (function: belongs_to) — *Configures the discord.py client and registers handlers.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_stream_squad_events_to_discord]] (function: belongs_to) — *Subscribes to NATS/LocalEventBus squad chat topics and mirrors agent communication into Discord.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|main]] (function: belongs_to) — *Invokes and starts the Discord Gateway Client adapter.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|on_message]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|on_ready]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|squad_event_callback]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start]] (function: belongs_to) — *Establishes connection to the Gateway.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start_async]] (function: belongs_to) — *Asynchronously establishes connection to the Discord Gateway.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
