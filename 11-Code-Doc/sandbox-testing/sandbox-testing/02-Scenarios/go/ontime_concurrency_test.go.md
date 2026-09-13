

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Log]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|TestOntimeConcurrentExecutionLock]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|TestOntimeConcurrentJobCreation]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|ontimeBaseURL]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|setOntimeDistributedMode]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|waitForOntimeServer]] (function: belongs_to)
<!-- SYNC:END -->
