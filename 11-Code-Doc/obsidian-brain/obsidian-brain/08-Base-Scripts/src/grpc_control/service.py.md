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
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/grpc_control/service.py`.

> **Essential Process**:
> Exposes the SquadControlService gRPC endpoints. Allows external clients to run subcommands, get status, switch modes, and get the active mode.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|run_subcommand_async]] (function: calls) — *Triggers a subcommand in a non-blocking background task.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|SquadControlServiceServicer]] (class: calls) — *Missing associated documentation comment in .proto file.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|add_SquadControlServiceServicer_to_server]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|squad_control_pb2_grpc.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|GetActiveMode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|GetStatus]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|RunCommand]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|SquadControlServiceImpl]] (class: belongs_to) — *Servicer implementation for gRPC Squad Control.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|SwitchMode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|get_grpc_server]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|start_grpc_server]] (function: belongs_to) — *Initializes and starts the asynchronous Squad Control gRPC server.*
<!-- SYNC:END -->
