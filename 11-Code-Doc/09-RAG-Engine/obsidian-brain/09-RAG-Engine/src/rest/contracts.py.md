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
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|ContractOperation]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|ContractPeer]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|ExchangeContract]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|build_contracts_envelope]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|display_address]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|extract_fastapi_operations]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|extract_proto_operations]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|read_schema_file]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|resolve_contract_port]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_tools_list_result]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_RAG_PROTO_PATH]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_RAG_ROOT]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_RAG_SQL_DDL]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|_resolve_addrs]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_engine_contracts]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_mcp_contracts]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
