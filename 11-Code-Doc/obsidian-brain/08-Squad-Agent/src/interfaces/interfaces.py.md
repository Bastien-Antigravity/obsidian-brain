---
source: obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.777771
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: interfaces.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py`.

> **Essential Process**:
> Provides the SquadEventBus interface and DualSquadEventBus concrete class routing multi-agent communications via NATS or LocalEventBus in offline mode.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|add]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|memory_store.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|eval_agent.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|DualSquadEventBus]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|EventDeduplicator]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|LocalEventBus]] (class: belongs_to) — *In-memory fallback event bus for NATS-offline/mock testing only.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|SquadEventBus]] (class: belongs_to) — *Abstract interface defining the pub/sub event bus contract for AI squad coordination.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|_get_subscribers]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|close]] (function: belongs_to) — *Cleans up resources and disconnects from the transit layer.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|close]] (function: belongs_to) — *Closes connection cleanly.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|connect]] (function: belongs_to) — *Attempts a resilient connection to NATS, failing fast if offline and fallback is disabled.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|connect]] (function: belongs_to) — *Initializes connection to the underlying message bus.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|is_duplicate]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|nats_callback]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|normalize_topic]] (function: belongs_to) — *Normalizes legacy topic names to canonical ecosystem prefix.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|publish]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|publish]] (function: belongs_to) — *Broadcasts a payload JSON dictionary onto a topic channel.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|publish]] (function: belongs_to) — *Routes message broadcast depending on NATS connection state.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to) — *Registers a non-blocking async callback listener for a topic channel.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|subscribe]] (function: belongs_to) — *Subscribes callback to the correct event provider.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|unsubscribe]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|unsubscribe]] (function: belongs_to) — *Unsubscribes callback and optional NATS subscriptions cleanly.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
