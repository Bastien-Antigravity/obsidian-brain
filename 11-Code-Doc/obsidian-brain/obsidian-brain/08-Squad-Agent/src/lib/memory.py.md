---
source: obsidian-brain/08-Squad-Agent/src/lib/memory.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:37.760909
---

# Mirror: memory.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/memory.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/interfaces/memory_store.py.md|MemoryStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls) — *Resolves public key PEM string from AppConfig or standard file paths.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_brain]] (function: calls) — *Search the knowledge base for relevant context. Supports verbosity overrides ('full', 'signatures').*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|DualLayerMemoryStore]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|PostgresMemoryStore]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|RAGMemoryStore]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|ShortTermMemory]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_format_results]] (function: belongs_to) — *Formats RAG results into system prompt turns.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|_init_db]] (function: belongs_to) — *Declares and builds the conversation_turns table if not already present.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Appends a new turn to the in-memory buffer, capping size.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *No-op. Chunks are indexed via RAG pipelines.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Persists a conversation turn in the short-term storage layer.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: belongs_to) — *Persists a new message turn to the database.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Clears the buffer.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *No-op.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Purges conversation history for the specified session from the database.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|clear]] (function: belongs_to) — *Purges history inside all integrated memory layers.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Queries the RAG Engine for relevant context matching the query.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves active conversation history buffer.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves and consolidates short-term turns and long-term semantic context turns.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: belongs_to) — *Retrieves and returns the last limit conversation turns from the database.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
