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
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.
       ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.       if ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.     thi]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE. {
        if (!th]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE. {
        if (!v]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.Poll = false)]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.e) {
    ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.le() {
        if ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.onMount]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.startPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.stopPolling]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.computeRates]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.fetchStats]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.bindEvents]] (method: calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.cacheDom]] (method: calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|RAGMCPInspectorMFE.onUnmount]] (method: calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|rag-mcp-inspector.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.calculateRate]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatBytes]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatNumber]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel.formatUptime]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMetricsModel]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.
       ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.       if ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.     thi]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE. {
        if (!th]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE. {
        if (!v]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.Poll = false)]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.e) {
    ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.le() {
        if ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.onMount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.startPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE.stopPolling]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSMonitorMFE]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.computeRates]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager.fetchStats]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|NATSStreamManager]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|lemen]] (class: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
