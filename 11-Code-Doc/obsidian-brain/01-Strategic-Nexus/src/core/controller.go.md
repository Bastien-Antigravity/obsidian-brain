---
microservice: 01-Strategic-Nexus
type: note
status: active
tags:
- '#service/01-Strategic-Nexus'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/01-Strategic-Nexus/src/core/controller.go`.

> **Essential Process**:
> Unified command controller coordinating database logging and background evolutionary skill iterations for 01-Strategic-Nexus.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.CreatePersona]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.ProcessCommand]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.SyncStrategicMemory]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Info]] (method: calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Warning]] (method: calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|mockEvolutionPipeline.RunEvolution]] (method: calls)
- [[obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: calls)
- [[obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.UpsertDecision]] (method: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|DBManager]] (interface: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|EvolutionPipeline]] (interface: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|Logger]] (interface: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|NewStrategicController]] (function: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.CreatePersona]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.ProcessCommand]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.SyncStrategicMemory]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|formatPascalCase]] (function: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|formatTitleName]] (function: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|parseAntiBacklog]] (function: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|parseStrategicPatterns]] (function: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|stringsHasPrefix]] (function: belongs_to) — *Inline helper to avoid external dependency checks*
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|controller_test.go]] (calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|mfe_client.go]] (calls)
<!-- SYNC:END -->
