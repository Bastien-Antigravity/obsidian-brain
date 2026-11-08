---
source: microservice-toolbox/rust/src/wiretap/mod.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T21:44:11.623817
---

# Mirror: mod.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/wiretap/mod.rs`.

> **Essential Process**:
> High-performance, lock-free WireTap transport telemetry engine for Rust. Aggregates inter-service and external network connections and segregated information channels with cache-line padded atomics and branch-free power-of-two sampling. Periodically flushes snapshots to web-interface topology hub.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.drop]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicChannelEntry.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicChannelEntry.record]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicEdgeEntry.new]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicChannelEntry.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicChannelEntry.record]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicChannelEntry]] (struct: belongs_to) — *Aligned to 64 bytes to prevent False Sharing across CPU cores on multi-threaded execution*
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicChannelEntry]] (struct: defines_method) — *Aligned to 64 bytes to prevent False Sharing across CPU cores on multi-threaded execution*
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicEdgeEntry.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicEdgeEntry]] (struct: belongs_to) — *Cache-line aligned edge entry*
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|AtomicEdgeEntry]] (struct: defines_method) — *Cache-line aligned edge entry*
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|ChannelMetric]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|EdgeReport]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|IngestPayload]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|IngestResponse]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|format_iso]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|get_edges_registry]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|get_hub_url]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|get_local_service]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|get_local_service_name]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|get_web_hub_url]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|is_enabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|normalize_service_id]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|record_event]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|record_event_with_conn_delta]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|reset]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|set_enabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|set_local_service_name]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|set_web_hub_url]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|should_sample]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|snapshot]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
