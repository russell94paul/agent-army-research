# Content collisions — v2/v3 versus v5

Eight documents exist in both the historical agent-factory packs and the v5 baseline **and differ
materially**. None of them were resolved during the migration. Both versions are preserved:
v5 at its canonical path, the older version under [[legacy/README|legacy/]].

> **Do not resolve any of these by preferring the newer file.** In six of the eight the older
> version carries something the newer one dropped. The newest pack is better *structured*; it is
> not uniformly better *grounded*.

Status key: **OPEN** = needs a synthesis decision. **DECIDED** = resolved by an ADR or by this
migration, recorded here for traceability.

---

## C1 — README.md · the repository topology itself · **DECIDED**

| | |
|---|---|
| OLD PATH | `agent-factory/docs/agent-army-research-pack/README.md` → `legacy/research-pack-v2/README.md` |
| NEW PATH | `README.md` |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | v5, on this point |

**SEMANTIC DIFFERENCE.** The two documents recommend *opposite* repository topologies, in writing.

v2 §"Recommended folder in your repo":

> Keep this in the same repository as the current Agent Factory, but separated from active
> implementation … **Why same repo? Because the research must stay grounded in the current
> codebase.**

v5 §"Two-repository model" states the research repository is "intentionally separate from the
production `agent-factory` repository".

**RECOMMENDED SYNTHESIS ACTION — already taken.** This migration implements the v5 topology, and
[[adr/ADR-0001-keep-agent-army-research-separate]] is the decision of record. But v2's *reason* for
same-repo is a real risk, not a mistake, and separation does not answer it: research that cannot
see the code drifts from it. The mitigation this repository actually relies on is
agent-factory's `docs/agent-army/CURRENT_STATE.md` plus R29's rule that repository
access is a precondition for the roadmap prompt. **If that bridge document goes stale, v2's
objection becomes correct.** Treat C1 as decided but load-bearing.

v2's README also carries two artefacts v5 does not: the *"VS Code / Kubernetes / Datadog / Git /
CI-CD → Agent Army"* positioning analogy, and the eight-rung *"observe → represent → debug → share
→ adapt → simulate → optimize → evolve"* progression. Both are candidate inputs to
[[vision/02-whitepaper-outline]]; neither is in v5.

---

## C2 — INDEX.md · **OPEN (low)**

| | |
|---|---|
| OLD PATH | `legacy/research-pack-v2/INDEX.md` |
| NEW PATH | `INDEX.md` |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | v5 |

**SEMANTIC DIFFERENCE.** Both are file indexes of their own pack; v2's covers 39 files, v5's covers
the full vault with per-directory annotations. No research content is at stake.

**RECOMMENDED SYNTHESIS ACTION.** None. v5 supersedes. Kept only because it is the manifest of what
the v2 pack contained, which is how you verify the archive is complete.

---

## C3 — R28 Governance · v5 dropped the control surface · **OPEN (high)**

| | |
|---|---|
| OLD PATH | `legacy/research-pack-v2/research/prompts/R28-governance-security-safety.md` (1,106 B) |
| NEW PATH | `research/prompts/R28-governance-security-safety.md` (2,045 B) |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | **split** |

**SEMANTIC DIFFERENCE.** v5 adds a threat model, an explicit capability/permission object list, a
knowledge-security section and adaptive-system promotion gates. It **removes** two things v2 had:

1. **A four-layer governance hierarchy** — `CONSTITUTION` (hard limits) → `POLICY` (operational
   rules) → `STRATEGY` (mission approach) → `PREFERENCE` (learned optimization). v5 has a
   constitution and an autonomy matrix but no layered model saying which layer a given rule
   belongs to, or which layers the organization may rewrite about itself.
2. **An operator control surface** — emergency stop, pause mission, freeze topology, revoke skill,
   quarantine knowledge, cap budget, force verification, rollback organization version. v5's
   deliverable 9 asks for an "incident/rollback model" but never enumerates the controls.

