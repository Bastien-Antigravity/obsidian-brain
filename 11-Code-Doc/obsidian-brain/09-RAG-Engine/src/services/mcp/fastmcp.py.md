

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py`.

> **Essential Process**:
> FastMCP (Model Context Protocol) Server implementation using SSE (Server-Sent Events) transport over HTTP. Exposes agent tools to IDEs, clients, and autonomous squad agents.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: calls) — *Standardized controller implementation for RAG operations.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_mcp_contracts]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|RAGRESTHandler]] (class: calls) — *REST API Handler mapping config and status queries to RAGController.*
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|register_routes]] (function: calls) — *Registers the REST routes to the FastAPI application mux.*
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/graph/ForceConfig.js.md|ForceConfig.reset]] (method: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|FastMCP]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|UniLogHandler]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_build_tool_schema]] (function: belongs_to) — *Derive a JSON Schema inputSchema from the function's type hints.*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_error]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_handle]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_load_version]] (function: belongs_to) — *Loads version dynamically from AppConfig / VERSION.txt single source of truth.*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_respond]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_send]] (function: belongs_to) — *Route a JSON-RPC message to the active SSE client stream.*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_tools_list_result]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|api_mcp_call]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|api_mcp_contracts]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|api_mcp_history]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|api_mcp_tools]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|decorator]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|delete_endpoint]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|emit]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|event_generator]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|get_caller_client]] (function: belongs_to) — *Resolve the client ID requesting the MCP tool (e.g. CursorIDE, VSCodeIDE, AntigravityIDE, SquadAgent).*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|log_http_errors_middleware]] (function: belongs_to) — *Custom ASGI Middleware to log HTTP client/server errors (status >= 400) to PostgreSQL*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|message_endpoint]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|mount_to_app]] (function: belongs_to) — *Mount the SSE transport endpoints on an existing FastAPI application.*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|on_startup]] (function: belongs_to) — *Register an async function to be called after the MCP initialize handshake.*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|register_tool]] (function: belongs_to) — *Programmatically register a tool function without using the decorator.*
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|run]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|send_to_session]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|sse_endpoint]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|tool]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|rag-mcp-inspector.js]] (calls)
<!-- SYNC:END -->
