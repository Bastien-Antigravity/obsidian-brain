---
source: obsidian-brain/09-RAG-Engine/src/core/server.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.984795
---

# Mirror: server.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/server.py`.

> **Essential Process**:
> FastMCP server instance definition for Obsidian Brain RAG. Registers all decoupled tools defined in `src/services/mcp/tools.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|register_tool]] (function: calls) — *Programmatically register a tool function without using the decorator.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|ALL_TOOLS]] (constant: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
