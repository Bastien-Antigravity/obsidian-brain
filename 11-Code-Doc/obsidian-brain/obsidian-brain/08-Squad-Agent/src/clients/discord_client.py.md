---
source: obsidian-brain/08-Squad-Agent/src/clients/discord_client.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.470226
---

# Mirror: discord_client.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/clients/discord_client.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|CommandController]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|process_message]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls) — *Resolves public key PEM string from AppConfig or standard file paths.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|DiscordClient]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|HAS_DISCORD]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_resolve_token]] (function: belongs_to) — *Resolves the Discord bot token from environment or settings file.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|_setup_bot]] (function: belongs_to) — *Configures the discord.py client and registers handlers.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|main]] (function: belongs_to) — *Invokes and starts the Discord Gateway Client adapter.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|on_message]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|on_ready]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start]] (function: belongs_to) — *Establishes connection to the Gateway.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
