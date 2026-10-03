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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/safe_socket_auto_hello_test.go.md|TestAutoHelloProfile_LocalResolution]] (function: belongs_to) — *client for a local address automatically selects the unencrypted TcpHelloClientProfile.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/safe_socket_auto_hello_test.go.md|TestAutoHelloProfile_RemoteResolution]] (function: belongs_to) — *client for a remote address automatically selects the encrypted TlsHelloClientProfile.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/safe_socket_auto_hello_test.go.md|TestAutoHello_IsCompletelyDynamic]] (function: belongs_to) — *TLS purely based on the target IP/host at runtime.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/safe_socket_auto_hello_test.go.md|TestAutoHello_LocalEndToEnd_Communication]] (function: belongs_to) — *3. Verifies successful connection, handshake, and bidirectional message delivery.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/safe_socket_auto_hello_test.go.md|TestAutoHello_ServiceAddressConfig]] (function: belongs_to) — *is retained and accessible on the created socket for dynamic discovery.*
<!-- SYNC:END -->
