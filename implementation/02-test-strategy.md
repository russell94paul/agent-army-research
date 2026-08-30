# Test Strategy

## Goal

Test both software correctness and organizational behavior.

## Unit tests

Cover:

- event schema validation,
- materializer transitions,
- provenance graph operations,
- intent constraint checks,
- capability readiness,
- field decay/reinforcement,
- Org-IR validation,
- doctrine applicability,
- context-package budget rules.

## Integration tests

Verify:

```text
runtime → typed event log
event log → materialized world state
world state → realtime client projection
mission intent → compiler → executable plan
action → evidence → verification
experience → knowledge candidate
```

## End-to-end mission tests

Minimum path:

1. create mission,
2. compile organization/team,
3. execute bounded work,
4. emit evidence,
5. verify outcome,
6. inspect timeline,
7. replay,
8. generate after-action result.

## Organizational regression suite

Any change to:

```text
topology
routing
skill
model assignment
policy
doctrine
verification
context packaging
```

should be tested against a versioned historical mission corpus where feasible.

## UI tests

Measure both correctness and operator comprehension.

- semantic state has accessible text;
- animation does not encode unique information;
- replay reaches same state;
- high-density views retain interaction performance.

## Failure tests

Use `experiments/03-organizational-chaos-tests.md`.

## Test evidence

Every approved implementation handoff must identify the exact tests proving completion.
