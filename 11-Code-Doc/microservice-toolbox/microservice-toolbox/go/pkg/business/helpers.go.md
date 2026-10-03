---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/business/helpers.go`.

> **Essential Process**:
> Helper utilities and conversion routines for core business domain models.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Deserialize]] (function: belongs_to) — *Deserialize converts a JSON byte array into the target business object.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Serialize]] (function: belongs_to) — *Serialize converts a business object into a JSON byte array.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|SystemTimestamp]] (function: belongs_to) — *SystemTimestamp returns the current unix timestamp in milliseconds.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|WrapMarketEvent]] (function: belongs_to) — *WrapMarketEvent creates a MarketEvent envelope for a payload.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|models_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|models_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|providers.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|serializer.rs]] (calls)
<!-- SYNC:END -->
