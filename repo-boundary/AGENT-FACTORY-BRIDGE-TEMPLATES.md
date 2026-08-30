# Agent Factory Bridge Templates

Claude should create these in `agent-factory/docs/agent-army/`.

## README.md

```markdown
# Agent Army

This directory contains the production-facing bridge for Agent Army work.

Research and speculative architecture live in the separate `agent-army-research` repository.

Use this directory for current implementation facts, approved concepts and active handoffs only.
```

## RESEARCH_REPO.md

```markdown
# Research Repository

Canonical research repository: `agent-army-research`.

Research is not proof of product implementation.

Before implementing a research concept, require an approved implementation handoff.
```

## CURRENT_STATE.md

Use a table:

```text
CONCEPT | STATUS | CODE EVIDENCE | NOTES
```

Allowed status:

```text
IMPLEMENTED
PARTIAL
PLANNED
NOT IMPLEMENTED
```

## APPROVED_CONCEPTS.md

Only list concepts accepted for product implementation.

For each:

- decision date,
- supporting research,
- product ADR,
- owner,
- state.

## IMPLEMENTATION_HANDOFFS.md

List active handoffs with:

- source research file,
- target area in code,
- implementation status,
- commit/PR when complete.
```
