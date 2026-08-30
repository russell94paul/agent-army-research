# R38 — The Living General Staff: Persistent Organizational Cognition

## Objective

Investigate a persistent organizational awareness layer separate from task agents.

Potential staff functions:

```text
Capability Staff
Intelligence Staff
Current Operations Staff
Future Plans Staff
Cognitive Logistics Staff
Communications Staff
Governance Staff
```

These need not all be LLM agents.

Some may be deterministic projections.

## Core primitive: Running Estimate

Each staff function continuously maintains a structured assessment relevant to its responsibility.

Example:

```text
INTELLIGENCE RUNNING ESTIMATE

Knowledge coverage        82%
Critical unknowns           4
Contradictions               2
Stale findings              11
Verification gaps            3

Assessment:
Schema uncertainty is the primary mission constraint.
```

## Questions

1. Which staff functions are useful?
2. Which should be services rather than agents?
3. How frequently should estimates update?
4. What data feeds each estimate?
5. How should estimates influence routing?
6. How do we avoid duplicating observability infrastructure?
7. Can a "Common Organizational Picture" become the primary shared state?

## Compare with

- blackboard systems,
- digital twins,
- command-and-control staff functions,
- control planes,
- SRE control rooms,
- materialized views,
- knowledge graphs.

## Required output

Staff taxonomy, running-estimate schemas, update architecture, world-state integration, UI, performance cost and MVP.
