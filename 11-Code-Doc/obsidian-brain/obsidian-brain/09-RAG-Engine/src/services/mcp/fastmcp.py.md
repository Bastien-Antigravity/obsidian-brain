

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py`.

> **Essential Process**:
> FastMCP (Model Context Protocol) Server implementation using SSE (Server-Sent Events) transport over HTTP. Exposes agent tools to IDEs, clients, and autonomous squad agents.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/graph/ForceConfig.js.md|ForceConfig.reset]] (method: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|FastMCP]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|UniLogHandler]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_build_tool_schema]] (function: belongs_to) — *Derive a JSON Schema inputSchema from the function's type hints.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_error]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_handle]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_respond]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_send]] (function: belongs_to) — *Route a JSON-RPC message to the active SSE client stream.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|_tools_list_result]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|decorator]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|delete_endpoint]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|emit]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|event_generator]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|get_caller_client]] (function: belongs_to) — *Resolve the client ID requesting the MCP tool (e.g. CursorIDE, VSCodeIDE, AntigravityIDE, SquadAgent).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|log_http_errors_middleware]] (function: belongs_to) — *Custom ASGI Middleware to log HTTP client/server errors (status >= 400) to PostgreSQL*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|message_endpoint]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|mount_to_app]] (function: belongs_to) — *Mount the SSE transport endpoints on an existing FastAPI application.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|on_startup]] (function: belongs_to) — *Register an async function to be called after the MCP initialize handshake.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|register_tool]] (function: belongs_to) — *Programmatically register a tool function without using the decorator.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|run]] (function: belongs_to) — *Start the MCP SSE server on the specified or current event loop.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|send_to_session]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|sse_endpoint]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|tool]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
<!-- SYNC:END -->
