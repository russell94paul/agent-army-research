# R44 — Trust, Reputation and Epistemic Independence

## Objective

Design an epistemic architecture that prevents an artificial organization from confusing repeated agreement with independent evidence.

This is a core risk for shared-memory multi-agent systems:

```text
one source
→ copied into memory
→ repeated by five agents
→ apparent consensus
```

The system must be able to recognize that this is still effectively one evidentiary root.

## Problems to investigate

- correlated memories,
- circular citations,
- copied claims,
- stale evidence,
- false majorities,
- agent reputation bias,
- source poisoning,
- groupthink,
- confirmation cascades,
- contradiction persistence,
- provenance collapse,
- over-trusting high-performing agents outside their competence.

## Research domains

Study relevant work in:

- provenance graphs,
- truth-maintenance systems,
- Bayesian evidence aggregation,
- Dempster-Shafer approaches where relevant,
- argumentation frameworks,
- trust and reputation systems,
- knowledge graphs,
- scientific meta-analysis,
- source-dependency detection,
- Byzantine systems,
- data lineage,
- collective intelligence.

Do not force one formalism across every task.

## Required ontology

Evaluate objects such as:

```text
Claim
Evidence
Source
RootSource
Derivation
Contradiction
Verification
TrustAssessment
CompetenceContext
ValidityWindow
DecisionDependency
```

## Source independence

Propose algorithms for estimating whether evidence items are meaningfully independent.

Potential indicators:

- same URL/document,
- same upstream database row,
- same retrieved passage,
- explicit derivation edge,
- temporal/content similarity,
- shared agent memory parent,
- common external authority.

The system must prefer explicit provenance over speculative similarity inference.

## Trust vs competence

Separate:

```text
trustworthiness
```

from:

```text
competence for this task/context
```

An agent that is excellent at SQL may have little evidentiary authority on legal interpretation.

Research contextual reputation rather than one global trust score.

## Decision dependency

The organization should answer:

```text
Which active decisions rely on this claim?
What breaks if this claim is false?
How many independent sources support it?
What directly contradicts it?
When was it last verified?
```

## UI requirements

Design a Knowledge Debugger representation for:

- evidence roots,
- copied evidence,
- contradictions,
- stale sources,
- dependency blast radius,
- contextual trust.

Avoid misleading consensus percentages.

## Experiments

Create adversarial scenarios:

1. five agents repeat one false source;
2. two independent sources contradict one popular source;
3. high-reputation agent operates outside expertise;
4. old verified knowledge becomes stale;
5. poisoned skill injects a false claim.

Measure whether the system detects and limits propagation.

## Required output

Produce:

1. evidence/provenance graph model;
2. independence model;
3. contextual competence/reputation model;
4. claim aggregation candidates;
5. contradiction lifecycle;
6. knowledge quarantine mechanisms;
7. UI specification;
8. performance/storage implications;
9. adversarial test suite;
10. recommended MVP.

Finish with:

> What is the simplest epistemic architecture that materially reduces false organizational consensus without creating an unusably complex knowledge system?
