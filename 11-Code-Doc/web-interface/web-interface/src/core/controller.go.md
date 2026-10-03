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
Automatically generated mirror for `web-interface/src/core/controller.go`.

> **Essential Process**:
> Implements the centralized system control interface for the web-interface microservice. Exposes health monitoring and TCP database availability checks.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/core/controller.go.md|Controller.CheckDatabase]] (method: defines_method) — *CheckDatabase checks database availability dynamically by querying the current appConfig.*
- [[web-interface/web-interface/src/core/controller.go.md|Controller.GetStatus]] (method: defines_method) — *GetStatus returns metadata about the web-interface runtime.*

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/core/controller.go.md|Controller.CheckDatabase]] (method: belongs_to) — *CheckDatabase checks database availability dynamically by querying the current appConfig.*
- [[web-interface/web-interface/src/core/controller.go.md|Controller.GetStatus]] (method: belongs_to) — *GetStatus returns metadata about the web-interface runtime.*
- [[web-interface/web-interface/src/core/controller.go.md|Controller]] (struct: belongs_to) — *CheckDatabase checks database availability dynamically by querying the current appConfig.*
- [[web-interface/web-interface/src/core/controller.go.md|Controller]] (struct: defines_method) — *CheckDatabase checks database availability dynamically by querying the current appConfig.*
- [[web-interface/web-interface/src/core/controller.go.md|NewController]] (function: belongs_to) — *NewController creates a new Controller instance with dynamic config support.*
- [[web-interface/web-interface/src/core/controller.go.md|StatusInfo]] (struct: belongs_to) — *StatusInfo represents the service health and runtime statistics.*
- [[web-interface/web-interface/src/core/controller.go.md|WebController]] (interface: belongs_to) — *WebController defines the unified interface for web interface management.*
- [[web-interface/web-interface/src/core/controller.go.md|init]] (function: belongs_to)
- [[web-interface/web-interface/src/telegram/manager.go.md|manager.go]] (imports)
<!-- SYNC:END -->
