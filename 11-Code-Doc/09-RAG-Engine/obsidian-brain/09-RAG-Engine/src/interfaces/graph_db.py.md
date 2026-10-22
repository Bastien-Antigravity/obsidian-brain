---
source: obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.552826
---

# Mirror: graph_db.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py`.

> **Essential Process**:
> Defines the abstract interface for the unified knowledge graph database (Graph-RAG). Handles traversals, pathfinding, and views combining codebase, alignment and parent databases.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|GraphDB]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|clear]] (function: belongs_to) — *Clears all local KMS nodes and edges.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|close]] (function: belongs_to) — *Closes the database connection or pool.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|export_unified_graph]] (function: belongs_to) — *Exports unified graph state to a JSON file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|find_path]] (function: belongs_to) — *Finds paths connecting start_id and end_id.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|insert_edge]] (function: belongs_to) — *Inserts a KMS relationship edge.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|insert_node]] (function: belongs_to) — *Inserts or updates a KMS node.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|remove_edges_by_source_or_type]] (function: belongs_to) — *Removes KMS edges by source and optional type.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|remove_node]] (function: belongs_to) — *Removes a KMS node and its connected edges.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|traverse_neighborhood]] (function: belongs_to) — *Finds all nodes and edges within max_depth of seed_ids.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
