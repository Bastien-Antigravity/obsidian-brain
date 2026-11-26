---
source: obsidian-brain/08-Squad-Agent/src/models/build_spec.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:04.259868
---

# Mirror: build_spec.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/models/build_spec.py`.

> **Essential Process**:
> Defines the canonical cross-brain MicroserviceBuildSpec contract and deterministic domain port allocator (18100-18999) so external domain brains can hand off structured feature and architecture specifications to 08-Squad-Agent with zero port collisions or rule drift. Failure Policy: Fail-Fast on malformed service slugs, unsupported languages/layers, or exhausted domain port ranges.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|scaffold_microservice.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|scaffold_microservice.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/models/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|MicroserviceBuildSpec]] (class: belongs_to) — *Formal cross-brain specification contract for one-shot compliant microservice generation.*
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|_SLUG_RE]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|_VALID_FLEET_MODES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|_VALID_LANGS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|_VALID_LAYERS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|allocate_domain_port]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|collect_reserved_ports]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|from_dict]] (function: belongs_to) — *Constructs and validates MicroserviceBuildSpec from a JSON/task_context dictionary.*
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|resolve_port]] (function: belongs_to) — *Resolves explicit port (verifying non-collision with base L1/L2 fleet) or auto-allocates.*
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|validate]] (function: belongs_to) — *Fail-fast cold-path validation of cross-brain microservice build parameters.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
