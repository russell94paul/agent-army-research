# Screen Spec — Organizational Debugger

## Purpose

Explain organizational causality without exposing hidden chain-of-thought.

The debugger uses structured runtime facts:

```text
intent
compiler decision
team formation
context package
selected evidence
decision summary
tool action
artifact change
verification
outcome
```

## Layout

### Left — Breakpoints

Breakpoint classes:

- policy,
- risk,
- cost,
- evidence,
- intent,
- contention,
- human approval.

Users can enable/disable and inspect trigger history.

### Center — Causal graph

Render causal nodes ordered by time and dependency.

Allow:
- collapse by team,
- collapse by artifact,
- highlight selected decision path,
- compare alternate branch when available.

### Right — Inspector

For selected node show:
- inputs,
- constraints,
- relevant evidence,
- action/result,
- policy decision,
- links to raw artifacts.

### Bottom — Time travel

Scrub organizational state.

Jump to:
- team formation,
- first failure,
- verification,
- human intervention.

## Key tasks

- Why did this agent act?
- Which rule allowed it?
- Which evidence influenced it?
- Which artifact changed?
- What failed verification?
- What would replay change?

## Accessibility

Every causal edge requires a textual relationship.
