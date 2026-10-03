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
Automatically generated mirror for `safe-socket/src/utils/machine_detector.go`.

> **Essential Process**:
> Detects whether an IP address or hostname belongs to the local host machine, enabling automatic optimization from network TCP to shared memory transport.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.IsLocalAddress]] (method: defines_method) — *IsLocalAddress checks if an address ("IP:Port", "host:Port", or "IP") belongs to the local machine.*
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.refresh]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|GetMachineDetector]] (function: belongs_to) — *GetMachineDetector returns the singleton MachineDetector instance.*
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.IsLocalAddress]] (method: belongs_to) — *IsLocalAddress checks if an address ("IP:Port", "host:Port", or "IP") belongs to the local machine.*
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.refresh]] (method: belongs_to)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector]] (struct: belongs_to) — *IsLocalAddress checks if an address ("IP:Port", "host:Port", or "IP") belongs to the local machine.*
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector]] (struct: defines_method) — *IsLocalAddress checks if an address ("IP:Port", "host:Port", or "IP") belongs to the local machine.*
- [[safe-socket/safe-socket/src/utils/machine_detector_test.go.md|machine_detector_test.go]] (calls)
- [[safe-socket/safe-socket/src/utils/machine_detector_test.go.md|machine_detector_test.go]] (same_package)
<!-- SYNC:END -->
