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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink.Write]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|logger_resilience_and_alerts_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.Close]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetLevel]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_performance_test.go.md|TestLogServerPerformanceScenario]] (function: belongs_to)
<!-- SYNC:END -->
