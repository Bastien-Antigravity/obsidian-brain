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
- [[microservice-toolbox/go/pkg/serializers/providers.go.md|NewBinSerializer]] (function: calls)
- [[microservice-toolbox/go/pkg/serializers/providers.go.md|NewJSONSerializer]] (function: calls)
- [[microservice-toolbox/go/pkg/serializers/serializer_test.go.md|serializer_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/integration/matrix_gen.go.md|IntegrationData]] (struct: belongs_to)
- [[microservice-toolbox/integration/matrix_gen.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
