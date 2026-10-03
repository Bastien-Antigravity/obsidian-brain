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
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py`.

> **Essential Process**:
> Provides the SquadEventBus interface and DualSquadEventBus concrete class routing multi-agent communications via NATS or LocalEventBus in offline mode.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/memory_store.py.md|add]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/memory_store.py.md|memory_store.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|DualSquadEventBus]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|EventDeduplicator]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|LocalEventBus]] (class: belongs_to) — *In-memory fallback event bus for NATS-offline/local testing.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|SquadEventBus]] (class: belongs_to) — *Abstract interface defining the pub/sub event bus contract for AI squad coordination.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|_get_subscribers]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|close]] (function: belongs_to) — *Cleans up resources and disconnects from the transit layer.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|close]] (function: belongs_to) — *Closes connection cleanly.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|connect]] (function: belongs_to) — *Attempts a resilient connection to NATS, falling back to Local otherwise.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|connect]] (function: belongs_to) — *Initializes connection to the underlying message bus.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|is_duplicate]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|nats_callback]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|publish]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|publish]] (function: belongs_to) — *Broadcasts a payload JSON dictionary onto a topic channel.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|publish]] (function: belongs_to) — *Routes message broadcast depending on NATS connection state.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to) — *Registers a non-blocking async callback listener for a topic channel.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to) — *Subscribes callback to the correct event provider.*
<!-- SYNC:END -->
