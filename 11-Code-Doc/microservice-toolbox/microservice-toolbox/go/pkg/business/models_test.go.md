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
Automatically generated mirror for `microservice-toolbox/go/pkg/business/models_test.go`.

> **Essential Process**:
> Defines standard market data domain models (MarketEvent, OHLCV, Signal) across the fleet.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Deserialize]] (function: calls) — *Deserialize converts a JSON byte array into the target business object.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|Serialize]] (function: calls) — *Serialize converts a business object into a JSON byte array.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|WrapMarketEvent]] (function: calls) — *WrapMarketEvent creates a MarketEvent envelope for a payload.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/helpers.go.md|helpers.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|TestMarketEventSerialization]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|TestOHLCVSerialization]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/business/models_test.go.md|TestSignalSerialization]] (function: belongs_to)
<!-- SYNC:END -->
