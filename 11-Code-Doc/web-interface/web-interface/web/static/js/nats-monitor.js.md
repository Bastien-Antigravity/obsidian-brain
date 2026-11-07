---
source: web-interface/web/static/js/nats-monitor.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 15:06:47.750963
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: nats-monitor.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/js/nats-monitor.js`.

> **Essential Process**:
> OpenMFE Micro-Frontend component providing real-time telemetry, stream metrics, and connection monitoring for the central NATS Core and JetStream message broker.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.calculateRate]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatBytes]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatNumber]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatUptime]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.bindEvents]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.cacheDom]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.loadTelemetry]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.onMount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.renderClientsTable]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.renderDiagnostics]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.renderStreamsTable]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.startPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.stopPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.switchTab]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.updateUI]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.computeRates]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.fetchStats]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onUnmount]] (method: calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|rag-mcp-inspector.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.clearPollTimers]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.registerPoll]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement]] (class: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|Alias]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.calculateRate]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatBytes]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatNumber]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatUptime]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.bindEvents]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.cacheDom]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.loadTelemetry]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.onMount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.renderClientsTable]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.renderDiagnostics]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.renderStreamsTable]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.startPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.stopPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.switchTab]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.updateUI]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.computeRates]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.fetchStats]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager]] (class: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
