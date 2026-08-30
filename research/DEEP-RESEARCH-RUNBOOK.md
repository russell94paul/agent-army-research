# Deep Research Runbook

## Where to run

Use ChatGPT Deep Research or another research system with strong web/paper access.

Claude Code should primarily:
- provide repository evidence packs,
- synthesize returned research,
- translate approved findings into architecture/implementation.

## Before dispatch

For each prompt:

1. read the prompt;
2. attach any required repo evidence;
3. record the Agent Factory commit SHA;
4. make sure earlier-wave synthesis is available if the prompt depends on it.

## Save answer

```text
research/answers/RXX-answer-<slug>.md
```

Do not edit the original answer to make it agree with later findings.

## Then audit

Use:
- `claude-skills/evidence-auditor/SKILL.md`

## At wave end

Use:
- `claude-skills/research-synthesizer/SKILL.md`

Output:
- `research/synthesis/WX-<name>.md`

## Canonical promotion

Only after synthesis should ontology/architecture/design/governance be updated.

## Research debt

Track:
- inaccessible primary sources,
- claims relying on vendor marketing,
- benchmark/task mismatch,
- results without code,
- unresolved contradictions.
