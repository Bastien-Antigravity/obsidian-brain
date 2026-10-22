---
source: obsidian-brain/09-RAG-Engine/src/grpc_control/service.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.200891
---

# Mirror: service.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/grpc_control/service.py`.

> **Essential Process**:
> Exposes the RAGControlService gRPC endpoints. Allows external clients to request status, index files/directories, rebuild index, and sync docs.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/rag_control_pb2_grpc.py.md|RAGControlServiceServicer]] (class: calls) — *Missing associated documentation comment in .proto file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/rag_control_pb2_grpc.py.md|add_RAGControlServiceServicer_to_server]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/rag_control_pb2_grpc.py.md|rag_control_pb2_grpc.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|BuildIndex]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|GetBrainStats]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|GetStatus]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|IndexDirectory]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|IndexFile]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|RAGControlServiceImpl]] (class: belongs_to) — *Servicer implementation for gRPC RAG Control.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|ResetIndex]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|SyncDocs]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|start_grpc_server]] (function: belongs_to) — *Initializes and starts the asynchronous RAG Control gRPC server.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
