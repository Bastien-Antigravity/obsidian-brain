---
source: safe-socket/src/models/hybrid_timeout.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:07.094533
---

# Mirror: hybrid_timeout.go

## 📝 Description
Automatically generated mirror for `safe-socket/src/models/hybrid_timeout.go`.

> **Essential Process**:
> Computes transport- and deployment-mode-aware hybrid idle timeouts and adaptive 2.5x heartbeat intervals for safe-socket connections: - SHM (Shared Memory): Infinite wait (Deadline=0, Heartbeat=0) with zero frame overhead. - UDP (Datagrams): Short datagram deadline (5s, Heartbeat=0). - TCP/TLS in Local Native Mode: Server=10m, Client=60s (auto 24s heartbeat). - TCP/TLS in Docker/Bridge Mode: Server=3m, Client=30s (auto 12s heartbeat to keep NAT/conntrack state warm and reap crashed containers rapidly).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[safe-socket/safe_socket.go.md|safe_socket.go]] (calls)
- [[safe-socket/src/models/hybrid_timeout.go.md|DefaultUDPIdleTimeout]] (constant: belongs_to) — *DefaultUDPIdleTimeout bounds single-datagram UDP socket reads/writes.*
- [[safe-socket/src/models/hybrid_timeout.go.md|DockerTCPClientHeartbeat]] (constant: belongs_to) — *DockerTCPClientHeartbeat satisfies the 2.5x safety ratio for DockerTCPClientIdleTimeout.*
- [[safe-socket/src/models/hybrid_timeout.go.md|DockerTCPClientIdleTimeout]] (constant: belongs_to) — *DockerTCPClientIdleTimeout drives a 12s (30s / 2.5) client heartbeat to prevent conntrack eviction.*
- [[safe-socket/src/models/hybrid_timeout.go.md|DockerTCPServerIdleTimeout]] (constant: belongs_to) — *DockerTCPServerIdleTimeout reaps crashed container peers rapidly across Docker bridges/overlays.*
- [[safe-socket/src/models/hybrid_timeout.go.md|IsDockerRuntime]] (function: belongs_to) — *IsDockerRuntime detects containerized execution from DOCKER_ENV or CONTAINER environment markers.*
- [[safe-socket/src/models/hybrid_timeout.go.md|LocalTCPClientHeartbeat]] (constant: belongs_to) — *LocalTCPClientHeartbeat satisfies the 2.5x safety ratio for LocalTCPClientIdleTimeout.*
- [[safe-socket/src/models/hybrid_timeout.go.md|LocalTCPClientIdleTimeout]] (constant: belongs_to) — *LocalTCPClientIdleTimeout drives a 24s (60s / 2.5) client heartbeat on native loopback hosts.*
- [[safe-socket/src/models/hybrid_timeout.go.md|LocalTCPServerIdleTimeout]] (constant: belongs_to) — *LocalTCPServerIdleTimeout bounds zombie sockets on native loopback hosts.*
- [[safe-socket/src/models/hybrid_timeout.go.md|NewHybridSocketConfig]] (function: belongs_to) — *and infinite reconnect resilience (MaxRetries: -1) for clients.*
- [[safe-socket/src/models/hybrid_timeout.go.md|ResolveHybridTimeouts]] (function: belongs_to) — *profile/transport name, socket role ("client" or "server"), and deployment mode (isDocker).*
- [[safe-socket/src/models/hybrid_timeout_test.go.md|hybrid_timeout_test.go]] (calls)
- [[safe-socket/src/models/hybrid_timeout_test.go.md|hybrid_timeout_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
