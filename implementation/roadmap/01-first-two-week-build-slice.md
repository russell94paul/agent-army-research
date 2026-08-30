# First Two-Week Build Slice

## Goal

Create the minimum useful Agent Army substrate and UI surface.

## Build slice

### Backend / shared

- define canonical entity interfaces:
  - Organization,
  - Mission,
  - Agent,
  - Team,
  - Artifact,
  - OrgEvent.
- create typed event examples.
- create materialized world-state mock/projection.
- expose endpoint or local data source for UI.

### Frontend

- Command World shell,
- operations rail,
- metrics header,
- world viewport,
- right inspector,
- bottom timeline,
- lens selector.

### Inspectors

- Agent Inspector,
- Team Inspector,
- Artifact Inspector.

### Events

Support structured events:

```text
AgentAssigned
ArtifactOpened
ToolCalled
EvidenceProduced
VerificationPassed
VerificationFailed
RiskChanged
```

### Acceptance criteria

User can:

- open Agent Army page,
- see missions,
- see agents and artifacts,
- select objects,
- inspect current state,
- view event timeline,
- switch basic lenses,
- understand what is happening without reading logs.

## Explicit non-goals

- no autonomous team growth,
- no evolution,
- no complex field engine,
- no production decisions,
- no federation,
- no real doctrine compiler.
