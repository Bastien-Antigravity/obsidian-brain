# 📚 Documentation Conventions Extracted from Ecosystem

## 1. Standardized File Structure
Every repository includes:

| File | Purpose | Present In |
|------|---------|-----------|
| `README.md` | User-facing documentation | ALL repos |
| `ARCHITECTURE.md` | System design deep-dive | ALL repos |
| `TESTING.md` | Test instructions | Most repos |
| `TODO.md` / `todo` | Pending tasks | Some repos |
| `AI-Session-State.md` | AI context persistence | ALL repos |
| `AI-Init.md` | AI onboarding beacon | ALL repos |
| `Makefile` | Build automation | Go repos |
| `.dockerignore` | Docker build exclusions | Most repos |
| `.github/` | CI/CD workflows | ALL repos |

## 2. Dataview YAML Frontmatter
All Obsidian-visible docs include standardized YAML:
```yaml
---
microservice: {repo-name}
type: {repository|session-state|architecture}
status: active
language: {go|rust|python}
tags:
  - domain/{area}
---
```

## 3. README Structure (Go Repos)
```
# {Service Name}
{One-paragraph description}

## Features
- Bullet list

## Architecture
Link to ARCHITECTURE.md

## Getting Started
### Prerequisites
### Installation
### Usage

## API Protocol / Usage
### Supported Operations

## Project Structure
{ASCII tree}
```

## 4. Commit Conventions
- **Conventional Commits**: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`
- **Scoped**: `feat(config-server): add gRPC support`
- **Branch Strategy**: `develop` → `main` (merge, never rebase)

## 5. Section Separators in Code
```go
// -------------------------------------------------------------------------
// Section Name
// -------------------------------------------------------------------------
```
Used in EVERY Go interface and implementation file to group related methods.

## 6. Obsidian Brain Structure (PARA-adjacent)
```
obsidian-brain/
├── 00-Daily-AI-Playbook.md     # Operational loop
├── 00-Master-MOC.md            # Ecosystem map
├── 01-AI-Assistant/            # AI workflow rules
├── 02-Standards/               # Architecture standards
├── 03-Coding-and-Libraries/    # Language-specific rules
├── 04-Microservice-Domain/     # Service documentation
└── 05-Scripts/                 # Automation tools
```
