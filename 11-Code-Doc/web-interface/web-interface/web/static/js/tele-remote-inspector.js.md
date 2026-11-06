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
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteDataManager {
 .hStats() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteDataManager {
 .tructor(bas]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.
        /]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.       t]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext. {
        i]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.Polling() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.a) {
     ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.ab) {
      ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.er() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.ers(clients) {
  ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.isAutoPoll = ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.nts) {
   ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.nus) {
    ]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.tPolling() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.tructor() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.unt() {]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.formatLatency]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.rmatTimestamp(i]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.tizeText(str]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteDataManager {
 .hStats() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteDataManager {
 .tructor(bas]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteDataManager {
 ]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteDataManager {
 ]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.
        /]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.       t]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext. {
        i]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.Polling() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.a) {
     ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.ab) {
      ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.er() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.ers(clients) {
  ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.isAutoPoll = ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.nts) {
   ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.nus) {
    ]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.tPolling() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.tructor() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext.unt() {]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|RemoteInspectorMFE ext]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.formatLatency]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.rmatTimestamp(i]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel.tizeText(str]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|TeleRemoteMetricsModel]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|cls {]] (class: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
