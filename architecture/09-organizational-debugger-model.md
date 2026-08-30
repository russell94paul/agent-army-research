# Organizational Debugger Model

## Goal

Make organizational causality reconstructable without storing or exposing private hidden reasoning.

## Causal trace

```text
Mission Intent
    ↓
Compiler Decision
    ↓
Team Formation
    ↓
Context Package
    ↓
Knowledge / Evidence Selection
    ↓
Structured Decision Summary
    ↓
Tool Action
    ↓
Artifact Change
    ↓
Verification
    ↓
Outcome
```

## Required event relationships

Events should support:

- `caused_by`,
- `depends_on`,
- `produced`,
- `used_evidence`,
- `constrained_by`,
- `verified_by`.

## Breakpoints

```text
policy
risk
cost
evidence
intent
contention
human approval
```

Example:

```yaml
breakpoint:
  when:
    action_class: production_write
    evidence_sufficiency_below: threshold
  action:
    pause_and_escalate
```

## Debugger data

Store:
- action inputs,
- selected artifacts/evidence,
- applicable constraints,
- structured rationale/decision summary,
- result,
- verification.

Do not depend on hidden chain-of-thought.

## Replay

The debugger should reconstruct organizational state at a sequence/time and jump to causally important transitions.

## Success metric

Reduce time required to answer "why did the organization do this?" and "which assumption caused the failure?"
