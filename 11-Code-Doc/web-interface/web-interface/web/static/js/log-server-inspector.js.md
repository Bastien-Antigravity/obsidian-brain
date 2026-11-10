---
source: web-interface/web/static/js/log-server-inspector.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T13:49:04.201087
---

# Mirror: log-server-inspector.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/js/log-server-inspector.js`.

> **Essential Process**:
> OpenMFE Micro-Frontend component providing real-time log ingestion observability, in-memory circular ring buffer telemetry, interactive query tail browsing, and high-throughput HTTP/2 gRPC streaming console for the Log Server.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/ChartManager.js.md|ChartManager.clear]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.sort]] (method: calls)
- [[web-interface/web-interface/src/logclient/log_service.pb.go.md|Level.Number]] (method: calls)
- [[web-interface/web-interface/web/pages/02-Ecosystem-Discovery/02-FleetLiveLogs.html.md|LEVEL_NAMES]] (constant: calls)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerDataManager.fetchStats]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerDataManager.fetchTailLogs]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.bindEvents]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.cacheDom]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.loadContracts]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.loadStats]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.loadTailLogs]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.onMount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.onUnmount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.renderConsoleBody]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.renderOverviewTab]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.startPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.startStream]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.stopPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.stopStream]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.switchTab]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.toggleStream]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.updateKPIs]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.updateStatusBadge]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.updateStreamSwitchUI]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.escapeHTML]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.formatNumber]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.formatShortTimeUTC]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.formatTimestampUTC]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.getLevelBadgeClass]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.getLevelName]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.clearPollTimers]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.registerPoll]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement]] (class: calls)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.fetchContracts]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.mountContractTabs]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warn]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|Alias]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerDataManager.fetchStats]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerDataManager.fetchTailLogs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerDataManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerDataManager]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.bindEvents]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.cacheDom]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.loadContracts]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.loadStats]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.loadTailLogs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.onMount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.onUnmount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.renderConsoleBody]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.renderOverviewTab]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.startPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.startStream]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.stopPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.stopStream]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.switchTab]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.toggleStream]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.updateKPIs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.updateStatusBadge]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.updateStreamSwitchUI]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.escapeHTML]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.formatNumber]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.formatShortTimeUTC]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.formatTimestampUTC]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.getLevelBadgeClass]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel.getLevelName]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerMetricsModel]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|pad]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (calls)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (same_package)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|tele-remote-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|tele-remote-inspector.js]] (same_package)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|timescaledb-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|timescaledb-inspector.js]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
