---
source: microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T18:04:36.364037
---

# Mirror: contracts.hpp

## 📝 Description
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp`.

> **Essential Process**:
> C++17 Exchange Contract data models, JSON serializers, and schema introspection extractors (.proto IDL and Cap'n Proto) matching the Go, Python, and Rust microservice-toolbox contract APIs 1:1.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|contracts.h]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|contracts.h]] (same_package)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_display_address]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_resolve_contract_port]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_utc_timestamp_iso8601]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.to_json]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|BuildContractsEnvelope]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|CompactNonCommentLines]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractOperation]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractPeer]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ContractsEnvelope]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|CurrentUtcTimestampIso8601]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|DisplayAddress]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExchangeContract]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExtractCapnpOperations]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ExtractProtoTextOperations]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|FindMatchingBraceBlock]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|IsIdentChar]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|JoinStrings]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|MICROSERVICE_TOOLBOX_SPEC_CONTRACTS_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_SPEC_CONTRACTS_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|NewContractsEnvelope]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ParseStreamingType]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ReadSchemaFile]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|ResolveContractPort]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|TrimStr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|build_contracts_envelope]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|displayAddress]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|display_address]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|extractCapnpOperations]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|extractProtoTextOperations]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|extract_capnp_operations]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|extract_proto_operations]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|prefix]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|readSchemaFile]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|read_schema_file]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|resolveContractPort]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|resolve_contract_port]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|spec.hpp]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
