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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_adversarial_test.go.md|config_adversarial_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_adversarial_test.go.md|config_adversarial_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_persistence_test.go.md|config_persistence_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_persistence_test.go.md|config_persistence_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_server_hardening_test.go.md|config_server_hardening_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_server_hardening_test.go.md|config_server_hardening_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_stress_test.go.md|config_stress_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_stress_test.go.md|config_stress_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_sync_on_arrival_test.go.md|config_sync_on_arrival_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_sync_on_arrival_test.go.md|config_sync_on_arrival_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|notif_server_hardening_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|notif_server_hardening_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|WaitForLogServer]] (function: belongs_to) — *Returns true if reachable, false on timeout, and closes sockets promptly.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|contains]] (function: belongs_to) — *contains is a primitive string containment check.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|doHandshake]] (function: belongs_to) — *doHandshake performs a standard tcp-hello handshake for testing purposes.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|getDockerLogs]] (function: belongs_to) — *getDockerLogs fetches the last N lines of logs from a container.*
<!-- SYNC:END -->
