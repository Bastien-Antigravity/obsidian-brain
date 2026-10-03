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
Automatically generated mirror for `safe-socket/src/facade/socket_client.go`.

> **Essential Process**:
> Implements the interfaces.Socket interface for client-side transport management, handling exponential-backoff dial reconnection, TLS/TCP/UDP/SHM transport setup, protocol handshakes, and thread-safe data sending and receiving.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|NewEnvelopedConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.ReadMessage]] (method: calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|NewHeartbeatConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|heartbeat_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|NewReliableConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|reliable_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetAddress]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetConnectTimeout]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetProtocol]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetTransport]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Accept]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Listen]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Open]] (method: defines_method) — *If MaxRetries > 0, it will attempt reconnection on failure.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Read]] (method: defines_method) — *Read reads from the transport into the provided buffer (io.Reader compliance).*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Receive]] (method: defines_method) — *It returns the data read and any error encountered.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Send]] (method: defines_method) — *Send writes the raw data to the transport.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetDeadline]] (method: defines_method) — *SetDeadline sets the read and write deadlines associated with the connection.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetIdleTimeout]] (method: defines_method) — *SetIdleTimeout updates the internal idle timeout and refreshes the current deadline.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetLogger]] (method: defines_method) — *Bind logger to safe-socket*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetReadDeadline]] (method: defines_method) — *SetReadDeadline sets the deadline for future Read calls.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetWriteDeadline]] (method: defines_method) — *SetWriteDeadline sets the deadline for future Write calls.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Write]] (method: defines_method) — *Write implements the io.Writer interface in logger.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.attemptOpen]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|EnsureSafeLogger]] (function: calls) — *In strict mode (STRICT_LOGGER=true), it panics immediately.*
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Warning]] (method: calls)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.Initiate]] (method: calls) — *Initiate executes the handshake sequence or protocol logic (Client).*
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|NewHelloProtocol]] (function: calls)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|hello_protocol.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|ConnectTLS]] (function: calls) — *ConnectTLS dialer helper for TLS-wrapped FramedTCPSocket.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|Connect]] (function: calls) — *Connect dialer helper for FramedTCPSocket.*
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|ConnectShm]] (function: calls) — *If the file is smaller than TotalSize, it is grown.*
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (imports)
- [[safe-socket/safe-socket/src/transports/udp_client.go.md|ConnectUDP]] (function: calls) — *Note: UDP is connectionless. "Dial" just sets the default destination address.*

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (imports)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/facade/heartbeat_restart_test.go.md|heartbeat_restart_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_restart_test.go.md|heartbeat_restart_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|NewSocketClient]] (function: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Accept]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Listen]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Open]] (method: belongs_to) — *If MaxRetries > 0, it will attempt reconnection on failure.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Read]] (method: belongs_to) — *Read reads from the transport into the provided buffer (io.Reader compliance).*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Receive]] (method: belongs_to) — *It returns the data read and any error encountered.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Send]] (method: belongs_to) — *Send writes the raw data to the transport.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetDeadline]] (method: belongs_to) — *SetDeadline sets the read and write deadlines associated with the connection.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetIdleTimeout]] (method: belongs_to) — *SetIdleTimeout updates the internal idle timeout and refreshes the current deadline.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetLogger]] (method: belongs_to) — *Bind logger to safe-socket*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetReadDeadline]] (method: belongs_to) — *SetReadDeadline sets the deadline for future Read calls.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetWriteDeadline]] (method: belongs_to) — *SetWriteDeadline sets the deadline for future Write calls.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Write]] (method: belongs_to) — *Write implements the io.Writer interface in logger.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.attemptOpen]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient]] (struct: defines_method)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (imports)
<!-- SYNC:END -->
