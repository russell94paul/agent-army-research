# ADR-0003 — Materialized Organizational World State

## Status

PROPOSED

## Context

A Command World UI cannot efficiently parse an unbounded raw event history on every client. Different screens also require consistent views of missions, teams, artifacts, fields and alerts.

## Decision

Materialize canonical backend projections from typed organizational events.

Clients receive:

- initial snapshot,
- incremental deltas,
- version/sequence markers.

## Consequences

### Positive

- bounded client work,
- consistent multi-surface state,
- easier semantic zoom,
- replayable projections.

### Negative

- materializer complexity,
- projection lag must be measured,
- rebuild semantics must be defined.

## Constraint

The projection is derived state. The durable event source remains the reconstructable history where feasible.

## Validation

Rebuild a projection from an event fixture and compare against persisted projection output.
