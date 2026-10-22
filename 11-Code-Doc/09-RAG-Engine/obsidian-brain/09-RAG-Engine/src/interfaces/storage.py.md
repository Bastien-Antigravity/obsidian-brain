---
source: obsidian-brain/09-RAG-Engine/src/interfaces/storage.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.577616
---

# Mirror: storage.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/storage.py`.

> **Essential Process**:
> Defines the abstract base interface for all storage systems in the RAG engine. Provides a unified contract for lifecycle management and data cleanup.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/storage.py.md|Storage]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/storage.py.md|delete_by_source]] (function: belongs_to) — *Deletes all data records associated with a specific source file path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/storage.py.md|reset_store]] (function: belongs_to) — *Clears all data from the store to allow a fresh start.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
