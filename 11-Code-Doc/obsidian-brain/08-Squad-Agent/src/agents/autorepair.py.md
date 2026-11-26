---
source: obsidian-brain/08-Squad-Agent/src/agents/autorepair.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-11-12 06:22:10.000407
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: autorepair.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/autorepair.py`.

> **Essential Process**:
> Real-Time Fleet Incident Subscriber & Capability-Aware Tiered Auto-Repair Coordinator. Listens on brain-partitioned NATS subjects emitted by watchdog-agent, enriches incidents with correlated TimescaleDB history & source snippets, classifies severity Tiers 1-4 per Prompt-Fleet-AutoRepair.md, and gates mutations behind isolated /tmp git worktree tests and 3-strike circuit breakers.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|decrypt_secret]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|list_fleet_incidents]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|query_recent_fleet_errors]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|upsert_fleet_incident]] (function: calls) — *Persists or updates an AutoRepair triage incident record in PostgreSQL.*
- [[obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|AutoRepairCoordinator]] (class: belongs_to) — *Real-time Watchdog incident consumer and capability-aware Tiered Auto-Repair coordinator.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|RestartCircuitBreaker]] (class: belongs_to) — *Enforces the 3-strike sliding window circuit breaker per (brain_id, service_name).*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|RuntimeCapabilities]] (class: belongs_to) — *Detects whether this Squad Agent instance can mutate files / run tests or must stay proposal-only.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_BLOCKED_PATCH_FILES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_MAX_MEMORY_INCIDENTS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_MAX_PATCH_LINES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_OPEN_INCIDENT_STATUSES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_TIER_NAMES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_append_audit_log]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_apply_patch_in_dir]] (function: belongs_to) — *Applies a unified diff at git_root, handling workspace-prefixed paths (-p2 / -p3) cleanly.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_check_upstream_dependencies]] (function: belongs_to) — *Checks configured upstream dependency listeners cleanly before restarting a Tier 3 service.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_get_cap_section]] (function: belongs_to) — *Merges global config-server capabilities[section] with local service slice config.data[section].*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_incident_cb]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_incident_signature]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_index_incident_memory]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_load_autorepair_prompt]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_notify_operator]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_on_live_conf_update]] (function: belongs_to) — *Applies live AppConfig changes to autorepair.enabled without overriding operator toggles.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_parse_bool_flag]] (function: belongs_to) — *Parses YAML boolean or env-expanded string ('true'/'false'), failing fast if malformed.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_prune]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_read_source_context]] (function: belongs_to) — *Reads a bounded 30-line source excerpt without leaving workspace_root.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_remember_incident]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_resolve_autorepair_enabled]] (function: belongs_to) — *Validates and extracts mandatory startup autorepair.enabled flag from AppConfig.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_resolve_brain_id]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_resolve_genai_client]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_resolve_git_root]] (function: belongs_to) — *Resolves the enclosing git repository root inside workspace_root and its relative service subdir.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_resolve_model_name]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_resolve_service_repo]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_resolve_subject_prefix]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_run_rca]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_seen_event]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_select_verification_command]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_trigger_watchdog_restart]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|_verify_patch_in_worktree]] (function: belongs_to) — *Verifies a candidate unified diff inside an isolated temporary git worktree without mutating HEAD.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|approve_incident]] (function: belongs_to) — *Applies a verified patch (when applicable) and restarts the affected service via Watchdog REST.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|classify_incident_tier]] (function: belongs_to) — *Classifies an incident payload into Operational Tiers 1-4.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|detect]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|get_autorepair_status]] (function: belongs_to) — *Returns current runtime toggle, capabilities, open incident count, and circuit breaker snapshot.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|get_incident]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|handle_incident]] (function: belongs_to) — *Processes an incoming IncidentEvent cleanly with toggle gating, coalescing, and bounded side effects.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|is_frozen]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|list_incidents]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|record_strike]] (function: belongs_to) — *Records a repair/restart strike; returns (is_now_frozen, count_in_window).*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|reject_incident]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|resolve_incident]] (function: belongs_to) — *Marks an active incident manually resolved without applying automated restarts.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|resolve_incident_subject]] (function: belongs_to) — *Matches watchdog-agent's ResolveIncidentSubject NATS partitioning convention.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|set_enabled]] (function: belongs_to) — *Enables or disables autonomous AutoRepair incident triage dynamically on the fly.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|start]] (function: belongs_to) — *Verifies schema readiness, hydrates open incidents, and subscribes to NATS incident alerts.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|status_snapshot]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|stop]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|to_dict]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|unfreeze]] (function: belongs_to) — *Clears frozen circuit breaker state and strike history for a service.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|unfreeze_service]] (function: belongs_to) — *Resets 3-strike circuit breaker freeze for a service and closes stale FROZEN signature locks.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|validate_proposed_diff]] (function: belongs_to) — *Validates unified diff syntax, size limits, and target path containment inside service_dir.*
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
