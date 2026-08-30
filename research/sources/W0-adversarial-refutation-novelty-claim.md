# W0 — Adversarial refutation of the surviving novelty claim

**Assignment:** kill the one claim Wave 0 left standing, by running the search the producing lane
admitted it skipped (metrology + software testing), plus adjacent literatures.
**Verdict, up front: REFUTED on all four components.** Every one has prior art that predates the
code, three of the four by decades, and one of them (TTCN-3) is *strictly finer-grained* than what
`factory/contract.py` implements.

**Evidence tiering used below:** `OBSERVED` = I opened the artefact and read the cited text.
`DERIVED` = inferred from something I read. `ASSUMED` = not verified. `MARKETED` = vendor/blog
assertion only. Every citation marked OBSERVED was extracted from the actual PDF/XML/HTML, not
from a search snippet. Two search snippets in this pass turned out to be wrong (noted in §7).

---

## 1. The claim, decomposed

> The narrowest defensible novelty claim is epistemic, not organizational: **an organizational
> runtime where the unit of truth is an evidence-bound claim** — (A) capability claims carrying
> sample size, (B) `UNMEASURABLE` as a first-class verdict that cannot collapse into pass/fail,
> (C) refusal-to-close living in the data store rather than in prompts, and (D) evidence-independence
> tracking.

What the code actually does, so the components are testable rather than rhetorical:

| Component | Concrete implementation | Cite |
|---|---|---|
| B | `Verdict = PASS/FAIL/UNMEASURABLE/NOT_RUN`; aggregate is FAIL > UNMEASURABLE > PASS | `factory/contract.py:17-21`, `:73-85` |
| A | *not implemented.* Nearest is `MEASURED\|DERIVED\|ASSUMED` basis labelling and `DECLARED` vs `VERIFIED`; the vocabulary crawl states "**NO COUNTERPART IN CODE**" for Capability | `factory/tasks.py:136`, crawl `:1387` |
| C | `TaskStore.close()` raises unless ≥1 `MEASURED`/`DERIVED` evidence row exists; `evidence.coverage()` folds rows into SATISFIED/ASSERTED/ABSENT per class | `factory/tasks.py:148-170`, `factory/evidence.py:66-140` |
| D | ordinal `INDEPENDENCE_RISK = LOW/MEDIUM/HIGH/SEVERE` keyed to research pass type; contract assertions requiring "an independent second instrument" | `factory/research_run.py:81-84`, `connector_contract.py:308`, `pbi_contract.py:456` |

⚠ Note before proceeding: **component A is a claim about code that does not exist.** The crawl this
programme itself produced says Capability has no counterpart in the codebase. The novelty claim is
therefore partly a claim about an intention. I refute it as stated anyway.

---

## 2. Component B — `UNMEASURABLE` as a first-class verdict that cannot collapse

### Verdict: **REFUTED.** Comprehensively, and by a standard from 1994.

#### Strongest prior art — ETSI ES 201 873-1 (TTCN-3), clause 24.1, Table 30

`OBSERVED` — I downloaded **ETSI ES 201 873-1 V4.16.1 (2024-10)**, *Methods for Testing and
Specification (MTS); The Testing and Test Control Notation version 3; Part 1: TTCN-3 Core Language*,
and read pages 284–285. Verbatim, p.285:

> "The verdict can have five different values: `pass`, `fail`, `inconc`, `none` and `error`, i.e. the
> distinguished values of the `verdicttype` (see clause 6.1).
> NOTE 2: `inconc` means an inconclusive verdict."

> "When changing the value of the local verdict (i.e. using the `setverdict` operation) the effect of
> this change shall follow the overwriting rules listed in table 30."

**Table 30 — Overwriting rules for the verdict** (verbatim structure):

| Current value ↓ / New assignment → | pass | inconc | fail | none |
|---|---|---|---|---|
| **none** | pass | inconc | fail | none |
| **pass** | pass | inconc | fail | pass |
| **inconc** | **inconc** | inconc | fail | **inconc** |
| **fail** | fail | fail | fail | fail |

