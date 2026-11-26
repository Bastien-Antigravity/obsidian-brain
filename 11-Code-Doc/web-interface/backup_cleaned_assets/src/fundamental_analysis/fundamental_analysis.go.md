---
source: web-interface/backup_cleaned_assets/src/fundamental_analysis/fundamental_analysis.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.577376
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: fundamental_analysis.go

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/src/fundamental_analysis/fundamental_analysis.go`.

> **Essential Process**:
> Retrieves and processes fundamental stock analysis metrics from PostgreSQL. Ranks equities by valuation, growth, profitability, and overall scoring models.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/src/fundamental_analysis/fundamental_analysis.go.md|ConnectStockDatabase]] (function: belongs_to) — *the service schema exists.*
- [[web-interface/web-interface/backup_cleaned_assets/src/fundamental_analysis/fundamental_analysis.go.md|FormData]] (struct: belongs_to) — *FormData holds view-level stock collections.*
- [[web-interface/web-interface/backup_cleaned_assets/src/fundamental_analysis/fundamental_analysis.go.md|GetTopStocks]] (function: belongs_to) — *GetTopStocks fetches top stocks from the specified table ordered by overall score.*
- [[web-interface/web-interface/backup_cleaned_assets/src/fundamental_analysis/fundamental_analysis.go.md|Stock]] (struct: belongs_to) — *Stock model represents an equity asset with fundamental analysis indicators.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
