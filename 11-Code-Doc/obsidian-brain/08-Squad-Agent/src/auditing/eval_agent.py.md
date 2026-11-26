---
source: obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-24 14:26:09.449023
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: eval_agent.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py`.

> **Essential Process**:
> Isolated single-agent evaluation, coherency, and ephemeral worktree sandbox harness for 08-Squad-Agent personas. Supports two execution modes: - 'readonly' (default): Zero-mutation audit over an in-memory SquadEventBus. - 'worktree': Detached HEAD git worktree inside /tmp with sanitized environment (secrets stripped, HOME/TMPDIR/GOCACHE/CARGO_TARGET_DIR/CONFIG_PATH jailed, LOGGER_PROFILE='minimal', GOWORK='off'), Complexity-Gate file cap, post-edit compliance + test verification, optional .patch export, unconditional teardown, and pre/post host Git fingerprint assertion proving zero host pollution.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_BLOCKED_IN_WORKTREE_TOOLS]] (constant: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_MUTATING_TOOL_NAMES]] (constant: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_get_effective_tools]] (function: calls) — *Returns active LLM tools filtered by read_only or worktree_sandbox_mode policy.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|enable_readonly_mode]] (function: calls) — *Enforces strict read-only tool permissions on this agent instance.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|enable_worktree_sandbox_mode]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|slugify_role_name]] (function: calls) — *Normalizes a prompt stem or role label into a canonical lowercase slug.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|start]] (function: calls) — *Registers the agent message consumer loop.*
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|stop]] (function: calls) — *Clean shut down.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|debloat_audit.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|debloat_audit.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|run_debloat_audit]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|ComplianceAuditor]] (class: calls) — *Mechanical compliance scanner for code files.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_file]] (function: calls) — *Audits a single source file and returns a list of detected violations.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_path]] (function: calls) — *Audits a path (file or recursive directory).*
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|ROLE_MAP]] (constant: calls) — *Role to Prompt Filename Mapping (21 Ecosystem Squad Personas)*
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|agent_dispatcher.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|get_role_prompt_path]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|SquadEventBus]] (class: calls) — *Abstract interface defining the pub/sub event bus contract for AI squad coordination.*
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_config]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|SquadAgentEvaluator]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_ISOLATED_DUMMY_CONFIG_YAML]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_SAFE_PASSTHROUGH_ENV_KEYS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_build_isolated_sandbox_env]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_build_scorecard]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_capture_git_fingerprint]] (function: belongs_to) — *Captures HEAD SHA, porcelain status, refs, and worktree list to prove zero host mutation.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_collect_worktree_diff]] (function: belongs_to) — *Collects changed/untracked relative paths and unified diff without mutating Git's index.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_evaluate_in_worktree]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_evaluate_readonly]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_resolve_git_root]] (function: belongs_to) — *Resolves the enclosing Git repository root for target_path, failing fast if not a Git repo.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_run_git]] (function: belongs_to) — *Executes a deterministic git subprocess with shell=False and returns (rc, stdout, stderr).*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|_run_worktree_verification_tests]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|close]] (function: belongs_to) — *Clears registered in-memory callbacks.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|connect]] (function: belongs_to) — *No-op connection hook for in-memory evaluation bus.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|evaluate]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|format_eval_markdown]] (function: belongs_to) — *Formats an evaluation scorecard dictionary into a human-readable Markdown report.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|instantiate_agent]] (function: belongs_to) — *Resolves and instantiates a daemon subclass or specialist BaseAgent persona.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|main]] (function: belongs_to) — *CLI entrypoint for `python3 08-Squad-Agent/main.py eval-agent`.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|publish]] (function: belongs_to) — *Records outgoing agent payloads published during evaluation.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|resolve_target_repo]] (function: belongs_to) — *Resolves and validates that the target repository resides inside workspace_root.*
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|subscribe]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
