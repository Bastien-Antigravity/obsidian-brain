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
Automatically generated mirror for `web-interface/src/fundamental_analysis/fundamental_analysis.go`.

> **Essential Process**:
> Retrieves and processes fundamental stock analysis metrics from PostgreSQL. Ranks equities by valuation, growth, profitability, and overall scoring models.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|ConnectStockDatabase]] (function: belongs_to) — *ConnectStockDatabase initializes the database connection for financial analysis.*
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|FormData]] (struct: belongs_to) — *FormData holds view-level stock collections.*
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|GetTopStocks]] (function: belongs_to) — *GetTopStocks fetches top stocks from the specified table ordered by overall score.*
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|Stock]] (struct: belongs_to) — *Stock model represents an equity asset with fundamental analysis indicators.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
<!-- SYNC:END -->
