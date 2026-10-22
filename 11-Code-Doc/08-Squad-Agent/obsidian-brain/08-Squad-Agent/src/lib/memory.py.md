---
source: obsidian-brain/08-Squad-Agent/src/lib/memory.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20T15:13:14.767997
---

# Mirror: memory.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/memory.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|MemoryStore]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_brain]] (function: calls) — *Search the knowledge base for relevant context. Supports verbosity overrides ('full', 'signatures').*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|DualLayerMemoryStore]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|PostgresMemoryStore]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|RAGMemoryStore]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|ShortTermMemory]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_format_results]] (function: belongs_to) — *Formats RAG results into system prompt turns.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_init_db]] (function: belongs_to) — *Declares and builds the conversation_turns table if not already present.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Appends a new turn to the in-memory buffer, capping size.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *No-op. Chunks are indexed via RAG pipelines.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Persists a conversation turn in the short-term storage layer.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Persists a new message turn to the database.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Clears the buffer.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *No-op.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Purges conversation history for the specified session from the database.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Purges history inside all integrated memory layers.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|delete_by_brain]] (function: belongs_to) — *Purges conversation records for a specific brain partition across storage layers.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|delete_by_brain]] (function: belongs_to) — *Purges conversation turns and chat logs for a brain partition, ensuring zero state pollution.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Queries the RAG Engine for relevant context matching the query.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves active conversation history buffer.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves and consolidates short-term turns and long-term semantic context turns.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves and returns the last limit conversation turns from the database.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
