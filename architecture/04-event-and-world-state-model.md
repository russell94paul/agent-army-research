# Event and World State Model

## Principle

The browser should not reconstruct the organization from raw logs.

Use:

```text
Runtime Events
   ↓
Durable Event Log
   ↓
World State Materializer
   ↓
Derived Projections
   ↓
Realtime Deltas
   ↓
UI
```

## Event examples

```text
MissionCreated
IntentContractCreated
AgentSpawned
AgentAssigned
TeamFormed
ArtifactOpened
ToolCalled
ClaimCreated
EvidenceAttached
KnowledgeValidated
SkillUsed
RiskSignalDeposited
FieldUpdated
VerificationFailed
VerificationPassed
TeamSplit
TeamMerged
AgentRetired
DoctrinePromoted
PolicyViolationDetected
```

## Event schema

```ts
export interface OrgEvent<T = unknown> {
  id: string;
  type: string;
  timestamp: string;
  missionId?: string;
  organizationId?: string;
  actorId?: string;
  targetId?: string;
  payload: T;
  causality?: {
    parentEventId?: string;
    traceId?: string;
    decisionId?: string;
  };
}
```

## World state

```ts
export interface OrganizationalWorldState {
  organizationId: string;
  missions: Record<string, MissionState>;
  agents: Record<string, AgentState>;
  teams: Record<string, TeamState>;
  artifacts: Record<string, ArtifactState>;
  fields: Record<string, FieldState>;
  claims: Record<string, ClaimState>;
  evidence: Record<string, EvidenceState>;
  capabilities: Record<string, CapabilityState>;
  skills: Record<string, SkillState>;
  policies: Record<string, PolicyState>;
  updatedAt: string;
}
```
