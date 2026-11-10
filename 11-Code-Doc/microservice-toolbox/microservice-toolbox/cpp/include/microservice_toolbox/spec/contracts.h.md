---
source: microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T18:04:36.354431
---

# Mirror: contracts.h

## 📝 Description
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h`.

> **Essential Process**:
> Pure C11/C99 Exchange Contract data structures and RFC 8259 JSON serialization helpers for microservice-toolbox. Enables C (and C/C++ FFI) services to build authoritative GET /api/v1/contracts payloads and ServiceSpec contract lists with zero external dependencies.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|MICROSERVICE_TOOLBOX_SPEC_CONTRACTS_H]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_SPEC_CONTRACTS_H*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|MtContractOperation]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|MtContractPeer]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|MtContractsEnvelope]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|MtExchangeContract]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|MtStrBuf]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|colon]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|gen_at]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_contract_operation_to_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_contract_peer_to_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_contracts_envelope_to_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_display_address]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_exchange_contract_to_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_resolve_contract_port]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_spec_free_string]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_strbuf_append]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_strbuf_append_char]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_strbuf_append_json_string]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_strbuf_append_n]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_strbuf_append_opt_kv]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_strbuf_append_req_kv]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_strbuf_reserve]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_utc_timestamp_iso8601]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_write_contract_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_write_operation_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|mt_write_peer_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|p]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|service]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|source]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|tm]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.h.md|version]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|contracts.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|contracts.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|contracts.hpp]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
