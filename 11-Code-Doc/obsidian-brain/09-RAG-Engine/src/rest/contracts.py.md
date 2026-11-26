---
source: obsidian-brain/09-RAG-Engine/src/rest/contracts.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:50.291523
---

# Mirror: contracts.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/rest/contracts.py`.

> **Essential Process**:
> Builds authoritative, runtime-introspected Exchange Contracts for both rag_engine (HTTP/REST + gRPC RAGControlService + PostgreSQL/pgvector + TeleRemote) and rag_mcp (FastMCP SSE Stream + JSON-RPC 2.0 Tool Schemas + Inspector REST + Audit SQL).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_tools_list_result]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_RAG_PROTO_PATH]] (constant: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_RAG_ROOT]] (constant: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_RAG_SQL_DDL]] (constant: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_resolve_addrs]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_engine_contracts]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_mcp_contracts]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
