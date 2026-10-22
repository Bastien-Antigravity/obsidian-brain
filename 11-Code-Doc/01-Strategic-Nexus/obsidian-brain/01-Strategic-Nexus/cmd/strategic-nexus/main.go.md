---
source: obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go
workspace: 01-Strategic-Nexus
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.358881
---

# Mirror: main.go

## 📝 Description
Automatically generated mirror for `obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go`.

> **Essential Process**:
> Boots and initializes the 01-Strategic-Nexus Go microservice. Automatically sets up Postgres connections, loads configurations, and routes either background server routines or direct CLI invocations.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|NewStrategicController]] (function: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|NewEvolutionPipeline]] (function: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient.Stop]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|NewMFEClient]] (function: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|NewDBManager]] (function: calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|NewTelegramClient]] (function: calls)

### 🔌 Consumers (Inbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
