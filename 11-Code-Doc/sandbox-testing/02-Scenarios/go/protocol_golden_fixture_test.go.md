---
source: sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go
workspace: sandbox-testing
type: code-mirror
status: auto-generated
last_sync: 2026-11-24 14:26:15.172492
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: protocol_golden_fixture_test.go

## 📝 Description
Automatically generated mirror for `sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go`.

> **Essential Process**:
> Cross-repository Golden Protocol & Wire Compatibility Verification Suite. Validates identical 4-byte Big-Endian frame headers, Cap'n Proto platform schemas (LoggerCapnpSchema, NotifierCapnpSchema), canonical 12-level log enum ordinal parity, and monotonic uint64 configuration revision guards.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|dynamic_ports_and_config_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|resolveWorkspaceRoot]] (function: calls) — *resolveWorkspaceRoot locates the root Bastien-Antigravity directory.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.SetLevel]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go.md|BenchmarkCapnpLoggerSchema_EncodeDecode]] (function: belongs_to) — *for Cap'n Proto LoggerMsg packed wire serialization and deserialization.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go.md|TestGoldenProtocol_Canonical12LogLevelsParity]] (function: belongs_to) — *in flexible-logger match the exact 0..11 wire ordinals in logger.capnp across all languages.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go.md|TestGoldenProtocol_PlatformCapnpSchemasSSoTParity]] (function: belongs_to) — *to schemas/platform/{logger,notifier}.capnp and produce valid contract operations.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go.md|TestGoldenProtocol_SafeSocket4ByteBigEndianFramingAndMaxPayloadGuard]] (function: belongs_to) — *deterministic 4-byte BE length prefix encoding and adversarial oversize rejection.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/protocol_golden_fixture_test.go.md|goldenMaxPayloadSize]] (constant: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
