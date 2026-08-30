# Organizational Interoperability Protocol — Draft

## Goal

Allow multiple artificial organizations to collaborate while preserving internal privacy.

## Public objects

```text
CapabilityAdvertisement
CapabilityRequest
TrustContract
DataBoundary
EvidenceRequirement
ResultPackage
ProvenanceEnvelope
AuditReceipt
```

## Capability request

```yaml
capability_request:
  id:
  objective:
  input_contract:
  required_evidence:
  allowed_data:
  forbidden_data:
  budget:
  deadline:
  trust_level:
  return_contract:
```

## Principle

Federation should exchange:

- goals,
- capabilities,
- evidence,
- bounded inputs/outputs,

not necessarily internal prompts, memories, credentials or topology.

## Non-goal

Do not implement federation before:

- permissions,
- provenance,
- evidence contracts,
- audit,
- organization identity

are mature.
