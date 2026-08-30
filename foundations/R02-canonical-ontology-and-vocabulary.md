# R02 — Canonical Ontology and Vocabulary

## Objective

Design the smallest precise language capable of representing Agent Army without allowing the Army metaphor, agent-framework terminology or historical research vocabulary to create ambiguity.

This result should become the vocabulary contract used by later research.

## Inputs

Read:

- R00,
- R01,
- current ontology drafts,
- current Agent Factory vocabulary if repository evidence is available.

## Candidate terms

Evaluate:

```text
Organization
OrganizationVersion
Intent
IntentContract
Mission
Operation
Task
Role
Agent
Team
Squad
Cell
StaffFunction
RunningEstimate
Artifact
Tool
Resource
Capability
Readiness
Skill
Procedure
Observation
Claim
Evidence
Knowledge
Experience
Lesson
Policy
Doctrine
Decision
Outcome
Event
Signal
Field
ContextPackage
OrgIR
Simulation
```

Do not preserve all of them.

## Required distinctions

Resolve difficult boundaries:

```text
mission vs task
team vs cell vs squad
role vs capability
skill vs capability
knowledge vs memory
policy vs doctrine
event vs observation
signal vs field
organization vs workflow
operation vs mission
```

## Research prior terminology

Compare terminology from:

- agent-oriented software engineering,
- organization-oriented MAS,
- workflow systems,
- organizational science,
- knowledge representation,
- military organizations,
- distributed systems.

Prefer established technical vocabulary when it is precise and does not mislead.

## Required schema for every canonical term

```text
Canonical name
Definition
Why it exists
Aliases
Deprecated synonyms
Not the same as
Identity
Lifecycle
Relationships
Persistence
Runtime owner
User-facing label
API/schema identifier
Example
Counterexample
```

## Army metaphor mapping

Maintain a separate mapping:

```text
technical primitive ↔ optional visual/Army label
```

The visual metaphor must never replace the technical definition.

## Naming quality tests

A term should be rejected if:

- two teams will plausibly use it differently;
- it represents only a UI metaphor;
- another canonical term already covers it;
- it cannot be mapped to state or behavior;
- it creates false novelty.

## Required deliverables

1. minimal canonical ontology;
2. relationship diagram;
3. glossary;
4. developer/API naming guide;
5. user-facing language guide;
6. Army-theme mapping;
7. deprecated-term list;
8. unresolved vocabulary questions.

Finish with:

> What is the minimum vocabulary Agent Army needs today, and which terms should remain research-only until their mechanisms are validated?
