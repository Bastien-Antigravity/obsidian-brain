---
source: obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.015834
---

# Mirror: __init__.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py`.

> **Essential Process**:
> Root-level environment bootstrapper and singleton manager. Sets up system path, redirects virtualenv execution, calculates thread parameters, configures offline modes, and instantiates the application configuration loader and the UniLog logging engine exactly once.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/config/lib_loader.py.md|load_libdistconf]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/config/loader.py.md|set_logger]] (function: calls) — *Updates the logger after instantiation.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/logger/facade.py.md|UniLog]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|bootstrap_microservice]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
