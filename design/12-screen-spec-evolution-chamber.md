# Screen Spec — Evolution Chamber

## Purpose

Evaluate and compare organizational variants without confusing simulation success with production readiness.

## Candidate population

Each candidate summarizes:

```text
organization version
topology
agent/model mix
skills
communication policy
verification depth
resource policy
parent lineage
```

## Quality-diversity view

Allow selectable axes such as:

- verified success,
- cost,
- latency,
- robustness,
- intervention.

Do not imply that one scalar "fitness" captures every tradeoff.

## Candidate comparison

Compare:

```text
CURRENT ORGANIZATION
vs
CANDIDATE
```

Show:
- structural diff,
- policy diff,
- expected resource change,
- per-mission replay outcomes,
- failures,
- confidence/coverage.

## Promotion pipeline

Candidate states:

```text
GENERATED
SIMULATION
HISTORICAL REPLAY
SHADOW
LIMITED LIVE
PRODUCTION
REJECTED
```

Each state shows entry/exit criteria.

## Guardrails

No direct generation → production path.

Constitution, hard permissions and human approval rules are outside the evolutionary genome.

## Operator tasks

- understand why candidate differs,
- identify which missions improved/worsened,
- inspect lineage,
- promote/reject,
- replay a failure.
