---
source: obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-11-04 23:07:15.826814
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: controller_test.go

## 📝 Description
Automatically generated mirror for `obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|NewStrategicController]] (function: calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.ProcessCommand]] (method: calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|controller.go]] (same_package)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Error]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Info]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Warning]] (method: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|mockEvolutionPipeline.RunEvolution]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|controller.go]] (calls)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|controller.go]] (same_package)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|TestController_NilDB_LogMilestone]] (function: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|TestController_ProcessCommand_RunEvolution_DryRunParsing]] (function: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Error]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Info]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Warning]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger]] (struct: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger]] (struct: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|mockEvolutionPipeline.RunEvolution]] (method: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|mockEvolutionPipeline]] (struct: belongs_to)
- [[obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|mockEvolutionPipeline]] (struct: defines_method)
- [[obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|pipeline.go]] (calls)
- [[obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|mfe_client.go]] (calls)
- [[obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|db.go]] (calls)
- [[obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|telegram_client.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
