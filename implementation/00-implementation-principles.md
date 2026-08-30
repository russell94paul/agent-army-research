# Implementation Principles

## 1. Preserve the working product

Do not rewrite Agent Factory to match speculative Agent Army architecture.

## 2. Stabilize identity first

Cross-agent, cross-mission and replay features require canonical IDs for agents, teams, missions, artifacts and events.

## 3. Prefer typed events to log interpretation

Human-readable logs remain useful, but machine state should not depend on regex-parsing terminal output.

## 4. Materialize organizational state server-side

The browser should receive bounded snapshots/deltas rather than reconstructing the entire organization from raw history.

## 5. Business state and visual state are separate

Animation can represent state. It cannot define state.

## 6. Evidence precedes organizational learning

Capture provenance before enabling automatic knowledge/skill/doctrine promotion.

## 7. Replay precedes self-modification

If a structural decision cannot be replayed or explained, do not make it strongly autonomous.

## 8. Governance precedes authority expansion

Permissions, budgets, escalation and required verification must be explicit.

## 9. Benchmark every optimization

Context routing, fields, team adaptation and model routing have overhead. Measure net value.

## 10. Experimental mechanisms remain removable

Use adapters and feature flags.

## 11. Deterministic services beat LLM agents when appropriate

Running estimates, readiness projections, event materialization and policy checks often should be code, not conversational agents.

## 12. Verified outcomes are the product metric

Activity is telemetry, not success.
