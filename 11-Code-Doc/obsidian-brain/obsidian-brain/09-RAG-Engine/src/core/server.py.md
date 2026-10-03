

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/server.py`.

> **Essential Process**:
> FastMCP server instance definition for Obsidian Brain RAG. Registers all decoupled tools defined in `src/services/mcp/tools.py`.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|register_tool]] (function: calls) — *Programmatically register a tool function without using the decorator.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|ALL_TOOLS]] (constant: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
