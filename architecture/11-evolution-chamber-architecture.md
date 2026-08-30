# Evolution Chamber Architecture

## Purpose

Explore organization designs safely using historical missions, simulations and shadow evaluation.

The Evolution Chamber is intentionally separated from live production control.

## Flow

```text
Production Event History
       ↓
Sanitized / Versioned Replay Corpus
       ↓
Simulation Runner
       ↓
Organization Candidate Generator
       ↓
Evaluation
       ↓
Candidate Registry
       ↓
Shadow Promotion
       ↓
Limited Live
```

## Candidate genome

May include:

```text
role mix
agent count
communication topology
model assignment
skills
context policy
review depth
routing policy
spawn/merge/dissolve rules
verification strategy
resource policy
```

Must **not** include unrestricted mutation of:
- constitution,
- hard permissions,
- audit rules.

## Candidate record

Store:
- candidate ID/version,
- parent lineage,
- genome diff,
- optimizer configuration,
- evaluation corpus version,
- metric vector,
- failures,
- promotion history.

## Evaluation

Prefer multi-objective / quality-diversity views rather than one opaque fitness score.

Metrics may include:
- verified success,
- cost,
- latency,
- robustness,
- intervention,
- communication overhead.

## Promotion gates

```text
offline simulation
→ historical replay
→ shadow
→ limited live
→ production
```

## Risks

- reward hacking,
- overfitting corpus,
- simulation mismatch,
- organizational churn,
- unexplained topology.

All require explicit tests before production promotion.
