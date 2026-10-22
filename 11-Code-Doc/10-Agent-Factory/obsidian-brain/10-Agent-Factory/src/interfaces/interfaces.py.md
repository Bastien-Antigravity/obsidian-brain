---
source: obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py
workspace: 10-Agent-Factory
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.853356
---

# Mirror: interfaces.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/identity.py.md|identity.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/planner.py.md|planner.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/skill.py.md|skill.py]] (imports)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|mfe.js]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|db_config.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/agent/agent.py.md|agent.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|factory.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/factory/factory.py.md|factory.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|Logger]] (class: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|critical]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|error]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|info]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|warning]] (function: belongs_to)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/memory/memory.py.md|memory.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|planner.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/planner/planner.py.md|planner.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|run_fleet.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/run_fleet.py.md|run_fleet.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|safety.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/safety/safety.py.md|safety.py]] (imports)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|summarize.py]] (calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/skills/summarize.py.md|summarize.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
