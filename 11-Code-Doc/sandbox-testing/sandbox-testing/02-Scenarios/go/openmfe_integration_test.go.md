---
microservice: sandbox-testing
type: note
status: active
tags:
- '#service/sandbox-testing'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|dynamic_ports_and_config_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|resolveWorkspaceRoot]] (function: calls) — *resolveWorkspaceRoot locates the root Bastien-Antigravity directory.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|logger_resilience_and_alerts_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.Close]] (method: calls)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/openmfe_integration_test.go.md|TestCrossRepoOpenMFELifecycleParity]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/openmfe_integration_test.go.md|TestOpenMFERegistrationScenario]] (function: belongs_to)
<!-- SYNC:END -->