Read the `inconc` row. **Assigning `pass` to a component already at `inconc` leaves it at `inconc`.**
This is not a convention or a lint rule — it is a normative monotone lattice in an international
standard, and it is the exact property the novelty claim asserts as novel: *a verdict meaning "I could
not tell" that cannot collapse into a pass.*

And p.285 goes further than agent-factory does:

> "The `error` verdict is special in that it is set by the test system to indicate that a test case
> (i.e. runtime) error has occurred. It shall not be set by the `setverdict` operation and will not be
> returned by the `getverdict` operation. **No other verdict value can override an `error` verdict.**"

The mapping onto `factory/contract.py` is one-to-one, and unfavourable:

| agent-factory | TTCN-3 | Note |
|---|---|---|
| `PASS` | `pass` | — |
| `FAIL` | `fail` | — |
| `UNMEASURABLE` | `inconc` | same meaning, same non-collapsibility |
| `NOT_RUN` | `none` | same role: initial value before any assignment |
| — | `error` | **agent-factory has no counterpart** |

`contract.py:57-59` catches *any* exception from a check and returns `UNMEASURABLE`
("instrument raised …"). TTCN-3 separates that case — the test system itself broke — into a distinct
`error` verdict that nothing can override. So on its own flagship distinction, **agent-factory is one
category coarser than a standard finalised in the 1990s.** That is the opposite of novelty.

#### Corroborating prior art (all `OBSERVED`)

- **ISO/IEC 9646 (OSI Conformance Testing Methodology), via Tretmans' overview.** `OBSERVED` — Jan
  Tretmans, *An Overview of OSI Conformance Testing*, §3.5, retrieved from
  `https://homes.cs.aau.dk/~kgl/TOV03/iso9646.pdf`, citing ISO IS-9646 (1991): "The verdict is either
  *pass*, *fail*, or *inconclusive*. … **Inconclusive indicates that no evidence of non-conformance
  was found, but that the test purpose was not achieved.**" The worked example is precisely the
  anti-collapse argument: a legal-but-off-purpose response "is allowed according to the Transport
  standard, but the verdict pass cannot be assigned since the test purpose was not achieved."
  *(The ISO standard itself is paywalled — see §7 NOT-ACCESSIBLE.)*
- **VIM / JCGM 200:2012, entry 4.18 `detection limit`.** `OBSERVED` — downloaded from BIPM,
  p.58: "measured quantity value, obtained by a given measurement procedure, for which the probability
  of **falsely claiming the absence of a component** in a material is β, given a probability α of
  falsely claiming its presence." Metrology does not merely *permit* the distinction between "zero"
  and "the instrument could not see" — it **defines a quantity whose entire purpose is to bound the
  probability of falsely claiming absence**, and assigns it default α = β = 0.05 (NOTE 1). The
  discipline agent-factory calls "a zero from an instrument you have not proved can see is not a
  measurement" is the definitional core of an entry in the international metrology vocabulary.
- **SMT-LIB `check-sat`: `sat` / `unsat` / `unknown`, with `(get-info :reason-unknown)`.** `DERIVED`
  from the cvc5 tutorial and the SMT-LIB standard as reported in search; I did not open the SMT-LIB
  standard PDF. This is `UNMEASURABLE` plus a detail string, and it has been standard practice in
  automated reasoning for two decades.
- **TAP version 14 `SKIP` / `TODO` directives.** `OBSERVED` (testanything.org TAP14 spec):
  "Harnesses *must not* treat failing `TODO` test points as a test failure"; "Harnesses *must not*
  treat failing `SKIP` test points as a test failure." A skipped point "indicate[s] that a test was
  not run" — a third status that is neither pass nor fail.
- **JUnit XML `<error>` vs `<failure>` vs `<skipped>`.** `DERIVED` (schema descriptions, not the XSD
  itself): a *failure* is an assertion the code explicitly failed; an *error* is "an unanticipated
  problem" that prevented the test completing. The instrument-broke / thing-is-broken split is the
  default shape of every mainstream test report format.

#### What this kills

Not just "the idea has been had". The specific, load-bearing sub-claim — *a verdict that cannot
collapse into pass* — is a **normative table in a maintained international standard**, and the
research lane could have found it by searching the phrase "inconclusive verdict".

---

