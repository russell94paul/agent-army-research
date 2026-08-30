# ADR-0005 — Typed Epistemic Objects

## Status

PROPOSED

## Context

Undifferentiated "memory" makes it easy for observations, guesses, repeated claims and validated knowledge to become indistinguishable.

## Decision

Represent at least these separately:

```text
Observation
Claim
Evidence
KnowledgeObject
Experience
Skill
Doctrine
```

## Key distinction

A claim does not become knowledge because several agents repeat it.

Evidence must retain source provenance and, where possible, source independence.

## Consequences

### Positive

- inspectable uncertainty,
- safer learning,
- better knowledge debugging,
- promotion pipelines.

### Negative

- more schema complexity,
- curation requirements.

## Migration

Existing memory records should initially be imported as unverified/legacy objects unless their provenance supports a stronger classification.
