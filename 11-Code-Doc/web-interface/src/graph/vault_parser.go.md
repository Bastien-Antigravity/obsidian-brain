---
source: web-interface/src/graph/vault_parser.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-10-27 17:45:57.372407
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: vault_parser.go

## 📝 Description
Automatically generated mirror for `web-interface/src/graph/vault_parser.go`.

> **Essential Process**:
> Parses the ecosystem Obsidian vault markdown documents, frontmatter metadata, and wikilink references into a Cytoscape-compatible knowledge graph JSON schema. Caches graph in memory with thread-safe TTL expiration for microsecond latency.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/src/graph/vault_parser.go.md|BrainVaultInfo]] (struct: belongs_to) — *BrainVaultInfo describes a discovered Obsidian brain vault in the workspace topology.*
- [[web-interface/src/graph/vault_parser.go.md|EdgeData]] (struct: belongs_to) — *EdgeData defines the relationship link properties between two nodes.*
- [[web-interface/src/graph/vault_parser.go.md|Edge]] (struct: belongs_to) — *Edge wraps edge attributes for Cytoscape element parsing.*
- [[web-interface/src/graph/vault_parser.go.md|ExtraWorkspaceEntry]] (struct: belongs_to) — *from EXTRA_WORKSPACES or persisted workspaces.yaml.*
- [[web-interface/src/graph/vault_parser.go.md|GetVaultGraphForBrain]] (function: belongs_to) — *GetVaultGraphForBrain returns the parsed knowledge graph for the specified brain ID.*
- [[web-interface/src/graph/vault_parser.go.md|GetVaultGraph]] (function: belongs_to) — *GetVaultGraph returns the parsed knowledge graph, serving from cache if valid.*
- [[web-interface/src/graph/vault_parser.go.md|GraphData]] (struct: belongs_to) — *GraphData defines the root JSON structure expected by brain_graph.js.*
- [[web-interface/src/graph/vault_parser.go.md|ListAvailableVaults]] (function: belongs_to) — *and optional workspaces.yaml.*
- [[web-interface/src/graph/vault_parser.go.md|LoadPersistedWorkspaces]] (function: belongs_to) — *or <primaryVault>/09-RAG-Engine/workspaces.yaml using yaml.v3.*
- [[web-interface/src/graph/vault_parser.go.md|NodeData]] (struct: belongs_to) — *NodeData defines the presentation metadata properties of a Cytoscape graph node.*
- [[web-interface/src/graph/vault_parser.go.md|Node]] (struct: belongs_to) — *Node wraps node attributes for Cytoscape element parsing.*
- [[web-interface/src/graph/vault_parser.go.md|ParseExtraWorkspaces]] (function: belongs_to) — *supporting both '/path' and 'brain_id=/path' formats while preserving absolute paths.*
- [[web-interface/src/graph/vault_parser.go.md|ParseVault]] (function: belongs_to) — *ParseVault scans markdown notes in the given vault directory and builds graph nodes and links.*
- [[web-interface/src/graph/vault_parser.go.md|ResolveVaultPath]] (function: belongs_to) — *ResolveVaultPath discovers the active obsidian-brain vault directory on the host filesystem.*
- [[web-interface/src/graph/vault_parser.go.md|SplitExtraWorkspaces]] (function: belongs_to) — *'brain_id=' prefixes and returning cleaned filesystem paths.*
- [[web-interface/src/graph/vault_parser.go.md|frontmatter]] (struct: belongs_to)
- [[web-interface/src/graph/vault_parser.go.md|generateID]] (function: belongs_to)
- [[web-interface/src/graph/vault_parser.go.md|getOrParseVault]] (function: belongs_to)
- [[web-interface/src/graph/vault_parser.go.md|isObsidianBrainDir]] (function: belongs_to)
- [[web-interface/src/graph/vault_parser.go.md|normalizeVaultPathKey]] (function: belongs_to)
- [[web-interface/src/graph/vault_parser.go.md|workspacesYAMLFile]] (struct: belongs_to)
- [[web-interface/src/graph/vault_parser_test.go.md|vault_parser_test.go]] (calls)
- [[web-interface/src/graph/vault_parser_test.go.md|vault_parser_test.go]] (same_package)
- [[web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
