

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.IsLocalAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.refresh]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (calls)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|GetMachineDetector]] (function: belongs_to)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.IsLocalAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector.refresh]] (method: belongs_to)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/utils/machine_detector.go.md|MachineDetector]] (struct: defines_method)
- [[safe-socket/safe-socket/src/utils/machine_detector_test.go.md|machine_detector_test.go]] (calls)
- [[safe-socket/safe-socket/src/utils/machine_detector_test.go.md|machine_detector_test.go]] (same_package)
<!-- SYNC:END -->
