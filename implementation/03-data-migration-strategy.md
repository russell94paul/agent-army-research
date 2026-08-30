# Data Migration Strategy

## Goal

Introduce Agent Army primitives without rewriting the current Agent Factory persistence model.

## Phase 1 — Identity

Map existing:

```text
session
agent
task
run
artifact
tool execution
```

to stable canonical IDs.

Do not backfill semantics that historical data does not prove.

## Phase 2 — Dual-write events

Emit typed organizational events alongside current telemetry.

Validate event parity.

## Phase 3 — Shadow world state

Build materialized organization projections without changing current product behavior.

Compare:

- entity counts,
- status,
- active work,
- artifact associations,
- completion.

## Phase 4 — Agent Army reads

The new UI may consume the new projections while old surfaces remain unchanged.

## Phase 5 — Shared services

Only after parity, migrate common consumers deliberately.

## Historical backfill

Classify historical fields:

```text
EXACT
DERIVABLE
HEURISTIC
UNAVAILABLE
```

Never label heuristic reconstruction as observed fact.

## Rollback

Dual-write architecture allows disabling the new projection while preserving old runtime behavior.

## Data retention

Typed events, evidence and knowledge may have different retention requirements. Define them explicitly before large-scale capture.
