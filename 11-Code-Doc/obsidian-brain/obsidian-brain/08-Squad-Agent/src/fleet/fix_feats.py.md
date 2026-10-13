---
source: obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.730485
---

# Mirror: fix_feats.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_config]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|FeatFixer]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|_get_hub_link]] (function: belongs_to) — *Try to find the hub file for a given microservice.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|_move_root_feats]] (function: belongs_to) — *Move root FEAT files to ontime-scheduler if appropriate.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|_process_single_file]] (function: belongs_to) — *Processes a single FEAT file to update frontmatter and backlinks.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|process_feats]] (function: belongs_to) — *Iterates through all FEAT files and applies standardization rules.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
