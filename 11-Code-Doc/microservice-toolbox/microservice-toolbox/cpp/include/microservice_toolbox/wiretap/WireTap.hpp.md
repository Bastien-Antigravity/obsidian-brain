---
source: microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T21:45:23.615824
---

# Mirror: WireTap.hpp

## 📝 Description
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp`.

> **Essential Process**:
> High-performance lock-free transport telemetry aggregator (WireTap) in C++17. Aggregates inter-service network connections and segregated information channels with 64-byte cache-line alignment to eliminate False Sharing and power-of-two sampling.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.AtomicChannelEntry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.Record]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry.AtomicEdgeEntry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.to_json]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.AtomicChannelEntry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.Record]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry]] (struct: belongs_to) — *Aligned to 64 bytes to prevent False Sharing across CPU cores on multi-threaded execution*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry]] (struct: defines_method) — *Aligned to 64 bytes to prevent False Sharing across CPU cores on multi-threaded execution*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry.AtomicEdgeEntry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|FormatIso]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetEdgeRegistry]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetRegistryMutex]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GlobalEnabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IsEnabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|NormalizeServiceID]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|RecordEvent]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|Reset]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|SetEnabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ShouldSample]] (function: belongs_to) — *Power-of-two sampling check (thread-local counter, zero mutex)*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|Snapshot]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
