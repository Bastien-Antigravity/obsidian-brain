---
source: web-interface/src/graph/vault_parser_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-10-27 17:45:57.376812
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: vault_parser_test.go

## 📝 Description
Automatically generated mirror for `web-interface/src/graph/vault_parser_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/src/graph/vault_parser.go.md|GetVaultGraphForBrain]] (function: calls) — *GetVaultGraphForBrain returns the parsed knowledge graph for the specified brain ID.*
- [[web-interface/src/graph/vault_parser.go.md|GetVaultGraph]] (function: calls) — *GetVaultGraph returns the parsed knowledge graph, serving from cache if valid.*
- [[web-interface/src/graph/vault_parser.go.md|ListAvailableVaults]] (function: calls) — *and optional workspaces.yaml.*
- [[web-interface/src/graph/vault_parser.go.md|ParseExtraWorkspaces]] (function: calls) — *supporting both '/path' and 'brain_id=/path' formats while preserving absolute paths.*
- [[web-interface/src/graph/vault_parser.go.md|ParseVault]] (function: calls) — *ParseVault scans markdown notes in the given vault directory and builds graph nodes and links.*
- [[web-interface/src/graph/vault_parser.go.md|SplitExtraWorkspaces]] (function: calls) — *'brain_id=' prefixes and returning cleaned filesystem paths.*
- [[web-interface/src/graph/vault_parser.go.md|vault_parser.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/src/graph/vault_parser_test.go.md|TestListAvailableVaultsAndGetVaultGraphForBrain]] (function: belongs_to)
- [[web-interface/src/graph/vault_parser_test.go.md|TestParseVault]] (function: belongs_to)
- [[web-interface/src/graph/vault_parser_test.go.md|TestSplitExtraWorkspacesAndWorkspacesYAML]] (function: belongs_to)
- [[web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
