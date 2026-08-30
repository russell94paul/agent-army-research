# ADR-0001 — Keep Agent Army Research Separate but in the Same Repository

## Status

Proposed.

## Context

Agent Army contains long-term speculative concepts:

- organizational autopoiesis,
- morphogenetic teams,
- evolution chamber,
- federated agent armies,
- executable doctrine,
- artificial organization engineering.

The current Agent Factory implementation is more immediate and practical.

## Decision

Keep Agent Army research in:

```text
docs/agent-army/
```

inside the current repo.

Do not mix speculative research into active app/package folders until validated.

## Consequences

Positive:

- research remains grounded in real code,
- easier to graduate concepts into implementation,
- avoids greenfield drift,
- keeps product vision near execution substrate.

Negative:

- repo docs may grow large,
- future/currents specs could be confused without discipline.

## Guardrail

Every implementation file or ticket must be labeled:

```text
NOW
NEXT
LATER
RESEARCH ONLY
DO NOT BUILD
```
