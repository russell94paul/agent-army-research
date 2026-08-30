# Benchmark Mission Corpus

## Purpose

Create a stable, versioned set of realistic missions for comparing organizational mechanisms.

## Mission classes

Include:

```text
connector migration
schema/data migration
bug repair
incident diagnosis
unknown repository investigation
feature implementation
code review
data-quality correction
release validation
documentation/research synthesis
```

## Mission record

Every benchmark should specify:

```yaml
id:
version:
class:
input_state:
objective:
intent:
constraints:
allowed_tools:
budget:
verification_contract:
ground_truth:
hidden_failure_cases:
difficulty_factors:
```

## Ground truth

Prefer objective verification:

- tests,
- database state,
- API contract,
- artifact diff,
- hidden assertions.

Human judgment may supplement but should not replace machine-verifiable outcomes where available.

## Dataset splits

```text
development
validation
holdout
adversarial
```

Do not optimize Evolution Chamber candidates against the entire corpus and then report that same corpus as unbiased evaluation.

## Versioning

Changes to:
- mission inputs,
- verifier,
- expected outcome

require a corpus version change.

## Coverage

Track whether the corpus overrepresents one codebase, one task type or one model.
