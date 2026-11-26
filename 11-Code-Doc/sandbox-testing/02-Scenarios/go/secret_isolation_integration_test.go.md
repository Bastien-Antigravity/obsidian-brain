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
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.AddMetadata]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Critical]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Debug]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Error]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.GetLevel]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.GetMetadata]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.GetNotifQueue]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Info]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.LogWithCaller]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Log]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Logon]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Logout]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Report]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Schedule]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetCallerSkip]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetLevel]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetLocalNotifQueue]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetMetadata]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Stream]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Trade]] (method: defines_method)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/02-Scenarios/go/concurrency_chaos_test.go.md|concurrency_chaos_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/concurrency_chaos_test.go.md|concurrency_chaos_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/config_adversarial_test.go.md|config_adversarial_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/config_adversarial_test.go.md|config_adversarial_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/dynamic_logging_and_alerts_test.go.md|dynamic_logging_and_alerts_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/dynamic_logging_and_alerts_test.go.md|dynamic_logging_and_alerts_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|dynamic_ports_and_config_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|dynamic_ports_and_config_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/ecosystem_tooling_parity_test.go.md|ecosystem_tooling_parity_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/ecosystem_tooling_parity_test.go.md|ecosystem_tooling_parity_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/log_server_performance_test.go.md|log_server_performance_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/log_server_performance_test.go.md|log_server_performance_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|logger_resilience_and_alerts_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|logger_resilience_and_alerts_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|ontime_concurrency_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|ontime_concurrency_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/protocol_adversarial_test.go.md|protocol_adversarial_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/protocol_adversarial_test.go.md|protocol_adversarial_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go.md|protocol_golden_fixture_test.go]] (calls)
- [[sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go.md|protocol_golden_fixture_test.go]] (same_package)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|TestScenario_ZeroKnowledgeSecretsIntegration]] (function: belongs_to) — *audit ensuring zero-knowledge boundaries, per-service key isolation, and non-shared configs.*
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|generateTestKeyPair]] (function: belongs_to) — *generateTestKeyPair creates an in-memory RSA key pair encoded as PEM strings.*
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.AddMetadata]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Critical]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Debug]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Error]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.GetLevel]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.GetMetadata]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.GetNotifQueue]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Info]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.LogWithCaller]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Log]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Logon]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Logout]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Report]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Schedule]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetCallerSkip]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetLevel]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetLocalNotifQueue]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetMetadata]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Stream]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Trade]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Warning]] (method: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger]] (struct: belongs_to)
- [[sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger]] (struct: defines_method)
<!-- SYNC:END -->
