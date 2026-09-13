

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_MAC]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|IS_WINDOWS]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_code_workspace]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_extensions]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_launch]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_settings]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|generate_vscode_tasks]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|get_workspace_folders]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_antigravity_ide]] (function: belongs_to)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
<!-- SYNC:END -->
