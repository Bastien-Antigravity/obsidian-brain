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

## 📝 Description
Automatically generated mirror for `safe-socket/cmd/test/factory_test.go`.

> **Essential Process**:
> Comprehensive end-to-end factory test suite validating TCP, UDP, TLS, and SHM socket initialization, handshake flows, and bidirectional transport I/O.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Close]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.ReadMessage]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Write]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Accept]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Open]] (method: calls) — *If MaxRetries > 0, it will attempt reconnection on failure.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Read]] (method: calls) — *Read reads from the transport into the provided buffer (io.Reader compliance).*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Receive]] (method: calls) — *It returns the data read and any error encountered.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Send]] (method: calls) — *Send writes the raw data to the transport.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|NewHelloProtocol]] (function: calls)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|hello_protocol.go]] (imports)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.FromName]] (method: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestSHM_FullExchange]] (function: belongs_to) — *TestSHM_FullExchange Verifies server/client exchange via SHM*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTCP_Hello]] (function: belongs_to) — *TestTCP_Hello Verifies TCP with Hello Protocol Handshake*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTCP_Raw]] (function: belongs_to) — *TestTCP_Raw Verifies basic TCP send/receive using the Factory*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTCP_Raw_Write_Method]] (function: belongs_to) — *TestTCP_Raw_Write_Method Verifies the new Write() method (Send alias)*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTLS_Hello]] (function: belongs_to) — *TestTLS_Hello Verifies TCP with TLS and Hello Protocol*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestUDP_Hello]] (function: belongs_to) — *TestUDP_Hello Verifies UDP with Hello Protocol + Stateless Envelope*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestUDP_Raw]] (function: belongs_to) — *TestUDP_Raw Verifies basic UDP send/receive using the Factory*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestUDP_Reliable]] (function: belongs_to) — *TestUDP_Reliable Verifies UDP with Reliability Layer (ACKs/Retries)*
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|generateSelfSignedCert]] (function: belongs_to)
<!-- SYNC:END -->
