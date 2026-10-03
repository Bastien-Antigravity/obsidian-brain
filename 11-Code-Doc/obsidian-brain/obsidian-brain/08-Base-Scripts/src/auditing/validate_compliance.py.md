---
source: obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:02.901048
---

# Mirror: validate_compliance.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py`.

> **Essential Process**:
> Mechanical Code Compliance and Architectural Invariant Auditor. Scans source code files across the Bastien-Antigravity fleet to verify strict adherence to: 1. Triple-Block Header Standard (ESSENTIAL PROCESS, DATA FLOW, KEY PARAMETERS) 2. Section Divider Standard (// --------- or # ---------) 3. Dynamic Port Invariant (No hardcoded canonical ports in production code) 4. Production Cleanliness Invariant (No test mocks, EnsureSafeLogger, or nil fallbacks in bin source) 5. Dynamic Host Invariant (No hardcoded 127.0.0.1 / localhost in capability connection logic)

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|CodeTransformer]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|improved_transformer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|transform_path]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|CANONICAL_PORTS]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|ComplianceAuditor]] (class: belongs_to) — *Mechanical compliance scanner for code files.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|EXCLUDED_DIRS]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|audit_file]] (function: belongs_to) — *Audits a single source file and returns a list of detected violations.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|audit_path]] (function: belongs_to) — *Audits a path (file or recursive directory).*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|format_report]] (function: belongs_to) — *Formats violations list into human and agent readable report.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|main]] (function: belongs_to) — *CLI runner for standalone audit execution.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
