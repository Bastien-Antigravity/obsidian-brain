---
source: obsidian-brain/10-Agent-Factory/src/planner/planner.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.665762
---

# Mirror: planner.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/planner/planner.py`.

> **Essential Process**:
> Planner -> LLM -> Skill dispatch. It builds a system prompt from the agent’s identity and memory, makes a (fake) LLM call, parses the structured JSON response, and invokes the appropriate skill.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|info]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|interfaces.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/planner.py.md|Planner]] (class: calls) — *Orchestrator that decides which `Skill` to invoke.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|retrieve]] (function: calls) — *Retrieves history. For simplicity, returns the entire active buffer.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/utils/utils.py.md|utils.py]] (imports)

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|PromptPlanner]] (class: belongs_to) — *Concrete `Planner` that uses a Jinja2 system-prompt template*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|__init__]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|_fake_llm_call]] (function: belongs_to) — *A deterministic stand-in for an LLM that is capability-aware.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|_render_prompt]] (function: belongs_to) — *Render the system prompt using the Jinja2 template.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|think]] (function: belongs_to) — *Orchestrate the LLM workflow and dispatch the chosen skill.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
