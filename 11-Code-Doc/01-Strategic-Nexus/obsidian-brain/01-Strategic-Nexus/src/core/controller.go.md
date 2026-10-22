---
source: obsidian-brain/01-Strategic-Nexus/src/core/controller.go
workspace: 01-Strategic-Nexus
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.363863
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
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.RunEvolution]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: calls)

### 🔌 Consumers (Inbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md| string) string ]] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|, prefix string)]] (function: belongs_to) — *Inline helper to avoid external dependency checks*
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|DBManager]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|EvolutionPipeline]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|Logger]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|NewStrategicController]] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.CreatePersona]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.LogMilestone]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController.TriggerEvolution]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|StrategicController]] (struct: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|erns(content string) []] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|ontent string) []] (function: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|string) string ]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
