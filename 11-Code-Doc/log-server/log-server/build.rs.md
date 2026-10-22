---
microservice: log-server
type: note
status: active
tags:
- '#service/log-server'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `log-server/build.rs`.

> **Essential Process**:
> Build script for log-server. Compiles protobuf schemas via tonic-build for gRPC services and resolves dynamic semver from VERSION.txt.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[log-server/log-server/build.rs.md|main]] (function: belongs_to)
<!-- SYNC:END -->
