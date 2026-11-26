---
source: obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.703377
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: check_coherence.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py`.

> **Essential Process**:
> Checks coherence between runtime agent definitions (.agents/skills/) and the static source Role-Prompts inside the obsidian-brain submodules.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|build_skill_markdown]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/auditor.py.md|Auditor]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|CoherenceAuditor]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|ROLES]] (constant: belongs_to) — *Precedence matching mapping*
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|audit]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|fix_mismatch]] (function: belongs_to) — *Auto-resolves prompt-skill mismatches using the canonical builder from convert_agents.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|main]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|run_coherence_check]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|strip_frontmatter]] (function: belongs_to) — *Removes the YAML frontmatter block from markdown content.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|strip_sandbox_headers]] (function: belongs_to) — *Removes attention restoration, complexity gate, and state management rules added to skills.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
