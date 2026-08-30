# Start Here

## 1. Create the research repository

If you are currently working inside Agent Factory, use:

[[handoff/CLAUDE-CREATE-RESEARCH-REPO-AND-MIGRATE]]

The target structure is:

```text
../agent-factory
../agent-army-research
```

## 2. Open the research repo in Obsidian

Open `agent-army-research` as the vault.

Use [[HOME]] as the navigation entry point.

## 3. Do not start by implementing the speculative system

The first goal is to stabilize:

- definition,
- novelty boundary,
- ontology,
- evidence model,
- research vocabulary.

## 4. Run Wave 0

Run in Deep Research:

- [[foundations/R00-foundations-of-artificial-organization-engineering]]
- [[foundations/R01-prior-art-and-novelty-boundary]]
- [[foundations/R02-canonical-ontology-and-vocabulary]]

Save the results under:

```text
research/answers/
```

## 5. Audit and synthesize

Use:

- [[claude-skills/evidence-auditor/SKILL]]
- [[claude-skills/research-synthesizer/SKILL]]

Then create:

```text
research/synthesis/W0-foundations.md
```

## 6. Update canonical objects

Only after synthesis update:

- ontology,
- architecture,
- governance,
- vocabulary.

## 7. Run subsequent waves

Follow `research/RESEARCH-MANIFEST.yaml`.

## 8. Prepare product handoffs

Research does not directly change Agent Factory.

Use:

[[implementation-handoffs/HANDOFF_TEMPLATE]]

## 9. UI work

Prototype UI early only to learn.

Do not hard-code unvalidated organizational primitives into production contracts until the ontology stabilizes.

## 10. Monthly review

At least monthly ask:

```text
What did we learn?
What did we falsify?
What concepts graduated?
What should we remove?
What is now blocking product progress?
```
