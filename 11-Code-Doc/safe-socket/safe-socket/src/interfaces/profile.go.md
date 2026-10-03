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
Automatically generated mirror for `safe-socket/src/interfaces/profile.go`.

> **Essential Process**:
> Defines SocketProfile abstractions and transport/protocol enum constants, enabling named profile resolution across TCP, TLS, UDP, and Shared Memory.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|ProtocolHello]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|ProtocolNone]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|ProtocolType]] (struct: belongs_to) — *ProtocolType defines the application-level handshake or startup protocol.*
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|SocketProfile]] (interface: belongs_to) — *SocketProfile defines the behavior for a connection strategy.*
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|TransportFramedTCP]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|TransportShm]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|TransportTLS]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|TransportType]] (struct: belongs_to) — *TransportType defines the underlying transport mechanism.*
- [[safe-socket/safe-socket/src/interfaces/profile.go.md|TransportUDP]] (constant: belongs_to)
<!-- SYNC:END -->
