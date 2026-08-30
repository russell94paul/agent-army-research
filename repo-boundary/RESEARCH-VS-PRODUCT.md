# Research Repository vs Product Repository

## Decision

Use **two sibling repositories**.

```text
workspace/
├── agent-factory/
└── agent-army-research/
```

## Agent Army Research owns

- foundational research,
- Deep Research prompts,
- research answers,
- literature notes,
- hypotheses,
- speculative architecture,
- ontology development,
- experiments,
- UI concept exploration,
- whitepaper work,
- long-horizon roadmaps,
- research ADRs,
- implementation handoff preparation.

## Agent Factory owns

- production code,
- tested schemas used by the application,
- current runtime architecture,
- production ADRs,
- implementation-specific docs,
- release/runbook material,
- product tests,
- migrations,
- operational telemetry contracts.

## Bridge

Agent Factory should retain:

```text
docs/agent-army/
├── README.md
├── CURRENT_STATE.md
├── APPROVED_CONCEPTS.md
├── IMPLEMENTATION_HANDOFFS.md
└── RESEARCH_REPO.md
```

The bridge prevents two bad outcomes:

1. speculative research becoming mistaken for implemented architecture;
2. production engineers losing access to the rationale behind approved concepts.

## Graduation rule

A concept graduates from research to product only through:

```text
Research
→ Evidence
→ Synthesis
→ Canonical research spec
→ ADR / decision
→ Approved implementation handoff
→ Product implementation
→ Verification
```

## Never automatically synchronize directories

The repos have different truth semantics.

Research edits should not overwrite product docs.

Use explicit handoffs and commits.
