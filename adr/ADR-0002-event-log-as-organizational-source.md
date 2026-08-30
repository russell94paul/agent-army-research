# ADR-0002 — Typed Organizational Event Log

## Status

PROPOSED

## Context

Agent Army requires replay, causal debugging, multiple UI projections and reliable reconstruction of organizational state. Terminal output and ad-hoc logs are too ambiguous to serve as the long-term integration contract.

## Decision

Introduce a typed, versioned organizational event stream.

The event stream records meaningful state transitions, while raw execution logs remain available separately for diagnostics.

Examples:

```text
mission.created
intent.accepted
agent.started
team.formed
artifact.read
artifact.changed
claim.created
evidence.attached
verification.completed
policy.blocked
```

## Consequences

### Positive

- deterministic materialization,
- replay,
- better observability,
- lower UI coupling to runtime internals.

### Negative

- schema governance,
- migration/versioning burden,
- additional write path.

## Migration

Begin dual-write/shadow-only. Do not replace current telemetry until parity is demonstrated.

## Reversal

Consumers can be returned to current telemetry while event emission remains non-authoritative.
