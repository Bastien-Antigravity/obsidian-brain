--- 
microservice: web-interface
type: service-hub
status: active
tags:
- '#type/service-hub'
- '#state/active'
---
# 🌐 Service Hub: Web-Interface

*Unified Fleet Dashboard: Vue.js / Tailwind Frontend.*

## 🔗 Knowledge Map
- **Code Repository**: [[web-interface/README.md|📂 web-interface/]]
- **Integration Protocol**: [[Web-Interface-Integration-Protocol|📜 Integration Rules]]
- **Live State**: Connects to Log-Server and Market-Observer.

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Vue-Frontend-Specialist|Vue-Frontend]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/web-interface"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```
