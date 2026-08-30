# R21 — Collective Cognition: Knowledge, Skills, Learning and Expertise

## Objective

Design the intelligence substrate of Agent Army.

Do not call everything "memory."

Define how an artificial organization knows, learns and teaches.

## Core primitives

Research and define:

```text
Observation
Claim
Evidence
Belief
Knowledge
Experience
Lesson
Skill
Procedure
Policy
Doctrine
Pattern
Capability
Expertise
Decision
Outcome
```

For each define:

- lifecycle,
- provenance,
- confidence,
- contradiction handling,
- decay,
- versioning,
- permissions,
- storage,
- retrieval,
- UI representation.

## Critical problem

Ten agents repeating the same source should not count as ten independent confirmations.

Design provenance-aware epistemics.

## Skill lifecycle

```text
experience
  ↓
candidate skill
  ↓
test
  ↓
verify
  ↓
publish
  ↓
reuse
  ↓
measure
  ↓
refine / retire
```

## Agent-to-agent learning

Research:

- messaging,
- shared memory,
- artifact-mediated learning,
- skill publication,
- knowledge graphs,
- pub/sub,
- stigmergy,
- context packaging,
- state-aware transmission protocols.

Answer:

```text
Who should share what with whom, when, at what detail, for how long, with what trust, at what token cost?
```

## Required output

Produce:

- epistemic data model,
- knowledge graph model,
- skill registry design,
- capability graph design,
- expertise model,
- knowledge health metrics,
- UI views,
- storage/retrieval architecture,
- implementation phases.

End with:

> What must Agent Army store today so agents can genuinely learn from one another tomorrow?
