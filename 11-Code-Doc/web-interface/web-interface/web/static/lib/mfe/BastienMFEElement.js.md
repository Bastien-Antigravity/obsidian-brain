---
source: web-interface/web/static/lib/mfe/BastienMFEElement.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-06T17:25:12.271200
---

# Mirror: BastienMFEElement.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/lib/mfe/BastienMFEElement.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.apiFetch]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.apiUrl]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.bindEvents]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.cacheDom]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.clearPollTimers]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.connectedCallback]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.disconnectedCallback]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.onMount]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.onUnmount]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.registerPoll]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.register]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.showError]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.showLoading]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger]] (class: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|rag-mcp-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|tele-remote-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|timescaledb-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.apiFetch]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.apiUrl]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.bindEvents]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.cacheDom]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.clearPollTimers]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.connectedCallback]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.disconnectedCallback]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.onMount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.onUnmount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.registerPoll]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.register]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.showError]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.showLoading]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement]] (class: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|SubclassedMFEElement]] (class: belongs_to) — *Constructor already defined for an alias tag: subclass dynamically to create a unique constructor*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
