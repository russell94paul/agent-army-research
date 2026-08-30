---
type: moc
tags: [agent-army/experiments]
---

# Experiments Map

## Program

- [[../experiments/00-experiment-plan]]
- [[../experiments/01-benchmark-mission-corpus]]
- [[../experiments/02-experiment-matrix]]
- [[../experiments/03-organizational-chaos-tests]]
- [[../research/prompts/R30-evaluation-benchmarks-experiments]]

## Simulation/evolution

- [[../architecture/11-evolution-chamber-architecture]]
- [[../research/prompts/R24-evolution-simulation-counterfactuals]]

## Primary experimental rule

Measure **verified outcomes**, not organizational activity.

Preferred metrics:

```text
verified success
correctness
latency
cost
robustness
human intervention
```

Diagnostic-only metrics include:

```text
agent count
message count
tool calls
generated artifacts
```

## Experiment lifecycle

```text
hypothesis
→ baseline
→ controlled variant
→ evaluation
→ replication/ablation
→ synthesis
→ architecture decision
```

Negative results belong in the vault.
