---
microservice: market-observer
type: service-hub
status: active
---
# 🌐 Service Hub: Market-Observer

*Real-time exchange connectivity and orderbook tracking.*

## 🔗 Knowledge Map
- **Code Repository**: [[market-observer/README.md|📂 market-observer/]]
- **Behavior Specs**: [[02-Business-BDD/02-Behavior-Specs/market-observer/|📜 BDD Specifications]]
- **Action Plan**: [[market-observer/TODO.md|📅 Local TODO]]

## 🛠️ Squad Assignment
- **Lead Developer**: [[Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[Go-Systems-Specialist|Go-Systems]]
- **Data Specialist**: [[Timescale-Data-Specialist|Timescale-Data]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/market-observer"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[AI-Session-State|Restore Session State]]*
