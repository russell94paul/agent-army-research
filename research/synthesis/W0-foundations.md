# Wave 0 Synthesis — Foundations

## Metadata

```yaml
wave: W0
date: 2026-08-30
research_included:
  - R00-answer-foundations-of-aoe.md
  - R01-answer-prior-art-and-novelty-boundary.md
  - R02-answer-canonical-ontology-and-vocabulary.md
  - sources/agent-factory-vocabulary-crawl.md
  - sources/W0-citation-verification-partial.md
  - sources/W0-audit-prior-art-citations.md
  - sources/W0-adversarial-refutation-novelty-claim.md
repository_commit: agent-factory @ bff45e4 (branch docs/agent-army-research-separation)
synthesizer: orchestrating session, local subagents
how_it_ran: >
  Local subagents in-repo, not an external deep-research tool. Less independent than an
  outside model; substantially stronger on file-and-line claims. Weigh accordingly.
status: draft
```

---

## Executive synthesis

**Wave 0 falsified the programme's founding premise. That is a success, and it cost one morning
instead of one build cycle.**

1. **Artificial Organization Engineering is not a new discipline.** It is organisation-oriented
   MAS / multi-agent-oriented programming, which already has a metamodel (Moise+), an enforcing
   runtime (JaCaMo/ORA4MAS), a methodology family (Gaia/Tropos/INGENIAS), a normative layer and a
   textbook. Every concern in the working hypothesis has a named home there. **That field failed to
   reach industry for tooling reasons, and LLMs do not remove tooling problems.**
2. **The category name is taken, twice, and recently.** *Artificial Organisations* (Waites,
   arXiv:2602.13275, Feb 2026) publishes under the name with our thesis. **IMACS** (Chen et al.,
   arXiv:2607.25446, 28 Jul 2026 — **five weeks old**) is the organizational-compiler thesis,
   published: Belbin/Mintzberg/RACI as executable, swappable configuration.
3. **Of 15 concepts, 5 remain at CRITICAL prior-art risk after audit**, 1 downgraded to HIGH, 1
   must be re-sourced. `PROSA` (1998) contains **"staff holons"** — the Staff Mesh, under the same
   word, and PROSA's are *centralised*, which independently confirms that "Staff **Mesh**" names the
   opposite of its own design.
4. **The single surviving novelty claim is refuted on all four components.** The strongest kill:
   `UNMEASURABLE`-that-cannot-collapse is **TTCN-3's `inconc`**, standardised since ISO/IEC 9646
   (1991). Verified here against primary standards text (ITU-T Z.140 §24.2).
5. **⛔ And the refutation found a live defect.** TTCN-3 has a fifth verdict, `error`, for failure of
   the test apparatus, which *nothing* can override. `agent-factory/factory/contract.py:57` folds
   instrument-crash into `UNMEASURABLE`. **A system founded on "never collapse two kinds of
   not-knowing" collapses two kinds of not-knowing.** It is one category coarser than the 1990s art
   on its flagship distinction.
6. **The most-quoted number in the estate lost its uncertainty in transit.** −3.5% carries a 95% CI
   of [−18.6%, +25.7%] and **σ=45.2%**. The mean was never the finding. Its peer-reviewed title is
   *"Capable language models can outgrow the benefits of collaboration"* — capability saturation,
   not multi-agent inferiority.
7. **There was never a resolvable citation to walk back to.** `agent-factory/docs/research/` cites
   via **1,388 opaque ChatGPT tokens across 7 files**; `R2-answer-topology.md` contains no arXiv id,
   DOI or URL at all.
8. **R02 found the real prize, and it is not what the brief asked for.** The nine "different names
   for the same thing" are not nine names for one concept — they are nine different *collapses* of
   **three orthogonal axes**: standing (did the instrument see?), basis (how strongly believed?),
   window (over what period?).
9. **IMACS splits the ontology in two.** Nine terms are **structural** (binding-independent); four
   are **configurational** and must carry a model `binding`, because *"the winning placement flips
   across model families."* Organizational design cannot be hard-coded.

**Bottom line: do not launch AOE as a category, and do not claim novelty. Reframe as a synthesis
claim** — *"known controls from conformance testing, metrology, assurance cases and analytic
tradecraft, assembled into one runtime for agent teams"* — which is defensible, honest, and
immediately improvable.

---

## Consensus findings

