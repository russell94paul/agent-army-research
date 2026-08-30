# R22 — Organizational OS: Stigmergy, Fields, Morphogenesis and Autopoiesis

## Objective

Design the adaptive runtime underneath Agent Army.

Investigate whether the organization can:

- sense local state,
- coordinate indirectly,
- grow capacity,
- contract capacity,
- split,
- merge,
- specialize,
- recover,
- and eventually improve itself.

## Runtime primitives

```text
Mission
Agent
Team
Cell
Artifact
Task
Tool
Resource
Signal
Field
Evidence
Event
Policy
```

## Stigmergy

Agents deposit environmental signals onto artifacts, tasks and locations.

Example:

```text
connector.py

risk                  0.92
uncertainty           0.81
edit_contention       0.72
verification_demand   0.94
knowledge_density     0.55
```

Signals may:

- decay,
- reinforce,
- contradict,
- saturate,
- propagate,
- expire,
- carry provenance.

## Morphogenesis

Study local rules:

```text
IF uncertainty demand > research capacity
THEN grow research cell

IF verification backlog > threshold
THEN spawn temporary validator

IF duplicated effort > threshold
THEN merge teams

IF capability idle and demand absent
THEN dissolve temporary cell
```

## Autopoiesis

Define concrete software meaning:

```text
work
 ↓
signals
 ↓
behavior
 ↓
organization
 ↓
outcome
 ↓
evidence
 ↓
memory/policy adaptation
 ↓
new organization
 ↺
```

## Required output

Produce:

- runtime architecture,
- event model,
- signal/field schema,
- morphogenesis rule engine,
- homeostatic controls,
- failure modes,
- safety boundaries,
- implementation sequence.

End with:

> What is the smallest safe runtime primitive that produces useful emergent coordination?
