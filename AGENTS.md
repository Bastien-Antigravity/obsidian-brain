---
microservice: obsidian-brain
type: rules
status: active
tags:
- '#service/obsidian-brain'
- '#domain/knowledge'
- '#type/rules'
- '#state/active'
- '#zone/0-core'
- '#ai/ignore'
---

# AGENTS.md: obsidian-brain

## Repository Mission & Architecture Role
`obsidian-brain` is the centralized knowledge base, architecture registry, operational runbook vault, and RAG intelligence engine for the Bastien-Antigravity ecosystem. It serves both human engineers and autonomous AI agents as the definitive single source of truth for architecture decisions (ADRs), coding standards, and inter-service schemas.

- **Primary Structure**:
  - `00-AI-Orchestration`: Agent personas, coordination protocols, fleet directives
  - `02-Business-BDD`: Domain glossary, BDD behavior specifications (`FEAT-*.md`), acceptance criteria
  - `03-Tech-Stack`: Authoritative architecture standards, networking protocols, coding rules
  - `06-Microservices`: Service specification sheets, endpoint registries, capability maps
  - `07-Core-KMS`: Key management service, encryption procedures, master secret rotation
  - `08-Base-Scripts`: AI squad operational engine room, CLI utilities (`main.py`), automated scaffolder
  - `09-RAG-Engine`: Python RAG service indexing documentation into TimescaleDB/pgvector
- **Configuration Link**: `standalone.yaml -> ../docker-deployment/modes/local/config/native.yaml`

## Key Commands & Verification
```bash
# Run ecosystem preflight check
python3 08-Base-Scripts/main.py preflight-check

# Scaffold a new microservice
python3 08-Base-Scripts/main.py scaffold-microservice --name <name> --lang <go|python|rust>

# Query knowledge base & AST via RAG
python3 09-RAG-Engine/main.py query "<topic>"

# RAG Engine tests
pytest 09-RAG-Engine/tests

# Check vault frontmatter & coherence
python3 08-Base-Scripts/main.py ensure-frontmatter
python3 08-Base-Scripts/main.py check-coherence
```

## AI Development & Integration Guidelines
1. **Never Contradict Architecture Blueprints**: Refer to `03-Tech-Stack/02-Project-Architecture/` before making cross-service design changes.
2. **Markdown Frontmatter Standard**: Every markdown file in this vault MUST begin with canonical YAML frontmatter (`microservice`, `type`, `status`, `tags`).
3. **Triple-Block Header in Code**: Any code script (`08-Base-Scripts`, `09-RAG-Engine`) must adhere to the Triple-Block header (`ESSENTIAL PROCESS`, `DATA FLOW`, `KEY PARAMETERS`).
4. **Encrypted Credentials**: Never commit plaintext secrets to markdown notes or config files. Use `ENC(...)` tokens.
5. **No Broken Links**: Always use relative links or verified obsidian wikilinks.
