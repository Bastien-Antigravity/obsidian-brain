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
- [[sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink.Write]] (method: calls)
- [[sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|logger_resilience_and_alerts_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.Close]] (method: calls)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Error]] (method: calls)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/test_utils.go.md|getDockerLogs]] (function: calls) — *getDockerLogs fetches the last N lines of logs from a container.*
- [[sandbox-testing/02-Scenarios/go/test_utils.go.md|test_utils.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|TestLogServerHardeningScenario]] (function: belongs_to)
<!-- SYNC:END -->
