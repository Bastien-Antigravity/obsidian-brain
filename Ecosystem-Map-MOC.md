---
microservice: ecosystem-core
type: moc
status: active
author: Ruzava & Antigravity
---

# 🌌 Bastien-Antigravity: Master Knowledge Hub (MOC)

Welcome to the central Map of Content (MOC) for the ecosystem. This serves as the root node of our Obsidian Brain, governing the architecture, standards, and workflows.

## 🌌 01 - Strategic Nexus
The "Strategic Oracle" that analyzes history, patterns, and project blind spots.
- **[[01-Strategic-Nexus/STRAT-001-The-Dormant-Pipeline|👁️ Current Strategic Audit]]**
- **[[01-Strategic-Nexus/Strategic-Patterns|🧩 Strategic Patterns]]**
- **[[01-Strategic-Nexus/Anti-Backlog|🚫 The Anti-Backlog]]**
- **[[07-Core-KMS/Role-Prompts/00-Oracle/Prompt-Chronos-Nexus|🛰️ Role 00: Chronos-Nexus]]**

## 🤖 00 - AI Orchestration
These define the generic "Team of Agents" architecture, workflows, and prompts for the AI.
- [[Workflow-Idea-to-Exploitation|Pipeline: Idea to Exploitation]]
- [[Daily-AI-Playbook|📖 Daily AI Playbook (Workflow)]]
- [[Git-Branching-Rules|AI Workflow & Git Branching]]
- [[00-Knowledge-Management-Playbook|📐 Knowledge Management Playbook (5D Paradigm)]]
- [[00-Obsidian-App-Config|⚙️ Obsidian App Configuration Guide]]
- [[00-Knowledge-Strategy|🛡️ AI Governance & Knowledge Strategy]]
- [[07-Core-KMS/Role-Prompts/09-Sentinel/Prompt-Sentinel|🛡️ Role 09: Sentinel (Integrity Auditor)]]
- [[10-State-and-Tasks/Inbox/Template-00-Idea-Pitch|📥 Task Inbox]]
- [[Sprint-Dashboard|⚡ Live Sprint Dashboard]]
- [[Domain-Dashboard|🌐 Domain Ontology Matrix]]

## 👔 02 - Business BDD
Behavior-Driven Development specifications, Domain-Driven Design glossary, and Acceptance Criteria. **(Zone 1: Frozen)**
- [[00-Glossary|📘 Domain Glossary (Ubiquitous Language)]]
- [[02-Business-BDD/User-Manual|📖 BDD Brain User Manual]]
- [[Connection-Lifecycle|🔌 SafeSocket Connection Lifecycle (Example Spec)]]

## 🚀 03 - Rapid Prototyping
Fast-path development, experiments, and prototypes. **(Zone 2: Fluid)**
- [[04-Rapid-Prototyping/README|🧪 Labs Overview]]

## 🛰️ 04 - Fleet Operations
Fleet-wide action plans, deployment logs, and migration states. **(Zone 3: Fleet)**
- [[05-Fleet-Operation/README|Fleet Operations (Zone 3)]]
- **Command Center**: [[05-Fleet-Operation/00-Repo-Control/inventory.json|Global Repo Registry]]
- **Automation**: `fleet-manager.py` (Mass Sync & Audit)
- **Logs**: [[05-Fleet-Operation/02-Deployment-Logs/README|Deployment History]]

## 📐 05 - Tech Stack (Architecture)
The structural paradigms for all polyglot microservices.
- [[Global-Architecture-Rules|The System Hub (Primary Rules)]]
- [[Ecosystem-Topology.canvas|🎨 Visual Ecosystem Topology]]
- [[01-Facade-Pattern|The Facade Pattern Rules]]
- [[02-Decoupling-and-Interfaces|Decoupling & Interfaces]]
- [[03-Repository-Structure|Repository Layouts]]
- [[04-Process-Lifecycle|Process Lifecycle]]
- [[05-Microservice-Map|Ecosystem Map]]
- [[06-Transverse-Event-Flows|🌀 Transverse Event Flows]]
- [[07-Configuration-Standard|Configuration Standard]]
- [[08-Networking-Protocols|Networking Protocols]]
- [[09-Log-Server-Architecture|Log-Server Architecture]]
- [[10-Testing-Sandbox-Standards|Testing & Sandbox Standards]]

