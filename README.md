# Bastien-Antigravity: Knowledge Hub

Welcome to the central knowledge repository for the Bastien-Antigravity ecosystem. This directory contains the modular "Source of Truth" documents that govern the architecture, coding standards, and operational workflows of our polyglot microservices platform.

## 🧭 Navigation Guide

Refer to the documents below for specific technical standards:

| Document | Purpose |
|---|---|
| [**System Hub**](bastien_antigravity_rules.md) | The primary AI system prompt and overview of all core pillars. |
| [**Architecture**](bastien_architecture.md) | Standards for the Facade pattern, Decoupling, and Component Organization. |
| [**AI Workflow**](bastien_ai_workflow.md) | Branching rules (`develop` -> `main`), Commit standards, and Testing requirements. |
| [**Coding Style**](bastien_coding_style.md) | Idioms for Go, Rust, and Python. Naming conventions (`IInterface`, `MModel`). |
| [**Libraries**](bastien_libraries.md) | Reference for `microservice-toolbox`, `universal-logger`, and `safe-socket`. |
| [**Networking**](bastien_networking.md) | gRPC control protocols, NATS bus, and WebSocket publishing. |
| [**Deployment**](bastien_deployment.md) | YAML standards, Profile management, and Docker Guard rules. |
| [**Documentation**](bastien_documentation.md) | ASCII topology diagrams and ARCHITECTURE.md requirements. |

---

## 🛠️ Operational Tools

This directory also houses the central automation scripts used to maintain the ecosystem:

*   [`bastien_make.py`](bastien_make.py): Modular build/test wrapper for individual repositories.
*   [`bastien_orchestrator.py`](bastien_orchestrator.py): High-level multi-repo builder used for workspace-wide validation.

---

## 🧪 Testing Excellence

Quality Assurance is centralized in the [**sandbox-testing**](../sandbox-testing/README.md) repository. 

### AI-Driven Scenarios
The AI assistant is trained to generate "Behavioral Specs" natively in the sandbox. To use this feature, simply request a scenario (e.g., *"Antigravity, generate a stress-test for the notif-server gRPC lifecycle"*).

Available testing modes:
*   **Native Mode**: Direct execution of local binaries.
*   **Docker Mode**: containerized orchestration via Docker Compose.
