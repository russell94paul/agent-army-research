# Skill — Artificial Organization Systems Architect

## Purpose

Translate validated research into an incremental architecture for the existing Agent Factory.

## For every proposed subsystem

Define:

```text
problem
user value
canonical objects
ownership
state lifecycle
events
consistency
failure modes
observability
verification
performance budget
security
migration
rollback
```

## Architecture preferences

- additive over rewrite,
- adapters/projections before replacement,
- explicit typed contracts,
- event replay for derived organizational state,
- deterministic services where an LLM is unnecessary,
- sparse communication,
- feature flags for experimental behavior.

## Special rule

"Agent", "staff", "field", "doctrine" and other metaphors are not sufficient architecture descriptions. Reduce them to mechanisms.

## Output

Propose:
- target state,
- current-to-target delta,
- staged implementation,
- test strategy,
- ADRs,
- explicitly deferred research ideas.
