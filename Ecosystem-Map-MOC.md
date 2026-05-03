---
microservice: ecosystem-core
type: moc
status: active
author: Ruzava & Antigravity
---

# 🌌 Bastien-Antigravity: Master Knowledge Hub (MOC)

Welcome to the central Map of Content (MOC) for the ecosystem. This serves as the root node of our Obsidian Brain, governing the architecture, standards, and workflows.

## 🌌 00 - The Chronos-Nexus (Meta-Brain)
The "Strategic Oracle" that analyzes history, patterns, and project blind spots.
- **[[nexus-strategic-brain/STRAT-001-The-Dormant-Pipeline|👁️ Current Strategic Audit]]**
- **[[core-kms-brain/Role-Prompts/00-Oracle/Prompt-Chronos-Nexus|🛰️ Role 00: Chronos-Nexus]]**

## 🤖 01 - AI Engine
These define the generic "Team of Agents" architecture, workflows, and prompts for the AI.
- [[Workflow-Idea-to-Exploitation|Pipeline: Idea to Exploitation]]
- [[Daily-AI-Playbook|📖 Daily AI Playbook (Workflow)]]
- [[Git-Branching-Rules|AI Workflow & Git Branching]]
- [[00-Knowledge-Management-Playbook|📐 Knowledge Management Playbook (5D Paradigm)]]
- [[00-Obsidian-App-Config|⚙️ Obsidian App Configuration Guide]]
- [[00-Knowledge-Strategy|🛡️ AI Governance & Knowledge Strategy]]
- [[core-kms-brain/Role-Prompts/09-Sentinel/Prompt-Sentinel|🛡️ Role 09: Sentinel (Integrity Auditor)]]
- [[state-and-tasks/Inbox/Template-00-Idea-Pitch|📥 Task Inbox]]
- [[Sprint-Dashboard|⚡ Live Sprint Dashboard]]
- [[Domain-Dashboard|🌐 Domain Ontology Matrix]]

## 👔 01 - Project Business (Specifications Brain)
Behavior-Driven Development specifications, Domain-Driven Design glossary, and Acceptance Criteria. **(Zone 1: Frozen)**
- [[00-Glossary|📘 Domain Glossary (Ubiquitous Language)]]
- [[business-bdd-brain/User-Manual|📖 BDD Brain User Manual]]
- [[Connection-Lifecycle|🔌 SafeSocket Connection Lifecycle (Example Spec)]]

## 🚀 02 - Experimental Labs (Rapid Prototyping)
Fast-path development, experiments, and prototypes. **(Zone 2: Fluid)**
- [[rapid-prototyping-brain/README|🧪 Labs Overview]]

## 🛰️ 03 - Fleet Operations (Management Brain)
Fleet-wide action plans, deployment logs, and migration states. **(Zone 3: Fleet)**
- [[fleet-operation-brain/README|Fleet Operations (Zone 3)]]
- **Command Center**: [[fleet-operation-brain/00-Repo-Control/inventory.json|Global Repo Registry]]
- **Automation**: `fleet-manager.py` (Mass Sync & Audit)
- **Logs**: [[fleet-operation-brain/02-Deployment-Logs/README|Deployment History]]

## 📐 04 - Project Architecture
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

## 📚 05 - Project Coding
Idioms, standards, and our shared toolbox.
- [[00-Coding-Style-Guide|🎨 Coding Style Guide (MOC)]]
- [[01-General-Naming-Conventions|General Naming Conventions]]
- [[02-Go-Memory-and-Concurrency|Go Memory and Concurrency]]
- [[03-Rust-Safety-and-Async|Rust Safety and Async]]
- [[04-Python-Types-and-Structure|Python Types and Structure]]
- [[Documentation-Requirements|Documentation Requirements]]
- [[Core-Libraries-and-Toolbox|Core Libraries & Toolbox]]

## 🚀 06 - Project Deployment
How we get our code to production.
- [[01-Docker-Infrastructure|Docker Infrastructure]]
- [[02-Environment-Variables|Environment Variables]]
- [[03-Health-Checks|Health Checks]]
- [[04-CICD-and-Lifecycle|CI/CD and Lifecycle]]

## 🧬 07 - Project Scripts
Scripts that string the ecosystem together.
- [[tech-stack-brain/05-Project-Scripts/Build-Wrapper.py|Modular Build Wrapper]]
- [[tech-stack-brain/05-Project-Scripts/Multi-Repo-Validator.py|Multi-repo Validator]]

## 🌐 08 - Ecosystem Microservices
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
