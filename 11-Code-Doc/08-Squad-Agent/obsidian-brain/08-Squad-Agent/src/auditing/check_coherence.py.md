---
source: obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.734533
---

# Mirror: check_coherence.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py`.

> **Essential Process**:
> Checks coherence between runtime agent definitions (.agents/skills/) and the static source Role-Prompts inside the obsidian-brain submodules.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/auditor.py.md|Auditor]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|CoherenceAuditor]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|ROLES]] (constant: belongs_to) — *Precedence matching mapping*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|audit]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|fix_mismatch]] (function: belongs_to) — *Auto-resolves prompt-skill mismatches by copying/formatting source prompt.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|run_coherence_check]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|strip_frontmatter]] (function: belongs_to) — *Removes the YAML frontmatter block from markdown content.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|strip_sandbox_headers]] (function: belongs_to) — *Removes attention restoration and state management rules added to skills.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
