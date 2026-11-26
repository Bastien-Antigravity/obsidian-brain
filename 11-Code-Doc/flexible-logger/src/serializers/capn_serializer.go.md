---
microservice: flexible-logger
type: note
status: active
tags:
- '#service/flexible-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.SetLevel]] (method: calls) — *SetLevel sets the current log level.*
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|CapnpSerializer.Serialize]] (method: defines_method) — *Serialize converts LogEntry to bytes using LoggerMsg Cap'n Proto schema.*

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|CapnpSerializer.Serialize]] (method: belongs_to) — *Serialize converts LogEntry to bytes using LoggerMsg Cap'n Proto schema.*
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|CapnpSerializer]] (struct: belongs_to) — *CapnpSerializer implements the Serializer interface manually using LoggerMsg schema.*
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|CapnpSerializer]] (struct: defines_method) — *CapnpSerializer implements the Serializer interface manually using LoggerMsg schema.*
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|NewCapnpSerializer]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|mapLevel]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (same_package)
<!-- SYNC:END -->
