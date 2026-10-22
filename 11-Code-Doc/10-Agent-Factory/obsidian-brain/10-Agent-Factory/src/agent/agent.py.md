---
source: obsidian-brain/10-Agent-Factory/src/agent/agent.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.758431
---

# Mirror: agent.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/agent/agent.py`.

> **Essential Process**:
> Core runtime object that represents a single autonomous LLM-driven agent. It glues together Identity, Memory, Planner, SafetyVerifier, and logging.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/identity/identity.py.md|ImmutableIdentity]] (class: calls) — *Concrete, immutable implementation of `Identity`.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/identity/identity.py.md|identity.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|info]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|interfaces.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|ShortTermMemory]] (class: calls) — *Concrete ShortTermMemory implementation of the MemoryStore contract.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|add]] (function: calls) — *Appends a new turn to the short-term buffer.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|memory.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|PromptPlanner]] (class: calls) — *Concrete `Planner` that uses a Jinja2 system-prompt template*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|planner.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|think]] (function: calls) — *Orchestrate the LLM workflow and dispatch the chosen skill.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|SafetyVerifier]] (class: calls) — *Enforces a simple term-blacklist policy on LLM outputs.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|check]] (function: calls) — *Raise `ValueError` if a prohibited term is present.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|safety.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|SummarizerSkill]] (class: calls) — *Simple extractive summarizer used in the demo squad.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|summarize.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/web_search.py.md|WebSearchSkill]] (class: calls) — *Strategy implementation that queries a web search service.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/web_search.py.md|web_search.py]] (imports)

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|Agent]] (class: belongs_to) — *Concrete, reusable agent instance.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|__init__]] (function: belongs_to) — *Construct the full stack from a JSON-compatible configuration.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|chat]] (function: belongs_to) — *Public façade – the only method a caller should invoke.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/facade/squad_facade.py.md|squad_facade.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|factory.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|factory.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
