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
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp`.

> **Essential Process**:
> Defines canonical market domain models (MarketEvent, Trade, Quote, OrderBook, OHLCV, Signal) and Base64-compatible JSON serialization helpers across C++17.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.to_json]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|AggressorFromString]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Base64CharVal]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Base64Decode]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Base64Encode]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Deserialize]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MICROSERVICE_TOOLBOX_BUSINESS_MODELS_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_BUSINESS_MODELS_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEventTypeFromString]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|MarketEvent]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OHLCV]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBookLevel]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|OrderBook]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Quote]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Serialize]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|SignalTypeFromString]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Signal]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|SystemTimestamp]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|Trade]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|WrapMarketEvent]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|deserialize]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|from_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|serialize]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|system_timestamp]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|to_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|to_string]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/business/Models.hpp.md|wrap_market_event]] (function: belongs_to)
<!-- SYNC:END -->
