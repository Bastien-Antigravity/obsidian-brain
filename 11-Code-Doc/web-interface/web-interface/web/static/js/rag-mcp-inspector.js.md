---
source: web-interface/web/static/js/rag-mcp-inspector.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 15:06:47.754408
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: rag-mcp-inspector.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/js/rag-mcp-inspector.js`.

> **Essential Process**:
> OpenMFE Micro-Frontend component providing interactive browsing, execution, and live bidirectional JSON-RPC traffic inspection for the RAG Model Context Protocol (MCP) server.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|_.disabled]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.find]] (method: calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getProperties]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getRequired]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.executeTool]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchHistory]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchTools]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.bindEvents]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.cacheDom]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.displayWirePayload]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.executeCurrentTool]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadCatalog]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadHistory]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onMount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onUnmount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.renderToolList]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.selectTool]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warn]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (calls)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (same_package)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getProperties]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPToolModel.getRequired]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPToolModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPToolModel]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.executeTool]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchHistory]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager.fetchTools]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|MCPTrafficManager]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.bindEvents]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.cacheDom]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.displayWirePayload]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.executeCurrentTool]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadCatalog]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.loadHistory]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onMount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onUnmount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.renderToolList]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.selectTool]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|ias e]] (class: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
