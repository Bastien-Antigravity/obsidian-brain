---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_MAC]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|get_native_config]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|MODES_DIR]] (constant: belongs_to) — *Locate root directory*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|ensure_ai_context]] (function: belongs_to) — *Ensure AI-CONTEXT.md exists at WORKSPACE_ROOT.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|ensure_go_work]] (function: belongs_to) — *Ensure go.work multi-module manifest exists and is synchronized.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|ensure_root_symlinks]] (function: belongs_to) — *Ensure essential root standalone.yaml configuration symlink exists.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_code_workspace]] (function: belongs_to) — *Generate Bastien-Antigravity.code-workspace.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_extensions]] (function: belongs_to) — *Generate .vscode/extensions.json.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_launch]] (function: belongs_to) — *Generate .vscode/launch.json tailored to OS.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_settings]] (function: belongs_to) — *Generate .vscode/settings.json tailored to OS.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_tasks]] (function: belongs_to) — *Generate .vscode/tasks.json tailored to OS.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|get_workspace_folders]] (function: belongs_to) — *Return configured folders for the 14 active workspace repositories.*
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_antigravity_ide]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
<!-- SYNC:END -->
