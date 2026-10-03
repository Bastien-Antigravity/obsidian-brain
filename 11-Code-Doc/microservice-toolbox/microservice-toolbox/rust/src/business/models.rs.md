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
Automatically generated mirror for `microservice-toolbox/rust/src/business/models.rs`.

> **Essential Process**:
> Defines standard market data domain models (MarketEvent, OHLCV, Signal) across the fleet.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Aggressor]] (enum: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|MarketEventType]] (enum: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|MarketEvent]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|OHLCV]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|OrderBookLevel]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|OrderBook]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Quote]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|SignalType]] (enum: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Signal]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Trade]] (struct: belongs_to)
<!-- SYNC:END -->
