# Organizational Staff Mesh

## Purpose

Agents execute work.

Staff functions maintain organizational awareness.

This avoids overloading task agents with every aspect of the mission.

## Staff functions

```text
Capability Staff
  Who can do what?

Intelligence Staff
  What do we know? What is uncertain?

Current Operations Staff
  What is happening now?

Future Plans Staff
  What should be prepared next?

Cognitive Logistics Staff
  What context, skills, tools, compute and permissions are needed?

Communications Staff
  Who needs what information?

Governance Staff
  Are actions within policy and intent?
```

## Running estimates

Each staff function maintains a running estimate.

Example:

```yaml
running_estimate:
  staff: intelligence
  mission_id: migrate-stripe
  coverage:
    repo: 0.82
    schema: 0.61
    tests: 0.74
  critical_unknowns:
    - pagination semantics
    - historical boundary behavior
  contradictions:
    - claim_id: C119
  recommendation:
    - expand schema research before implementation
```

## Common Organizational Picture

All estimates roll into a shared world model.

```text
Staff Estimates
      ↓
Organizational World State
      ↓
Command World UI
      ↓
Agent Context Packages
      ↓
Mission Decisions
```

## Implementation note

Not every staff function needs to be an LLM agent.

Many can be deterministic services or projections over the event log.
