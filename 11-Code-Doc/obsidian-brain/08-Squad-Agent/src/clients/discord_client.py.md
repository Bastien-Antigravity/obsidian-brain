---
source: obsidian-brain/08-Squad-Agent/src/clients/discord_client.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.470226
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: discord_client.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/clients/discord_client.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|decrypt_secret]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|CommandController]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|publish_user_message]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|DiscordClient]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|HAS_DISCORD]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_resolve_channel_id]] (function: belongs_to) — *Resolves the designated Discord channel ID for squad chat monitoring.*
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_resolve_token]] (function: belongs_to) — *Resolves the Discord bot token from environment or settings file.*
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_setup_bot]] (function: belongs_to) — *Configures the discord.py client and registers handlers.*
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_stream_squad_events_to_discord]] (function: belongs_to) — *Subscribes to NATS/LocalEventBus squad chat topics and mirrors agent communication into Discord.*
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|main]] (function: belongs_to) — *Invokes and starts the Discord Gateway Client adapter.*
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|on_message]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|on_ready]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|squad_event_callback]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start]] (function: belongs_to) — *Establishes connection to the Gateway.*
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start_async]] (function: belongs_to) — *Asynchronously establishes connection to the Discord Gateway.*
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
