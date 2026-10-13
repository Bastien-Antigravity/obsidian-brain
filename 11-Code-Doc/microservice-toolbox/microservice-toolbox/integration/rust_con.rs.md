---
microservice: microservice-toolbox
type: note
status: active
tags:
- '#service/microservice-toolbox'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: calls) — *Synchronize with the Config Server*
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/integration/rust_con.rs.md|IntegrationData]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/integration/rust_con.rs.md|main]] (function: belongs_to)
<!-- SYNC:END -->
