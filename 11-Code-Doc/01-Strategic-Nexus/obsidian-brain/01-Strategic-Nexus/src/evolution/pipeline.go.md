---
source: obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go
workspace: 01-Strategic-Nexus
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.369353
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: pipeline.go

## 📝 Description
Automatically generated mirror for `obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go`.

> **Essential Process**:
> Implements the Genetic-Pareto Prompt Evolution algorithm inside the 01-Strategic-Nexus. Uses Google GenAI Go SDK to mutate prompt candidates and checks fitness.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Error]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Info]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller_test.go.md|dummyLogger.Warning]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.EvaluateFitness]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.MutatePrompt]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.RunEvolution]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.ProposeSkill]] (method: calls)

### 🔌 Consumers (Inbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|DBManager]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.EvaluateFitness]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.MutatePrompt]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline.RunEvolution]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline]] (struct: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|EvolutionPipeline]] (struct: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|Logger]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|NewEvolutionPipeline]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
