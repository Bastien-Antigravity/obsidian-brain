

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/controller.py`.

> **Essential Process**:
> Provides the unified controller for managing RAG Engine operations and configuration settings. Wraps the core RAGFacade and distributes updates across the ecosystem.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: belongs_to) — *Standardized controller implementation for RAG operations.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|StatusInfo]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|build_index]] (function: belongs_to) — *Triggers index rebuild.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_brain_stats]] (function: belongs_to) — *Calculates stats respecting active squad firewalls.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_config]] (function: belongs_to) — *Retrieves a configuration value from the configuration loader.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_status]] (function: belongs_to) — *Checks RAG Engine layer health, checking each store component.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: belongs_to) — *Indexes directory/microservice repository.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_file]] (function: belongs_to) — *Indexes a single file.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|is_mock]] (function: belongs_to) — *Helper to check if a component is a unittest mock*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|list_config]] (function: belongs_to) — *Returns the entire active configuration map.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|reset_index]] (function: belongs_to) — *Resets all database layers.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|set_config]] (function: belongs_to) — *Sets a configuration value via Go DistConf bridge.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|sync_docs]] (function: belongs_to) — *Syncs codebase documentation mirrors.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