| # | Finding | Research IDs | Tier | Architectural implication | Disposition |
|---|---|---|---|---|---|
| C1 | AOE ≡ organisation-oriented MAS; not a new discipline | R00, R01 | A | Stop treating the ontology as greenfield; adopt Moise+/OperA vocabulary where precise | **RESEARCH ONLY** |
| C2 | Category name occupied twice, both 2026 | R00 (verified) | A | Do not launch the category publicly | **DO NOT BUILD** |
| C3 | `UNMEASURABLE` ≡ TTCN-3 `inconc`, monotone lattice since 1991 | refutation, R02, verified primary | A | Adopt the standard's shape rather than inventing one | **NOW** |
| C4 | A fifth verdict is missing: harness-error, un-assertable, dominant | refutation, verified primary | A | `contract.py` change, small, high value | **NOW** |
| C5 | Basis labelling ≡ ICD 203 Tradecraft Standard 3 (US IC policy, 2015) | refutation | A | Not novel; adopt ICD 206 source-descriptor discipline | **NEXT** |
| C6 | Refusal-to-close in the store is ordinary workflow engineering | refutation | A | Keep the control; drop the novelty framing | **NOW (framing only)** |
| C7 | Standing / basis / window are three orthogonal axes, not one | R02 | B | The nine vocabularies are correct as-is; do **not** refactor | **NEXT** |
| C8 | Organizational configuration is model-binding-dependent | R00, R02, IMACS verified | B | Split ontology structural vs configurational | **NEXT** |
| C9 | Compiler and debugger are the weakest analogies; version-control and test-framework the strongest — and the strongest two are already built | R00 | C | Stop leading the vision with the compiler | **RESEARCH ONLY** |
| C10 | Law 4 ("context is a resource, not a transcript") holds and is best-evidenced | R00 | B | Keep; `context.py` already implements it | **NOW** |

---

## Conflicting findings

| Topic | Position A | Position B | Why the conflict exists | Resolution |
|---|---|---|---|---|
| Does −3.5% exist in the source? | **R01**: verbatim in the body, with CI | **R00**: `NOT-VERIFIED`, in no abstract | R00 searched abstracts; the figure is in the body of **v1** only | **A.** Verified by fetching v1 full text. R00's verdict was *honest about what it did* — a correct `NOT-VERIFIED`, not an error |
| Was the TTCN-3 standard actually opened? | **refutation**: downloaded ETSI ES 201 873-1, read Table 30 | **R02**: paywalled, semantics are SECONDARY, flagged `NOT-SUPPLIED` | Different editions; ETSI 403s to some clients | **Both superseded.** Synthesizer fetched ITU-T Z.140 (07/2001) and extracted §24.2 / §24.2.1 / Table 20 directly. Semantics confirmed. Note clause+table numbering differs by edition — cite the edition you read |
| Is `Claim` canonical? | **R00**: fundamental object #5 | **R02**: delete it | R00 reasoned from the draft ontology; R02 from the code | **B.** The crawl measured **four live senses** in one codebase (lane lease / task status / bus kind / prose). Fails R02's rejection test (a) on measured fact. The code already names the research sense `Assertion` (`contract.py:41`) |
| Is `Event` canonical? | **R00**: fundamental object #1 | **R02**: fold into `Task` | Both agree no organizational event log exists | **B, provisionally.** Naming it canonically invites building an org event log before there is anything to log. Revisit when something emits organizational events |
| Is `IntentContract` a naming or a type problem? | **R00**: merge into GreenContract as new assertion kinds | **R02**: type error — authority/budget are permissions, not falsifiable | R00 optimised for fewer objects | **B.** A `GreenContract`'s fold is meaningful *only* because every member is falsifiable; adding permissions breaks the property the object exists for. Adopt R02's three-way split — `Contract` / `Mandate` / `Task` — with `Mandate` gated (below) |
| Are the 7 CRITICAL verdicts independent? | **R01**: seven results | **audit**: four lineages + two single-lab programmes | R01 counted papers, not labs | **Audit.** KB-ORG and ODML are JAAMAS **16(2):151–185** and **16(2):95–149** — consecutive articles, same issue, same lab, Lesser on both. Novelty is not rescued, but "seven independent confirmations" was never true |

---

## Vocabulary changes

### Added

- **`Instrument`** — canonical name for the nine-way collapse, with `standing = LIVE | DARK | UNPROVEN`
  plus a `cause`. Not a coinage: the word already appears in prose across 15 `factory/` modules
  (68 occurrences) and is a `Finding.KIND`, but has never been a type. Carries two named rules: the
  **Live-Instrument Rule**, and its violation, a **Blind Zero**.
- **`Mandate`** — permissions/authority, continuous, evaluated at a boundary. `mandate` is a free
  word: **zero occurrences** in agent-factory, verified. **Ships NEXT with a hard gate** — if nothing
  can enforce authority at a boundary, it demotes to `RESEARCH ONLY` and `prohibition` keeps its
  honest name.
- **A fifth verdict** for harness error (see C4). Name TBD; must not be `ERROR` if that collides.

