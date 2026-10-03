---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go`.

> **Essential Process**:
> Boots and initializes the 01-Strategic-Nexus Go microservice. Automatically sets up Postgres connections, loads configurations, and routes either background server routines or direct CLI invocations.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|NewStrategicController]] (function: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|NewEvolutionPipeline]] (function: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient.Stop]] (method: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|NewMFEClient]] (function: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|NewDBManager]] (function: calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|NewTelegramClient]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
