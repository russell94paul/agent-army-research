# Sync and Handoff Protocol

## Research → Product

Create a file in:

```text
implementation-handoffs/approved/
```

with:

- problem,
- user value,
- research basis,
- decision/ADR,
- proposed product objects,
- migration plan,
- acceptance tests,
- observability,
- rollback,
- explicitly deferred ideas.

Then link it from Agent Factory's:

```text
docs/agent-army/IMPLEMENTATION_HANDOFFS.md
```

## Product → Research

When implementation produces new facts, benchmarks or failures:

1. record them in the product repo;
2. create a research observation or experiment result;
3. update the hypothesis ledger;
4. do not rewrite historical research answers.

## Cross-repo references

Prefer stable repository-relative references plus commit SHA in formal handoffs.

Example:

```text
agent-factory@abc1234
packages/runtime/src/events.ts
```

## Cadence

Recommended monthly research synthesis:

- what changed,
- what was falsified,
- what graduated,
- what should be removed,
- what the next research wave should test.
