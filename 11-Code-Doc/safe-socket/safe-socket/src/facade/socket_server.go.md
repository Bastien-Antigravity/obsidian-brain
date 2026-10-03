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
Automatically generated mirror for `safe-socket/src/facade/socket_server.go`.

> **Essential Process**:
> Implements the interfaces.Socket interface for server-side lifecycle management, handling transport listening, connection tracking, handshakes, and graceful draining.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|NewEnvelopedConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|NewHandshakeConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|handshake_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|NewHeartbeatConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|heartbeat_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|NewReliableConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|reliable_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetAddress]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetConnectTimeout]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetProtocol]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetTransport]] (method: calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Accept]] (method: defines_method) — *Accept accepts a new connection and performs the handshake if defined.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Close]] (method: defines_method) — *If connections remain open after the drain timeout, they are force-closed to prevent shutdown hangs.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.GetAddr]] (method: defines_method) — *GetAddr returns the listener's network address, if the server is listening.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Listen]] (method: defines_method) — *Listen starts listening on the address specified by the profile.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Open]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Read]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Receive]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Send]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetIdleTimeout]] (method: defines_method) — *SetIdleTimeout updates the internal idle timeout for newly accepted connections.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetLogger]] (method: defines_method) — *Bind logger to safe-socket*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetReadDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetWriteDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Write]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|trackingConnection.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|EnsureSafeLogger]] (function: calls) — *In strict mode (STRICT_LOGGER=true), it panics immediately.*
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Debug]] (method: calls)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Info]] (method: calls)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Warning]] (method: calls)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.WaitInitiation]] (method: calls) — *WaitInitiation waits for a HelloMsg from the client and unmarshals it.*
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|NewHelloProtocol]] (function: calls)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|hello_protocol.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|ListenTLS]] (function: calls) — *ListenTLS creates a new TLS-enabled FramedTCPListener.*
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (imports)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ListenShm]] (function: calls) — *ListenShm creates (or opens) the SHM file and prepares it for a client connection.*
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|ListenUDP]] (function: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|NewSocketServer]] (function: belongs_to) — *NewSocketServer creates a new instance of SocketServer.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Accept]] (method: belongs_to) — *Accept accepts a new connection and performs the handshake if defined.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Close]] (method: belongs_to) — *If connections remain open after the drain timeout, they are force-closed to prevent shutdown hangs.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.GetAddr]] (method: belongs_to) — *GetAddr returns the listener's network address, if the server is listening.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Listen]] (method: belongs_to) — *Listen starts listening on the address specified by the profile.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Open]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Read]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Receive]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Send]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetIdleTimeout]] (method: belongs_to) — *SetIdleTimeout updates the internal idle timeout for newly accepted connections.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetLogger]] (method: belongs_to) — *Bind logger to safe-socket*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetReadDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.SetWriteDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.Write]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer]] (struct: belongs_to) — *SetIdleTimeout updates the internal idle timeout for newly accepted connections.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer]] (struct: defines_method) — *SetIdleTimeout updates the internal idle timeout for newly accepted connections.*
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|trackingConnection.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|trackingConnection]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|trackingConnection]] (struct: defines_method)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
<!-- SYNC:END -->
