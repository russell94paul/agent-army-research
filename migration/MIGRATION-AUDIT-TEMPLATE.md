# Agent Factory → Agent Army Research Migration Audit

## Metadata

```yaml
date:
agent_factory_root:
agent_factory_commit:
research_repo_root:
operator:
```

## Starting working tree

Paste `git status --short`.

## Inventory

| Original path | Classification | Action | Destination | Rationale |
|---|---|---|---|---|
| | production | KEEP | | |
| | research | MOVE | | |
| | mixed | SPLIT | | |
| | duplicate | REVIEW | | |

## Content collisions

For every pair of related files that differ:

- source path,
- research path,
- semantic differences,
- recommended canonical version,
- manual decision required.

## Files moved

## Files retained

## Files split

## Files deleted only after verified migration

## Links repaired

## Product bridge created

Confirm:

```text
docs/agent-army/README.md
docs/agent-army/RESEARCH_REPO.md
docs/agent-army/CURRENT_STATE.md
docs/agent-army/APPROVED_CONCEPTS.md
docs/agent-army/IMPLEMENTATION_HANDOFFS.md
```

## Secrets scan

Confirm no credentials/client secrets were moved into the research repo.

## Validation

Research repo validator:

Agent Factory tests/build:

## Commits

Research:

Agent Factory:

## Open issues
