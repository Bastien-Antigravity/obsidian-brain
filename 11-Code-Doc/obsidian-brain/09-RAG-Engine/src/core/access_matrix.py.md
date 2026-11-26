

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/access_matrix.py`.

> **Essential Process**:
> Loads and parses the Access Control Matrix (ACM) config file. Provides fallback matrix definitions when access_matrix.yaml is missing or corrupt.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/core/access_matrix.py.md|_load_access_matrix]] (function: belongs_to) — *Load the access matrix YAML once. Falls back to hardcoded defaults on error.*
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
<!-- SYNC:END -->
