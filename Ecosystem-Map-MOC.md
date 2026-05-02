---
microservice: ecosystem-core
type: moc
status: active
author: Ruzava & Antigravity
---

# 🌌 Bastien-Antigravity: Master Knowledge Hub (MOC)

Welcome to the central Map of Content (MOC) for the ecosystem. This serves as the root node of our Obsidian Brain, governing the architecture, standards, and workflows.

## 🤖 00 - AI Engine
These define the generic "Team of Agents" architecture, workflows, and prompts for the AI.
- [[Workflow-Idea-to-Exploitation|Pipeline: Idea to Exploitation]]
- [[Daily-AI-Playbook|📖 Daily AI Playbook (Workflow)]]
- [[Git-Branching-Rules|AI Workflow & Git Branching]]
- [[00-Knowledge-Management-Playbook|📐 Knowledge Management Playbook (5D Paradigm)]]
- [[00-Obsidian-App-Config|⚙️ Obsidian App Configuration Guide]]
- [[00-Knowledge-Strategy|🛡️ AI Governance & Knowledge Strategy]]
- [[core-kms-brain/state-and-tasks/Inbox/Legacy-Tasks|📥 Task Inbox]]
- [[Sprint-Dashboard|⚡ Live Sprint Dashboard]]
- [[Domain-Dashboard|🌐 Domain Ontology Matrix]]

## 👔 01 - Project Business (BDD Brain)
Behavior-Driven Development specifications, Domain-Driven Design glossary, and Acceptance Criteria.
- [[00-Glossary|📘 Domain Glossary (Ubiquitous Language)]]
- [[business-bdd-brain/User-Manual|📖 BDD Brain User Manual]]
- [[Connection-Lifecycle|🔌 SafeSocket Connection Lifecycle (Example Spec)]]
- [[Template-Acceptance-Criteria|📋 Acceptance Criteria Template]]

## 📐 02 - Project Architecture
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

## 📜 Architecture Decision Records (ADRs)
The historical ledger of ecosystem-wide technical decisions.
- [[ADR-001-Safe-Socket-Protocol|ADR-001: Safe-Socket Custom TCP Protocol]]

## 📚 03 - Project Coding
Idioms, standards, and our shared toolbox.
- [[00-Coding-Style-Guide|🎨 Coding Style Guide (MOC)]]
- [[01-General-Naming-Conventions|General Naming Conventions]]
- [[02-Go-Memory-and-Concurrency|Go Memory and Concurrency]]
- [[03-Rust-Safety-and-Async|Rust Safety and Async]]
- [[04-Python-Types-and-Structure|Python Types and Structure]]
- [[Documentation-Requirements|Documentation Requirements]]
- [[Core-Libraries-and-Toolbox|Core Libraries & Toolbox]]

## 🚀 04 - Project Deployment
How we get our code to production.
- [[01-Docker-Infrastructure|Docker Infrastructure]]
- [[02-Environment-Variables|Environment Variables]]
- [[03-Health-Checks|Health Checks]]
- [[04-CICD-and-Lifecycle|CI/CD and Lifecycle]]

## 🧬 05 - Project Scripts
Scripts that string the ecosystem together.
- [[Build-Wrapper.py|Modular Build Wrapper]]
- [[Multi-Repo-Validator.py|Multi-repo Validator]]

## 🌐 06 - Ecosystem Microservices
Live documentation directly from the source code repositories.
- [[config-server/README.md|Config-Server]]
- [[log-server/README.md|Log-Server]]
- [[notif-server/README.md|Notif-Server]]
- [[safe-socket/README.md|Safe-Socket]]
- [[microservice-toolbox/README.md|Microservice-Toolbox]]
- [[flexible-logger/README.md|Flexible-Logger]]
- [[universal-logger/README.md|Universal-Logger]]
- [[distributed-config/README.md|Distributed-Config]]

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
1. **Definition Layer** (`business-bdd-brain`): Behavior specs written in markdown BDD format (Given/When/Then).
2. **Execution Layer** (`sandbox-testing`): Automated test scenarios that validate the behavior specs against real infrastructure.

The flow is: `business-bdd-brain` (WHAT) → `sandbox-testing` (HOW) → microservice (CODE).

---
> [!info]- ⚙️ Quick Global Query
> *(Note: You need the Dataview plugin active to see this)*
> ```dataview
> table status, type
> from ""
> where type = "moc" or type = "architecture"
> sort file.name asc
> ```
