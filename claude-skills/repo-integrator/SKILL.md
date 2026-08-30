# Skill — Agent Army Repository Integrator

## Purpose

Safely translate an approved research handoff into the actual Agent Factory codebase.

## Procedure

1. Read the handoff.
2. Inspect the current code paths it references.
3. Verify assumptions against code.
4. Document any mismatch.
5. Reuse existing primitives before creating new ones.
6. Implement the smallest reversible slice.
7. Add typed contracts/tests.
8. Add telemetry.
9. Run relevant tests/builds.
10. update production ADR/current-state docs.

## Never

- rewrite broad subsystems because the research architecture is cleaner;
- claim a migration succeeded without tests;
- delete working compatibility paths before parity;
- import speculative research docs into product source-of-truth folders.

## Completion report

Include:
- files changed,
- behavior added,
- tests,
- benchmarks,
- remaining gaps,
- research assumptions disproven by implementation.