### Changed

- **`Contract`** stays bound to `GreenContract`. Do **not** introduce `IntentContract`.
- **`ContextPackage` → adopt `ContextPack`/`ContextRef`** as they exist in `context.py:121,:71` —
  built, tested, and already carrying a mandatory `source`, freshness state and confidence.

### Deprecated

- `Claim` (four live senses; use `Assertion`) · `Role` (killed on the IMACS leg, stronger than
  R00's) · `Cell` · `Signal` · `Field` · `Squad` · `Simulation` (nothing to simulate).

### Forbidden synonyms

- **"Staff Mesh"** — PROSA's staff holons are *centralised*; "mesh" names the opposite of the design.
  Prefer **staff function**, the established term.
- **"Temporal Echelons"** — *echelon* means command level, not time horizon. Use **planning horizon**.
- **"Collective Cognition Fabric"** — our usage inverts the industry senses of *fabric* and *mesh*.
- **"Organizational OS"** (collides with trademarked EOS®), **"Executable Doctrine"** (Doctrine PHP
  ORM), **"Evolution Chamber"** (StarCraft), **"Cognitive Logistics"** (EU H2020 project).

---

## Hypothesis updates

| ID | Hypothesis | New status | Why |
|---|---|---|---|
| H01 | Intent contracts improve bounded autonomy | **NEEDS EXPERIMENT — reframed** | Not a contract; it is a `Mandate`. The falsifiability property forbids merging them |
| H02 | Artifact-mediated coordination reduces token overhead | **UNCHANGED** | Not addressed in W0 |
| H03 | Capability readiness predicts better routing than idle-agent selection | **UNCHANGED** | Note: `Capability` has **no counterpart in code** — this is a claim about an intention |
| H04 | NOW/NEXT/LATER cells reduce critical-path idle time | **WEAKENED** | `Cell` deleted from the ontology; restate without it or drop |
| H05 | Doctrine improves repeated mission performance | **WEAKENED** | Law 6 falsified: *routine as truce* (Nelson & Winter) is a political settlement between people with interests; agents have none. Meanwhile model versions churn faster than strategy |
| H06 | Organizational world visualization reduces time-to-diagnosis | **UNCHANGED** | Deferred to W4 |
| H07 | Evolution discovers better topologies than manual templates | **SUPPORTED, with a sting** | IMACS shows manual hard-coding *cannot* be right, which supports learned selection — but every learned result is **model-binding-specific** and expires with the binding |
| **H08** | *(new)* Adding a harness-error verdict changes at least one current gate outcome | **NEEDS EXPERIMENT** | Directly testable against the 30 gates |
| **H09** | *(new)* Organizational configuration must be re-validated per model binding | **SUPPORTED** | IMACS ablation, verified |

---

## Concepts promoted

- **The three-axis model** (standing / basis / window) — the most substantive original contribution
  of W0, and it is *descriptive of code that already exists*.
- **`Instrument` + Live-Instrument Rule** — names the estate's most-repeated design decision.
- **The structural / configurational split** — the highest-leverage cut in the ontology.

## Concepts demoted

- **Organizational Compiler** — real prior art (KB-ORG, "fully automated", implemented in Java) and
  a published 2026 competitor. Useful framing; not a first-class primitive, and not a differentiator.
- **Organizational Debugger** — organizational mining (Song & van der Aalst, DSS 46:300–317, **2008**).
- **Evolution Chamber** — Organization Self-Design (1992). Also blocked by the product gate.

## Concepts rejected

- **AOE as a public category** — occupied twice in 2026. *Preserved reason:* the name is not the
  asset; the runtime is.
- **The four-part novelty claim** — refuted component by component. *Preserved reason:* each
  component's best prior art is **better than our implementation**, which is the more useful finding.
- **`Role`, `Cell`, `Signal`, `Field`, `Squad`, `Simulation`** — no mechanism, no state, or covered
  by a surviving term.

---

## Canonical architecture changes — **proposed, not applied**

Nothing in `ontology/`, `architecture/` or `governance/` was modified by this wave. Proposed diffs:

| File | Change |
|---|---|
| `ontology/00-core-ontology.md` | 37 candidates → 13. Delete `Claim`, `Role`, `Cell`, `Signal`, `Field`. Add `Instrument`, `Mandate`. Mark 4 terms configurational with a mandatory `binding` |
| `ontology/01-relationship-map.md` | Remove the four `Claim` edges (meaningless for a lane lease) |
| `architecture/01-intent-contract-schema.md` | Rename away from `IntentContract`; adopt `Contract`/`Mandate`/`Task` |
| `architecture/02-organizational-staff-mesh.md` | Rename — "mesh" is wrong; PROSA's staff holons are centralised |
| `architecture/05-temporal-echelons.md` | Rename to planning horizons |
| `foundations/FOUNDATIONAL_LAWS_DRAFT.md` | Law 6 falsified; Law 9 vacuous; Laws 1/3/5 weakened; Law 4 holds. Add N6 — *structure buys reliability only when it buys independence* |
| `vision/00-agent-army-master-context.md` | Stop leading with compiler/debugger; lead with version-control and test-framework, which are built |

**Do not apply these until a human accepts this synthesis.**

---

## Product implications

### NOW
- **Add the fifth verdict to `agent-factory/factory/contract.py`.** Settable only by the harness,
  not returnable from `Assertion.check`, dominant over `FAIL` in `ContractResult.verdict`.
  *(agent-factory decision — filed, not applied.)*
- **Drop the novelty framing.** Say "synthesis of known controls". It is true and it is stronger.

### NEXT
- Adopt **ICD 206** source-descriptor discipline on top of `MEASURED|DERIVED|ASSUMED`.
- `Mandate`, **behind its enforcement gate**.
- A lint failing on `turn\d+(view|search)\d+` in `agent-factory/docs/research/`, plus a back-fill
  of tokens supporting load-bearing claims.

### LATER
- The structural/configurational split, once something is built to be configured.

### RESEARCH ONLY
- Everything else in the 15 concepts.

### DO NOT BUILD
- The public AOE category. Supervisor tiers — still gated on *one certified team*, unmet, and the
  peer-reviewed title now argues the gain shrinks as models improve.

---

## Experiments created

| ID | Hypothesis | Baseline | Measurable outcome | Stop condition |
|---|---|---|---|---|
| E1 | A harness-error verdict changes gate outcomes | Current 30-gate board | Count of gates whose verdict changes when instrument-crash is separated from `inconc` | If zero change across 30 gates, the distinction is real but inert here — record and stop |
| E2 | The three axes are genuinely orthogonal | The nine existing vocabularies | Can every one of the nine be reconstructed from (standing, basis, window)? | If any needs a fourth axis, the model is wrong |
| E3 | Configuration flips across model bindings *in our estate* | One task class, one topology | Re-run the same team spec across ≥2 model families; does the winner flip? | If it does not flip in 2 families, IMACS may not generalise here |

---

## ADRs required

1. **Do not launch AOE as a public category** (accept C2).
2. **`Contract` / `Mandate` / `Task` three-way split**, superseding `IntentContract`.
3. **Adopt TTCN-3's verdict shape**, including the fifth verdict.
4. **Novelty position:** synthesis claim, not novelty claim.
5. **Ontology cut to 13 terms**, with the structural/configurational split.

---

## Unresolved questions

1. **`Mandate`'s enforcement gate** — is there any boundary in the system that can actually enforce
   authority? If not, it demotes.
2. **ISO 26262 / DO-178C verification vocabularies** are paywalled and unread. A further kill on the
   verdict lattice could come from there.
3. **ODML must be re-sourced** — it is a predictive design model targeting Mathematica, not an IR.
   The Org-IR verdict survives on Moise+/OperA/AGR, not on the source R01's headline sentence names.
4. **The ORA4MAS enforcement quote is behind a paywall** and its chapter subtitle points the other
   way. `NOT-ACCESSIBLE`.
5. Four primary PDFs in R00 are **scanned images** — declared, still a gap.

---

## Methodological finding — carry this forward

**Two WebFetch summaries were wrong in this wave**, in opposite directions:
- one reported no sample-size passage in arXiv:2606.03034 (there is one — reading the PDF killed a
  novelty component);
- one reported an empty arXiv `journal-ref`, from which the synthesizer wrongly concluded
  `UNSUPPORTED` on a Nature paper that exists (retitled).

**A fetch summary is a lead, not evidence.** Load-bearing citations must be extracted from the
artefact — PDF text, metaschema, DOI handle — not from a summariser. Both kills that mattered most
in this wave came from opening the file.

---

## Next research wave

W0 removed the foundation the later waves assumed, so **the manifest's W1 is no longer the highest-
value next question.** Recommended instead:

1. **Re-scope the programme against IMACS and Waites.** Two 2026 papers occupy the thesis. Before any
   further primitive research: what do they *not* do that we would? This is a `prospect`-shaped
   question, not a `deep-research` one.
2. **R40 (AOE as a field) — invert it.** It was written to establish a discipline. Run it to decide
   whether to *join* one.
3. **R30 (evaluation) early, not in W5.** Every surviving claim is now an evaluation claim, and E1–E3
   are ready to run.
4. **Only then W1.** Mission command, intent-centric computing and temporal echelons all presume the
   ontology W0 just cut in half.
