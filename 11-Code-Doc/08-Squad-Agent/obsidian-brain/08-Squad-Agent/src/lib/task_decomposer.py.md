---
source: obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-18T05:33:56.916317
---

# Mirror: task_decomposer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py`.

> **Essential Process**:
> TaskDecomposer — Deterministic Complexity Gate and Micro-Task Splitter for the AI Squad. Evaluates incoming user prompts across blast radius (file count), architectural layer span, polyglot scope, and action density to prevent context drift on fast models (e.g., gemini-3.8-flash).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py.md|TaskDecomposer]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py.md|decompose_request]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py.md|evaluate_complexity]] (function: belongs_to) — *Computes a deterministic complexity breakdown for a user request.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/task_decomposer.py.md|format_execution_plan]] (function: belongs_to) — *Formats the decomposition result as an actionable markdown directive for the LLM context.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
