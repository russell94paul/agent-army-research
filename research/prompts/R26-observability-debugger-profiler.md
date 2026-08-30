# R26 — Organizational Observability, Debugger and Profiler

## Objective

Design observability for artificial organizations.

Traditional logs are insufficient.

## Must answer

```text
Why did this agent act?
Why was this agent selected?
Why did this team form?
Why did it grow?
Why is this artifact high risk?
What evidence influenced this decision?
Where did that knowledge come from?
Why did verification fail?
Why was this skill chosen?
What is blocked?
```

## Causal stack

```text
Mission
 ↓
Intent Contract
 ↓
Constraint
 ↓
Compiler Decision
 ↓
Team Formation
 ↓
Knowledge / Evidence
 ↓
Agent Decision
 ↓
Tool Call
 ↓
Artifact Change
 ↓
Verification Outcome
```

## Debugging primitives

- organizational breakpoints,
- causal trace,
- time-travel replay,
- knowledge inspector,
- communication trace,
- skill trace,
- topology history,
- decision explanations.

## Profiler

Measure:

```text
reasoning time
tool time
waiting time
coordination time
knowledge retrieval
context loading
validation time
human waiting
duplicate work
retry overhead
```

## Required output

Produce:

- observability data model,
- event schema,
- causal graph,
- replay architecture,
- breakpoint model,
- profiler design,
- knowledge debugger,
- UI specs,
- storage/performance plan.

End with:

> What observability primitives must exist before Agent Army can safely adapt itself?