## 3. Component A — capability claims carrying sample size

### Verdict: **REFUTED.** Including, fatally, in the agent literature itself.

#### Strongest prior art — arXiv:2606.03034, §4.2

`OBSERVED` — Gaurav Naresh Mittal, *Capability Advertisement as a Market for Lemons: A Trust Layer
for Heterogeneous Agent Networks*, arXiv:2606.03034 [cs.MA], submitted 2 June 2026. I downloaded the
PDF and read §4.2 on page 6. Verbatim:

> "**4.2 Probabilistic capability descriptors (signaling).** The descriptor replaces the boolean
> claim with a structured one. Instead of 'I summarize indemnification clauses,' an agent publishes
> that it does so with reliability approximately 0.91, **calibrated on a named benchmark of a stated
> size and date**, with accuracy that falls past roughly eight thousand tokens, produced by backend
> version v3.2, valid for thirty days. It is, in effect, a nutrition label for competence.
>
> The point is not merely richer metadata; it is credible metadata. A bare number is cheap to
> inflate, so **the descriptor's load-bearing field is provenance: the evidence behind the claim —
> which evaluation, when, on how many samples.**"

This is component A, stated more precisely than the novelty claim states it, in the same domain
(LLM agents delegating over MCP/A2A), published three months before this research programme's Wave 0.
It also independently arrives at three further things agent-factory has: **staleness/TTL on a claim**
("descriptors and attestations carry a time-to-live, after which they are discounted or re-checked,
so that stale claims do not accrue unearned trust", §4.4 — cf. `context.py` CURRENT/STALE/UNVERIFIED),
**independent attestation as a separate principal** (§4.3: "an independent party evaluates the agent
and issues a signed statement" — cf. `corpus.py`'s grader separation), and **verifiability over
authority** (§4.3.1: "An attestation should not say 'trust me, this agent is good.' It should say
'I ran this public benchmark with this seed; here is the signed, reproducible transcript.'" — cf.
the hashed corpus + `stamp()` provenance block).

#### Corroborating prior art (all `OBSERVED`)

- **GRADE.** Certainty in a claim is downgraded for *imprecision* on an explicitly sample-size-driven
  criterion, the **optimal information size (OIS)**: when event counts fall below OIS the rating is
  downgraded even if the confidence interval excludes the null. Guyatt et al., *GRADE guidelines 6:
  Rating the quality of evidence — imprecision*, J Clin Epidemiol 2011 (PMID 21839614). `DERIVED` —
  I read the CDC ACIP GRADE Handbook ch.8 and the search-returned summary of the guideline; I did not
  open the Guyatt PDF itself. The principle — *a claim carries a certainty grade that is a function of
  how much evidence stands behind it* — is the core of evidence-based medicine and predates the code
  by ~15 years.
- **Model Cards.** `OBSERVED` — Mitchell et al., *Model Cards for Model Reporting*, arXiv:1810.03993;
  I downloaded the PDF. §4.4.3 *Confidence*: "Performance metrics that are disaggregated by various
  combinations of instrumentation, environments and groups makes it especially important to understand
  the confidence intervals for the reported metrics." §4.7 *Quantitative Analyses*: "Quantitative
  analyses should provide the results of evaluating the model according to the chosen metrics,
  **providing confidence interval values when possible** … should demonstrate the metric variation
  (e.g., with error bars)". A model card is definitionally a capability claim carrying its evaluation
  data and its evidence strength.
- **ICD 203, Analytic Tradecraft Standard (2).** `OBSERVED` — I extracted the text from the ODNI
  ICD 203/206/208 compilation PDF (ICD 203 as technically amended; original signed 2 January 2015).
  Standard (2) requires products to explain the basis for uncertainty, where "Analysts' confidence in
  an assessment or judgment may be based on the logic and evidentiary base that underpin it,
  **including the quantity and quality of source material**". Quantity of evidence as a mandatory
  qualifier on a published judgment, enforced across the US Intelligence Community, since 2015 (and
  in ICD 203's 2007 predecessor).
- **Adding Error Bars to Evals.** `DERIVED` — Evan Miller (Anthropic), arXiv:2411.00640, 1 Nov 2024;
  I verified the arXiv record but did not read the PDF. Recommends confidence intervals and power
  analysis for LLM evaluation reporting — i.e. the same discipline aimed at exactly the class of
  capability claim agent-factory would be making.

---

## 4. Component C — refusal-to-close in the data store rather than in prompts

### Verdict: **REFUTED.** This is the single least novel of the four; it is ordinary workflow engineering.

The claim's distinguishing move is *where* the refusal lives — in the store, not in a prompt. Every
mainstream work-tracking and delivery system already does exactly this, and has for years.

#### Strongest prior art

- **Jira workflow validators.** `DERIVED` (Atlassian support/admin documentation; one target page
  returned a summary that did not carry the definition, so I am tiering this DERIVED rather than
  OBSERVED). A *validator* on a workflow transition checks a condition after submission and **blocks
  the transition** if unmet — the canonical instance being a Required Field validator on the
  transition into Done. This is the identical shape to `TaskStore.close()` raising unless an evidence
  row exists: the issue store refuses the state change, and no amount of instruction to the actor can
  bypass it. Atlassian ships it; countless teams use it to enforce definition-of-done.
- **GitHub branch protection / rulesets — required status checks.** `OBSERVED` (GitHub Docs, *About
  protected branches*): "Required status checks must have a `successful`, `skipped`, or `neutral`
  status before collaborators can make changes to a protected branch"; "all required status checks
  must pass before collaborators can merge changes into the protected branch." Enforced server-side,
  not by a client hook a developer can `--no-verify` past — the exact prompts-vs-store distinction the
  novelty claim rests on. Note also that GitHub's own status vocabulary is four-valued
  (`success`/`failure`/`neutral`/`skipped`), again refusing a two-valued collapse.
- **OPA / Gatekeeper admission control.** `DERIVED` (Kubernetes blog 2019-08-06; OPA docs): a
  validating admission webhook where `enforcementAction` defaults to `deny`, so a resource that
  violates a constraint is refused at the API server — policy-as-code enforced at the store, with an
  explicit `warn`/dry-run mode for the advisory case. Graduated CNCF project since January 2021.
- **NIST OSCAL Assessment Results model.** `OBSERVED` — I fetched
  `src/metaschema/oscal_assessment-common_metaschema.xml` from `usnistgov/OSCAL` @ main and read the
  definitions. A `finding` carries an `objective-status`; an `observation` carries one or more
  `method` values from `{EXAMINE, INTERVIEW, TEST, UNKNOWN}` and a `relevant-evidence` assembly that
  "Links this observation to relevant evidence" by resolvable URL. That is *the unit of truth being an
  evidence-bound claim*, as a machine-readable NIST standard, with a typed vocabulary for how the
  observation was made.
- **in-toto / SLSA attestations.** `DERIVED` (slsa.dev attestation-model and in-toto/SLSA blog):
  a Statement binds a Predicate (e.g. SLSA Provenance) to Subjects; a policy engine consumes
  attestations and yields an admit/refuse decision, and Binary Authorization refuses to deploy an
  artifact lacking the required attestation. Refusal-to-promote, grounded in recorded evidence,
  enforced by machinery rather than by asking nicely.
- **Guard-Stage-Milestone / artifact-centric business processes.** `DERIVED` (Hull et al., IBM; ACM
  DEBS 2011 `10.1145/2002259.2002270`): a declarative lifecycle where stages open on *guards* and
  close on *milestones* evaluated over the artifact's own information model. The academic form of
  "the process constraint lives in the data, not in the instructions", published ~2011.

#### One honest nuance, which does not save the claim

The closest thing in the *agent* literature runs the other way: **SmartSnap** (Youtu-Agent Team,
arXiv:2512.22322, 26 Dec 2025) — `OBSERVED`, I read the PDF — gates task success on evidence with a
"**success only upon unequivocal proof**" rule and "**Zero Assumptions: … What is not shown in the
evidence is assumed not to have happened**" (§ p.6). That is agent-factory's evidence gate, stated
almost word for word. But SmartSnap implements it *in a judge prompt* (the verbatim rubric is in its
appendix, p.24) and its outcome reward is binary, `R_complete ∈ {1,0}`. So SmartSnap occupies
"evidence-bound close" and concedes "in the store, not the prompt" — while Jira, GitHub, OPA, OSCAL
and in-toto occupy "in the store, not the prompt" decisively. Between them the component is covered;
there is no gap in the middle, only the un-novel act of pointing the second group's mechanism at the
first group's subject matter.

---

## 5. Component D — evidence-independence tracking

### Verdict: **REFUTED.**

#### Strongest prior art — Bloomfield & Rushby on diverse evidence in assurance cases

`OBSERVED` — Robin Bloomfield and John Rushby, *Confidence in Assurance 2.0 Cases*, arXiv:2409.10665,
v1 16 Sep 2024, v2 7 Aug 2025 (expanded version of a paper in *The Practice of Formal Methods: Essays
in Honour of Cliff Jones*, Springer LNCS 14780, pp. 1–23). Verbatim from the paper:

> "if E1 is evidence of successful tests, it will not be surprising if additional tests are
> successful; instead we should seek evidence E2 that is 'diverse' from E1, such as static analysis."

> "E2 delivers the largest 'boost' … when E2 would be surprising given only E1, but not when given C
> as well, which confirms that E2 should be diverse from E1."

This is the Bayesian formalisation of exactly what `connector_contract.py:308` ("A10-source-agreement
— independent second instrument") and `pbi_contract.py:456` ("M9-warehouse-agreement — independent
second instrument") assert, and of what `research_run.py`'s `INDEPENDENCE_RISK` ordinal gestures at.
The multi-legged-argument literature it sits in (CAE, Bloomfield et al. 1998; eliminative induction
and Baconian confidence, Goodenough/Weinstock/Klein) is 25+ years old.

#### Corroborating prior art (all `OBSERVED` unless noted)

- **ICD 203 Analytic Tradecraft Standard (1) + ICD 206 source descriptors.** `OBSERVED` from the ODNI
  PDF. Standard (1) requires products to "use source descriptors in accordance with ICD 206 … to
  describe factors affecting source quality and credibility. Such factors can include accuracy and
  completeness, possible denial and deception, age and continued currency of information, and
  technical elements of collection as well as source access, validation, motivation, possible bias, or
  expertise." ICD 206's glossary defines *source descriptor* and *source summary statement*, the
  latter "to provide a holistic assessment of the strengths or weaknesses in the source base". The
  named failure this guards against — **circular reporting**, where information appears to come from
  multiple independent sources but traces to one — is the exact hazard `INDEPENDENCE_RISK` names.
- **ICD 203 Analytic Tradecraft Standard (3).** `OBSERVED`, and worth flagging separately because it
  refutes a *fifth* thing the crawl called novel: "**Properly distinguishes between underlying
  intelligence information and analysts' assumptions and judgments**: Analytic products should clearly
  distinguish statements that convey underlying intelligence information used in analysis from
  statements that convey assumptions or judgments. … Products should state assumptions explicitly when
  they serve as the linchpin of an argument." That is `MEASURED | DERIVED | ASSUMED` basis labelling,
  mandated across the US IC since 2007/2015. The crawl (`:1520`) lists basis labelling as something
  "the research ontology lacks entirely"; it is in fact standard analytic tradecraft.
- **W3C PROV-O.** `DERIVED` (W3C Recommendation, 30 April 2013): `prov:wasDerivedFrom` and its
  sub-property `prov:hadPrimarySource` make derivation chains machine-traceable, which is the
  substrate on which independence is *computed* (two entities sharing a primary source are not
  independent). PROV does not itself define an independence verdict — this is the one component where
  the strongest hit is a formalism rather than a ready-made control — but Bloomfield & Rushby supply
  the verdict layer and ICD 203/206 supply the operational one.
- **Agent-domain coverage exists too.** `OBSERVED` (abs/HTML) — Wang et al., *From Agent Traces to
  Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents*, arXiv:2606.04990v4,
  28 June 2026: a survey, with a six-dimension taxonomy, whose provenance relations extend PROV with
  "Support, Depend-on, Contradict, Invalidate, Trigger, and Update". A field with a survey is not a
  field with an unoccupied claim.

---

## 6. What is left of the novelty claim

Stated as narrowly as the evidence forces: **nothing that should be called novel.**

The umbrella framing — *an organizational runtime where the unit of truth is an evidence-bound claim*
— is itself occupied, twice over and in two directions:

- **NIST OSCAL** already models findings bound to observations bound to typed evidence, machine-
  readably, as a US federal standard (`OBSERVED`, metaschema read directly).
- **Protocol-Driven Development** (He & Yu, arXiv:2605.12981, 13 May 2026 — `OBSERVED`, abstract read
  in full) proposes that for *generated* software "An implementation is admitted only if it satisfies
  the protocol and produces a verifiable **Evidence Chain** of compliance. Admission is grounded in
  protocol satisfaction and recorded evidence rather than trust in the generator," extended at runtime
  into a "**Dynamic Evidence Ledger**" where "Runtime verifiers append signed observations, invariant
  checks, and violations". Same thesis, same year, aimed at the same problem (governing machine-
  generated work product), explicitly combining "formal methods, property testing, runtime
  verification, policy-as-code, and software provenance".

Three things survive contact with the evidence, and I state them without inflating them:

1. **The specific conjunction, wired into one runnable artefact for agent-team work, does not appear
   to exist elsewhere.** No source I found combines a non-collapsing verdict lattice + basis-labelled
   evidence + store-enforced closure + an independence ordinal in a single operational runtime for
   agent teams. But *conjunction of four independently standard components is not novelty*, and the
   programme should not accept it as such — particularly when each component's best prior art is
   better than the local implementation.
2. **A narrow gap of application, not of idea:** the compliance/assurance world's own machine-readable
   format collapses where TTCN-3 does not. OSCAL's `objective-status/@state` is **binary** —
   `OBSERVED`, verbatim from the metaschema: `satisfied` ("The objective has been completely
   satisfied") and `not-satisfied` ("has not been completely satisfied, but may be partially
   satisfied") — with an unenumerated `reason` flag whose values are `pass`/`fail`/`other`. So
   "a non-collapsing verdict lattice inside an *organizational* evidence runtime" is genuinely
   underoccupied. It is also a two-hour port of Table 30, and claiming it as the programme's
   epistemic foundation would be claiming credit for reading a 1990s standard.
3. **The evidence-class vector** (`TARGET`/`CONSUMER`/`REGRESSION`/`ROLLBACK`, each with
   SATISFIED/ASSERTED/ABSENT) — I found no prior art for these *four specific questions*. But the
   *shape* (typed evidence classes, enumerated methods, required for closure) is exactly OSCAL's
   `method ∈ {EXAMINE, INTERVIEW, TEST, UNKNOWN}` + `relevant-evidence`, and NIST SP 800-53A's
   assessment methods before it. The four questions are hard-won domain doctrine from real incidents.
   Doctrine is valuable. It is not a novel primitive.

### The finding the programme most needs to hear

On its flagship component, **agent-factory is coarser than the 1994 art.** `contract.py:57-59` folds
"the instrument could not decide" and "the instrument itself crashed" into a single `UNMEASURABLE`;
TTCN-3 separates `inconc` from `error` and makes `error` un-overridable by anything. A programme whose
stated foundation is "never collapse two different kinds of not-knowing" is currently collapsing two
different kinds of not-knowing, and would have caught it by reading the standard it did not search.

**Recommendation:** do not build on this as a novelty claim. Build on it as a *synthesis* claim —
"we assembled known controls from conformance testing, metrology, assurance cases and analytic
tradecraft into one runtime for agent teams" — which is defensible, honest, and immediately improvable
by adopting TTCN-3's fifth verdict and ICD 206's source-descriptor discipline.

---

## 7. Searches run, and what could not be completed

### Run and productive (artefact opened)

| # | Target | Method | Result |
|---|---|---|---|
| 1 | TTCN-3 verdict types + overwriting rules | downloaded `es_20187301v041601p.pdf` (2.08 MB, 395 pp) from ETSI, extracted pp. 284–285, 293 with PyMuPDF | **kill** — Table 30 |
| 2 | ISO 9646 inconclusive verdict | downloaded Tretmans overview PDF, extracted pp. 11, 13 | **kill (secondary source)** |
| 3 | VIM detection limit | downloaded `JCGM_200_2012.pdf` (108 pp) from BIPM, extracted entry 4.18 p.58 | **corroborates** |
| 4 | Capability descriptors w/ sample size | downloaded arXiv:2606.03034 PDF, read §4.2–4.4 pp. 5–7 | **kill** |
| 5 | Model cards | downloaded arXiv:1810.03993 PDF, extracted §4.4.3, §4.7 | **corroborates** |
| 6 | OSCAL assessment model | fetched `oscal_assessment-common_metaschema.xml` from GitHub raw, read status/method/relevant-evidence definitions | **kill (C) + gap (B)** |
| 7 | ICD 203 / ICD 206 | downloaded ODNI compilation PDF, extracted pp. 3–5, 8, 13 | **kill (D) + kills basis-labelling** |
| 8 | Assurance-case evidence diversity | fetched arXiv:2409.10665 HTML + verified abs record | **kill (D)** |
| 9 | SmartSnap evidence gating | downloaded arXiv:2512.22322 PDF, read §p.6 and appendix p.24 | **partial (C)** |
| 10 | Protocol-Driven Development | fetched arXiv:2605.12981 abs, abstract in full | **kill (umbrella)** |
| 11 | TAP14 SKIP/TODO | fetched testanything.org TAP14 spec | **corroborates (B)** |
| 12 | GitHub branch protection | fetched GitHub Docs *About protected branches* | **kill (C)** |
| 13 | Agent evidence-provenance survey | fetched arXiv:2606.04990v4 HTML | **field is occupied (D)** |

### Run, search-level only (tiered DERIVED above, not OBSERVED)

GRADE imprecision/OIS; SMT-LIB `unknown`; JUnit XML `<error>`/`<failure>`/`<skipped>`; OPA/Gatekeeper
default-deny; Jira workflow validators; in-toto/SLSA attestation model; Guard-Stage-Milestone.
Each is reported at the tier its verification supports.

### NOT-ACCESSIBLE — named, not inferred

- **ISO/IEC 9646-1:1994** (and Parts 2, 3, 7) — paywalled at iso.org. I did **not** read the standard.
  The `inconclusive` definition above comes from Tretmans' academic overview citing IS-9646 (1991),
  which I did read. The primary text is unverified.
- **ISO/IEC 17025** — paywalled; not consulted. I make no claim about its reporting requirements.
- **ISO 26262** and **DO-178C** — paywalled; not consulted. The brief suggested checking their
  verification-status vocabularies; **I did not, and nothing above rests on them.** They remain a live
  place a further kill could come from.
- **ISO/IEC 9646-7 PICS proformas** — not consulted beyond a glossary mention. The component-A angle
  ("declared capability with a conformance statement") is therefore *under*-searched; given
  arXiv:2606.03034 already refutes A, this does not change the verdict, but it would likely add an
  older citation.
- **ETSI ES 201 873-1 §6.1** (`verdicttype` formal definition) — the PDF was read at clause 24 only;
  clause 6.1 was not extracted. The five values are confirmed at clause 24.1 regardless.
- **Guyatt et al. GRADE guidelines 6 PDF** — located but not opened; tiered DERIVED.

### Searches deliberately not run

Medical indeterminate/equivocal result categories, and Belnap four-valued logic. Component B was
already killed by a normative standards table with a verbatim lattice; further corroboration would
have added length without changing the verdict. Flagged here so the omission is visible rather than
silent.

### Two search snippets that were wrong, recorded as a caution

- A WebFetch summary of arXiv:2606.03034 stated there were "**no passages where capability descriptors
  explicitly carry sample size, benchmark size, number of samples, date, or provenance**." That is
  false; §4.2 says exactly that, verbatim, on page 6. Caught by extracting the PDF text directly.
- A search snippet attributed to the same paper a phrase about "reliability approximately with a stated
  benchmark size and date" that reads as a paraphrase; the actual sentence is quoted verbatim in §3.

Both are the failure mode the brief warned about. **Every OBSERVED citation in this document was
extracted from the artefact itself**, not from a search result or a fetch summary.
