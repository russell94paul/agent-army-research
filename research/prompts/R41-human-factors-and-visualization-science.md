# R41 — Human Factors and Visualization Science for the Command World

## Objective

Determine whether a living spatial representation of an artificial organization actually improves operator comprehension over conventional dashboards, tables and graphs.

The desired UI may be cinematic and premium, but **legibility is the primary requirement**.

## Research domains

Study:

- visual analytics,
- spatial cognition,
- semantic zoom,
- graph visualization,
- distributed tracing UI,
- network operations centers,
- incident command interfaces,
- RTS/city-builder interfaces,
- change blindness,
- attentional load,
- animated transitions,
- accessibility,
- large-canvas performance.

## Core operator tasks

A user should quickly answer:

```text
What is happening?
What is important?
What is blocked?
Why did this action occur?
Where is uncertainty?
What does the organization know?
What needs human attention?
Which capability is not ready?
What evidence proves completion?
```

## Spatial hypotheses to test

Potential encodings:

```text
district/building     system/artifact domain
agent movement        actual work transition
route flow            dependency/handoff/context supply
formation             team topology
fog of war            epistemic coverage
heat field            risk/uncertainty/contention
lock                   verification
traffic                queue pressure
```

Identify which mappings are intuitive versus misleading.

## Stable geography

Research spatial stability.

The operator should develop spatial memory; routine state updates should not reshuffle the world.

Compare:

- manually anchored layout,
- hierarchical layout,
- semantic layout,
- force layout,
- hybrid.

## Semantic zoom

Define LOD levels.

Example:

```text
L0 organization
L1 missions/domains
L2 teams/services
L3 agents/artifacts
L4 causal/evidence detail
```

What must disappear or aggregate at each level?

## Motion

Determine when motion improves change comprehension and when it creates noise.

No animation may be the only channel for important information.

## Experimental comparison

Prototype:

A. dense dashboard/table,
B. graph/control room,
C. Command World.

Test tasks:

- locate blocker,
- explain agent action,
- detect duplicate work,
- find stale knowledge,
- find unverified output,
- identify readiness bottleneck.

Measure:

- task time,
- accuracy,
- navigation count,
- confidence,
- subjective cognitive load.

## Required output

1. visualization principles;
2. recommended spatial model;
3. LOD system;
4. motion grammar;
5. uncertainty/evidence encodings;
6. accessibility rules;
7. performance constraints;
8. prototype experiment;
9. anti-patterns;
10. go/no-go criteria for immersive world UI.

Finish with:

> Which parts of Agent Army deserve spatial representation, and which should remain conventional high-precision UI?
