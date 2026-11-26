

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/storage.py`.

> **Essential Process**:
> Defines the abstract base interface for all storage systems in the RAG engine. Provides a unified contract for lifecycle management and data cleanup.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/storage.py.md|Storage]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/storage.py.md|delete_by_source]] (function: belongs_to) — *Deletes all data records associated with a specific source file path.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/storage.py.md|reset_store]] (function: belongs_to) — *Clears all data from the store to allow a fresh start.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (same_package)
<!-- SYNC:END -->
