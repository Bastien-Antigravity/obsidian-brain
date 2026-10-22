---
source: obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.425171
---

# Mirror: llm_expander.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py`.

> **Essential Process**:
> LLM-based query expander. Generates semantic variants of a user's natural language query to improve search recall.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|generate_response]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|llm_client.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|QueryExpander]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|query_expander.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|LLMQueryExpander]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_SYSTEM_PROMPT]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_USER_PROMPT_TMPL]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|expand_query]] (function: belongs_to) — *Expands a given query into multiple semantic variants.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
