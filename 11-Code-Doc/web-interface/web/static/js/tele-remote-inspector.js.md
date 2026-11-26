---
source: web-interface/web/static/js/tele-remote-inspector.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.020586
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: tele-remote-inspector.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/js/tele-remote-inspector.js`.

> **Essential Process**:
> OpenMFE Micro-Frontend component providing real-time telemetry, bot gateway health, active gRPC streaming subscriber monitoring, and dynamic interactive command inspection for the Tele-Remote telemetry bridge.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|_.disabled]] (method: calls)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|LogServerInspectorMFE.onUnmount]] (method: calls)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|log-server-inspector.js]] (same_package)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteDataManager.fetchStats]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.applyFilters]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.bindEvents]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.cacheDom]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.loadContracts]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.loadTelemetry]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.onMount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderKPIs]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderLogs]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderMenus]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderSubscribers]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.setActiveTab]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.startPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.stopPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.formatLatency]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.formatTimestamp]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.sanitizeText]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.clearPollTimers]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.registerPoll]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement]] (class: calls)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.fetchContracts]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.mountContractTabs]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|Alias]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteDataManager.fetchStats]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteDataManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteDataManager]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.applyFilters]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.bindEvents]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.cacheDom]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.loadContracts]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.loadTelemetry]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.onMount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderKPIs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderLogs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderMenus]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.renderSubscribers]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.setActiveTab]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.startPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE.stopPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteInspectorMFE]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.formatLatency]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.formatTimestamp]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.sanitizeText]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel]] (class: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
