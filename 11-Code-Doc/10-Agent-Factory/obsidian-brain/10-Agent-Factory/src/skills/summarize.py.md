---
source: obsidian-brain/10-Agent-Factory/src/skills/summarize.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.789244
---

# Mirror: summarize.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/skills/summarize.py`.

> **Essential Process**:
> Implements a naive summarizer that extracts the first sentence from each search result. The skill is deliberately simple so that the end-to-end demo stays lightweight.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|info]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|interfaces.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/skill.py.md|Skill]] (class: calls) — *Strategy-pattern contract. Each skill is a single, atomic action.*

### 🔌 Consumers (Inbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|SummarizerSkill]] (class: belongs_to) — *Simple extractive summarizer used in the demo squad.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|__init__]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|run]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
