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
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.capeHTML(s]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatDuration]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatNumber]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.truncateSQL]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.Mount()]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.QueriesTable() {
 ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.adTelemetry(i]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.artPolling()]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.cheDom()]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.dateUI(d]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.erChunksTable() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.erHypertablesTable() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.itchTab(t]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.ndEvents()]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.nder()]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.nstructor()]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.opPolling()]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDataManager {.nstructor(b]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDataManager {.tchStats()]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|stienMFEElement e.Unmount()]] (method: calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|stienMFEElement e.earPollTimers()]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.capeHTML(s]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatDuration]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.formatNumber]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel.truncateSQL]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|TimescaleMetricsModel]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.Mount()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.QueriesTable() {
 ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.adTelemetry(i]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.artPolling()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.cheDom()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.dateUI(d]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.erChunksTable() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.erHypertablesTable() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.itchTab(t]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.ndEvents()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.nder()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.nstructor()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e.opPolling()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDBInspectorMFE e]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDataManager {.nstructor(b]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDataManager {.tchStats()]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDataManager {]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|mescaleDataManager {]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|tends]] (class: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
