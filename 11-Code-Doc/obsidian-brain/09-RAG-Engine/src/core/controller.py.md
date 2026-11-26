

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/controller.py`.

> **Essential Process**:
> Provides the unified controller for managing RAG Engine operations and configuration settings. Wraps the core RAGFacade and distributes updates across the ecosystem.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: belongs_to) — *Standardized controller implementation for RAG operations.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|StatusInfo]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|_load_version]] (function: belongs_to) — *Loads version dynamically from AppConfig / VERSION.txt (fail-fast).*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|build_index]] (function: belongs_to) — *Triggers index rebuild.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|delete_by_brain]] (function: belongs_to) — *Purges an entire brain partition atomically.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_brain_stats]] (function: belongs_to) — *Calculates stats respecting active squad firewalls.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_config]] (function: belongs_to) — *Retrieves a configuration value from the configuration loader.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_drifted_documents]] (function: belongs_to) — *Retrieves drifted code-to-documentation alignment links.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_file_dependencies]] (function: belongs_to) — *Returns inbound consumers and outbound dependencies for a target source file.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_status]] (function: belongs_to) — *Checks RAG Engine layer health, checking each store component.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: belongs_to) — *Indexes directory/microservice repository.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_document_content]] (function: belongs_to) — *Indexes document content directly into a brain partition.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_file]] (function: belongs_to) — *Indexes a single file.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|list_config]] (function: belongs_to) — *Returns the entire active configuration map.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|query]] (function: belongs_to) — *Queries the RAG engine across partitions and returns serializable results.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|reset_index]] (function: belongs_to) — *Resets all database layers.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|search_symbols]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|set_config]] (function: belongs_to) — *Sets a configuration value via Go DistConf bridge.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|sync_docs]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
