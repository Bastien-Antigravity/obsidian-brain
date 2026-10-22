---
source: obsidian-brain/10-Agent-Factory/src/safety/safety.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.769869
---

# Mirror: safety.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/safety/safety.py`.

> **Essential Process**:
> Provides a thin wrapper that validates LLM output against a JSON-based policy. The wrapper is *decorator-style* but is used explicitly for clarity.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|error]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|interfaces.py]] (imports)

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|SafetyVerifier]] (class: belongs_to) — *Enforces a simple term-blacklist policy on LLM outputs.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|__init__]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|check]] (function: belongs_to) — *Raise `ValueError` if a prohibited term is present.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
