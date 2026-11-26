---
source: obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-24 04:57:51.704524
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: audit_secret_leakage.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py`.

> **Essential Process**:
> Ecosystem Secret Leakage and Plaintext Parameter Auditor. Scans configurations, manifests, and log files across the Bastien-Antigravity fleet to guarantee: 1. No sensitive parameter (token, password, secret, chat_id, api_key) is stored in plaintext in YAML/JSON configs. 2. All secret configuration values are strictly wrapped in ENC(...) tokens. 3. No decrypted secret value or sensitive credential appears in plaintext inside log files. 4. Optionally scrubs historical log files of leaked credentials.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|autorepair.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|IGNORED_LOG_DIRS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|SENSITIVE_KEY_REGEX]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|SecretLeakAuditor]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|_resolve_private_key]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|audit_config_files]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|audit_log_files]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|decrypt_secret]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|extract_known_secrets]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|main]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|discord_client.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|pg_pool.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
