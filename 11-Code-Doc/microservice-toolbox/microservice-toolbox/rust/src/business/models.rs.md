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

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/business/models.rs`.

> **Essential Process**:
> Defines standard market data domain models (MarketEvent, OHLCV, Signal) across the fleet.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.expecting]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_byte_buf]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_bytes]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_seq]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_str]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|helpers.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|loader.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/facade.py.md|facade.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/notification/client.py.md|client.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/providers.py.md|providers.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|spec.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|wiretap.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/helpers.rs.md|helpers.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/helpers.rs.md|helpers.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/helpers.rs.md|helpers.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Aggressor]] (enum: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|B64_TABLE]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|MarketEventType]] (enum: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|MarketEvent]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|OHLCV]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|OrderBookLevel]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|OrderBook]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.expecting]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_byte_buf]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_bytes]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_seq]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor.visit_str]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|PayloadVisitor]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Quote]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|SignalType]] (enum: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Signal]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|Trade]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|decode]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|deserialize]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|encode]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|serialize]] (function: belongs_to)
<!-- SYNC:END -->
