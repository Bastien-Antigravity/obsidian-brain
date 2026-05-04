---
microservice: data-ingestor
type: service-hub
status: active
---
# 🌐 Service Hub: Data-Ingestor

*Pipeline for high-volume data transformation and storage.*

## 🔗 Knowledge Map
- **Code Repository**: [[data-ingestor/README.md|📂 data-ingestor/]]
- **Behavior Specs**: [[02-Business-BDD/02-Behavior-Specs/data-ingestor/|📜 BDD Specifications]]

## 🛠️ Squad Assignment
- **Lead Developer**: [[Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[Go-Systems-Specialist|Go-Systems]]
- **Data Specialist**: [[Timescale-Data-Specialist|Timescale-Data]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/data-ingestor"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[AI-Session-State|Restore Session State]]*