**RECOMMENDED SYNTHESIS ACTION.** Re-insert both into the v5 R28 prompt before dispatching W5.
The four layers are a *typing discipline* for governance rules and are cheap to carry; the control
list is the concrete answer to "what does a human do when it goes wrong", which
[[governance/02-autonomy-matrix]] currently presumes exists. Neither conflicts with anything v5
added.

---

## C4 — R29 Repo integration · v5 dropped the ordering hypothesis · **OPEN (high)**

| | |
|---|---|
| OLD PATH | `legacy/research-pack-v2/research/prompts/R29-implementation-roadmap-repo-integration.md` |
| NEW PATH | `research/prompts/R29-implementation-roadmap-repo-integration.md` |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | **split** |

**SEMANTIC DIFFERENCE.** v5 is a much stronger prompt — it adds a strangler-migration pattern, a
current-state audit schema (owner / persistence / contracts / tests / migration risk per
primitive), feature flags, performance budgets, a 30/60/90 plan, and a *removal* plan naming
research-inspired code that should **not** be built yet.

v2 carried a **numbered twelve-step ordering** that v5 replaces with an unordered substrate list
plus the single constraint "do not prioritize morphogenesis/evolution before the substrate":

```text
1 canonical entity IDs      5 timeline/replay              9  adaptive routing
2 durable typed events      6 agent/team/artifact inspect. 10 simulation
3 materialized world state  7 knowledge/skill objects      11 morphogenesis
4 artifact-centric evidence 8 field overlays               12 evolution
```

**RECOMMENDED SYNTHESIS ACTION.** Do **not** paste the ladder back into the prompt — a prompt that
supplies its own answer contaminates the research. Instead promote it to a **falsifiable
hypothesis** in [[research/HYPOTHESIS_LEDGER]]: *"the twelve substrate capabilities must be built
in this dependency order."* R29 then either confirms, reorders or refutes it against the real
repository. That is the difference between a prior and a premise.

---

## C5 — R30 Evaluation · v5 dropped six concrete metrics · **OPEN (medium)**

| | |
|---|---|
| OLD PATH | `legacy/research-pack-v2/research/prompts/R30-evaluation-benchmarks-experiments.md` |
| NEW PATH | `research/prompts/R30-evaluation-benchmarks-experiments.md` |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | **split** |

**SEMANTIC DIFFERENCE.** v5 adds a mission-class corpus, per-mechanism isolation experiments, an
experimental-rigor schema, a reward-hacking defence, a sim-to-real validity section and
statistical-reporting guidance sized to the sample. Strictly better as method.

But v5 replaces v2's flat seventeen-metric list with ten abstract *outcome categories*, and six of
v2's metrics have no home in the new categories:

```text
context bytes          duplicate work        recovery time
false-confidence rate  skill reuse           intent alignment
```

`false-confidence rate` is the most consequential loss: it is the only metric in either version
that measures the system claiming success it cannot support — the exact failure agent-factory
already has a named mechanism for (`docs/evidence/false-succeeded-mechanism.md`).

**RECOMMENDED SYNTHESIS ACTION.** Carry the six forward as named metrics under v5's
"metric definitions" deliverable. Map each to a category rather than appending a second list.

---

## C6 — R31 Frontier primitives · v5 dropped the scoring formula · **OPEN (medium)**

| | |
|---|---|
| OLD PATH | `legacy/research-pack-v2/research/prompts/R31-frontier-organizational-primitives.md` (932 B) |
| NEW PATH | `research/prompts/R31-frontier-organizational-primitives.md` (3,631 B) |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | v5, mostly |

**SEMANTIC DIFFERENCE.** v5 is far stronger: it names sixteen candidate primitives up front, adds a
ten-step per-candidate search method, a mechanism-reducibility test that classifies anything
irreducible as *metaphorical only*, a combination-effects section hunting dangerous feedback loops,
and a five-way disposition (`BUILD NOW / PROTOTYPE / SIMULATE / RESEARCH FURTHER / REJECT`).

