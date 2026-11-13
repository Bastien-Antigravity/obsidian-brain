---
source: microservice-toolbox/python/microservice_toolbox/version/version.py
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:58.566605
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: version.py

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/version/version.py`.

> **Essential Process**:
> Implements hierarchical dynamic semver resolution for Python components. Guarantees VERSION.txt is the Single Source of Truth with fail-fast errors.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/version/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/version/version.py.md|_THIS_FILE]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/version/version.py.md|get_version]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/version/version.py.md|reset_version]] (function: belongs_to) — *Clears the cached version so the next get_version() will re-resolve.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/version/version.py.md|resolve_version]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/version/version.py.md|set_version]] (function: belongs_to) — *Explicitly sets the cached version (primarily for testing). Rejects empty values.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
