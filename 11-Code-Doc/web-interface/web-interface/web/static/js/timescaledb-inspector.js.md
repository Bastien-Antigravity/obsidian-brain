---
source: web-interface/web/static/js/timescaledb-inspector.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 15:06:47.752931
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: timescaledb-inspector.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/js/timescaledb-inspector.js`.

> **Essential Process**:
> OpenMFE Micro-Frontend component providing real-time telemetry, hypertable inspection, chunk distribution analytics, and running query monitoring for TimescaleDB.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.onUnmount]] (method: calls)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|log-server-inspector.js]] (same_package)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.bindEvents]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.cacheDom]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.loadContracts]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.loadTelemetry]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.onMount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.renderChunksTable]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.renderHypertablesTable]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.renderQueriesTable]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.startPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.stopPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.switchTab]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.updateUI]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDataManager.fetchStats]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.escapeHTML]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatDuration]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatNumber]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.truncateSQL]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.clearPollTimers]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.registerPoll]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement]] (class: calls)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.fetchContracts]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.mountContractTabs]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.duration]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|Alias]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.bindEvents]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.cacheDom]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.loadContracts]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.loadTelemetry]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.onMount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.renderChunksTable]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.renderHypertablesTable]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.renderQueriesTable]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.startPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.stopPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.switchTab]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE.updateUI]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDBInspectorMFE]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDataManager.fetchStats]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDataManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleDataManager]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.escapeHTML]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatDuration]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatNumber]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.truncateSQL]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel]] (class: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