v2 carried two things v5 does not:

1. **A quota** — "Find at least 25 concepts", then rank. v5 asks for a top-20 with no floor on the
   search, which permits a narrow search that terminates early.
2. **An explicit ranking function** — `value × feasibility × novelty ÷ complexity`, plus per-concept
   `EVIDENCE LEVEL` and `RECOMMENDATION` fields.

**RECOMMENDED SYNTHESIS ACTION.** Restore the search quota (it costs nothing and defends against a
shallow pass). Do **not** restore the formula as stated — multiplying four unmeasured subjective
scores produces a number with no units that will be quoted as if it were evidence, which is the
`MEASURED | DERIVED | ASSUMED | PROXY` failure this programme exists to avoid. Keep
`EVIDENCE LEVEL` as a per-candidate field; let ranking be argued, not computed.

---

## C7 — R00 Foundations · v3 skeleton vs v5 prompt · **OPEN (low)**

| | |
|---|---|
| OLD PATH | `legacy/research-pack-v3/foundations/R00-...md` (878 B) |
| NEW PATH | `foundations/R00-foundations-of-artificial-organization-engineering.md` (6,603 B) |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | v5 |

**SEMANTIC DIFFERENCE.** v3 is a fifteen-item deliverable checklist and six questions. v5 is a full
prompt with a working hypothesis, prior disciplines, a boundary test, foundational objects, a
lifecycle, a compiler/runtime/debugger analogy, proposed laws, evaluation science and a novelty
map — and it subsumes every v3 deliverable.

Two v3 items are not literally present in v5 R00:

- *"Which ideas should never be implemented?"* — v5 asks this in R31 (`REJECT`), not R00.
- *"Produce a canonical vocabulary that all future research must use."* — v5 moves this to
  [[foundations/R02-canonical-ontology-and-vocabulary]].

**RECOMMENDED SYNTHESIS ACTION.** None. v5 supersedes; both residuals are covered elsewhere. Recorded
so nobody re-derives the mandate believing it was lost.

---

## C8 — Research execution order · **OPEN (low)**

| | |
|---|---|
| OLD PATH | `legacy/research-pack-v3/meta/RESEARCH_EXECUTION_ORDER.md` |
| NEW PATH | `research/RESEARCH-MANIFEST.yaml` |
| WHICH IS NEWER | v5 |
| WHICH IS BETTER GROUNDED | v5 |

**SEMANTIC DIFFERENCE.** v3 orders 15 prompts across 3 waves. v5 orders 29 prompts across 6 waves
(W0–W5) with a status vocabulary, and is machine-readable. The orderings disagree on placement:

| Prompt | v3 | v5 |
|---|---|---|
| R20 Product thesis | Wave 1, position 3 | W4 (product/human interface) |
| R21 Collective cognition | Wave 1, position 4 | W2 (intelligence/runtime) |
| R31 Frontier primitives | Wave 1, position 5 | W3 (compilation/adaptation) |
| R28 Governance | Wave 2 | W5 (production architecture) |

v5 moves the product thesis *later* — foundations and organizational principles are settled before
the product claim is made. That is the more defensible sequence and it is the one
[[START_HERE]] implements.

v3's after-every-wave ritual — *"consolidate vocabulary, update architecture, only then proceed"* —
survives in v5 as [[START_HERE]] steps 5–7.

**RECOMMENDED SYNTHESIS ACTION.** None. v5 supersedes.

---

## Not a collision

The remaining **33 of the v2 pack's 39** markdown files are **byte-identical** to their v5
counterparts, verified by `cmp`. There is nothing to synthesize in vision, architecture 00–04,
design 00–05, experiments, ADR-0001, the implementation/claude and implementation/roadmap
documents, R20–R27, or R32–R34.

The **14 v3 prompt stubs** are not collisions either — each is a one-line pointer at a pack that no
longer exists. They carry no content and live only in
`legacy/archives/agent-army-research-pack-v3.zip`.
