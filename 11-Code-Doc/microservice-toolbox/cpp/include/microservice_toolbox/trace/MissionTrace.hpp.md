---
source: microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:06.556079
---

# Mirror: MissionTrace.hpp

## 📝 Description
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp`.

> **Essential Process**:
> Cross-service and cross-brain mission trace correlation (X-Bastien-Mission-ID) for C++17 microservices. Sanitizes, extracts, injects, and binds mission_id into structured Logger metadata.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/cpp/include/microservice_toolbox/logger/Logger.hpp.md|Logger.hpp]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|BindLoggerMission]] (function: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|InjectHeaders]] (function: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|MICROSERVICE_TOOLBOX_TRACE_MISSION_TRACE_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_TRACE_MISSION_TRACE_HPP*
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|ResolveEnvMissionId]] (function: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|SanitizeMissionId]] (function: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|clean]] (constant: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|first]] (constant: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|kEnvMissionId]] (constant: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|kHeaderMissionId]] (constant: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|kMaxMissionIdLen]] (constant: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|kMetadataKey]] (constant: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|last]] (constant: belongs_to)
- [[microservice-toolbox/cpp/include/microservice_toolbox/trace/MissionTrace.hpp.md|raw]] (constant: belongs_to)
- [[microservice-toolbox/rust/src/config/loader.rs.md|loader.rs]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
