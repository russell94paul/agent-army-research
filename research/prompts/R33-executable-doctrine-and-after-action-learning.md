# R33 — Executable Doctrine and After-Action Learning

## Objective

Design a learning loop where mission experience becomes tested, versioned, executable organizational doctrine.

## Core loop

```text
MISSION
  ↓
OUTCOME
  ↓
AFTER ACTION REVIEW
  ↓
LESSON CANDIDATES
  ↓
EVIDENCE
  ↓
REPLAY TESTING
  ↓
DOCTRINE CANDIDATE
  ↓
SIMULATION
  ↓
PROMOTION
  ↓
EXECUTABLE DOCTRINE
```

## Key distinction

Memory stores what happened.

Doctrine changes what the organization does next time.

## Research questions

1. How do organizations turn experience into procedures?
2. How can AI organizations avoid learning bad lessons?
3. How should lessons be tested before promotion?
4. How does doctrine differ from policy, skill, memory and strategy?
5. How can doctrine be versioned, diffed and rolled back?
6. Can doctrine be compiled into mission plans and organization topologies?

## Doctrine object

Design:

```yaml
doctrine:
  id:
  version:
  mission_classes:
  rule:
  rationale:
  supporting_evidence:
  tests:
  performance_history:
  known_failure_modes:
  owner:
  status:
```

## UI

Design:

- Doctrine Library,
- Doctrine Diff,
- Lesson Candidate Queue,
- After Action Review Surface,
- Doctrine Impact View,
- Doctrine Simulation Result,
- Doctrine Rollback.

## Required output

Produce:

- doctrine lifecycle,
- schemas,
- testing strategy,
- promotion pipeline,
- governance controls,
- UI designs,
- repo integration plan.

End with:

> How does Agent Army learn procedures without turning every anecdote into a permanent rule?
