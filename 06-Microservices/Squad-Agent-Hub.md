---
microservice: squad-agent
type: service-hub
status: active
tags:
- '#service/squad-agent'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Squad-Agent (`08-Squad-Agent`)

*Autonomous polyglot AI Squad orchestrator managing cross-brain BDD specifications, code generation, AST compliance gates, and self-healing AutoRepair.*

## 🔗 Knowledge Map
- **Code Directory**: `obsidian-brain/08-Squad-Agent`
- **Behavior Specs**: `obsidian-brain/02-Business-BDD/02-Behavior-Specs/`
- **Protocols**: FastAPI REST & WebSocket (`8085`), gRPC Control (`8087`), OpenMFE (`<squad-agent-mfe>`), and `src/rest/contracts.py`

## 🛠️ Squad Assignment
- **Orchestrator**: [[07-Core-KMS/Role-Prompts/02-Orchestrator/Prompt-Orchestrator|Orchestrator]]
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[Python-Integration-Specialist|Python-Integration]]
- **Compliance Sentinels**: [[Prompt-Pattern-Sentinel|PatternSentinel]] & [[Prompt-Debloat-Sentinel|DebloatSentinel]]

## 🏗️ Architecture Decision Records (ADR)

### ADR-001: Zero-Mixing Domain Workspace Delegation
*   **Context**: Copying `08-Squad-Agent` and `03-Tech-Stack` into satellite domain brains caused prompt/auditor drift across ecosystems.
*   **Decision**: Standardize on a single central `08-Squad-Agent` orchestrator (`Bastien-Antigravity/obsidian-brain/08-Squad-Agent`) executing missions against registered Zero-Mixing Domain Workspaces (`<Domain>-Antigravity/`) via `target_brain_id` and `target_workspace_path`.
*   **Consequence**: Zero runtime duplication, atomic cross-brain port allocation, and guaranteed enforcement of the latest `ComplianceAuditor` and `microservice-toolbox` standards on every generated service.
