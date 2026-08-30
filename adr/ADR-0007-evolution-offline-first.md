# ADR-0007 — Organizational Evolution Is Offline-First

## Status

PROPOSED

## Context

Optimizing agent topology, prompts, skills or policies directly against live production outcomes introduces reward hacking, instability and difficult rollback.

## Decision

Evolutionary/automated organization search begins in:

```text
simulation
→ historical replay
→ shadow
→ limited live
→ production
```

Each promotion stage has explicit criteria.

## Required provenance

Store:

- candidate genome,
- parent lineage,
- evaluation version,
- corpus version,
- metrics,
- optimizer configuration,
- promotion decision.

## Consequences

This slows autonomous optimization but creates a defensible evidence trail and makes counterfactual analysis possible.

## Exception

None for constitution or hard governance changes: those remain human-controlled.
