---
source: watchdog-agent/src/server/controller_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-12 21:06:27.734670
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: controller_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/server/controller_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: calls) — *GetStatus retrieves the status metadata of all supervised services*
- [[watchdog-agent/src/server/controller.go.md|Controller.PauseService]] (method: calls) — *PauseService suspends auto-restart supervision for a service and terminates any running process*
- [[watchdog-agent/src/server/controller.go.md|Controller.ResumeService]] (method: calls) — *ResumeService re-enables supervision for a service, clears crash history, and allows supervisor to relaunch*
- [[watchdog-agent/src/server/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance*
- [[watchdog-agent/src/server/controller.go.md|controller.go]] (same_package)
- [[watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/src/server/controller_test.go.md|TestController_PauseAndResumeService]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
