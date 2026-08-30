# R29 — Repository Integration and Implementation Roadmap

## Required context

Attach the current Agent Factory repository.

Do not design a greenfield rewrite.

Read the code.

## Objective

Create an incremental implementation plan moving the current system toward Agent Army.

## Inspect

- frontend,
- backend,
- agent runtime,
- session manager,
- events,
- state management,
- storage,
- memory,
- knowledge,
- task/mission schemas,
- team schemas,
- tool abstraction,
- sandboxing,
- verification,
- UI components.

Cite actual files and lines where possible.

## Proposed early sequence to test

```text
1. canonical entity IDs
2. durable typed events
3. materialized organizational world state
4. artifact-centric evidence/provenance
5. timeline/replay
6. agent/team/artifact inspectors
7. knowledge/skill objects
8. field overlays
9. adaptive routing
10. simulation
11. morphogenesis
12. evolution
```

## Required output

Produce:

- current architecture diagram,
- target architecture diagram,
- gap analysis,
- file-by-file integration map,
- schemas,
- APIs,
- migration phases,
- test strategy,
- rollback strategy,
- implementation tickets,
- first 2-week build slice.

End with:

> What is the smallest useful code change that unlocks the future architecture?
