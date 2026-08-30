# Autonomy Matrix

## Levels

```text
MANUAL
Human performs/approves the action.

SUGGEST
Organization proposes; human commits.

GUARDED_AUTO
Organization may act when explicit policy, evidence, budget and rollback conditions are satisfied.

AUTONOMOUS
Organization may act within pre-authorized scope without per-action approval.
```

Autonomy should usually attach to an **action/capability/scope**, not a single organization-wide number.

## Draft matrix

| Action | MANUAL | SUGGEST | GUARDED_AUTO | AUTONOMOUS |
|---|---|---|---|---|
| assign ordinary task | human | propose | allowed | allowed |
| spawn temporary agent | human | propose | budget-bound | policy-bound |
| change team topology | human | propose | reversible + observed | mission-policy bound |
| publish knowledge | human | propose | evidence threshold | constrained |
| publish skill | human | propose | tests required | test/policy bound |
| production write | approval | approval | verification + rollback | exceptional |
| increase budget | human | human | human | human |
| raise autonomy | human | human | human | human |
| promote doctrine | human | human | human | human |
| change constitution | human | human | human | human |

## Evaluation inputs

A guarded action may depend on:

- action risk,
- environment,
- evidence sufficiency,
- rollback availability,
- budget,
- historical capability,
- policy.

## Requirement

The UI must show **why** an action is allowed at its current autonomy level.
