# Temporal Echelons Architecture

## Goal

Separate execution and future preparation.

```text
NOW
  current execution

NEXT
  stage near-future dependencies

LATER
  research likely blockers and alternatives
```

## State

```ts
type Horizon = "now" | "next" | "later";

interface HorizonWorkItem {
  id: string;
  missionId: string;
  horizon: Horizon;
  objective: string;
  dependencies: string[];
  promotionCriteria: string[];
  expiry?: string;
}
```

## Promotion

```text
LATER → NEXT
when relevance becomes sufficiently likely.

NEXT → NOW
when dependency gates are satisfied.
```

## Guardrail

Speculative work must have:

- budget,
- expiry,
- relevance threshold,
- cancellation path.

## Metrics

- critical-path idle time,
- speculative waste,
- promotion accuracy,
- setup latency,
- replanning frequency.
