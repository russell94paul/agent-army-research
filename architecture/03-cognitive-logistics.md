# Cognitive Logistics

## Purpose

Treat context, skills, tools, compute, models and permissions as supplies.

Agents should not receive giant context dumps.

They should receive mission-ready context packages.

## Supplies

```text
context
knowledge
skills
tools
permissions
models
tokens
compute
sandboxes
API quotas
human attention
verification capacity
```

## Context package

```ts
export interface ContextPackage {
  id: string;
  missionId: string;
  recipientAgentId: string;

  intentContractId: string;
  artifactScope: string[];
  knowledgeRefs: string[];
  skillRefs: string[];
  evidenceRefs: string[];
  activeFieldRefs: string[];

  constraints: string[];
  toolPermissions: string[];
  verificationRequirements: string[];

  tokenBudget?: number;
  expiresAt?: string;
}
```

## Capability readiness

```yaml
capability_readiness:
  capability: schema_migration
  readiness: 0.83
  available_agents: true
  required_skill: true
  fresh_knowledge: true
  repo_indexed: true
  test_sandbox: true
  credentials: true
  validator_available: false
  blocker: verification_capacity
```

## Metrics

Track:

```text
context waste
knowledge cache hit
duplicate retrieval
context delivery latency
tool utilization
token usage
model utilization
capability readiness
verification capacity
```
