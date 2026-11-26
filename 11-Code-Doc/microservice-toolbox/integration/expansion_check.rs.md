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
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_local]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|load_config]] (function: calls) — *Initializes a configuration loader following the Microservice Toolbox 'Hierarchy of Truth'.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|loader.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.rs.md|main]] (function: belongs_to)
<!-- SYNC:END -->
