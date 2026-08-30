# Organizational Chaos Tests

## Purpose

Test whether the artificial organization detects, contains and recovers from realistic failures.

## Failure injections

### Execution

- agent dies mid-task,
- sandbox terminates,
- tool becomes unavailable,
- model request repeatedly fails.

### Coordination

- duplicate agents assigned,
- dependency event delayed,
- handoff lost,
- validator capacity exhausted.

### Knowledge

- stale knowledge inserted,
- contradictory evidence appears,
- five agents repeat one incorrect root source,
- skill references deprecated procedure.

### Governance

- action exceeds budget,
- agent lacks permission,
- doctrine conflicts with mission invariant,
- adaptive team tries to self-escalate authority.

### Performance

- event burst,
- projection lag,
- retrieval overload,
- API rate limit.

## Metrics

Measure:

```text
detection latency
containment
recovery time
incorrect propagation
human escalation
mission success
data integrity
cost of recovery
```

## Required result

For each test record:

- injected fault,
- expected detection path,
- observed path,
- failed controls,
- recovery,
- follow-up architecture change.

Chaos tests should be reproducible fixtures, not one-off demonstrations.
