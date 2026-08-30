# Performance Reference Architecture

## Runtime

```text
Execution
  ↓
typed events
  ↓
durable log
  ↓
incremental materializers
  ↓
mission/org projections
  ↓
realtime delta stream
  ↓
client world state
```

## Context

```text
Knowledge Store
Artifact Index
Skill Registry
Mission State
      ↓
Context Compiler
      ↓
small mission-specific ContextPackage
      ↓
Agent
```

## Performance principles

- sparse fields,
- incremental state,
- top-K local context,
- shared validated results,
- deduplicated retrieval,
- LOD rendering,
- event coalescing,
- worker-based layout/rendering if needed,
- no raw-log reconstruction in browser.

## Benchmarks

Track:

- tokens per verified task,
- messages per verified task,
- repeated retrieval rate,
- context waste,
- state-update latency,
- renderer frame time,
- event backlog,
- memory.
