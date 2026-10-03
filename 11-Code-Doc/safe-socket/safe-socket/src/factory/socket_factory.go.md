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
Automatically generated mirror for `safe-socket/src/factory/socket_factory.go`.

> **Essential Process**:
> Instantiates and composes Socket instances from profile definitions and runtime configs, automatically selecting optimal transports (SHM vs FramedTCP) and protocol decorators.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|NewSocketClient]] (function: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Listen]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Open]] (method: calls) — *If MaxRetries > 0, it will attempt reconnection on failure.*
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|NewSocketServer]] (function: calls) — *NewSocketServer creates a new instance of SocketServer.*
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|NewShmHelloProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/shm_profile.go.md|NewShmProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|NewTcpClientProfile]] (function: calls) — *NewTcpClientProfile creates a new instance of a TCP profile without a protocol.*
- [[safe-socket/safe-socket/src/profiles/tcp_client_profile.go.md|NewTcpHelloClientProfile]] (function: calls) — *NewTcpHelloClientProfile creates a new instance of a TCP profile with the Hello protocol.*
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|NewTcpHelloServerProfile]] (function: calls) — *NewTcpHelloServerProfile creates a new instance of a TCP server profile with the Hello protocol.*
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|NewTcpServerProfile]] (function: calls) — *NewTcpServerProfile creates a new instance of a TCP server profile without a protocol.*
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|tcp_server_profile.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsClientProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsHelloClientProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsHelloServerProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/tls_profile.go.md|NewTlsServerProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|NewUdpHelloProfile]] (function: calls)
- [[safe-socket/safe-socket/src/profiles/udp_profile.go.md|NewUdpProfile]] (function: calls)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|GetMachineDetector]] (function: calls) — *GetMachineDetector returns the singleton MachineDetector instance.*
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.IsLocalAddress]] (method: calls) — *IsLocalAddress checks if an address ("IP:Port", "host:Port", or "IP") belongs to the local machine.*
- [[safe-socket/safe-socket/src/utils/machine_detector_test.go.md|machine_detector_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (calls)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateOpenSocket]] (function: belongs_to) — *CreateOpenSocket constructs a Socket based on the provided parameters and opens/listens it.*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateSocket]] (function: belongs_to) — *Useful for connection pools or when deferred connection is required.*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateWithConfig]] (function: belongs_to) — *- autoConnect: if true, automatically calls Open() / Listen()*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|Create]] (function: belongs_to) — *An interfaces.Socket which can be used to Send/Receive (Client) or Accept (Server).*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|DefaultHandshakeTimeout]] (constant: belongs_to) — *DefaultHandshakeTimeout is used for network transports (TCP/UDP)*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|DefaultLocalHandshakeTimeout]] (constant: belongs_to) — *DefaultLocalHandshakeTimeout is used for loopback (127.0.0.1/localhost)*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|DefaultShmHandshakeTimeout]] (constant: belongs_to) — *DefaultShmHandshakeTimeout is used for Shared Memory (SHM)*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|createProfile]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|parseSocketType]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (calls)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (same_package)
<!-- SYNC:END -->
