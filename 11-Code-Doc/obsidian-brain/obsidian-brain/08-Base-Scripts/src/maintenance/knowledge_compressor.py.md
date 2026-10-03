---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py`.

> **Essential Process**:
> Knowledge Compressor and Context Distiller for the Bastien-Antigravity ecosystem. Automates distillation of active session state logs into fresh architectural decision patterns, ensuring AI session context remains compact and actionable.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|ensure_frontmatter.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/clients/discord_client.py.md|discord_client.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/build_inventory.py.md|build_inventory.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|fleet_commander.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|fleet_refresh.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|KnowledgeCompressor]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|distill_to_pattern]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|extract_recent_sessions]] (function: belongs_to) — *Extracts the last N sessions from AI-Session-State.md.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|run]] (function: belongs_to)
<!-- SYNC:END -->
