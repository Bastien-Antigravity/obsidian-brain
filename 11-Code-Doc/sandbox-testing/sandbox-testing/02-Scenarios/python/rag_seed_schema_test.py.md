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
Automatically generated mirror for `sandbox-testing/02-Scenarios/python/rag_seed_schema_test.py`.

> **Essential Process**:
> Validates that: 1. PostgreSQL database tables reside strictly in schema "09-RAG-Engine" and public contains zero data tables. 2. Seed export (export-seed) produces valid manifest and compressed jsonl dataset. 3. Secret & local host path sanitization filter redacts sensitive tokens and absolute paths. 4. Seed import (import-seed --reset) restores database tables cleanly. 5. Post-import vector similarity search executes successfully against pgvector.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|execute]] (function: calls)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_seed_schema_test.py.md|RAG_ENGINE_DIR]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_seed_schema_test.py.md|SANDBOX_DIR]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_seed_schema_test.py.md|TEST_DIR]] (constant: belongs_to) — *Add 09-RAG-Engine to python path*
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_seed_schema_test.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_seed_schema_test.py.md|run_scenario_tests]] (function: belongs_to)
<!-- SYNC:END -->
