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
- **Protocols**: log-server/capnp/logger.capnp

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

### ADR-001: Liveness over Completeness (Gap Timeout)
*   **Context**: Out-of-order delivery via TCP/UDP can cause sequence gaps in the BTreeMap buffer.
*   **Decision**: Enforce a **500ms timeout** on missing sequences. If the missing sequence doesn't arrive within this window, the server forces progress to the next available sequence.
*   **Rationale**: Service availability is prioritized over perfect sequential integrity. A blocked writer stops the entire fleet from logging (back-pressure).
*   **Consequence**: Small gaps in logs are possible under high packet loss, but service uptime is guaranteed.

### ADR-002: Pure gRPC HTTP/2 Streaming for Real-Time Fleet Observability
*   **Context**: The web-interface requires live log inspection and recent history for the browser console. Embedding an HTTP REST server in `log-server` introduced unwanted web dependencies (`axum`), port fragmentation (`9022`), and dual-protocol responsibilities.
*   **Decision**: Implement native gRPC server streaming (`rpc StreamLogs(StreamLogsRequest) returns (stream LogRequest)`) and buffered history queries (`rpc GetTailLogs(TailLogsRequest) returns (TailLogsResponse)`) on existing gRPC port `9021`. Ingestion events are pushed directly to an in-memory `LogRingBuffer` (5,000 capacity) and a Tokio broadcast channel. `web-interface` acts as the single web gateway, bridging gRPC to Server-Sent Events (SSE).
*   **Rationale**: Preserves single responsibility, purges all web dependencies from the Rust daemon, and guarantees sub-millisecond streaming latency with zero polling and zero disk I/O bottlenecks.
*   **Consequence**: Standard binary protocol across the fleet; `web-interface` manages all HTTP/browser-facing transport.
