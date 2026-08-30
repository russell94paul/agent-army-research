# Agent Army Research v5

**Standalone, Obsidian-ready, multi-month research repository for Agent Army and Artificial Organization Engineering.**

This repository is intentionally separate from the production `agent-factory` repository.

> **Research discovers. Synthesis decides. Product implements.**

## What this repo is for

Agent Army is exploring a long-term shift from:

```text
building agents and teams
```

toward:

```text
engineering complete artificial organizations
```

The research program asks how such organizations should be:

- represented,
- compiled,
- operated,
- observed,
- debugged,
- supplied with context/skills/resources,
- governed,
- taught,
- simulated,
- reorganized,
- evaluated,
- and eventually evolved.

## Open in Obsidian

Open this repository folder as a vault.

Start at:

- [[HOME]]
- [[START_HERE]]

The committed `.obsidian` configuration contains only portable vault settings; personal workspace state is ignored.

## Two-repository model

```text
workspace/
├── agent-factory/          production software
└── agent-army-research/    this repository
```

See:
- [[repo-boundary/RESEARCH-VS-PRODUCT]]
- [[handoff/CLAUDE-CREATE-RESEARCH-REPO-AND-MIGRATE]]

## Candidate platform stack

```text
┌──────────────────────────────────────────────────────────────┐
│ AGENT ARMY — Command World / Organization IDE              │
├──────────────────────────────────────────────────────────────┤
│ Organizational Observability & Debugging                    │
├──────────────────────────────────────────────────────────────┤
│ Organizational Compiler / Org-IR                            │
├──────────────────────────────────────────────────────────────┤
│ Collective Cognition: Evidence / Knowledge / Skills         │
├──────────────────────────────────────────────────────────────┤
│ Organizational Runtime / OS                                 │
├──────────────────────────────────────────────────────────────┤
│ Models / Tools / Sandboxes / Repos / APIs / DBs             │
└──────────────────────────────────────────────────────────────┘
                   ↕
          Evolution Chamber
```

## Major candidate primitives

- Intent Contract
- Mission / Operation
- Organization / Organization Version
- Agent / Team / Cell / Role
- Staff Function / Running Estimate
- Capability / Readiness
- Context Package / Cognitive Logistics
- Observation / Claim / Evidence / Knowledge
- Skill / Procedure / Doctrine
- Organizational Event
- Organizational World State
- Signal / Field
- Org-IR / Organizational Genome
- Simulation / Organization Candidate

These are subject to R00–R02 and later synthesis. Their presence here does not establish novelty or finality.

## Research order

### W0 — Foundations

```text
R00 Foundations of Artificial Organization Engineering
R01 Prior Art and Novelty Boundary
R02 Canonical Ontology and Vocabulary
```

### W1 — Organizational principles

```text
R32 Mission Command
R39 Intent-Centric Agentic Computing
R38 Living General Staff
R36 Temporal Echelons
R37 Cognitive Logistics
R35 Laws of Artificial Organizations
```

### W2 — Intelligence/runtime

```text
R21 Collective Cognition
R22 Organizational OS / Stigmergy / Morphogenesis
R43 Knowledge & Capability Economy
R44 Trust / Epistemic Independence
R33 Executable Doctrine
```

### W3 — Compilation/adaptation

```text
R23 Organizational Compiler
R42 Organizational DSL / Org-IR
R24 Evolution
R31 Frontier Primitives
R45 Mechanism Design
```

### W4 — Product/human interface

```text
R20 Product Thesis
R25 UI/UX Command World
R41 Human Factors
R26 Debugger / Profiler
```

### W5 — Production architecture

```text
R27 Performance
R28 Governance
R30 Evaluation
R29 Repo Integration
R34 Federation
R40 Field / Methodology Synthesis
```

## Evidence model

Use:

```text
A — established / replicated
B — multiple credible results or mature implementations
C — promising early evidence
D — speculative but testable
E — metaphor only
```

Research answers must distinguish evidence from proposed product behavior.

## Repository structure

```text
HOME.md
foundations/
research/
  prompts/
  answers/
  synthesis/
  sources/
ontology/
architecture/
design/
experiments/
governance/
claude-skills/
implementation/
implementation-handoffs/
repo-boundary/
handoff/
maps/
templates/
migration/
```

## Product graduation

A concept reaches Agent Factory through:

```text
research
→ evidence audit
→ synthesis
→ canonical spec
→ ADR
→ approved handoff
→ implementation
→ verification
```

## The key long-term question

Can **Artificial Organization Engineering** become a coherent engineering discipline with its own:

- primitives,
- lifecycle,
- compiler,
- runtime,
- debugger,
- profiler,
- knowledge system,
- evaluation methodology,
- design laws,
- and developer environment?

R00 begins by trying to falsify that thesis.
