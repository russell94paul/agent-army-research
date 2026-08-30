---
type: moc
tags: [agent-army/implementation]
---

# Implementation Map

## Boundary

- [[../repo-boundary/RESEARCH-VS-PRODUCT]]
- [[../repo-boundary/WHAT-MOVES-TO-RESEARCH]]
- [[../repo-boundary/WHAT-STAYS-IN-AGENT-FACTORY]]
- [[../repo-boundary/SYNC-AND-HANDOFF-PROTOCOL]]

## Safe integration

- [[../implementation/00-implementation-principles]]
- [[../implementation/01-feature-flag-plan]]
- [[../implementation/02-test-strategy]]
- [[../implementation/03-data-migration-strategy]]
- [[../implementation/04-quarterly-roadmap]]

## Handoffs

- [[../implementation-handoffs/README]]
- [[../implementation-handoffs/HANDOFF_TEMPLATE]]

## Claude

- [[../handoff/CLAUDE-CREATE-RESEARCH-REPO-AND-MIGRATE]]
- [[../claude-skills/repo-integrator/SKILL]]
- [[../claude-skills/systems-architect/SKILL]]

## Graduation path

```text
research
→ synthesis
→ canonical spec
→ ADR
→ approved handoff
→ Agent Factory code
→ tests/benchmarks
→ completion evidence
```

A research note should never be used as an implicit production specification.
