# Skill — Agent Army Evidence Auditor

## Purpose

Audit whether a research answer is strong enough to influence canonical architecture.

## Audit dimensions

### Source authority
Prefer primary papers, official specifications and source code.

### Claim fit
Does the cited source actually support the stated mechanism?

### Independence
Are several citations ultimately based on one dataset, one benchmark or one source?

### Recency
For rapidly changing LLM-agent work, inspect publication date and version.

### Reproducibility
Is there code, data or an independently repeated result?

### Generalization
Did the evidence demonstrate the same task class Agent Army cares about?

## Verdict vocabulary

```text
SUPPORTED
PARTIALLY SUPPORTED
UNSUPPORTED
MISLEADING
NEEDS REPLICATION
```

## Required output

For each major claim provide:

- verdict,
- evidence tier,
- strongest source,
- counterevidence,
- missing evidence,
- whether the claim should affect architecture now.

End with a list of claims that must be downgraded in the synthesis.
