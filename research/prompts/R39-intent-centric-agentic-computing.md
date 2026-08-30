# R39 — Intent-Centric Agentic Computing

## Objective

Research whether mission intent can replace brittle task-by-task orchestration as the central control abstraction.

## Hypothesis

Humans specify:

```text
WHY
WHAT END STATE
BOUNDARIES
INVARIANTS
AUTHORITY
ESCALATION CONDITIONS
```

The artificial organization chooses much of:

```text
HOW
WHO
WHEN
LOCAL SEQUENCE
TEAM STRUCTURE
```

## Intent Contract

Research a formal object containing:

```text
objective
desired end state
invariants
authority envelope
verification requirements
risk tolerance
budget
escalation conditions
```

## Intent preservation

Could each major decision record:

```text
mission alignment
policy alignment
evidence sufficiency
risk
explanation
```

Do not assume a single intent-alignment scalar is reliable.

Investigate alternatives.

## Research analogues

- commander's intent,
- intent-based networking,
- declarative systems,
- constraint programming,
- policy-based management,
- goal-oriented agents,
- control objectives,
- planning domains.

## Experiments

Compare:

```text
fixed workflow
planner-generated workflow
intent contract + decentralized execution
```

Measure:

- adaptability to unexpected events,
- intervention,
- errors,
- cost,
- policy violations,
- completion.

## Required output

Formal intent model, runtime enforcement, compiler implications, UI, evaluation, failure modes and recommended MVP.
