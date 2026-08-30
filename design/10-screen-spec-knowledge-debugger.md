# Screen Spec — Knowledge Debugger

## Purpose

Answer:

```text
What does the organization believe?
Why?
How independent is the evidence?
What contradicts it?
How stale is it?
Which decisions depend on it?
```

## Layout

### Claim header

Show:
- canonical statement,
- status,
- confidence representation,
- validity window,
- scope,
- last verification.

Avoid a misleading single confidence percentage if evidence structure matters more.

### Evidence graph

Visualize:

```text
root source
→ observation
→ evidence
→ claim
```

Highlight:
- duplicated derivations,
- shared roots,
- contradictions,
- stale evidence,
- missing provenance.

### Dependency blast radius

List:
- decisions,
- missions,
- skills,
- doctrine,
- artifacts

that currently depend on the selected claim.

## Controls

- request independent verification,
- quarantine,
- mark stale,
- inspect source,
- inspect causal decisions,
- compare contradictions.

## States

Design explicit:
- empty,
- unverifiable,
- contested,
- stale,
- verified,
- quarantined.

## Performance

Large evidence graphs should aggregate by root source at low zoom and expand on demand.
