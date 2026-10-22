---
source: obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.479158
---

# Mirror: codebase_db.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py`.

> **Essential Process**:
> Defines the abstract interface for the structural codebase graph database. Retains information about symbol definitions, references, and workspace mapping.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|CodebaseDB]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|clear]] (function: belongs_to) — *Clears all codebase nodes and edges.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|close]] (function: belongs_to) — *Closes the database connection or pool.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|find_symbols]] (function: belongs_to) — *Resolves matching symbols by workspace and label.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|get_edges]] (function: belongs_to) — *Returns all codebase edges.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|get_nodes]] (function: belongs_to) — *Returns all codebase nodes.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|insert_edge]] (function: belongs_to) — *Inserts a codebase dependency edge.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|insert_edges_batch]] (function: belongs_to) — *Batch inserts multiple codebase edges.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|insert_node]] (function: belongs_to) — *Inserts or updates a codebase node.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|insert_nodes_batch]] (function: belongs_to) — *Batch inserts multiple codebase nodes.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
