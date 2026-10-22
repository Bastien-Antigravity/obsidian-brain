---
source: obsidian-brain/09-RAG-Engine/src/core/controller.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.989692
---

# Mirror: controller.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/controller.py`.

> **Essential Process**:
> Provides the unified controller for managing RAG Engine operations and configuration settings. Wraps the core RAGFacade and distributes updates across the ecosystem.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: belongs_to) — *Standardized controller implementation for RAG operations.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|StatusInfo]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|_load_version]] (function: belongs_to) — *Loads version dynamically from VERSION.txt single source of truth.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|build_index]] (function: belongs_to) — *Triggers index rebuild.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|delete_by_brain]] (function: belongs_to) — *Purges an entire brain partition atomically.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_brain_stats]] (function: belongs_to) — *Calculates stats respecting active squad firewalls.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_config]] (function: belongs_to) — *Retrieves a configuration value from the configuration loader.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_status]] (function: belongs_to) — *Checks RAG Engine layer health, checking each store component.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: belongs_to) — *Indexes directory/microservice repository.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_document_content]] (function: belongs_to) — *Indexes document content directly into a brain partition.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_file]] (function: belongs_to) — *Indexes a single file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|is_mock]] (function: belongs_to) — *Helper to check if a component is a unittest mock*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|list_config]] (function: belongs_to) — *Returns the entire active configuration map.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|query]] (function: belongs_to) — *Queries the RAG engine across partitions and returns serializable results.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|reset_index]] (function: belongs_to) — *Resets all database layers.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|set_config]] (function: belongs_to) — *Sets a configuration value via Go DistConf bridge.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|sync_docs]] (function: belongs_to) — *Syncs codebase documentation mirrors.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
