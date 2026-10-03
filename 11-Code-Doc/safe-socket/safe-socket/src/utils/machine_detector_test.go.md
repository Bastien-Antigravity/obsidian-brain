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

## 📝 Description
Automatically generated mirror for `safe-socket/src/utils/machine_detector_test.go`.

> **Essential Process**:
> Validates loopback and local network IP resolution for MachineDetector.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|GetMachineDetector]] (function: calls) — *GetMachineDetector returns the singleton MachineDetector instance.*
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.IsLocalAddress]] (method: calls) — *IsLocalAddress checks if an address ("IP:Port", "host:Port", or "IP") belongs to the local machine.*
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|machine_detector.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (imports)
- [[safe-socket/safe-socket/src/utils/machine_detector_test.go.md|TestMachineDetector]] (function: belongs_to)
<!-- SYNC:END -->
