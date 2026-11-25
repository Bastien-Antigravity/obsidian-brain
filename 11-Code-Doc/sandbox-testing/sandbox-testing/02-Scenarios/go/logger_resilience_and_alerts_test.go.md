---
source: sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go
workspace: sandbox-testing
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 01:29:29.026298
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: logger_resilience_and_alerts_test.go

## 📝 Description
Automatically generated mirror for `sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink.Close]] (method: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink.Write]] (method: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.Close]] (method: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.GetAlerts]] (method: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.Notify]] (method: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|slowScenarioSink.Close]] (method: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|slowScenarioSink.Write]] (method: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Error]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/concurrency_chaos_test.go.md|concurrency_chaos_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/concurrency_chaos_test.go.md|concurrency_chaos_test.go]] (same_package)
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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_logging_and_alerts_test.go.md|dynamic_logging_and_alerts_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_logging_and_alerts_test.go.md|dynamic_logging_and_alerts_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|dynamic_ports_and_config_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|dynamic_ports_and_config_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/full_pipeline_test.go.md|full_pipeline_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/full_pipeline_test.go.md|full_pipeline_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_performance_test.go.md|log_server_performance_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_performance_test.go.md|log_server_performance_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|TestLoggerResilience_BoundedDrainTimeoutShutdown]] (function: belongs_to) — *enforces bounded drain timeout and unblocks without deadlocking when downstream sinks hang.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|TestLoggerResilience_CanonicalSchemaRoundtrip]] (function: belongs_to) — *serialization adheres strictly to the canonical SSoT schema in microservice-toolbox.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|TestLoggerResilience_ThrottledTelegramDropAlert]] (function: belongs_to) — *AsyncSink queue emits at most 1 warning alert per throttle window tagged 'telegram'.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink.Close]] (method: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink.Write]] (method: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink]] (struct: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|discardScenarioSink]] (struct: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.Close]] (method: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.GetAlerts]] (method: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier.Notify]] (method: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier]] (struct: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|mockScenarioNotifier]] (struct: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|slowScenarioSink.Close]] (method: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|slowScenarioSink.Write]] (method: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|slowScenarioSink]] (struct: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/logger_resilience_and_alerts_test.go.md|slowScenarioSink]] (struct: defines_method)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|nats_and_fleet_control_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|nats_and_fleet_control_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|notif_server_hardening_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|notif_server_hardening_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|ontime_concurrency_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|ontime_concurrency_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/openmfe_integration_test.go.md|openmfe_integration_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/openmfe_integration_test.go.md|openmfe_integration_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/orderbook_aggregator_test.go.md|orderbook_aggregator_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/orderbook_aggregator_test.go.md|orderbook_aggregator_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/protocol_adversarial_test.go.md|protocol_adversarial_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/protocol_adversarial_test.go.md|protocol_adversarial_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/rag_engine_storage_test.go.md|rag_engine_storage_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/rag_engine_storage_test.go.md|rag_engine_storage_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/safe_socket_auto_hello_test.go.md|safe_socket_auto_hello_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/safe_socket_auto_hello_test.go.md|safe_socket_auto_hello_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/squad_control_integration_test.go.md|squad_control_integration_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/squad_control_integration_test.go.md|squad_control_integration_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/technical_analysis_test.go.md|technical_analysis_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/technical_analysis_test.go.md|technical_analysis_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|test_utils.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|test_utils.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/triple_pipeline_test.go.md|triple_pipeline_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/triple_pipeline_test.go.md|triple_pipeline_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/web_interface_bootstrap_test.go.md|web_interface_bootstrap_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/web_interface_bootstrap_test.go.md|web_interface_bootstrap_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