## 📜 Architecture Decision Records (ADRs)
The historical ledger of ecosystem-wide technical decisions.
- [[ADR-001-Safe-Socket-Protocol|ADR-001: Safe-Socket Custom TCP Protocol]]

## 📚 05 - Tech Stack (Coding)
Idioms, standards, and our shared toolbox.
- [[00-Coding-Style-Guide|🎨 Coding Style Guide (MOC)]]
- [[01-General-Naming-Conventions|General Naming Conventions]]
- [[02-Go-Memory-and-Concurrency|Go Memory and Concurrency]]
- [[03-Rust-Safety-and-Async|Rust Safety and Async]]
- [[04-Python-Types-and-Structure|Python Types and Structure]]
- [[Documentation-Requirements|Documentation Requirements]]
- [[Core-Libraries-and-Toolbox|Core Libraries & Toolbox]]

## 🚀 05 - Tech Stack (Deployment)
How we get our code to production.
- [[01-Docker-Infrastructure|Docker Infrastructure]]
- [[02-Environment-Variables|Environment Variables]]
- [[03-Health-Checks|Health Checks]]
- [[04-CICD-and-Lifecycle|CI/CD and Lifecycle]]

## 🧬 05 - Tech Stack (Scripts)
Scripts that string the ecosystem together.
- [[03-Tech-Stack/05-Project-Scripts/Build-Wrapper.py|Modular Build Wrapper]] *(Legacy — use `cargo build` / `go build` directly)*
- [[03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py|Multi-repo Validator]]

## 🧠 05 - Tech Stack (Role Wisdom)
The historical knowledge and best practices for each AI role.
- [[03-Tech-Stack/06-Role-Wisdom/Architect/|Architect Wisdom]]
- [[03-Tech-Stack/06-Role-Wisdom/Developer/|Developer Wisdom]]
- [[03-Tech-Stack/06-Role-Wisdom/QA/|QA Wisdom]]
- [[03-Tech-Stack/06-Role-Wisdom/Purger/|Purger Wisdom]]

## 🌐 06 - Microservices
Live documentation and operational hubs for the service fleet.
- **[[Config-Server-Hub|🌐 Config-Server Hub]]** (Go)
- **[[Log-Server-Hub|🌐 Log-Server Hub]]** (Rust)
- **[[Notif-Server-Hub|🌐 Notif-Server Hub]]** (Go)
- **[[Safe-Socket-Hub|🌐 Safe-Socket Hub]]** (Go/SHM)
- **[[Distributed-Config-Hub|🌐 Distributed-Config Hub]]** (Go/Polyglot)
- **[[Market-Observer-Hub|🌐 Market-Observer Hub]]** (Go)
- **[[Data-Ingestor-Hub|🌐 Data-Ingestor Hub]]** (Go)
- **[[Fundamental-Analysis-Hub|🌐 Fundamental-Analysis Hub]]** (Python)
- [[microservice-toolbox/README.md|Microservice-Toolbox]]
- [[flexible-logger/README.md|Flexible-Logger]]
- [[universal-logger/README.md|Universal-Logger]]

> [!info]- 📊 Live Microservices List
> ```dataview
> table language as "Language", status as "Status"
> from ""
> where type = "repository"
> sort microservice asc
> ```

---
## 🧪 Quality & Testing
Quality Assurance follows a two-layer architecture:
1. **Definition Layer** (`02-Business-BDD`): Behavior specs written in markdown BDD format (Given/When/Then).
2. **Execution Layer** (`sandbox-testing`): Automated test scenarios that validate the behavior specs against real infrastructure.

The flow is: `02-Business-BDD` (WHAT) → `sandbox-testing` (HOW) → microservice (CODE).

---
> [!info]- ⚙️ Quick Global Query
> *(Note: You need the Dataview plugin active to see this)*
> ```dataview
> table status, type
> from ""
> where type = "moc" or type = "architecture"
> sort file.name asc
> ```
