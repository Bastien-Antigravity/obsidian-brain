---
microservice: watchdog-agent
type: note
status: active
tags:
- '#service/watchdog-agent'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/rest/mfe.js`.

> **Essential Process**:
> OpenMFE web component for watchdog-agent, encapsulating supervisor status, managed processes telemetry, restart actions, and database initialization.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.bindEvents]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.cacheDom]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.displayServices]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.displayStatus]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.escapeAttribute]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.escapeHTML]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.loadAll]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.loadContracts]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.loadStatus]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.onMount]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.render]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.restartAll]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.restartService]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.startPostgres]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.switchTab]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|Alias]] (class: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.bindEvents]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.cacheDom]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.displayServices]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.displayStatus]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.escapeAttribute]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.escapeHTML]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.loadAll]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.loadContracts]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.loadStatus]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.onMount]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.render]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.restartAll]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.restartService]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.startPostgres]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE.switchTab]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE]] (class: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|WatchdogAgentMFE]] (class: defines_method)
<!-- SYNC:END -->
