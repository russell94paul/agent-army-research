# Obsidian Guide

## Open

Open the repository root `agent-army-research` as an Obsidian vault.

Start from:

```text
HOME.md
```

## Why Obsidian fits

Agent Army research is highly relational.

Examples:

```text
Intent Contract
↔ Mission Command
↔ Governance
↔ Organizational Compiler

Evidence
↔ Knowledge
↔ Trust
↔ Doctrine
↔ Capability
```

Backlinks make it easier to see when one research result changes assumptions elsewhere.

## Maps of content

Use `maps/` as curated navigation.

The global graph is secondary; do not rely on it as the information architecture.

## Templates

Configured folder:

```text
templates/
```

Available templates:
- research answer,
- research synthesis,
- source note,
- concept note,
- ADR,
- implementation handoff.

## Link style

Use Obsidian wiki links for internal conceptual navigation.

Formal implementation handoffs should additionally include repository path + commit SHA where exact provenance matters.

## Tags

Use tags sparingly for broad facets:

```text
#agent-army/source
#agent-army/concept
#agent-army/architecture
#agent-army/experiment
```

Prefer explicit links over hundreds of taxonomy tags.

## Personal settings

Do not commit:
- workspace layout,
- local cache,
- personal device state.

Those are ignored in `.gitignore`.
