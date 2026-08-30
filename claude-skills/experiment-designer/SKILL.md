# Skill — Artificial Organization Experiment Designer

## Purpose

Turn an exciting organizational mechanism into a falsifiable experiment.

## Required fields

```text
hypothesis
baseline
variant
mission corpus
independent variable
primary metric
secondary metrics
confounders
ablation
sample plan
acceptance criterion
rejection criterion
failure interpretation
```

## Metric priority

Prefer:
- verified success,
- correctness,
- latency,
- cost,
- robustness,
- human intervention.

Treat:
- agent count,
- messages,
- tool calls,
- animations

as diagnostic metrics only.

## Anti-bias requirements

- holdout missions where possible;
- compare against simple baselines;
- measure overhead of the mechanism itself;
- record negative results;
- do not optimize and evaluate on the same entire corpus.
