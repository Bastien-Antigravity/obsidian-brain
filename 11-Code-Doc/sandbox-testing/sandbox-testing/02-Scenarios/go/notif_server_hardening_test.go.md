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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|doHandshake]] (function: calls) — *doHandshake performs a standard tcp-hello handshake for testing purposes.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|getDockerLogs]] (function: calls) — *getDockerLogs fetches the last N lines of logs from a container.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|test_utils.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|TestNotifServerHardeningScenario]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|getDockerPort]] (function: belongs_to)
<!-- SYNC:END -->
