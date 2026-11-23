---
microservice: log-server
type: service-hub
status: active
tags:
- '#service/log-server'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 🌐 Service Hub: Log-Server

*High-Performance ordered logging and rotation engine.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 log-server](https://github.com/Bastien-Antigravity/log-server)
- **Behavior Specs**: [📜 BDD Specifications](02-Business-BDD/02-Behavior-Specs/log-server/)
- **Protocols**: `src/schema/capnp/logger.capnp`, `src/schema/proto/log_service.proto` (includes `LogBridge.GetExchangeContracts`), and `src/core/contracts.rs`

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[Rust-Safety-Specialist|Rust-Safety]]
- **Systems Specialist**: [[CPP-Low-Latency-Specialist|CPP-Low-Latency]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/log-server"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

## 🏗️ Architecture Decision Records (ADR)

### ADR-001: Evolution to Single-Authority FIFO Sequencing
*   **Context**: Out-of-order pre-channel sequence assignment caused sequence gaps and BTreeMap stall intervals.
*   **Decision**: Adopted Single-Authority FIFO Sequencing within `LogWriter::writer_task`. Sequence IDs are assigned monotonically on channel dequeue, and bursts are drained greedily via `rx.try_recv()`.
*   **Rationale**: Eliminates artificial gap timeouts and multi-producer race conditions while ensuring exact 1-to-1 order parity between disk files and the in-memory `LogRingBuffer`.
*   **Consequence**: Zero artificial gap skips, predictable low-latency persistence, and deterministic clean shutdown draining.

### ADR-002: Pure gRPC HTTP/2 Streaming for Real-Time Fleet Observability
*   **Context**: The web-interface requires live log inspection and recent history for the browser console. Embedding an HTTP REST server in `log-server` introduced unwanted web dependencies (`axum`), port fragmentation (`9022`), and dual-protocol responsibilities.
*   **Decision**: Implement native gRPC server streaming (`rpc StreamLogs(StreamLogsRequest) returns (stream LogRequest)`) and buffered history queries (`rpc GetTailLogs(TailLogsRequest) returns (TailLogsResponse)`) on existing gRPC port `9021`. Ingestion events are pushed directly to an in-memory `LogRingBuffer` (5,000 capacity) and a Tokio broadcast channel. `web-interface` acts as the single web gateway, bridging gRPC to Server-Sent Events (SSE).
*   **Rationale**: Preserves single responsibility, purges all web dependencies from the Rust daemon, and guarantees sub-millisecond streaming latency with zero polling and zero disk I/O bottlenecks.
*   **Consequence**: Standard binary protocol across the fleet; `web-interface` manages all HTTP/browser-facing transport.

### ADR-003: Microservice-Sourced Exchange Contracts & OpenMFE Registry Heartbeat
*   **Context**: OpenMFE `<log-server-inspector>` previously hardcoded `.proto` and `.capnp` schema snippets in `web-interface`.
*   **Decision**: `log-server` embeds `src/schema/proto/log_service.proto` and `src/schema/capnp/logger.capnp` natively (`src/core/contracts.rs`), serves them over `LogBridge.GetExchangeContracts` (`grpc_server.rs`), and sends an async background `POST /api/v1/register` heartbeat (`src/facade/log_server.rs`) attaching `contracts[]` to `web-interface`. `web-interface` proxies gRPC first and falls back only to `mfe.Registry` on `/api/v1/system/logs/contracts`.
