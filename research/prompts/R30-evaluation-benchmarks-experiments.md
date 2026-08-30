# R30 — Evaluation, Benchmarks and Experimental Science for Artificial Organizations

## Objective

Design an evaluation system capable of proving whether Agent Army's organizational mechanisms actually improve outcomes.

The benchmark must not reward theatrical activity.

## Primary outcome categories

Evaluate:

```text
verified correctness
mission completion
latency
cost
robustness
human intervention
adaptability
reproducibility
knowledge quality
organizational stability
```

## Benchmark corpus

Design mission classes including:

- connector migration,
- schema/data migration,
- bug repair,
- incident diagnosis,
- unfamiliar repository investigation,
- feature implementation,
- release verification,
- data-quality correction,
- research/synthesis.

Every mission should have a verification contract.

## Organizational mechanisms to isolate

Create experiments for:

- direct messaging vs stigmergic coordination,
- fixed team vs adaptive formation,
- full context vs context packages,
- single horizon vs temporal echelons,
- task agents only vs staff mesh,
- no doctrine vs tested doctrine,
- idle-agent routing vs capability readiness,
- manual topology vs evolutionary candidates,
- dashboard vs Command World.

## Experimental rigor

For each mechanism require:

```text
hypothesis
baseline
variant
dataset/corpus version
primary metric
secondary metrics
ablation
confounders
sample plan
acceptance criterion
rejection criterion
```

## Reward-hacking defense

Identify metrics that can be gamed.

Examples:

- more agents,
- more messages,
- more diagnoses,
- more generated artifacts,
- self-reported confidence.

Prefer externally verified state change.

## Simulation validity

For Evolution Chamber work, research sim-to-real risk.

Determine which mission properties must be preserved in historical replay for optimization results to transfer.

## Statistical reporting

Recommend confidence intervals/effect sizes appropriate to benchmark volume.

Do not require statistical machinery that the sample size cannot support.

## Required output

Produce:

1. benchmark architecture;
2. mission corpus schema;
3. verification contract;
4. metric definitions;
5. experiment templates;
6. anti-gaming checks;
7. regression dashboard design;
8. promotion thresholds for experimental features;
9. simulation-validity protocol;
10. first 10 experiments to run.

End with:

> What evidence would be sufficient to justify enabling an adaptive organizational mechanism in real product workflows?
