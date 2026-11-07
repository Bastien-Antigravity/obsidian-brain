---
source: obsidian-brain/01-Strategic-Nexus/src/core/controller.go
workspace: 01-Strategic-Nexus
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.363863
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: controller.go

## 📝 Description
Automatically generated mirror for `obsidian-brain/01-Strategic-Nexus/src/core/controller.go`.

> **Essential Process**:
> Unified command controller coordinating database logging and background evolutionary skill iterations for 01-Strategic-Nexus.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.CreatePersona]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.ProcessCommand]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.SyncStrategicMemory]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Info]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Warning]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|mockEvolutionPipeline.RunEvolution]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.UpsertDecision]] (method: calls)

### 🔌 Consumers (Inbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|DBManager]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|EvolutionPipeline]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|Logger]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|NewStrategicController]] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.CreatePersona]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.ProcessCommand]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.SyncStrategicMemory]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|formatPascalCase]] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|formatTitleName]] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|parseAntiBacklog]] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|parseStrategicPatterns]] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|stringsHasPrefix]] (function: belongs_to) — *Inline helper to avoid external dependency checks*
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|controller_test.go]] (calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|mfe_client.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
