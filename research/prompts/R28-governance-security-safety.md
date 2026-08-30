# R28 — Governance, Security and Safety Architecture

## Objective

Design a governance system that allows useful autonomy without making authority implicit, irreversible or unobservable.

## Threat model

Consider:

- prompt injection through artifacts,
- malicious or compromised tools,
- secret leakage,
- excessive permissions,
- cross-mission data contamination,
- unsafe production changes,
- runaway agent spawning,
- resource exhaustion,
- poisoned knowledge/skills,
- policy bypass,
- self-modification,
- federation trust failures.

## Authority model

Research explicit capability/permission objects for:

```text
read repository
write repository
execute shell
query production
mutate production
access secrets
publish knowledge
publish skill
spawn agent
change team topology
approve verification
```

## Constitutional boundary

Define rules the organization cannot autonomously change.

Candidate hard boundaries:

- audit cannot be disabled,
- autonomy cannot self-escalate,
- budget cannot self-increase,
- required verification cannot be bypassed,
- constitution changes require human authority.

## Autonomy levels

Evaluate:

```text
MANUAL
SUGGEST
GUARDED_AUTO
AUTONOMOUS
```

Determine whether autonomy should be global or action/capability-specific.

## Knowledge security

Address:

- provenance,
- tenant/client boundaries,
- retention,
- stale secrets,
- poisoned memory,
- knowledge promotion permissions.

## Adaptive systems

Define special controls for:

- morphogenetic team formation,
- doctrine changes,
- evolutionary organization search,
- automated skill publication,
- federation.

## Required deliverables

1. threat model;
2. authority/capability model;
3. constitution model;
4. autonomy matrix;
5. escalation rules;
6. audit-event requirements;
7. knowledge/skill security;
8. adaptive-system promotion gates;
9. incident/rollback model;
10. implementation sequence.

Finish with:

> What is the minimum governance substrate that must exist before Agent Army can safely increase organizational autonomy?
