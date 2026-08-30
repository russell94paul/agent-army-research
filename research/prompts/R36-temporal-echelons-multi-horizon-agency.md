# R36 — Temporal Echelons: Multi-Horizon Agency

## Objective

Investigate separating organizational cognition by time horizon.

Hypothesis:

```text
NOW
executes current work

NEXT
prepares near-future dependencies

LATER
anticipates blockers, research and alternatives
```

This may prevent the organization from becoming entirely reactive.

## Research analogues

- military current/future operations,
- model predictive control,
- rolling-horizon planning,
- operations research,
- pipeline scheduling,
- speculative execution,
- lookahead planning,
- receding horizon control.

## Questions

1. Should NOW/NEXT/LATER be agents, services, queues or views?
2. How does information move between horizons?
3. What synchronization cadence prevents drift?
4. How do we avoid wasteful speculative work?
5. Which mission types benefit?
6. Can this reduce critical-path latency?
7. Can future planning be precomputed cheaply?

## Experiment design

Compare:

```text
single planning horizon
vs
NOW + NEXT
vs
NOW + NEXT + LATER
```

Measure:

- idle time,
- critical-path latency,
- wasted work,
- token cost,
- re-planning frequency,
- intervention.

## UI

Design a temporal organizational view:

```text
PAST          NOW           NEXT          LATER
evidence   execution      staging       anticipation
```

## Required output

Architecture, synchronization rules, state model, experiments, UI, failure modes and recommendation.
