---
source: obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.503804
---

# Mirror: alignment.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py`.

> **Essential Process**:
> Defines the abstract interface for checking alignment between code and documentation.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|AlignmentService]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|check_alignment]] (function: belongs_to) — *Compares the current code content against the hash stored when docs were written to detect drift.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|get_all_drifted]] (function: belongs_to) — *Returns a list of all documentation notes that are currently out of sync with code.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|get_dead_links]] (function: belongs_to) — *Identifies links where the code chunk ID no longer exists in the system.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|get_drift_details]] (function: belongs_to) — *Returns details needed for a rewrite: current hash vs stored hash and linked docs.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|get_linked_code]] (function: belongs_to) — *Retrieves all code chunks linked to a specific Obsidian note.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|get_linked_docs]] (function: belongs_to) — *Retrieves all Obsidian documentation notes linked to a specific code chunk.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|register_link]] (function: belongs_to) — *Registers a bidirectional link between a code chunk and a documentation note.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|register_links_batch]] (function: belongs_to) — *Registers multiple links in a single database batch transaction. Each tuple is (code_id, doc_id, code_hash).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|reset_registry]] (function: belongs_to) — *Clears the alignment registry.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
