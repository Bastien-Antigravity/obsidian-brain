---
source: obsidian-brain/01-Strategic-Nexus/src/store/db.go
workspace: 01-Strategic-Nexus
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.382182
---

# Mirror: db.go

## 📝 Description
Automatically generated mirror for `obsidian-brain/01-Strategic-Nexus/src/store/db.go`.

> **Essential Process**:
> Manages the PostgreSQL database connection pool and schema lifecycle for the 01-Strategic-Nexus.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.GetDecisions]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.InitSchema]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.ProposeSkill]] (method: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.UpsertDecision]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|controller.go]] (calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|pipeline.go]] (calls)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.GetDecisions]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.InitSchema]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.ProposeSkill]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.UpsertDecision]] (method: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager]] (struct: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager]] (struct: defines_method)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|Logger]] (interface: belongs_to)
- [[01-Strategic-Nexus/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|NewDBManager]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
