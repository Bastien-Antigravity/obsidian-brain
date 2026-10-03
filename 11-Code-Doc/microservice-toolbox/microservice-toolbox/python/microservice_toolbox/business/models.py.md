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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/business/models.py`.

> **Essential Process**:
> Defines the core data structures and enums for the microservice ecosystem. Enforces a standardized schema for Market Events, Trades, Quotes, and OHLCV data to ensure cross-language compatibility between Python, Go, and Rust.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|BotCommand_CommandType.Enum]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|helpers.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|helpers.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/helpers.py.md|helpers.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Aggressor]] (class: belongs_to) — *Indicates which side initiated the trade (taker side).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|MarketEventType]] (class: belongs_to) — *Standard identifiers for different types of market data events.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|MarketEvent]] (class: belongs_to) — *The primary envelope for all real-time market data across the fleet.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|OHLCV]] (class: belongs_to) — *Standardized representation of a candlestick (Time-Series data).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|OrderBookLevel]] (class: belongs_to) — *A single price level in an order book.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|OrderBook]] (class: belongs_to) — *Standardized representation of a Limit Order Book (L2).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Quote]] (class: belongs_to) — *Standardized representation of a Top-of-Book (L1) quote.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|SignalType]] (class: belongs_to) — *Standard identifiers for trading signal directions.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Signal]] (class: belongs_to) — *Standardized structure for strategy-generated trading signals.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/business/models.py.md|Trade]] (class: belongs_to) — *Standardized representation of an individual trade execution.*
<!-- SYNC:END -->
