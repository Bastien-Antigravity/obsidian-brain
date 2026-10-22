---
source: obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20T15:13:14.818661
---

# Mirror: interfaces.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py`.

> **Essential Process**:
> Provides the SquadEventBus interface and DualSquadEventBus concrete class routing multi-agent communications via NATS or LocalEventBus in offline mode.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|add]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|memory_store.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|DualSquadEventBus]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|EventDeduplicator]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|LocalEventBus]] (class: belongs_to) — *In-memory fallback event bus for NATS-offline/mock testing only.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|SquadEventBus]] (class: belongs_to) — *Abstract interface defining the pub/sub event bus contract for AI squad coordination.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|_get_subscribers]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|close]] (function: belongs_to) — *Cleans up resources and disconnects from the transit layer.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|close]] (function: belongs_to) — *Closes connection cleanly.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|connect]] (function: belongs_to) — *Attempts a resilient connection to NATS, failing fast if offline and fallback is disabled.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|connect]] (function: belongs_to) — *Initializes connection to the underlying message bus.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|is_duplicate]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|nats_callback]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|normalize_topic]] (function: belongs_to) — *Normalizes legacy topic names to canonical ecosystem prefix.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|publish]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|publish]] (function: belongs_to) — *Broadcasts a payload JSON dictionary onto a topic channel.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|publish]] (function: belongs_to) — *Routes message broadcast depending on NATS connection state.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to) — *Registers a non-blocking async callback listener for a topic channel.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to) — *Subscribes callback to the correct event provider.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
