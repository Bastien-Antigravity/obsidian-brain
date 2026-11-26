---
source: obsidian-brain/08-Squad-Agent/src/agents/qa.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.643498
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: qa.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/qa.py`.

> **Essential Process**:
> QA Engineer agent daemon specialized in verifying logic implementation, auditing unit tests, probing internal service health/contracts endpoints safely, and reporting verification reports.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|QAAgent]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|_ALLOWED_LOOPBACK_HOSTS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|_MAX_RESPONSE_BYTES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|_perform_http_probe]] (function: belongs_to) — *Executes the synchronous HTTP GET probe inside a worker thread.*
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|_validate_internal_probe_url]] (function: belongs_to) — *Enforces strict SSRF allowlist permitting only 127.0.0.1, 127.0.0.2, or single-label container DNS.*
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|execute_tool]] (function: belongs_to) — *Executes a function call requested by the model.*
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|probe_service_health]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|run_squad_tests]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
