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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/business/helpers.py`.

> **Essential Process**:
> Provides serialization and deserialization utilities for business models. Includes custom JSON encoding for dataclasses, enums, and byte arrays to ensure ecosystem-wide data parity.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|MarketEventType]] (class: calls) — *Standard identifiers for different types of market data events.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|MarketEvent]] (class: calls) — *The primary envelope for all real-time market data across the fleet.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|models.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|BusinessEncoder]] (class: belongs_to) — *JSON encoder that handles dataclasses, enums, and byte arrays.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|default]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|deserialize]] (function: belongs_to) — *Converts a JSON byte array back into a business object or dataclass.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|serialize]] (function: belongs_to) — *Converts a business object into a JSON byte array.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|system_timestamp]] (function: belongs_to) — *Returns the current unix timestamp in milliseconds.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|wrap_market_event]] (function: belongs_to) — *Creates a MarketEvent envelope for a payload.*
<!-- SYNC:END -->
