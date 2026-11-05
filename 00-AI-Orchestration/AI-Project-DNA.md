---
microservice: ecosystem-core
type: governance
status: active
tags:
- '#type/governance'
- '#state/active'
- '#zone/0-orchestration'
- '#service/ecosystem-core'
---
# 🧬 Project DNA: obsidian-brain

## 🎯 High-Level Intent (BDD)
- **Goal**: Serve as the "Global Memory" and "Strategic Command Center" for the entire Bastien-Antigravity ecosystem, housing all architectural decisions, sprint plans, and cross-repo knowledge.
- **Key Pattern**: **Atomic Knowledge** (Zettelkasten-style notes) and **Strategic MOCs** (Maps of Content for navigation).
- **Behavioral Source of Truth**: 02-Business-BDD/02-Behavior-Specs/obsidian-brain
- **Taxonomy Mandate**: Mandatory use of `#service/`, `#tech/`, `#tier/`, and `#zone/` tags for transversal concepts.
- **Isolation Protocol**: Human-centric documentation must reside in `quick-overview/` folders and carry the `#ai/ignore` tag.

## 🛠️ Role Specifics
- **FleetArchitect**: 
    - Maintain the integrity of the `Knowledge-Strategy.md` and `Ecosystem-Map-MOC.md`.
    - Ensure that submodules (`01-Strategic-Nexus`, `07-Core-KMS`, `03-Tech-Stack`, `02-Business-BDD`, `05-Fleet-Operation`, `04-Rapid-Prototyping`) are synchronized.
- **Orchestrator**: 
    - Act as the central "Pipeline Director."
    - Score task complexity (Fast-Track vs Standard) and route to downstream roles.
- **FleetCommander**: 
    - Manage the synchronization and deployment of the entire fleet.
    - Enforce compliance before all git pushes using `fleet-manager.py`.
- **DocMaintainer**:
    - Manage the **Isolation Protocol** and frontmatter integrity across the fleet.
    - Automate the injection of `#service/` tags.
- **Sentinel**: 
    - Run `Brain-Health-Audit.py` to verify link integrity and YAML compliance.
    - Audit the `AI-Session-State` consistency across repositories.
- **Purger**:
    - Periodically identify and remove legacy files, orphaned drafts, and technical debt.
- **Oracle (Chronos-Oracle)**:
    - Perform **Log-Driven Strategic Synthesis** by default at the start of every session.
    - Maintain the `01-Strategic-Nexus/` vault and the **Anti-Backlog**.
- **Developer**:
    - Follow the PARA/Diátaxis hybrid organizational system.
- **Architect**:
    - Design decoupled system interfaces and blueprints, performing Mode 1 design verification gates.
- **QA**:
    - Design BDD Gherkin test scenarios and sandbox execution skeletons before coding, verifying exit pass gates.
- **DocIndexer**:
    - Specialize in parsing, tokenizing, and indexing markdown files into the hybrid lexical/vector storage.
- **CodeIndexer**:
    - Specialize in AST-based code analysis, chunking, and code dependency index management.
- **PatternSentinel**:
    - Audit changes to enforce strict governance protocols, decoupling, and coding style standards.
- **MatryoshkaScripter**:
    - Specialize in creating self-contained, single-file Python tools (Matryoshka pattern) that embed their own dependencies.

## 📦 Engineering Standards
- **Matryoshka Python Scripts**: All Python tools and utilities meant for cross-environment execution must follow the "Matryoshka" pattern—single, self-contained files that include their own dependencies and can be executed without external installation or virtual environments.
    - **Self-containment**: The script must include its own code plus all third-party libraries it depends on, bundled into ONE file.
    - **Auto-callable**: Executable directly (`python script.py`) without prior `pip install`.
    - **No external files**: No separate `requirements.txt` or external modules required.
    - **PEP 723**: Use inline script metadata for modern Python environments to declare dependencies.
    - **Interpretable**: Scripts must remain as readable Python code (not binary executables).

## 🚦 Lifecycle & Versioning
- **Primary Branch**: `develop`
- **Protected Branches**: `main`
- **Versioning Strategy**: N/A (Continuous updates).
- **Version Source of Truth**: `VERSION.txt` (Set to `1.0.0` for tracking).

## 🛡️ Non-Negotiable Engineering Directives for AI Coding Assistants

### 1. Zero Production-for-Test Alterations
- **Principle**: Tests validate production code; production code does NOT bend to accommodate test fixtures.
- **Rule**: NEVER alter production or business logic to make a failing unit or integration test pass.
- **Action**: When a test fails due to out-of-date mock behavior, missing protocol handshakes (e.g., `tcp-hello` vs raw `tcp`), uninitialized mock buffers, or race conditions, update the **test fixture or mock**, never the production source.

### 2. Zero Defensive Boilerplate for Static Linters (e.g., `nilaway`)
- **Principle**: Production code must remain clean, concise, and focused on business value—not cluttered with defensive noise to silence linters.
- **Rule**: NEVER inject redundant `if x != nil` checks, fake zero-value fallbacks (e.g., `"unknown"`), or dummy structs (e.g., `&net.UDPAddr{}`) to satisfy static analyzers when variables are guaranteed safe by system architecture.

### 3. Exhaustive Architectural Reliance Invariants (Safe-By-Design Contracts)
Downstream services and application handlers MUST trust upstream framework guarantees and architectural invariants without defensive re-validation:
- **Configuration Framework (`microservice-toolbox/config`)**:
  - `AppConfig` and `Config` are validated and populated during initialization. If configuration loading fails, the service fails fast at boot. Downstream handlers can assume configuration structs are non-nil and valid.
  - Capability endpoints, IPs, and ports are resolved via `GetListenAddr` / `GetGRPCListenAddr` according to strict schema definitions.
- **Transport & Communication Frameworks (`safe-socket`, `gRPC`, `Cap'n Proto`)**:
  - **Handshake Validation**: `safe-socket` (`tcp-hello`, Unix domain, SHM) guarantees identity validation and connection viability before passing sockets to application handlers. Handshake metadata is structurally guaranteed.
  - **Schema Enforcement**: Protobuf and Cap'n Proto schemas strictly govern message formats across the wire. Payloads unpacked by generated decoders are structurally valid.
  - **Standard Library Contracts**: Trust standard language contracts (e.g., Go's `http.Client.Do` guarantees `resp != nil` when `err == nil`).
- **Orchestration & Supervision (`watchdog-agent`)**:
  - The supervisor enforces dependency DAGs: upstream dependencies (`log-server`, `config-server`) are confirmed listening and healthy before dependent services are started.
  - Reconnections and socket retries are managed by the connection layer (`conn_manager`); application handlers must not duplicate transport reconnection logic.

### 4. Mandatory Manual User Validation Gate
- **Rule**: NEVER execute `git commit` or apply modifications silently without presenting the exact changes to the human developer for manual review and explicit validation.
