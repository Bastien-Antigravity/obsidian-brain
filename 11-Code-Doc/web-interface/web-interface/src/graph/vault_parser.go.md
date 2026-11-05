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
- [[web-interface/web-interface/src/graph/vault_parser.go.md|EdgeData]] (struct: belongs_to) — *EdgeData defines the relationship link properties between two nodes.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|Edge]] (struct: belongs_to) — *Edge wraps edge attributes for Cytoscape element parsing.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|GetVaultGraph]] (function: belongs_to) — *GetVaultGraph returns the parsed knowledge graph, serving from cache if valid.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|GraphData]] (struct: belongs_to) — *GraphData defines the root JSON structure expected by brain_graph.js.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|NodeData]] (struct: belongs_to) — *NodeData defines the presentation metadata properties of a Cytoscape graph node.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|Node]] (struct: belongs_to) — *Node wraps node attributes for Cytoscape element parsing.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|ParseVault]] (function: belongs_to) — *ParseVault scans markdown notes in the given vault directory and builds graph nodes and links.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|ResolveVaultPath]] (function: belongs_to) — *ResolveVaultPath discovers the active obsidian-brain vault directory on the host filesystem.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|frontmatter]] (struct: belongs_to)
- [[web-interface/web-interface/src/graph/vault_parser.go.md|generateID]] (function: belongs_to)
- [[web-interface/web-interface/src/graph/vault_parser_test.go.md|vault_parser_test.go]] (calls)
- [[web-interface/web-interface/src/graph/vault_parser_test.go.md|vault_parser_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
