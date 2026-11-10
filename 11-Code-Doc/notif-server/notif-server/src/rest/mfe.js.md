---
microservice: notif-server
type: note
status: active
tags:
- '#service/notif-server'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `notif-server/src/rest/mfe.js`.

> **Essential Process**:
> OpenMFE web component for notif-server, encapsulating dynamic alerting engine, provider management, and test notification dispatching.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bindEvents]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.cacheDom]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.deleteProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayNotifiers]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayStatus]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.escapeAttribute]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.escapeHTML]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadAll]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadContracts]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadNotifiers]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadStatus]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadSupportedTypes]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.onMount]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.reloadSenders]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.render]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.sendTestNotification]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.stringifyValue]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.submitAddProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.submitEditConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.switchTab]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (imports)
- [[notif-server/notif-server/src/rest/mfe.js.md|Alias]] (class: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bindEvents]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.cacheDom]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.deleteProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayNotifiers]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.escapeAttribute]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.escapeHTML]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadAll]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadContracts]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadNotifiers]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadSupportedTypes]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.onMount]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.reloadSenders]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.render]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.sendTestNotification]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.stringifyValue]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.submitAddProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.submitEditConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.switchTab]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE]] (class: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE]] (class: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|triggerEdit]] (function: belongs_to) — *Bind inline edit clicks and pencil buttons*
<!-- SYNC:END -->
