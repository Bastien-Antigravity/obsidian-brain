---
source: obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T13:06:47.242698
---

# Mirror: checkpoint.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py`.

> **Essential Process**:
> Squad Checkpoint Manager - Deterministic Git Restore Point Protocol. Native first-class engine room orchestrator in 08-Squad-Agent.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|print_help]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|CHECKPOINT_FILENAME]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|cmd_create]] (function: belongs_to) — *Creates a new pre-task restore point tag and records state.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|cmd_release]] (function: belongs_to) — *Finalizes and commits verified changes, pruning the temporary restore point tag.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|cmd_rollback]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|cmd_status]] (function: belongs_to) — *Displays the status and diff of the active restore point.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|get_checkpoint_file]] (function: belongs_to) — *Returns the primary path for .squad_checkpoint.json.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|get_git_root]] (function: belongs_to) — *Finds the root directory of the git repository containing path.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|is_git_repo]] (function: belongs_to) — *Verifies whether a directory belongs to a git working tree.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|load_active_checkpoint]] (function: belongs_to) — *Loads existing checkpoint metadata if present.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|remove_checkpoint_file]] (function: belongs_to) — *Removes the checkpoint metadata file.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|resolve_target_repos]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|run_git_cmd]] (function: belongs_to) — *Executes a git command in the specified directory and returns (code, stdout, stderr).*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/checkpoint.py.md|save_checkpoint]] (function: belongs_to) — *Saves checkpoint metadata to .squad_checkpoint.json.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
