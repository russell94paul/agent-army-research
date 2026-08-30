# What Stays in Agent Factory

## Principle

Agent Factory owns facts required to understand, build, test, deploy and operate the **current product**.

## Keep

- production source code,
- current runtime architecture,
- actual event/schema contracts,
- database models/migrations,
- API contracts,
- build/run instructions,
- active feature flags,
- operational runbooks,
- current UI contracts,
- production ADRs,
- tests/fixtures,
- approved handoffs under implementation.

## Product bridge

Keep:

```text
docs/agent-army/
├── README.md
├── RESEARCH_REPO.md
├── CURRENT_STATE.md
├── APPROVED_CONCEPTS.md
└── IMPLEMENTATION_HANDOFFS.md
```

Additional Agent Army docs may remain if they describe implemented behavior that developers need locally.

## CURRENT_STATE rule

Use only:

```text
IMPLEMENTED
PARTIAL
PLANNED
NOT IMPLEMENTED
```

Every `IMPLEMENTED` or `PARTIAL` claim should have code evidence.

## Split mixed documents

If an existing document contains both current facts and future research:

1. preserve current factual sections in Agent Factory;
2. move speculative/research sections into the research repository;
3. cross-link the two where useful;
4. record the split in the migration audit.

## Do not keep duplicated speculative trees

The product repo should not contain a stale mirror of the research vault.
