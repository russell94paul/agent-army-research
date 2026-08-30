# Claude Implementation Boot Prompt

You are working inside the existing Agent Factory repository.

The long-term product vision is:

# Agent Army — an Artificial Organization Engineering Platform

Do not attempt to implement the full vision.

## Current priority

Find the smallest code changes that:

1. improve the product today,
2. preserve current behavior,
3. support future organizational observability,
4. support evidence/provenance,
5. support replay,
6. avoid speculative complexity.

## Strong candidates

Investigate:

- canonical organization/mission/agent/team/artifact identity,
- durable typed events,
- materialized organizational world state,
- evidence/provenance,
- agent/team/artifact inspectors,
- timeline/replay,
- basic Command World projection.

## Do not implement yet

- autonomous morphogenesis,
- self-evolving organizations,
- production evolutionary search,
- uncontrolled stigmergic coordination,
- federated external organizations.

## Required process

1. Read the repository.
2. Map current architecture.
3. Identify reusable components.
4. Identify least invasive extension points.
5. Propose a small implementation slice.
6. Define tests and acceptance criteria.
7. Implement incrementally.
8. Preserve backward compatibility.
9. Use feature flags.
10. Record architectural decisions.

## Every feature must answer

```text
What user problem does this solve?
What data does it require?
Where does it live?
How is it observed?
How is it verified?
What is its failure mode?
What does it unlock later?
```

Build the substrate first.
