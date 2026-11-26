---
source: obsidian-brain/08-Squad-Agent/src/lib/memory.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:37.760909
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: memory.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/memory.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|MemoryStore]] (class: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|DualLayerMemoryStore]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|PostgresMemoryStore]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|RAGMemoryStore]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|ShortTermMemory]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_buffer]] (function: belongs_to) — *Backwards-compatible view of the default session buffer.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_build_rag_query_url]] (function: belongs_to) — *Constructs the RAG query URL supporting explicit schemes or capability TLS settings.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_format_results]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_init_db]] (function: belongs_to) — *Declares and builds the conversation_turns table if not already present.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_normalize_session_id]] (function: belongs_to) — *Normalizes a session identifier to guarantee non-empty isolation keys.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Appends a new turn to the isolated session buffer, capping per-session and total capacity.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *No-op. Chunks are indexed via RAG pipelines.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Persists a conversation turn in the short-term storage layer.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Persists a new message turn to the database.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Clears the buffer for the specified session, or all sessions when session_id is None.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *No-op.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Purges conversation history for the specified session strictly within this brain partition.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Purges history inside all integrated memory layers.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|delete_by_brain]] (function: belongs_to) — *Purges conversation records for a specific brain partition across storage layers.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|delete_by_brain]] (function: belongs_to) — *Purges conversation turns and chat logs for a brain partition, ensuring zero state pollution.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Queries the RAG Engine for relevant context matching the query.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves active conversation history strictly for the requested session.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves and consolidates short-term turns and long-term semantic context turns.*
- [[obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves and returns the last limit conversation turns strictly isolated by session_id and brain_id.*
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
