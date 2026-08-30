# Implementation Handoffs

## Purpose

This directory is the controlled bridge from research to the production Agent Factory repository.

Research findings do **not** become product requirements automatically.

## Lifecycle

```text
proposed/
approved/
completed/
rejected/
```

### Proposed

Research has identified a potentially useful product change.

The handoff must define:
- problem,
- evidence,
- scope,
- technical approach,
- tests,
- risks.

### Approved

A product/architecture decision has accepted the change for implementation.

Approval should reference:
- canonical research synthesis,
- ADR,
- target product area.

### Completed

The implementation exists and has verification evidence.

Add:
- Agent Factory commit/PR,
- tests,
- benchmark results,
- deviations from original proposal.

### Rejected

Preserve the rejected handoff and reason.

This prevents repeated re-proposal without new evidence.

## Rule

A completed handoff is **not** the source of truth for current product behavior. Once implemented, Agent Factory code/tests/current-state docs are authoritative.
