# R29 — Repository-Grounded Implementation Roadmap

## Objective

Given the actual Agent Factory repository plus synthesized Agent Army research, produce a precise incremental migration plan.

This prompt is valuable only with repository access.

## Rule

Treat every research concept as a hypothesis until code and synthesis support it.

Read source, tests, schemas and runtime paths before proposing changes.

## Required current-state audit

Map:

```text
apps
packages
runtime/orchestration
sessions
agents
teams
tools
event/logging
storage
UI state
realtime transport
tests
docs
```

For every relevant existing primitive answer:

- where it lives,
- who owns it,
- persistence,
- public contracts,
- tests,
- migration risk.

## Gap analysis

Compare current repo against durable Agent Army substrate:

```text
stable entity IDs
typed organizational events
materialized world state
evidence/provenance
replay
inspectors
intent boundaries
knowledge/skill objects
```

Do not prioritize morphogenesis/evolution before the substrate.

## Strangler migration

Prefer:

```text
existing runtime
  + typed event adapter
  + shadow projection
  + Agent Army UI
```

before replacement.

## Required roadmap

Produce phases with:

- exact files/packages,
- new interfaces,
- migrations,
- feature flags,
- tests,
- observability,
- rollback,
- dependency ordering.

## First slices

Identify:

1. smallest 1–2 day proof,
2. first 2-week vertical slice,
3. first production-worthy milestone,
4. first research-only prototype.

## Removal plan

Identify research-inspired code that should **not** be added yet.

Also identify any existing experimental code that conflicts with the new architecture and should be retired only after parity.

## Required output

1. current architecture;
2. target architecture;
3. current→target diff;
4. sequenced backlog;
5. file-level change map;
6. migration strategy;
7. test plan;
8. performance budgets;
9. risks;
10. 30/60/90-day plan.

Finish with:

> What is the smallest set of changes that makes the future Agent Army architecture easier without forcing the current product to become the speculative future system?
