---
source: sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py
workspace: sandbox-testing
type: code-mirror
status: auto-generated
last_sync: 2026-09-14 00:32:41.249973
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: rag_mcp_sse_test.py

## 📝 Description
Automatically generated mirror for `sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py`.

> **Essential Process**:
> Validates that: 1. FastMCP mounts /sse and /message routes properly on FastAPI via mount_to_app. 2. Initial handshake initializes an MCP session with UUID and session queue. 3. POST /sse dispatches JSON-RPC requests (initialize, tools/list, tool call). 4. DELETE /sse cleanly terminates the session and signals the queue. 5. Docker Compose and local configurations maintain 100% port parity (port 8090).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py.md|RAG_ENGINE_DIR]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py.md|SANDBOX_DIR]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py.md|TEST_DIR]] (constant: belongs_to) — *Add paths*
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py.md|echo_test]] (function: belongs_to) — *Simple echo test tool.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_mcp_sse_test.py.md|run_mcp_sse_scenario]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
