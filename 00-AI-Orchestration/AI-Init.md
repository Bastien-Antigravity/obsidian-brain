---
microservice: ecosystem-core
type: governance
status: active
tags:
- '#zone/0-orchestration'
- '#service/ecosystem-core'
- '#type/governance'
- '#state/active'
---
# ⚡ AI Initialization: ecosystem-core

> [!IMPORTANT] MANDATORY INITIALIZATION
> Copy and paste this prompt when starting a new session in this vault:
> 
> "1. **Core Invariants**: Read workspace root `../AGENTS.md`, `../AI-CONTEXT.md`, and vault `./AGENTS.md`."
> "2. **Ecosystem Map & DNA**: Read **[[Ecosystem-Map-MOC]]**, **[[00-AI-Orchestration/AI-Project-DNA]]**, and `03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules.md`."
> "3. **Session State & Mode**: Restore session state from **[[00-AI-Orchestration/AI-Session-State]]**, check `00-AI-Orchestration/Config/MODE-MANUAL.md`, and load `00-AI-Orchestration/Workflows/ACTIVE-RITUALS.md`."
> "4. **AI-Ignore Rule**: Immediately ignore any files containing the `#ai/ignore` tag. Do not read them unless explicitly asked."
> "5. **Sentinel Audit & Specialists**: From the workspace root, run `python3 obsidian-brain/08-Squad-Agent/main.py preflight-check` and `python3 obsidian-brain/08-Squad-Agent/main.py brain-health-audit`, resolve any drift, and enforce all language specialist rules in `07-Core-KMS/Role-Prompts/03-Developer/Squad/` (including Python granular camelCase aliased imports)."

> [!TIP] Cross-Platform Notes
> - On Windows, use `python` instead of `python3`.
> - Always run scripts from the **workspace root** (`Bastien-Antigravity/`), not from inside `obsidian-brain/`.
> - The Preflight Check runs automatically at squad startup via `squad-agent`.
