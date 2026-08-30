# Safety and Control Boundaries

## Principle

Adaptive organizations require strong boundaries before autonomy.

## Constitution examples

The system may never autonomously:

- disable audit logs,
- exceed hard budget,
- bypass verification,
- grant itself new secrets,
- raise autonomy level,
- publish untested skills as trusted,
- promote doctrine without evidence,
- remove human approval from protected actions.

## Autonomy levels

```text
MANUAL
  Human approves all structural changes.

SUGGEST
  System proposes changes.

GUARDED_AUTO
  System acts within narrow policies and budgets.

AUTONOMOUS
  System can restructure within constitution.
```

## Emergency controls

- pause mission,
- freeze topology,
- stop all agents,
- revoke tool,
- quarantine knowledge,
- disable skill,
- rollback organization version,
- force manual mode.

## Required audit

Every major autonomous action must log:

```text
actor
decision
inputs
policy
evidence
intent alignment
risk
outcome
```
