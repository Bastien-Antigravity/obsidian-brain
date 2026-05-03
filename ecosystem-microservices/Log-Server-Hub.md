---
microservice: log-server
type: service-hub
status: active
---
# 🌐 Service Hub: Log-Server

*High-Performance ordered logging and rotation engine.*

## 🔗 Knowledge Map
- **Code Repository**: [[log-server/README.md|📂 log-server/]]
- **Behavior Specs**: [[business-bdd-brain/02-Behavior-Specs/log-server/|📜 BDD Specifications]]
- **Protocols**: [[log-server/capnp/logger.capnp|📄 Cap'n Proto Schema]]

## 🛠️ Squad Assignment
- **Lead Developer**: [[Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[Rust-Safety-Specialist|Rust-Safety]]
- **Systems Specialist**: [[CPP-Low-Latency-Specialist|CPP-Low-Latency]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "business-bdd-brain/02-Behavior-Specs/log-server"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```
