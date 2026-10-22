---
source: obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.808288
---

# Mirror: fleet_version.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py`.

> **Essential Process**:
> Fleet-wide dynamic semantic versioning manager for Bastien-Antigravity. Audits, verifies, increments, and synchronizes VERSION.txt across all 14 workspaces and ensures strict mechanical parity with AI-Project-DNA.md and Git release tags.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_BOLD]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_DIM]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_GREEN]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_RED]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_RESET]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_YELLOW]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_fleet_repositories]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|SEMVER_REGEX]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|get_repo_git_tag]] (function: belongs_to) — *Returns the latest Git tag for the repository, or 'none'.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|increment_semver]] (function: belongs_to) — *Computes the next semver string based on bump type.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|inspect_repo_version]] (function: belongs_to) — *Inspects VERSION.txt and AI-Project-DNA.md within a repository directory.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|parse_semver]] (function: belongs_to) — *Parses a semver string into (major, minor, patch, prerelease).*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|resolve_target_repos]] (function: belongs_to) — *Resolves target repositories to operate on.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|run_status_or_check]] (function: belongs_to) — *Displays version audit status table. Returns True if all are coherent and valid.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|update_repo_version]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
