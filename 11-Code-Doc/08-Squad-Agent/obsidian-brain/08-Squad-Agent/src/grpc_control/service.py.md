---
source: obsidian-brain/08-Squad-Agent/src/grpc_control/service.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.619900
---

# Mirror: service.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/grpc_control/service.py`.

> **Essential Process**:
> Exposes the SquadControlService gRPC endpoints. Allows external clients to run subcommands, get status, switch modes, and get the active mode.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|run_subcommand_async]] (function: calls) — *Triggers a subcommand in a non-blocking background task.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/squad_control_pb2_grpc.py.md|SquadControlServiceServicer]] (class: calls) — *Missing associated documentation comment in .proto file.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/squad_control_pb2_grpc.py.md|add_SquadControlServiceServicer_to_server]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/squad_control_pb2_grpc.py.md|squad_control_pb2_grpc.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|GetActiveMode]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|GetStatus]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|RunCommand]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|SquadControlServiceImpl]] (class: belongs_to) — *Servicer implementation for gRPC Squad Control.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|SwitchMode]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|get_grpc_server]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|start_grpc_server]] (function: belongs_to) — *Initializes and starts the asynchronous Squad Control gRPC server.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
