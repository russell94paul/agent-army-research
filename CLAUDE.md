# Claude Instructions — Agent Army Research

## Repository role

This repository is the **research, knowledge, architecture exploration and design laboratory** for Agent Army / Artificial Organization Engineering.

It is not the production Agent Factory application.

The production repository is expected to live separately as `agent-factory`.

## Source-of-truth rules

1. `research/answers/` contains evidence and analysis, not product truth.
2. `research/synthesis/` resolves conflicts across research runs.
3. `ontology/`, `architecture/`, `governance/` and selected `design/` documents contain the current canonical research specification.
4. `implementation-handoffs/approved/` contains the only research artifacts that should directly drive product implementation.
5. Never claim a concept exists in production unless verified in the Agent Factory repository.
6. Never rewrite production architecture from speculative documents.

## Working protocol

When asked to research:
- read `START_HERE.md`;
- read the relevant foundation/context docs;
- inspect prior answers for overlap;
- preserve evidence tiers;
- update the hypothesis ledger;
- produce a synthesis when a research wave finishes.

When asked to design:
- identify which findings are canonical versus experimental;
- explicitly list assumptions;
- keep experimental variants reversible.

When asked to prepare implementation:
- create an implementation handoff;
- reference the exact research and ADRs supporting it;
- define acceptance tests and rollback;
- do not edit the production repo from this repository unless explicitly asked.

## Canonical status vocabulary

Use:

```text
ESTABLISHED
EMERGING
EXPERIMENTAL
SPECULATIVE
METAPHORICAL ONLY
```

Implementation disposition:

```text
NOW
NEXT
LATER
RESEARCH ONLY
DO NOT BUILD
```

## Core safety/quality principle

Agent Army must optimize for **verified outcomes**, not activity.

Do not use raw message count, tool calls, agent count or visual motion as proxies for progress.
