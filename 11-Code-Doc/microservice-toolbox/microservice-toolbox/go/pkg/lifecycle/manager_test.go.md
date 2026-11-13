---
microservice: microservice-toolbox
type: note
status: active
tags:
- '#service/microservice-toolbox'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/lifecycle/manager_test.go`.

> **Essential Process**:
> Manages application lifecycle, OS signal traps (SIGINT, SIGTERM), and orderly LIFO cleanups.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.ExecuteCleanups]] (method: calls) — *ExecuteCleanups runs all registered cleanup hooks in LIFO order and drains the hook list.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Register]] (method: calls) — *Register adds a named cleanup function to the shutdown sequence safely under mutex.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|Manager.Wait]] (method: calls) — *then executes all registered cleanups in reverse registration order (LIFO).*
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|NewManager]] (function: calls) — *NewManager creates a new lifecycle manager with default logging.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|manager.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager_test.go.md|TestManager_Lifecycle]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/spec/spec.go.md|spec.go]] (imports)
<!-- SYNC:END -->
