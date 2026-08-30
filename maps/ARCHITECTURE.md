---
type: moc
tags: [agent-army/architecture]
---

# Architecture Map

## Target stack

- [[../architecture/00-target-architecture]]

## Intent / compilation

- [[../architecture/01-intent-contract-schema]]
- [[../architecture/08-organization-compiler-pipeline]]
- [[../research/prompts/R42-organizational-dsl-and-org-ir]]

## Runtime / world state

- [[../architecture/04-event-and-world-state-model]]
- [[../architecture/12-performance-reference-architecture]]
- [[../architecture/02-organizational-staff-mesh]]
- [[../architecture/05-temporal-echelons]]

## Knowledge / capability

- [[../architecture/03-cognitive-logistics]]
- [[../architecture/06-knowledge-evidence-model]]
- [[../architecture/07-skill-capability-doctrine-model]]

## Observability

- [[../architecture/09-organizational-debugger-model]]
- [[../research/prompts/R26-observability-debugger-profiler]]

## Long-horizon

- [[../architecture/11-evolution-chamber-architecture]]
- [[../architecture/10-federation-protocol-draft]]

## Dependency intuition

```text
identity/events
→ world state/replay
→ evidence/knowledge
→ intent/capability
→ adaptive routing/staff
→ simulation
→ evolution/federation
```

Do not reverse this sequence merely because the later ideas are more visually exciting.
