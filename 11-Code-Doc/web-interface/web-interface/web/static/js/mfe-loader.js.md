---
microservice: web-interface
type: note
status: active
tags:
- '#service/web-interface'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `web-interface/web/static/js/mfe-loader.js`.

> **Essential Process**:
> OpenMFE Micro-Frontend Dynamic Loader and Schema-Driven Shell Coordinator. Populates standardized Bastien-UI shell, binds AI/RAG context assistant, and instantiates decentralized microservice Web Components.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.find]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/prism/prism-module.js.md|highlightElement]] (function: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|bindGlobalPopoverDismissers]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|bindTabNavigation]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|enrichAISection]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|enrichStandardShell]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|fetchServices]] (function: belongs_to) — *Fetch registered MFE services with deduplication*
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|init]] (function: belongs_to) — *Initialize*
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|injectNavigation]] (function: belongs_to) — *Inject MFE navigation links dynamically into the right #Sidenav drawer*
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|loadMFE]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|norm]] (function: belongs_to) — *Resilient service resolution: match exact name, navTitle, tag, or alphanumeric normalized equivalent*
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|runRAGQuery]] (function: belongs_to) — *Semantic RAG Query Runner*
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|setSpecsPopoverOpen]] (function: belongs_to)
<!-- SYNC:END -->
