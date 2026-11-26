---
source: obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-11-06T15:39:41.969467
---

# Mirror: rag-mcp-inspector.js

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js`.

> **Essential Process**:
> OpenMFE Micro-Frontend component providing interactive browsing, execution, and live bidirectional JSON-RPC traffic inspection for the RAG Model Context Protocol (MCP) server.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|tool]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getProperties]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getRequired]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.executeTool]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchHistory]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchTools]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.bindEvents]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.cacheDom]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.displayWirePayload]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.executeCurrentTool]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadCatalog]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadHistory]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onMount]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onUnmount]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.renderToolList]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.render]] (method: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.selectTool]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|Alias]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getProperties]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getRequired]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPToolModel]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPToolModel]] (class: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.executeTool]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchHistory]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchTools]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager]] (class: defines_method)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.bindEvents]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.cacheDom]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.displayWirePayload]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.executeCurrentTool]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadCatalog]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadHistory]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onMount]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onUnmount]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.renderToolList]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.render]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.selectTool]] (method: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE]] (class: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
