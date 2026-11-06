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
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.adAlertingConfig()]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.adNotifiers()]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.adSupportedTypes()]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bindEvents]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bmitAddProvider(t]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bmitEditConfig(p]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.cacheDom]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.capeAttribute(v]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.capeHTML(v]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayStatus]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.leteProvider(p]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadAll]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadSenders()]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadStatus]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.ndTestNotification(l]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.onMount]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.render]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.ringifyValue(v]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.splayAlertingConfig()]] (method: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.splayNotifiers()]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (imports)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.adAlertingConfig()]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.adNotifiers()]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.adSupportedTypes()]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bindEvents]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bmitAddProvider(t]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.bmitEditConfig(p]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.cacheDom]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.capeAttribute(v]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.capeHTML(v]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.displayStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.leteProvider(p]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadAll]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadSenders()]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.loadStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.ndTestNotification(l]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.onMount]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.render]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.ringifyValue(v]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.splayAlertingConfig()]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE.splayNotifiers()]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE]] (class: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|NotifServerMFE]] (class: defines_method)
- [[notif-server/notif-server/src/rest/mfe.js.md|ias e]] (class: belongs_to)
- [[notif-server/notif-server/src/rest/mfe.js.md|iggerEdit =]] (function: belongs_to) — *Bind inline edit clicks and pencil buttons*
<!-- SYNC:END -->
