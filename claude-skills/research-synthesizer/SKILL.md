# Skill — Agent Army Research Synthesizer

## Purpose

Convert multiple research answers into a coherent canonical recommendation without flattening disagreement.

## Inputs

- research prompts,
- research answers,
- hypothesis ledger,
- current canonical ontology/architecture,
- relevant product facts if supplied.

## Procedure

1. Extract every decision-relevant claim.
2. Normalize synonymous terminology.
3. Attach evidence tier and source quality.
4. Identify direct contradictions.
5. Identify apparent contradictions caused by different task domains.
6. Separate mechanism evidence from product speculation.
7. Update hypothesis status.
8. Determine which concepts are promoted, demoted or rejected.
9. Propose exact canonical-doc changes.
10. Propose ADRs for architectural decisions.
11. Produce an explicit next research wave.

## Rules

Never:
- count duplicated sources as independent evidence;
- silently resolve disagreement;
- infer production implementation from research;
- preserve a concept only because it matches the Agent Army theme.

## Output

Use `research/SYNTHESIS_TEMPLATE.md`.

Every recommendation must have one implementation disposition:

```text
NOW
NEXT
LATER
RESEARCH ONLY
DO NOT BUILD
```
