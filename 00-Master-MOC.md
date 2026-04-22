---
microservice: ecosystem-core
type: moc
status: active
author: Ruzava & Antigravity
---

# 🌌 Bastien-Antigravity: Master Knowledge Hub (MOC)

Welcome to the central Map of Content (MOC) for the ecosystem. This serves as the root node of our Obsidian Brain, governing the architecture, standards, and workflows.

## 🤖 01 - AI Assistant & System Hub
These define how I (Antigravity) and other assistants must operate and behave.
- [[AI-System-Rules|The System Hub (Primary Prompt)]]
- [[AI-Workflow-and-Branching|AI Workflow & Git Branching]]
- [[00-Daily-AI-Playbook|📖 Daily AI Playbook (Workflow)]]
- [[00-Knowledge-Management-Playbook|📐 Knowledge Management Playbook (5D Paradigm)]]
- [[00-Obsidian-App-Config|⚙️ Obsidian App Configuration Guide]]
- [[01-AI-Assistant/Inbox/Legacy-Tasks|📥 Task Inbox]]
- [[Sprint-Dashboard|⚡ Live Sprint Dashboard]]
- [[Domain-Dashboard|🌐 Domain Ontology Matrix]]

## 📐 02 - Architecture & Design
The structural paradigms for all polyglot microservices.
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

## 📚 03 - Coding & Libraries
Idioms, standards, and our shared toolbox.
- [[00-Coding-Style-Guide|🎨 Coding Style Guide (MOC)]]
- [[01-General-Naming-Conventions|General Naming Conventions]]
- [[02-Go-Memory-and-Concurrency|Go Memory and Concurrency]]
- [[03-Rust-Safety-and-Async|Rust Safety and Async]]
- [[04-Python-Types-and-Structure|Python Types and Structure]]
- [[Documentation-Requirements|Documentation Requirements]]
- [[Core-Libraries-and-Toolbox|Core Libraries & Toolbox]]

## 🚀 04 - Deployment
How we get our code to production.
- [[01-Docker-Infrastructure|Docker Infrastructure]]
- [[02-Environment-Variables|Environment Variables]]
- [[03-Health-Checks|Health Checks]]
- [[04-CICD-and-Lifecycle|CI/CD and Lifecycle]]

## 🧬 05 - Automation Scripts
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
Quality Assurance is centralized down in the `sandbox-testing` microservice repo. We will eventually link test scenarios here natively.
Always request native behavior specs, and we will translate them into Docker/Native execution!

---
> [!info]- ⚙️ Quick Global Query
> *(Note: You need the Dataview plugin active to see this)*
> ```dataview
> table status, type
> from ""
> where type = "moc" or type = "architecture"
> sort file.name asc
> ```
