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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: calls)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/scaffolding_scenario_test.py.md|scaffolding_scenario_test.py]] (calls)
- [[sandbox-testing/sandbox-testing/04-Mock-Provider/main.go.md|main]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/04-Mock-Provider/main.go.md|startWebSocketServer]] (function: belongs_to)
<!-- SYNC:END -->
