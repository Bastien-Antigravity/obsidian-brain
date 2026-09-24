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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Error]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|doHandshake]] (function: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|test_utils.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_adversarial_test.go.md|TestConfigServerAdversarialHardening]] (function: belongs_to)
<!-- SYNC:END -->
