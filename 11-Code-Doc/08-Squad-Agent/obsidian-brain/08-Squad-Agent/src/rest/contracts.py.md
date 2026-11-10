---
source: obsidian-brain/08-Squad-Agent/src/rest/contracts.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:49.742819
---

# Mirror: contracts.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/rest/contracts.py`.

> **Essential Process**:
> Builds authoritative, runtime-introspected Exchange Contracts for squad-agent across FastAPI REST & SSE endpoints, gRPC SquadControlService, NATS Event Bus chat/incident topics, and PostgreSQL conversation memory tables.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|ContractOperation]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|ContractPeer]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|ExchangeContract]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|_SQUAD_PROTO_PATH]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|_SQUAD_ROOT]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|_SQUAD_SQL_DDL]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|build_contracts_envelope]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|build_squad_agent_contracts]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|display_address]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|extract_fastapi_operations]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|extract_proto_operations]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|read_schema_file]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|resolve_contract_port]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/contracts.py.md|to_dict]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|server.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|server.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
