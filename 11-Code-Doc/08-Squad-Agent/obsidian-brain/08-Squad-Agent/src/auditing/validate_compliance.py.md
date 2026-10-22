---
source: obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.723079
---

# Mirror: validate_compliance.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py`.

> **Essential Process**:
> Mechanical Code Compliance and Architectural Invariant Auditor. Scans source code files across the Bastien-Antigravity fleet to verify strict adherence to: 1. Triple-Block Header Standard (ESSENTIAL PROCESS, DATA FLOW, KEY PARAMETERS) 2. Section Divider Standard (// --------- or # ---------) 3. Dynamic Port Invariant (No hardcoded canonical ports in production code) 4. Production Cleanliness Invariant (No test mocks, EnsureSafeLogger, or nil fallbacks in bin source) 5. Dynamic Host Invariant (No hardcoded 127.0.0.1 / localhost in capability connection logic) 6. Ecosystem Tooling Invariant (Entrypoints must use BootstrapService / bootstrap_microservice) 7. Observability Invariant (Zero bare print/println in production code) 8. Path Sovereignty Invariant (Zero legacy manual sys.path climbing) 9. SSoT Configuration Invariant (No direct parsing of standalone.yaml) 10. Dynamic Versioning Invariant (No manual directory loops for VERSION.txt)

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|CodeTransformer]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|transform_path]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|CANONICAL_PORTS]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|ComplianceAuditor]] (class: belongs_to) — *Mechanical compliance scanner for code files.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|EXCLUDED_DIRS]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_file]] (function: belongs_to) — *Audits a single source file and returns a list of detected violations.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_path]] (function: belongs_to) — *Audits a path (file or recursive directory).*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_staged]] (function: belongs_to) — *Audits git staged files in the current repository / workspace.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|format_report]] (function: belongs_to) — *Formats violations list into human and agent readable report.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|main]] (function: belongs_to) — *CLI runner for standalone audit execution.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
