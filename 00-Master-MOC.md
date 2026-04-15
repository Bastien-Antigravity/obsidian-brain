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
- [[bastien_antigravity_rules|The System Hub (Primary Prompt)]]
- [[bastien_ai_workflow|AI Workflow & Git Branching]]
- [[Sprint-Dashboard|⚡ Live Sprint Dashboard]]

## 📐 02 - Architecture & Design
The structural paradigms for all polyglot microservices.
- [[Ecosystem-Topology.canvas|🎨 Visual Ecosystem Topology]]
- [[01-Facade-Pattern|The Facade Pattern Rules]]
- [[02-Decoupling-and-Interfaces|Decoupling & Interfaces]]
- [[03-Repository-Structure|Repository Layouts]]
- [[04-Process-Lifecycle|Process Lifecycle]]
- [[05-Microservice-Map|Ecosystem Map]]
- [[bastien_configuration|Configuration Standard]]
- [[bastien_networking|Networking Protocols]]

## 📚 03 - Coding & Libraries
Idioms, standards, and our shared toolbox.
- [[bastien_coding_style|Shared Coding Idioms]]
- [[bastien_documentation|Documentation Requirements]]
- [[bastien_libraries|Core Libraries & Toolbox]]

## 🚀 04 - Deployment
How we get our code to production.
- [[bastien_deployment|Deployment Strategies]]

## 🧬 05 - Automation Scripts
Scripts that string the ecosystem together.
- [[bastien_make.py|Modular Build Wrapper]]
- [[bastien_orchestrator.py|Multi-repo Validator]]

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
