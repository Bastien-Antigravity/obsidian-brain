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
> High-performance lock-free transport telemetry aggregator (WireTap) in C++17. Aggregates inter-service network connections and segregated information channels with 64-byte cache-line alignment, power-of-two sampling, and periodic HTTP hub sync.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetCommon]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetLocal]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.AtomicChannelEntry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.Record]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry.AtomicEdgeEntry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.to_json]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.AtomicChannelEntry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry.Record]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicChannelEntry]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry.AtomicEdgeEntry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|AtomicEdgeEntry]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ChannelMetric]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ConfigureFromConfig]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|EdgeReport]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|FormatIso]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetEdgeRegistry]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetLocalServiceRef]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetLocalService]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetRegistryMutex]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetReporterOnceFlag]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetStateMutex]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetWebHubURLRef]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GetWebHubURL]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|GlobalEnabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestPayload]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IngestResponse]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|IsEnabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|MergeRemoteSnapshot]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|NormalizeServiceID]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|PostIngestHttp]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|RecordEventWithConnDelta]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|RecordEvent]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ReporterLoop]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|Reset]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|SetEnabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|SetLocalService]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|SetWebHubURL]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|ShouldSample]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|Snapshot]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|addrinfo]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|configure_from_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|get_local_service]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|get_web_hub_url]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|is_enabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|merge_remote_snapshot]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|normalize_service_id]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|record_event]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|reset]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|set_enabled]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|set_local_service]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|set_web_hub_url]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|should_sample]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|snapshot]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/wiretap/WireTap.hpp.md|timeval]] (struct: belongs_to) — *else*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
