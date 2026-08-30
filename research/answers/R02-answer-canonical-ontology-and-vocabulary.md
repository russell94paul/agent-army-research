# Research Answer — R02 / Canonical Ontology and Vocabulary

## Metadata

```yaml
research_id: R02
title: Canonical Ontology and Vocabulary
run_date: 2026-08-30
status: complete
researcher_or_model: Claude Opus 5 (1M context), running as a LOCAL SUBAGENT inside
  C:/Users/PaulRussell/repos/aldc-launchpad, with read access to agent-army-research and
  agent-factory.
pass_type: STRUCTURE_CRITIQUE (per factory/research_run.py:54-61)
independence_risk: HIGH — factory/research_run.py:81 assigns STRUCTURE_CRITIQUE the HIGH band,
  and that is the correct band for this pass. Declared honestly, both halves:
  WEAKER than an outside model. I read R00, R01 and the vocabulary crawl before forming a view,
    and all three were produced inside this estate. The pull toward agreeing with them is real and
    I could not fully counter it, because unlike R00 I could not read the contested terminology
    "blind" — the drafts were the brief's required input. What I DID do instead: for every term
    where I disagree with R00 or R01 I state the disagreement explicitly and give the mechanism,
    and I ran one literature search that W0 records as never having been run (§Finding 1), which
    materially weakens R01's central novelty claim. A pass that only agreed would not have done
    that.
  STRONGER than an outside model on file-and-line claims. Every agent-factory citation I lean on
    was re-read by me from the source file at HEAD a090f6f, not inherited from the crawl. Where I
    rely on the crawl without re-reading, I say so inline.
repository_access: read-only. No file other than this answer was created, edited, staged,
  committed or branched. ontology/ was NOT touched.
repositories_inspected:
  - agent-army-research @ main (read - ontology/00, ontology/01, vision/01, foundations/R02,
    research/answers/R00, research/answers/R01, research/sources/*, research/ANSWER_TEMPLATE.md)
  - agent-factory @ docs/agent-army-research-separation, HEAD a090f6fe1778cd328b419641a937f723cec3c249
    - NOTE the crawl was produced at a691043 and R00 saw a691043 -> ed89cb3. HEAD moved twice more
      during this pass. Another session is committing to that branch. All line numbers below were
      re-read at a090f6f and held.
web_access: yes - 6 searches, 2 fetches. Deliberately narrow: I did NOT re-run R00's or R01's
  surveys. The only literature I went to is the one W0-citation-verification-partial.md:202-204
  records as never having been searched, because R01's single surviving novelty claim rests on it.
primary_sources_read: 4 external (2 read via search synthesis = SECONDARY, 2 fetch attempts, one
  403 and one unparseable PDF - both declared below), plus 21 agent-factory modules re-read.
counting_basis: |
  "Canonical term" = a term I give the brief's full 15-field schema to. 13 of them.
  "Candidate term" = a line in foundations/R02:22-60. 37 of them, counted from the literal.
  Command that regenerates the candidate count:
    sed -n '23,59p' foundations/R02-canonical-ontology-and-vocabulary.md | grep -c .
```

---

## Executive conclusion

**The single highest-value thing in this answer is not the ontology. It is one term the ontology
did not have.**

The vocabulary crawl found the same design decision implemented nine times under nine different
value vocabularies, and the research ontology has no word for it. I have named it, given it the
15-field schema, and mapped all nine onto it — and in doing so found that the nine are not nine
instances of one vocabulary. **They are nine different collapses of three orthogonal axes.** That
result is in §Deliverable 1 / `Instrument`, and it is the finding I would keep if everything else
here were thrown away.

**What appears true.**

1. **`Instrument` is the missing term, and it is not a coinage.** The word "instrument" appears in
   prose in 15 `factory/` modules (68 occurrences, `grep -rc instrument --include=*.py factory
   evaluator_service`) and is a `Finding.KIND` (`findings.py:40`) — but there is no `Instrument`
   type anywhere. The estate has been talking about instruments for months without being able to
   name one. Promoting its own prose word to a type is the cheapest possible ontology change and
   the highest-leverage one.
2. **The nine vocabularies collapse three orthogonal axes, differently each time.** Every one of
   the nine mixes some of: **standing** (did the instrument see?), **basis** (how strongly do we
   believe the value?), and **window** (over what period?). `context.py:56-58` is the only module
   that has noticed this and separated two of the three — *"A ref can be perfectly current and
   still be somebody's guess; a ref can be a hard measurement taken a year ago."* Naming all three
   once explains why `context.py` needs four confidence values while `tasks.py` needs three, and
   why nobody has ever reconciled them: **they are measuring different axes.**
3. **`contract` is decided, and both R00 and the draft are wrong about how.** Keep `Contract` =
   `GreenContract`. Do not create `IntentContract` (the draft). But also do not *merge* intent into
   it (R00's Deliverable 6). A `GreenContract` is a set of **falsifiable** assertions with a
   four-verdict outcome; authority, escalation and acceptable variation are **permissions**, which
   are not falsifiable and therefore cannot be members of that set without destroying the property
   the object exists for. They need a different home, and I name it `Mandate`. See §Finding 3.
4. **The four-verdict vocabulary is not novel, and I can now say so with a citation.** ISO/IEC 9646
   (1991) and TTCN-3 (`none / pass / inconc / fail / error`, with an explicit *"error indicates an
   error in the test devices"*) standardised a five-verdict conformance vocabulary with the
   instrument-versus-subject split thirty-five years ago, and with a dominance lattice. This is a
   direct hit on R01's "narrowest defensible novelty claim", which W0:202-204 flagged as resting on
   a search nobody had run. I ran it. §Finding 1.
5. **The IMACS finding forces a cut nobody has made yet.** If the winning organizational placement
   flips across model families, then terms describing *structure* and terms describing
   *configuration* have different epistemic status and must not sit in one flat list. Nine of my
   thirteen terms are structural; four are configurational and carry a mandatory model binding.
   §Finding 6. **I believe this is the most important cut in the ontology and it is the one the
   draft, R00 and R01 all miss.**

**What remains uncertain.**

- Whether `Mandate` is enforceable at a boundary *in this harness at all*. R00's N3 says a
  constraint in a prompt is not a constraint, and `blueprint.prohibition` (`blueprint.py:50`) is
  prose in a prompt. If nothing can enforce a Mandate, the term is a wish and should be demoted to
  RESEARCH ONLY. Nobody has tested it. §Open questions Q1.
- Where `REFUSED` sits in the verdict lattice. TTCN-3 puts `error` **above** `fail`; agent-factory
  puts `FAIL` above `UNMEASURABLE` and leaves `REFUSED` outside the enum entirely, so the question
  has never been forced. §Finding 2.
- Whether the `basis` ladders should be reconciled. `tasks.py:136` has three values;
  `context.py:63` has four (it adds `STATED`); nothing reconciles them. I recommend **four
  everywhere**, but this is `DERIVED`, not measured. §Deliverable 8, Q3.

**What we should do.**

- Adopt **13 canonical terms** from the 37 candidates. Nine structural, four configurational.
  Everything else is derived, deprecated or deleted (§Deliverable 1, §Deliverable 7).
- Adopt `Instrument` with `standing = LIVE | DARK | UNPROVEN`, and adopt the two named rules that
  hang off it: the **Live-Instrument Rule** and its violation, a **Blind Zero**.
- Adopt `ContextPack` / `ContextRef` verbatim from the code and delete `ContextPackage`. I agree
  with the crawl and I checked its reasoning rather than inheriting it (§Finding 5).
- Delete `Claim` from the ontology **entirely** — not rename, delete. Use `Assertion`. This is an
  explicit disagreement with R00, which kept `Claim` as one of its nine objects (§Finding 4).

**What we should explicitly NOT do.**

- **Do not rename the nine vocabularies in code.** Every one is validated, several are tested, and
  the rename buys nothing. Name the concept once in the ontology so the *tenth* module does not
  invent a tenth vocabulary. This is a documentation change, not a refactor. §Recommendation.
- **Do not introduce `IntentContract`, `Claim`, `ContextPackage`, `Readiness`, `Policy`,
  `Doctrine`, `Outcome` or `Role`** as schema identifiers. Each collides with something live.
- **Do not put an Army label in a schema identifier, an API field, or a definition.** The mapping
  in §Deliverable 6 is display-layer only, and it has one enforcement rule.
- **Do not write the relationship map as edges between all thirteen.** The draft
  `01-relationship-map.md` gives `Claim` four edges (`:35-39`) that are meaningless for the object
  the code calls `Claim`. A relationship map drawn before the terms are settled encodes the
  unsettled version.

---

## Question decomposition

The subquestions actually investigated, in the order worked:

1. What does the code actually bind, and which bindings are cheap to break? (§Finding 7, and the
   re-verification pass in §Evidence)
2. Is there an established name for the "zero from a blind instrument" concept, in metrology,
   testing, statistics or monitoring? (§Finding 1 — the search W0 says was never run)
3. Given that answer, what is the smallest set of terms that covers the nine vocabularies without
   nine names? (§Deliverable 1 / `Instrument`)
4. Is `IntentContract` resolvable at all, or must the head noun move? (§Finding 3)
5. Is R00 right to keep `Claim`? (§Finding 4 — no)
6. Is the crawl right that `ContextPack` should be adopted rather than renamed? (§Finding 5 — yes,
   and for a reason the crawl does not state)
7. What does IMACS's model-binding result do to a fixed ontology? (§Finding 6 — it splits it in
   two)
8. Which of the ten required distinctions are real boundaries and which dissolve? (§Deliverable 2)
9. Which candidate terms fail the four rejection tests, and on which test? (§Deliverable 7)
10. What is the minimum vocabulary needed *today*? (§Closing answer)

---

## Prior art

Per the template's format. Only the concepts where I did primary work; R00 §Prior art and R01
§Deliverable 6 cover the organizational lineage and I do not repeat them.

```text
concept                 A non-collapsible verdict vocabulary in which "the instrument could not
                        run" is a first-class outcome
earliest precedent      ISO/IEC 9646-1:1991, OSI Conformance Testing Methodology and Framework —
                        pass / fail / inconclusive as standardised verdicts. SECONDARY: I confirmed
                        the standard exists and its scope at iso.org; the verdict definitions
                        themselves I could not read (see NOT-SUPPLIED).
modern precedent        TTCN-3 (ETSI ES 201 873-1 / ITU-T Z.161). Five predefined verdicts —
                        none, pass, inconc, fail, error — where "inconc describes a situation where
                        neither a pass nor a fail can be assigned" and "error indicates an error in
                        the test devices", set automatically by the runtime. Verdicts form a
                        dominance lattice none < pass < inconc < fail < error and may only ever
                        get worse.
                        Also: Grafana Alerting's NoData vs Error vs OK — "the alert rule query runs
                        successfully but returns no data points" (NoData) is a different state from
                        "the alert rule fails to evaluate its query" (Error), and both are distinct
                        from OK.
what transfers          Almost everything. The five-value shape, the instrument-vs-subject split,
                        the dominance lattice, and the aggregation rule. factory/contract.py:73-85
                        independently re-derived the lattice: any FAIL -> FAIL; else any
                        UNMEASURABLE -> UNMEASURABLE; empty -> NOT_RUN; else PASS. That is
                        TTCN-3's ordering for the three values they share.
what does not           TTCN-3 verdicts are per test case in a conformance run against a protocol
                        specification. They carry no basis axis, no evidence class, no coverage
                        state, no window, and the refusal does not live in a store that rejects a
                        close. Nothing in TTCN-3 says "an assumed proof is not a proof".
novelty risk            SEVERE for "UNMEASURABLE as a first-class verdict" stated alone.
                        MODERATE for the composition (verdict x basis x evidence-class coverage,
                        enforced in the store). See §Finding 1 for the narrowed claim.
```

```text
concept                 Refusing to report an unobserved absence as a zero
earliest precedent      Analytical chemistry / metrology: the detection limit and the
                        left-censored "non-detect". "Non-detection is different from zero
                        concentration"; statisticians call the threshold a censoring limit.
                        IUPAC (1995, 1998) recommends that results should not be censored and
                        should always carry a quantitative uncertainty estimate.
modern precedent        Altman & Bland, "Absence of evidence is not evidence of absence",
                        BMJ 1995;311:485 — a non-significant result shows "an absence of evidence
                        of a difference", not evidence of no difference. ~1,100+ citations.
what transfers          The distinction itself, and — importantly — the vocabulary discipline:
                        metrology reports a non-detect WITH its detection limit, because the
                        number is uninterpretable without the instrument's sensitivity. That is
                        exactly the `standing` + `window` pair proposed below.
what does not           Metrology's censoring is quantitative (the value exists, bounded below).
                        Ours is usually categorical (no observation at all), which is nearer
                        Rubin's missing-data framing than censoring. Do not import "censored" as
                        the word; it promises a bound we do not have.
novelty risk            SEVERE as a principle. LOW as an enforced runtime state on an
                        organizational object — I found nothing that does that.
```

---

## Evidence

```text
ESTABLISHED
```

| Claim | Support |
|---|---|
| `Verdict` has exactly four members: PASS, FAIL, UNMEASURABLE, NOT_RUN | `factory/contract.py:17-21`, re-read at a090f6f `OBSERVED` |
| `REFUSED` is a fifth verdict-shaped value defined outside the enum, service-side | `evaluator_service/service.py:62` (`REFUSED = "REFUSED"`), `factory/evaluator.py:65` (`UNSCORED_VERDICTS = frozenset({"REFUSED", "UNMEASURABLE", "NOT_RUN"})`) `OBSERVED` |
| `contract` resolves to `GreenContract` across 7 non-test modules | `evaluator_service/service.py`, `factory/certify.py`, `connector_contract.py`, `demo.py`, `evals.py`, `live_probes.py`, `pbi_contract.py` — enumerated by grep, not sampled `OBSERVED` |
| `TeamSpec.contract` binds the word to the certification object | `factory/blueprint.py:47` — `contract: str = ""  # name of the GreenContract that certifies it` `OBSERVED` |
| `claims.Claim` is a `(lane, since, who, note)` lease with no truth value | `factory/claims.py:69-72` `OBSERVED` |
| `lane` is self-documented as the most overloaded word in the repo | `factory/claims.py:53-57` — *"R14 measured that `lane` is already four objects wearing one string — work package, file-conflict key, git branch, directory, claim key, ledger key"* (says four, lists six) `OBSERVED` |
| `ContextRef` at `context.py:71`, `ContextPack` at `context.py:121` | re-read; line numbers exact `OBSERVED` |
| `context.py` carries THREE separate closed vocabularies: KINDS(:47), STATUSES(:54), CONFIDENCE(:63) | `OBSERVED` |
| `CONFIDENCE` has four values including `STATED`; `tasks.py` basis has three | `context.py:63` vs `tasks.py:136-137` `OBSERVED` |
| `NOT_IDENTITY` is a two-element deny-list | `factory/blueprint.py:39` `OBSERVED` |
| `findings.KINDS` / `findings.STATUSES` are validated closed sets | `factory/findings.py:40,43` `OBSERVED` |
| The task-store event kinds are the one closed set with no constant and no validation | `factory/tasks.py:81-84` dispatches `if kind == "create"` with no tuple; unknown kinds fall through `OBSERVED` |
| `VERDICT_MARK` exists — colour is never the only carrier | `factory/flow.py:41`, used at `:150` `OBSERVED` |
| `must_be_blank_not_zero` is an enforced target field | `factory/pbi_contract.py:88`, checked at `:322-330` `OBSERVED` |
| "instrument" appears in prose in 15 factory modules, as a type in none | `grep -rc instrument --include=*.py factory evaluator_service` `OBSERVED` |
| "mandate" appears zero times in `factory/`, `evaluator_service/`, `tests/` | `OBSERVED` — the coinage is free |
| TTCN-3 defines five verdicts with `error` = test-device fault, in a dominance lattice | Grabowski et al., *An Introduction to TTCN-3* (2003) and the TTCN-3 User Conference tutorial `SECONDARY` — see NOT-SUPPLIED |
| Grafana Alerting separates NoData (query ran, no points) from Error (query failed) from OK | grafana.com/docs — *No Data and Error states* `SECONDARY` (doc summary, not fetched in full) |
| Non-detection is not zero concentration; the threshold is a censoring limit | ITRC / EPA / ASTM guidance `SECONDARY` |

```text
EMERGING
```

| Claim | Support |
|---|---|
| Organizational configuration is model-binding-dependent and must be re-validated per binding | IMACS, arXiv:2607.25446, quoted verbatim in `W0-citation-verification-partial.md:148-151`, itself CONFIRMED by direct fetch by the orchestrating session. I did **not** re-fetch. `SECONDARY-ON-VERIFIED` |
| The estate's strongest asset is epistemic, not organizational | R00 Finding 2, R01 Finding 7 — two lanes agreeing, which per the brief is not evidence. But they agree with the code, which is. `DERIVED` |

```text
EXPERIMENTAL
```

- That thirteen terms is the right number. There is no experiment behind it; the number fell out of
  applying the four rejection tests to 37 candidates. Its falsification is cheap and named in
  §Experiments required.

```text
SPECULATIVE
```

- That `Mandate` can be enforced at a tool boundary in this harness. Zero code, zero test.
- That naming the concept once actually stops a tenth vocabulary appearing. Testable, §Experiments.

```text
METAPHORICAL ONLY
```

- Every Army label in §Deliverable 6, by construction. That is what the section is for.
- `Signal`, `Field`, `Cell`, `Squad`, `Command World`, `Organizational Cortex`. Deleted, not
  deferred — I agree with R00 §Prior art 10 and R01's SERIOUS collision rating, and add one reason
  neither gives: **all four fail rejection test (d)** — they cannot be mapped to state or behaviour
  in any repository I can read. Zero occurrences of any of them in `factory/`.

---

## Findings

### Finding 1 — The verdict vocabulary is thirty-five-year-old prior art, and R01's novelty claim needs narrowing

**Mechanism.** `W0-citation-verification-partial.md:202-204` records, as the last item under "Still
outstanding": *"The search R01 says it did not run: `UNMEASURABLE` as a first-class verdict in the
metrology and software-testing literatures. R01's narrowest-defensible-novelty claim rests entirely
on that gap, so the one surviving novelty claim is the least verified thing in Wave 0."*

I ran it. It does not survive as stated.

**Evidence.** TTCN-3 — the Testing and Test Control Notation, standardised as ETSI ES 201 873-1 and
ITU-T Z.161, in continuous use for protocol conformance testing since 2000 — defines five
predefined verdict values of type `verdicttype`:

| TTCN-3 | Meaning (as given in the tutorial literature) | agent-factory counterpart |
|---|---|---|
| `none` | the initial value; no verdict has been assigned yet | `NOT_RUN` (`contract.py:21`) |
| `pass` | the SUT behaves according to the test purpose | `PASS` |
| `inconc` | *"neither a pass nor a fail can be assigned"* | no exact counterpart — see below |
| `fail` | the SUT violates its specification | `FAIL` |
| `error` | *"an error in the test devices"*, set automatically by the runtime | `UNMEASURABLE` (`contract.py:20` — *"instrument could not run"*) and, partly, `REFUSED` |

And the verdicts form a dominance lattice — `none < pass < inconc < fail < error` — with the rule
that a verdict may only ever get worse. `factory/contract.py:73-85` independently re-derived the
same ordering for the three values they share: any `FAIL` wins over any `UNMEASURABLE`, which wins
over `PASS`, and an empty set is `NOT_RUN`.

Independently, the same shape exists in modern monitoring: Grafana Alerting distinguishes **NoData**
("the alert rule query runs successfully but returns no data points") from **Error** ("the alert
rule fails to evaluate its query") from **OK**, and *"NoData (default) triggers a new
DatasourceNoData alert, treating No data as a specific problem"* rather than as health. And in
metrology the discipline is older still: a non-detect is reported *with* its detection limit,
because "non-detection is different from zero concentration".

**Counterevidence — and it is what saves the claim in narrowed form.** None of the three prior arts
carries the other two axes. TTCN-3 has no `basis` (there is no "this pass was ASSUMED"), no evidence
class, no coverage state, and no store that refuses a close. Grafana has no notion of a proof that
the instrument can fire. Metrology has the sensitivity discipline but no verdict object. And **none
of them has the negative control as an enforced property** — `tests/test_readiness_probes_can_pass.py::test_every_gate_can_refuse`
and `tests/test_connector_contract.py::test_every_assertion_has_been_proved_able_to_fail` require
every gate and every assertion to have been *observed refusing*. TTCN-3 has no equivalent
requirement on a test case.

**Agent Army implication.** Two, and the second is the important one.

1. **Narrow the novelty claim.** R01's narrowest defensible claim (`R01:105-111`) should be rewritten
   from *"`UNMEASURABLE` is a first-class outcome that cannot be collapsed"* — which is ISO/IEC 9646
   (1991) — to: **the composition of a non-collapsible verdict with a per-row basis, a four-class
   evidence coverage state, and a store that refuses to close without a MEASURED or DERIVED row.**
   Each element has prior art; I found nothing that composes them, and the composition is what
   `tasks.py:150-171` actually enforces.
2. **Steal the lattice.** TTCN-3 answers a question the estate has left open — where `REFUSED` sits.
   See Finding 2.

**Conflict reported per §7 of the brief:** this contradicts R01 Finding 7 and R01's closing claim.
R01 stated honestly that it had not searched these literatures; it did not overclaim, it
under-searched. The correction is to the claim, not to R01's integrity.

---

### Finding 2 — `REFUSED` is a distinction worth keeping and a bug in where it lives

The brief asks whether the four-in-enum / five-in-use split is a bug to name or a distinction to
keep. It is both, and separating the two halves is the whole answer.

**The distinction is real, and has independent prior art.** `evaluator_service/service.py:19-21`:
*"REFUSED — the submitted sha256 does not match the bytes on disk. … Not a FAIL — we never scored
anything."* That is exactly TTCN-3's reason for splitting `error` from `inconc`: a fault in the
test apparatus is a different claim from an inconclusive observation of the subject. Collapsing
`REFUSED` into `UNMEASURABLE` would lose *whose fault it was*, which is the difference between "our
grader is broken" and "your artefact did not arrive intact". **Keep it.**

**The bug is that it cannot reach the aggregator.** `REFUSED` is not a member of `Verdict`
(`contract.py:17-21`, re-read), so:

- `ContractResult.verdict` (`contract.py:73-85`) — the function that folds many assertions into one
  answer — **structurally cannot produce or consume it.** Its rule enumerates FAIL, UNMEASURABLE,
  empty and PASS. A refusal reaching that fold today would have to have been converted into
  something else first.
- Meanwhile `factory/evaluator.py:65` puts `REFUSED` in `UNSCORED_VERDICTS` alongside `UNMEASURABLE`
  and `NOT_RUN` — i.e. the client treats it as a verdict.
- So the value crosses a process boundary as a verdict and re-enters a codebase whose verdict type
  cannot represent it.

**The consequence, stated as a failure the estate has already paid for once elsewhere.** This is
the same shape as `Unmeasurable` being defined three times (`contract.py:63`, `readiness.py:42`,
`schedule.py:54` — the crawl's finding, which I re-checked and confirm): a concept that exists in
several places under several types cannot be reasoned about by any one of them. The specific risk
here is that the first code path that has to aggregate a REFUSED alongside a FAIL will pick an
ordering *locally*, and nothing will notice.

**Recommendation.** Five verdicts in one enum, with the lattice decided deliberately and cited:

```text
NOT_RUN  <  PASS  <  UNMEASURABLE  <  FAIL  <  REFUSED
```

— which is TTCN-3's ordering with its names swapped for ours. Note this puts `REFUSED` **above**
`FAIL`, on TTCN-3's reasoning that an apparatus fault invalidates the run more completely than a
subject failure does. I am recommending it rather than deciding it: it is a design choice, the
estate has never had to make it, and I am flagging it in §Open questions as Q2 rather than
pretending the citation settles it.

---

### Finding 3 — `IntentContract` is unresolvable, and merging it into `GreenContract` is also wrong

**Mechanism.** Two live bindings, not one:

- `contract` resolves to `GreenContract` in every one of the 7 non-test modules that import
  `factory.contract` (enumerated, not sampled).
- `TeamSpec.contract` (`blueprint.py:47`) is a *field* whose declared meaning is *"name of the
  GreenContract that certifies it"*. A field named `contract` on the top-level configuration object
  is a much harder binding than an import, because it appears in every serialized blueprint YAML.

So a reader encountering `contract:` in a blueprint file has no way to tell which of two objects is
meant, and the existing answer — always the certification object — is currently unambiguous. **An
`IntentContract` would destroy an unambiguous binding to gain a name.** That fails rejection test
(a): two teams will plausibly use it differently, and here the two "teams" are the research repo and
the running code.

**Where I disagree with R00.** R00 §Data-model implications and §Deliverable 6 both say: *"One
contract object, not two … an Intent Contract is a GreenContract stated before execution, with
authority and escalation as additional assertion kinds."* I think the last eight words are the
error, and it is a mechanism error, not a naming one:

> A `GreenContract` is *"a named set of assertions"* (`contract.py:104`), and an `Assertion` is
> *"One falsifiable claim"* (`contract.py:42`). Every member of the set must evaluate to one of the
> verdicts. **"This agent may spend $5" is not falsifiable.** It is a permission. You cannot ask a
> probe whether a permission is PASS or FAIL; you can only ask whether it was *violated*, which is
> a different question with a different subject and a different time of evaluation (continuously,
> at the boundary, versus once, at the end).

Adding permissions as "assertion kinds" would mean `GreenContract` no longer has the property that
made it the root object: that every member is falsifiable and the fold over them is meaningful. The
aggregation rule at `contract.py:73-85` would be folding two different kinds of thing.

**My resolution — a third option neither the draft nor R00 offers.** Three objects, cleanly split
by *what kind of thing they are*:

| Object | What it holds | When evaluated | Falsifiable? |
|---|---|---|---|
| `Contract` (= `GreenContract`, unchanged) | what "done" means | once, at the end | yes — that is its defining property |
| `Mandate` (new) | what this agent may do, up to what budget, and what it must escalate | continuously, at the boundary | no — it is violated or not, which is a different predicate |
| `Task` (= `tasks.Task`, unchanged) | the objective in prose, and its evidence | throughout | n/a |

The draft's `IntentContract` (`00-core-ontology.md:89`) lists five things: *mission objective, end
state, invariants, authority and escalation boundaries.* Under this split: **objective** and **end
state** are `Task.title` and the `Contract` respectively; **invariants** are assertions on the
`Contract`; **authority** and **escalation** are the `Mandate`. Nothing is lost and no object holds
two kinds of predicate.

**Why `Mandate` and not something else.** It is free — zero occurrences in `factory/`,
`evaluator_service/` or `tests/`, checked. It does not share a head noun with `contract`. It avoids
`policy` (which R01 rates as colliding with Ponder/Rei/XACML/OPA, and which fails rejection test (a)
on its own — the draft defines Policy as "Operational rule", which two teams will certainly use
differently) and `doctrine` (BLOCKING collision with the PHP ORM, per R01 §Deliverable 3, which
means every code search for `doctrine` in a software repo returns PHP). And it does not create false
novelty: a Mandate is a narrowing of Moise's **deontic specification** (obligations and permissions
bound to a role), and the ontology entry says so.

⛔ **The hard gate on `Mandate`, stated so it cannot be quietly dropped.** Per R00's N3 and per
`blueprint.py:50` (`prohibition` is a prose string carried into a prompt), **a Mandate that is only
prose is not a Mandate.** If, after investigation, nothing in this harness can enforce authority at
a tool boundary, `Mandate` must be demoted to RESEARCH ONLY and `prohibition` must keep its honest
name. I am classifying it NEXT, not NOW, for exactly this reason.

---

### Finding 4 — `Claim` should be deleted from the ontology, not renamed — and here I disagree with R00

**Mechanism.** R00 §Deliverable 4 keeps `Claim` as fundamental object #5, with lifecycle *"asserted
→ supported / contradicted / stale"*. I think that is a mistake, and the mistake is visible in a
count.

`claim` / `claimed` already carries **four live senses in one codebase**, all re-verified:

| Sense | Where | What it is |
|---|---|---|
| a filesystem mutual-exclusion **lease** | `claims.py:69-72` — `Claim(lane, since, who, note)` | no truth value, no evidence, no derivation |
| a **task status** | `tasks.py:26` — `OPEN, CLAIMED, BLOCKED, DONE, ABANDONED` | "this task has an owner" |
| a **bus message kind** | `bus.py:50` — `claimed` | *"I am touching this file/area"* |
| the prose sense the research means | `contract.py:42` — *"One falsifiable claim"* | the class is named `Assertion` |

Note the fourth row: **the codebase already uses the research word in prose and deliberately named
the class something else.** That is not an accident to be corrected; it is a naming decision that
has already been made, correctly, by someone who had to live with the other three senses.

Now apply the brief's rejection tests to `Claim`:

- **(a) two teams will plausibly use it differently** — they already do, four ways, inside one
  repository. This is not a hypothetical risk; it is a measured fact.
- **(c) another canonical term already covers it** — `Assertion` does, and it is a real dataclass
  with a real test suite.

Two of four rejection tests fail on measured evidence. The term goes.

**The specific hazard, made concrete.** `01-relationship-map.md:35-39` gives `Claim` four edges:
`supported by → Evidence`, `contradicted by → Evidence`, `derived from → Claim`, `used by →
Decision`. Not one of those four edges is meaningful for a lane lease. If a schema is ever generated
from that map, `claim` is the identifier it will produce, and it will collide with a live,
race-tested (`tests/test_claim_race.py`), filesystem-backed store — and `claims.py:52-57` records
that the estate has *already* refused a change of exactly this shape once, declining to register
"synthesis" as a lane because it *"would have added a fifth meaning to the most overloaded word in
this codebase to save a dozen lines."* The same reasoning applies here and points the same way.

**Where I go further than the crawl.** The crawl (Part 3 §2) says the research `Claim` "maps to"
`Assertion` and that the mapping "must be stated". I say stating the mapping is not enough: a
mapping documented in one file is a footnote, and the word will be used anyway. **Delete the term.**
`Assertion` is the canonical name; `Claim` appears in §Deliverable 7 (deprecated) with a one-line
"use `Assertion`" and nothing else.

**Secondary recommendation, low priority, for agent-factory not this repo:** `claims.Claim` would be
more honestly named `Lease`, and the module `leases.py`. It is a mutual-exclusion lease with a
staleness warning, which is a completely standard distributed-systems object with a completely
standard name. I am *not* recommending this be done now — it touches a race-tested store for a
naming gain — but it should be recorded as the correct end state, because the estate has already
paid twice for `lane`'s overloading and this is the same disease one word over.

---

### Finding 5 — Adopt `ContextPack`, and the strongest reason is not the one the crawl gives

The crawl's recommendation (§Part 5) is: adopt `ContextPack`/`ContextRef` rather than invent
`ContextPackage`, because it is built, tested, carries a mandatory `source`, a freshness state and a
confidence, and renaming breaks `lanes.py:100-112`. I checked each of those and they hold —
`ContextRef` is at `context.py:71`, `ContextPack` at `:121`, and the module carries three separate
validated closed vocabularies at `:47`, `:54` and `:63`.

**But the decisive reason is a different one, and it is the reason this pass exists.**
`factory/context.py` is the only module in the codebase that has **already separated two of the
three axes** that the other eight vocabularies collapse:

> *"A ref can be perfectly current and still be somebody's guess; a ref can be a hard measurement
> taken a year ago."* (`context.py:56-58`)

`STATUSES` (`CURRENT / STALE / UNVERIFIED`) is a *window* axis. `CONFIDENCE` (`MEASURED / DERIVED /
STATED / ASSUMED`) is a *basis* axis. They are declared orthogonal and validated separately. Every
other one of the nine vocabularies mixes at least two axes into one three-value ladder.

So `ContextPack` is not merely "the built one". **It is the only existing object in the codebase
whose shape is already correct under the ontology I am proposing**, and adopting it verbatim means
the ontology has one worked example rather than zero. That is worth more than the name.

One consequence follows immediately, and it is the answer to a question the crawl raised and left
open (*"These two four/three-value ladders are similar but not identical, and are not reconciled
anywhere in the code"*): **`context.CONFIDENCE` is the right ladder and `tasks.py`'s three-value
basis is the truncated one.** `STATED` — *"a human said so; true by assertion, not by measurement"*
— is a real and distinct epistemic position, and it is exactly the one that `evidence.ASSERTED`
exists to catch. Recommending four everywhere is `DERIVED`, and I flag it as Q3 rather than
asserting it, because widening a validated enum has a migration cost I have not measured.

---

### Finding 6 — Structural versus configurational is the cut the ontology is missing

**Mechanism.** IMACS (arXiv:2607.25446, verified by the orchestrating session and quoted in
`W0:148-151`) reports that *"the winning placement flips across model families, so organizational
design cannot be hard-coded; it must be revalidated, or learned, for each model binding."*

A flat ontology treats every term as equally durable. If that finding is right, they are not. Some
terms describe things that are true regardless of which model is behind the agents — an artefact has
a hash, a verdict is one of five, evidence has a basis. Others describe things whose *correct value*
changes when the model changes — how many agents, which topology, who reviews whom, how much context
each gets. Putting both kinds in one list invites the second kind to be written down once and then
treated as settled, which is precisely the failure IMACS names.

**Evidence.** Beyond IMACS: `readiness.py:1206` `VERSION_DIMENSIONS` lists fifteen dimensions of
agent identity — `prompt, model, effort, tools, max_turns, budget_usd, tool_implementation,
sandbox_image, model_routing, context_policy, external_knowledge, permissions, contract_version,
harness_version, side_effect_replay` — with the gloss *"An agent is not a name; it is everything
here, and anything absent is something a certification silently transfers across."* Note that
`model` is in that list. **The codebase already treats the model binding as part of identity.** What
it does not yet do is say which *terms* are downstream of that binding.

`SUPPORTED_TOPOLOGIES = {"manager_to_agent"}` (`blueprint.py:79`, enforced at `:86-89`) is the same
instinct expressed defensively: one topology, *"until a second team demonstrably needs another"*.

**Counterevidence.** IMACS is one paper, and its result is about placement of accountability under
specific protocols, not about every configurational term. I am generalising from one study to a
whole tier of the ontology, and that is `DERIVED`. The mitigation is that the cut is cheap to
reverse: if configuration turns out to be binding-stable, the two tiers merge and nothing was lost
but a column.

**Agent Army implication — three concrete consequences.**

1. **Nine structural terms, four configurational.** Listed in §Deliverable 1. The configurational
   ones carry a mandatory `binding` field, and a certification against one binding does not transfer
   to another. `blueprint.py:31-33` already computes an identity hash that includes `model`; this
   makes the reason explicit rather than incidental.
2. **`Role` dies here, on a cleaner mechanism than R00's.** R00 cut `Role` (its Finding 6) partly on
   Dochkina, whose effect sizes R00 itself calls not credible (*"a reported Cohen's d of 22.9 that
   is not a credible effect size"*). That is a weak leg. The stronger argument needs no Dochkina: a
   role is a *configurational* term, so it cannot have a stable ontological identity across
   bindings; and in the code it is a free-text string on `AgentSpec` with no template, registry or
   validation. It fails rejection test (d) — it maps to no state anything reads. **Same verdict as
   R00, load-bearing on a fact rather than on a study R00 distrusts.**
3. **`Topology` is a field with a binding, never a term.** The draft never lists it, but the vision
   document's whole "organizational compiler" framing presumes it is one. It is not.

---

### Finding 7 — Reported per the brief's conflict rule: three places where the drafts and the code disagree, and the code wins

The brief asks for these explicitly. All three re-verified at HEAD a090f6f.

**7a. `Evidence` — the draft's definition is a strict weakening.** `00-core-ontology.md:77` says
*"An observation or artifact that supports or contradicts a claim."* The code requires a validated
`basis` at write time (`tasks.py:136-137`, raises `ValueError`), an optional-but-validated
`evidence_class` (`tasks.py:139-140`), folds rows into a three-state per-class coverage
(`evidence.py:68-70`), and refuses a close that does not satisfy the named classes
(`tasks.py:163-171`, raising `EvidenceRequired`). **The hazard is dilution, not collision:** adopt
the draft's sentence as the canonical definition and the four-class gate reads as an implementation
detail rather than as part of what the word means. My canonical entry uses the code's meaning and
says so in the definition line, not in a footnote.

**7b. `Team` — the code itself disagrees with the code.** Two objects wear the word:
`TeamSpec` (`blueprint.py:43`, a versioned configuration with a `version` hash and a `contract`) and
`roadmap.TEAMS` (`roadmap.py:181`, an authored dict with `intent` / `gates` / `blocked_on`). These
are not two views of one thing — nothing executes a `TeamSpec` (`runs.py` records that attribution
is entirely `NOT-RECORDED`), so the first is a config that has never run and the second is a goal
somebody wrote down. **My resolution:** `Team` is not a canonical term at all. It is a field on
`Configuration`. The `roadmap.TEAMS` sense is an *objective*, and the correct fix is in
agent-factory (rename the dict), not here. Until that happens, the word must always be qualified in
prose: "a TeamSpec" or "a roadmap objective", never bare "team".

**7c. `Readiness` — same name, different subject.** The draft has no `Readiness` entry but the
candidate list does, and `vision/01:42` lists it. `factory/readiness.py:1` answers *"can an agent
team run a connector migration unattended?"* — a property of **the whole estate**. The research
sense is a property of a unit or a capability. Two subjects, one word: rejection test (a). Compounded
by R01's note that `readiness` is a defined term of art in TRL, CMMI, DRRS/SORTS and Kubernetes
`readinessProbe`. **Delete the term.** What the estate actually has is a `Contract` (a named set of
assertions) whose assertions happen to be called gates. Which produces a free result — see below.

**A result that falls out of 7c, and it is worth more than the deletion.** `readiness.GATES` (30
gates, `readiness.py:1394`) and `plan_gates.PLAN_GATES` (`plan_gates.py:235`) carry a shouted comment
that they *"must never be summed"* with each other (`plan_gates.py:13-18`, recording that the
conflation *"has already been made once in this estate and had to be corrected"*). Under the
ontology proposed here, that rule is not a comment. **They are two `Contract`s over two different
subjects, and summing assertions across two contracts is meaningless by construction** — the same
reason you cannot average two `ContractResult`s. The comment can stay, but the property is now
structural.

---

## Deliverable 1 — Minimal canonical ontology

**13 canonical terms from 37 candidates.** Nine structural, four configurational. Everything else is
derived (§below), deprecated (§Deliverable 7) or deleted.

The brief's 15-field schema, for every one. Fields exactly as specified in
`foundations/R02:98-112`.

---

### STRUCTURAL — stable across model bindings

---

#### 1. `Instrument` ⭐

**This is the term the estate has been missing.** The refusal to report a zero from an instrument
not shown able to see a non-zero appears nine times under nine vocabularies; this is its one name.

```text
Canonical name        Instrument
Definition            A named procedure that produces a value about the world, together with the
                      window it covers and the demonstration that it could have produced a
                      different value. An Instrument that has not been observed producing a
                      different value has no standing, and an absence it reports is not a zero.
Why it exists         Because nine modules independently invented a value meaning "we could not
                      see", each with a different name, and no module can talk about another's.
                      Naming it once is the difference between nine conventions and one rule.
                      The word is the estate's own: "instrument" appears in prose in 15 factory
                      modules and is a Finding.KIND (findings.py:40); it has never been a type.
Aliases               probe (factory/connector_contract.py:61, pbi_contract.py:101 — the class
                      that IS an instrument today); sensor (Army label only, §Deliverable 6);
                      "the referee" (evidence.py:33)
Deprecated synonyms   Observation (it is the OUTPUT of an Instrument, not the Instrument);
                      Simulation (a Corpus is the world an Instrument scores against);
                      Signal, Field (deleted entirely, §Deliverable 7)
Not the same as       - Evidence: Evidence is what an Instrument produced. An Instrument with no
                        readings is still an Instrument; a reading with no Instrument is a rumour.
                      - Assertion: an Assertion is the question; an Instrument is what answers it.
                        readiness.Gate has both (`question` and `probe`, readiness.py:50) and
                        conflating them is why "gate" is ambiguous.
                      - Contract: a Contract names a set of Assertions; the Instruments are how
                        they get answered.
Identity              (name, bundle_sha256) — the name plus a hash over the files that decide what
                      it measures. Precedent in code: evaluator_service/service.py:57 BUNDLE +
                      bundle_sha256() at :77. Two readings from differently-hashed builds of the
                      same-named instrument may never be compared as though they agreed.
Lifecycle             declared -> proven (observed producing a different value) -> live (ran in
                      this window) -> dark (did not / could not run) -> retired.
                      ⛔ declared -> live is FORBIDDEN. An instrument goes live only through
                      proven. This edge is the whole term.
Relationships         answers -> Assertion (0..n)
                      produces -> Evidence (0..n)
                      scores against -> Artifact (0..1)   [the corpus; absent = a live run]
                      declared by -> Configuration
Persistence           The declaration is source-controlled with the code. The standing is NOT
                      persisted — it is computed per window, per run, and a persisted standing is
                      a staleness bug by construction (this is exactly claims.py:83-87's lesson:
                      "Age is a clock reading; liveness is a measurement").
Runtime owner         The evaluator process, never the agent being measured. corpus.py:9 — "An
                      agent that can edit its own grader is not graded."
User-facing label     "check" in ordinary UI; "sensor" only in Army-themed chrome.
                      Its STANDING is what users must see, and it is never a colour alone
                      (flow.py:41 VERDICT_MARK is the pattern).
API/schema identifier instrument ; fields: name, bundle_sha256, standing, window, cause
                      standing enum: LIVE | DARK | UNPROVEN
                      cause enum (only when standing != LIVE):
                        NO_INSTRUMENT | EMPTY_WINDOW | INSTRUMENT_BLIND | NOT_RECORDED |
                        NEVER_PROVEN
Example               factory/connector_contract.py:61 `Probes` — the base class refuses
                      everything, "which is the correct default: an unconfigured harness reports
                      UNMEASURABLE, never PASS" (:65-67). That is standing=DARK with
                      cause=NO_INSTRUMENT, correctly rendered.
Counterexample        factory/pbi_contract.py, which roadmap.py:190-194 records as having zero
                      tests and zero callers: "A contract never watched refusing is decoration."
                      Twelve assertions, no proof any can fail => every instrument behind them is
                      standing=UNPROVEN, and a GREEN from it means nothing. This is the term
                      earning its place: without it, pbi_contract and connector_contract look
                      alike.
```

**The three axes, and why nine vocabularies exist.** The nine are not nine names for one thing. Each
collapses a different subset of three orthogonal axes into one flat ladder:

| Axis | Question | Canonical values | Where the code already has it right |
|---|---|---|---|
| **standing** | did the instrument see? | `LIVE / DARK / UNPROVEN` | `sessions.py:130` `UNKNOWN-INSTRUMENT-BLIND` — literally this axis, named |
| **basis** | how strongly do we believe the value? | `MEASURED / DERIVED / STATED / ASSUMED` | `context.py:63` `CONFIDENCE` — the four-value version |
| **window** | over what period? | a date range, or `NOT-SET` | `readiness.py:100` `MEASURED_SINCE`; `context.py` `checked` date required when `CURRENT` |

`context.py` is the only module that separated two of the three (`STATUSES` = window,
`CONFIDENCE` = basis) and says so at `:56-58`. Everything else mixes.

**The nine mapped.** Every row re-checked against the source file.

| # | Where | Its vocabulary | standing | basis | window | Zero it refuses |
|---|---|---|---|---|---|---|
| 1 | `runs.py:42` | RECORDED / RECONSTRUCTED / NOT-RECORDED | LIVE / LIVE / **DARK**(NOT_RECORDED) | MEASURED / DERIVED / — | implicit | "0 runs" for an unrecorded past |
| 2 | `evidence.py:68-70` | SATISFIED / ASSERTED / ABSENT | LIVE / LIVE / **DARK**(NEVER_PROVEN) | MEASURED+DERIVED / ASSUMED / — | — | "no evidence" for an assumed claim |
| 3 | `context.py:51-53` | CURRENT / STALE / UNVERIFIED | LIVE / LIVE / **DARK** | (separate axis) | **this IS the window axis** | "fresh" for never-checked |
| 4 | `claims.py:96-98` | HELD-LIVE / HELD-GONE / HELD-UNVERIFIED | LIVE / LIVE / **DARK**(INSTRUMENT_BLIND) | MEASURED | now | "free" for an unreadable process table |
| 5 | `sessions.py:121-134` | RUNNING-ATTACHED … UNKNOWN-INSTRUMENT-BLIND / NO-SESSION | 4 LIVE + **DARK**(INSTRUMENT_BLIND) + LIVE(NO_SESSION) | MEASURED | now | "nothing running" for a blind instrument |
| 6 | `goals.py:75` | MEASURED / NOT-MEASURED | LIVE / **DARK** | — | — | "0%" for an unmeasured goal |
| 7 | `launch.py:62`, `teamplan.py:36` | UNGATED | **DARK**(NO_INSTRUMENT) | — | — | "0%" for a team with no contract |
| 8 | `deploy.py:33-35` | hit / none / undetermined | LIVE / LIVE / **DARK** | — | per attempt | "not a cap" from an absence of signal |
| 9 | `readiness.py:96-97` | empty window -> UNMEASURABLE | **DARK**(EMPTY_WINDOW) | — | `MEASURED_SINCE` (:100) | "controls work" for "nothing has run" |

**Read the table across, not down.** Six of the nine have a `standing` axis and nothing else. Two
have standing + basis. One (`context.py`) has all three, separated. **No two of the nine cover the
same subset** — which is the mechanistic reason they were never unified: each module invented
exactly the ladder its own problem needed, and there was no vocabulary in which to notice they were
the same problem.

**The two named rules.** These are the deliverable the brief asked for, and they are rules, not
objects:

> **The Live-Instrument Rule.** An absence may be reported as a zero only from an Instrument whose
> standing is `LIVE` for the window the zero covers. From `DARK` or `UNPROVEN`, the honest report is
> `UNMEASURABLE` with the `cause`.

> **A Blind Zero** is the violation: a zero, a "none", a "never", a "0%" or a blank published from
> an Instrument that was `DARK` or `UNPROVEN`. It is the defect this whole vocabulary exists to
> prevent, and it now has a name that fits in a code review comment.

Prior art, cited so the rules do not read as inventions: metrology's non-detect ("non-detection is
different from zero concentration"); Altman & Bland, BMJ 1995 ("absence of evidence is not evidence
of absence"); Grafana's NoData-is-not-OK; ISO/IEC 9646's `inconclusive`. §Prior art.

⛔ **What I am NOT recommending.** Do not refactor the nine into one enum. Every one of them is
validated, several are tested (`test_evidence_classes.py`, `test_claim_race.py`,
`test_readiness_probes_can_pass.py`), and a rename buys no behaviour. The purpose of naming the
concept is so that the **tenth** module does not invent a tenth vocabulary, and so that a reviewer
has a word. §Recommendation classifies this as a documentation change with blast radius zero.

---

#### 2. `Verdict`

```text
Canonical name        Verdict
Definition            The outcome of evaluating one Assertion, or the fold of many. Five values,
                      never collapsed, ordered by dominance.
Why it exists         contract.py:6-8 states it: "The distinction between FAIL and UNMEASURABLE is
                      the entire reason this file exists: a check whose instrument could not run
                      has not passed, and reporting it as a pass is how a measurement gap becomes
                      a claim about the system."
Aliases               result, outcome (both DEPRECATED as identifiers — see Not-the-same-as)
Deprecated synonyms   Outcome (two live senses already: metrics.py:21 activity/outcome, and
                      runs.py:41 FINISHED/REFUSED/ABANDONED. Never use bare "outcome".)
Not the same as       - runs.outcome, which is a RUN's disposition, not a judgement of correctness.
                      - Metric.kind == "outcome" (metrics.py:21), which is the anchor half of a
                        Goodhart pair.
                      - board.py:29 DONE/READY/BLOCKED, which is derived task status.
Identity              the value itself (an enum member); it has no independent identity
Lifecycle             none. A Verdict is immutable once produced. It may be superseded by a later
                      Verdict from a later run, never edited.
Relationships         produced by -> Instrument
                      attached to -> Assertion (one) or Contract (a fold)
                      attributed to -> evaluator identity + bundle_sha256 (evaluator.py:61)
Persistence           write-once. evaluator_service/store.py:42 VerdictExists enforces this today.
Runtime owner         the evaluator. A verdict that does not say who produced it is refused rather
                      than believed (evaluator.py:24-25).
User-facing label     "result". UNMEASURABLE renders as "couldn't check", never as a failure and
                      never as a warning colour alone.
API/schema identifier verdict — enum: NOT_RUN | PASS | UNMEASURABLE | FAIL | REFUSED
                      ⚠ FIVE. Today four are in the enum (contract.py:17-21) and REFUSED lives at
                      evaluator_service/service.py:62, outside it. See Finding 2.
Example               contract.py:73-85 — "An UNMEASURABLE required assertion yields UNMEASURABLE
                      for the whole contract — not FAIL, because we did not observe a failure, and
                      emphatically not PASS."
Counterexample        A three-value {pass, fail, error} vocabulary. It cannot distinguish "the
                      subject is broken" from "our apparatus is broken" from "nothing ran", and
                      TTCN-3 needed five for the same reason (Finding 1).
```

---

#### 3. `Assertion`

```text
Canonical name        Assertion
Definition            One falsifiable statement about the world, with the Instrument that answers
                      it, evaluating to exactly one Verdict.
Why it exists         Because "Claim" is unusable (Finding 4) and because a question and its
                      answer are different objects. Also because it is already the code's name:
                      contract.py:41.
Aliases               gate (readiness.Gate, readiness.py:50, is an Assertion plus a phase);
                      check; "one falsifiable claim" (contract.py:42, the code's own prose)
Deprecated synonyms   Claim — DELETED from the ontology, four live senses (Finding 4)
                      Observation — that is an Evidence row, not an Assertion
Not the same as       - Mandate: a Mandate is a permission and is not falsifiable. This is the
                        distinction that kills IntentContract (Finding 3).
                      - Finding: a Finding records that a premise WAS wrong; an Assertion asks
                        whether one IS.
Identity              (contract name, assertion name). A1-config-satisfiable within the connector
                      contract; ids are contract-scoped, not global.
Lifecycle             authored -> proven-able-to-fail -> evaluated -> (re-evaluated…)
                      ⛔ authored -> evaluated without proven-able-to-fail produces a Verdict with
                      no standing. tests/test_connector_contract.py::
                      test_every_assertion_has_been_proved_able_to_fail is the enforcement.
Relationships         member of -> Contract (exactly one)
                      answered by -> Instrument (exactly one)
                      yields -> Verdict (one per evaluation)
Persistence           source-controlled, as code. connector_contract.py:299-310 and
                      pbi_contract.py:444-461 are the two live sets (A1-A12, M1-M12).
Runtime owner         the Contract that names it.
User-facing label     "check" — with its question shown, never just its id. readiness.Gate carries
                      `question` and `why` for exactly this reason (readiness.py:50).
API/schema identifier assertion ; fields: name, question, required, instrument, why
Example               connector_contract.py:304 — "A6-run-completed … description='necessary,
                      insufficient — see A7'". An assertion that states its own insufficiency.
Counterexample        "The migration went well." Not falsifiable, no instrument, no verdict. Also:
                      any assertion satisfied by the ABSENCE of an error — connector_contract.py:7-8
                      forbids these explicitly ("Every assertion states a positive fact that must
                      be observed. None is satisfied by the absence of an error.")
```

---

#### 4. `Contract`

```text
Canonical name        Contract     (= GreenContract; the short form is canonical, the code name
                                    stays)
Definition            A named set of Assertions defining what "done" means for one unit of work,
                      folding to exactly one Verdict.
Why it exists         It is the root success object of the running system: "Every team, every
                      optimizer run and every certification reads its verdict from here"
                      (contract.py:3).
Aliases               GreenContract (the class name, unchanged); "the referee" (evidence.py:33)
Deprecated synonyms   IntentContract — REJECTED, highest-risk collision in the set (Finding 3)
                      Verification Contract — do not create a second contract object
                      Readiness — DELETED as a term (Finding 7c); readiness.GATES is a Contract
Not the same as       - Mandate: what is permitted, checked continuously at a boundary. A Contract
                        is what is required, checked once, at the end.
                      - Task: a Task is the work; a Contract is the definition of its completion.
                      ⚠ A Contract carries NO objective, NO authority boundary and NO escalation
                        rule. That absence is deliberate and is the property that makes the fold
                        at contract.py:73-85 meaningful.
Identity              name + a hash over its assertion set. Two contracts with the same name and
                      different assertion sets are different contracts and their verdicts must
                      never be compared.
Lifecycle             authored -> every assertion proven able to fail -> calibrated against a
                      Corpus -> run live -> superseded
Relationships         contains -> Assertion (1..n)
                      certifies -> Configuration (0..1)   [TeamSpec.contract, blueprint.py:47]
                      yields -> Verdict
                      gates -> Task closure
Persistence           source-controlled, as code, versioned with the repo.
Runtime owner         the evaluator process. Not the agent it certifies.
User-facing label     "definition of done". Never "the contract" to a client — R01 §D3 rates
                      "contract" as SERIOUS collision (Contract Net task allocation, 1980).
API/schema identifier contract ; and this identifier is ALREADY TAKEN by this meaning in 7
                      importing modules and in TeamSpec.contract. Nothing else may claim it.
Example               connector_contract.build_contract (:117) with A1-A12.
Counterexample        pbi_contract's M1-M12: a complete, well-argued contract with zero tests and
                      zero callers (roadmap.py:190-194). It is a Contract by shape and decoration
                      by standing — which is exactly what the Instrument term makes visible.
```

---

#### 5. `Evidence`

```text
Canonical name        Evidence
Definition            One recorded observation supporting a Task's closure, carrying a mandatory
                      basis (how it came to be believed) and a class (which of the four questions
                      it answers). An unclassified row counts toward nothing.
Why it exists         Because four artefacts answering ONE question look identical to four
                      answering four (evidence.py:11-13), and because an assumed proof is not a
                      proof (tasks.py:125).
Aliases               proof (loosely); "a row" in prose
Deprecated synonyms   Observation — an Evidence row with basis=MEASURED. No separate term.
                      Experience — deleted (§Deliverable 7)
Not the same as       - Assertion: an Assertion is judged; Evidence is recorded.
                      - Artifact: an Artifact is the thing produced; Evidence is a statement ABOUT
                        an artifact, with a basis.
                      - Finding: Evidence supports one task; a Finding corrects a premise across
                        tasks and merges with the branch.
Identity              (task id, ordinal). Evidence is task-scoped and recorded once.
Lifecycle             recorded -> (never edited). Append, never overwrite (tasks.py:5-7).
Relationships         belongs to -> Task (exactly one)
                      produced by -> Instrument
                      cites -> Artifact (0..1)
                      folds into -> Coverage (a derived per-class state)
Persistence           durable, in the task store, as an append-only event.
Runtime owner         the task store, which REFUSES a close without a MEASURED or DERIVED row
                      (tasks.py:163, EvidenceRequired). The refusal is in the store, not in
                      instructions — this is the pattern R00's N3 says to generalise.
User-facing label     "evidence". Its class and basis are shown, always. ASSERTED must never
                      render like SATISFIED.
API/schema identifier evidence ; fields: task, class, basis, ref, note
                      class enum:  TARGET | CONSUMER | REGRESSION | ROLLBACK  (evidence.py:43-46)
                      basis enum:  MEASURED | DERIVED | STATED | ASSUMED
                                   ⚠ tasks.py:136 accepts three today; adding STATED is Q3.
                      coverage state (derived, not stored): SATISFIED | ASSERTED | ABSENT
Example               evidence.py:20-23 — "Three states, never two. ABSENT means nobody looked.
                      ASSERTED means somebody claimed it without measuring. Only SATISFIED is a
                      pass."
Counterexample        Four screenshots of the same dashboard offered as full coverage. All four
                      are class CONSUMER; TARGET, REGRESSION and ROLLBACK are ABSENT. Tested:
                      test_four_pieces_of_one_class_do_not_satisfy_four_classes.
```

---

#### 6. `Task`

```text
Canonical name        Task
Definition            One unit of work with an id, an owner, a parent, an append-only event
                      history, and evidence that gates its closure.
Why it exists         It is the only object in the estate that can be claimed, blocked, closed and
                      refused, and its history is a fold over events rather than a mutable row.
Aliases               work item; ticket (external); "mission" ONLY when parent is None
Deprecated synonyms   Mission — a Task with parent=None. A LABEL, not an object. (Agreeing with
                        R00 here; the test is `parent is None`, which is state, so it passes
                        rejection test (d) as a label but fails test (c) as a term.)
                      Operation — DELETED. "A runtime execution of a mission" is a Run.
                      Cell, Squad — DELETED, no distinct behaviour or storage.
Not the same as       ⚠ a `board` task (board.py:19) — a DERIVED VIEW of a non-passing gate, with
                        no id, no owner and no store. Two different things wear "task" INSIDE the
                        code. Neither is cheaply renameable. In prose always say "a stored task"
                        or "a board item".
                      - Run: a Task is the work; a Run is one execution episode.
Identity              id (+ parent for the tree). Stable, human-quotable.
Lifecycle             open -> claimed -> [blocked <-> claimed] -> done | abandoned
                      (tasks.py:26; terminal set at :27)
                      ⛔ claimed -> done requires >=1 MEASURED or DERIVED evidence row, enforced
                      by the store (tasks.py:150, :163).
Relationships         parent -> Task (0..1)     [parent=None means it is a mission]
                      owner -> Agent (0..1)
                      has -> Evidence (0..n)
                      gated by -> Contract (0..1)
                      history -> Event (1..n, append-only)   [nested type, not a canonical term]
Persistence           durable. Current state is a fold over events; no field is ever overwritten.
Runtime owner         the task store.
User-facing label     "task"; "mission" for a root task in Army chrome only.
API/schema identifier task ; status enum: open | claimed | blocked | done | abandoned
                      event kinds: create | claim | block | unblock | evidence | close | note
                      ⚠ These event kinds are the ONE closed set in the codebase that is not
                      enforced — tasks.py:81-84 dispatches on `if kind ==` with no constant tuple,
                      and an unknown kind falls through silently (:103). Fix named in
                      §Deliverable 4.
Example               tasks.py:7-8 — "A task cannot close without evidence. status=done with an
                      empty evidence list is rejected by the store, not by convention."
Counterexample        A board item. It is computed from a gate's verdict; claiming one, or
                      attaching evidence to one, is a category error.
```

---

#### 7. `Artifact`

```text
Canonical name        Artifact
Definition            A content-addressable thing produced by work: a URI plus a sha256. If it
                      cannot be hashed, it is not an Artifact.
Why it exists         Because a verdict about an artefact is worthless unless the bytes are pinned
                      — evaluator_service refuses a submission whose sha256 does not match the
                      bytes on disk (service.py:19-21).
Aliases               deliverable; submission (the grading sense, evaluator.py:96-97);
                      corpus (an Artifact used as the reference world, corpus.py)
Deprecated synonyms   Simulation Scenario -> a Corpus, which is an Artifact.
                      Skill Package -> do not model; Agent Skills is an open standard.
Not the same as       - The draft list at 00-core-ontology.md:48-57 includes "ticket" and
                        "deployment". NEITHER is an Artifact — they cannot be hashed. They are
                        TARGETS (an evidence class), which is a different relation entirely. This
                        narrowing resolves the overload the crawl flagged.
                      - Evidence: an Artifact is the object; Evidence is a claim about it.
Identity              sha256. The URI is an address, not an identity — the same bytes at two URIs
                      are one Artifact.
Lifecycle             created (outside the system) -> submitted -> scored -> superseded.
                      The system does not own an Artifact's creation and must not pretend to.
Relationships         produced by -> Task
                      submitted to -> Instrument
                      scored against -> Artifact   [the corpus case; self-referential by design]
                      cited by -> Evidence
Persistence           external. The system persists the hash and the URI, not the bytes.
Runtime owner         whoever produced it. The evaluator owns only the hash it verified.
User-facing label     "output", or the concrete noun ("the report", "the dataset").
API/schema identifier artifact ; fields: artifact_uri, artifact_sha256
                      ⚠ These two identifiers are already taken by this meaning
                      (evaluator.py:55 SUBMISSION_FIELDS). Do not redefine.
Example               corpus.py — "the known-good world every assertion is scored against"
                      (:3), loaded as hash-verified JSON, never as executable Python, so that
                      "the corpus changed" and "the corpus computes something different today"
                      stop being indistinguishable (:6-7).
Counterexample        A Jira ticket. Not hashable, not immutable, not the thing a consumer reads.
                      It is a TARGET.
```

---

#### 8. `Finding`

```text
Canonical name        Finding
Definition            A corrected premise: what was believed, what is actually true, what measured
                      it, and what it affects. Addressable, permanent, and it merges with the
                      branch.
Why it exists         Because knowledge that lives in a chat message is not knowledge. The estate
                      already split the RECORD (docs/findings.d/, in git, permanent) from the
                      CHANNEL (.data/bus/, gitignored, ephemeral) — bus.py:11-16 — after a
                      documented failure that forced it.
Aliases               correction; lesson (Army/AAR label only)
Deprecated synonyms   Knowledge Object — vaguer, and the code's version has a mandatory schema.
                      Lesson, Experience — Finding.KIND is a finer cut (CORRECTION / INSTRUMENT /
                        DESIGN / AGENT-DESIGN / PROCESS, findings.py:40).
                      Doctrine — BLOCKING collision (PHP ORM, per R01 §D3) AND no mechanism
                        (R00 Finding 7: human doctrine is sticky because of a political truce that
                        does not exist here). A "doctrine" is a Mandate that cleared a promotion
                        threshold and carries its model binding. Not a term.
Not the same as       - Evidence: Evidence supports one Task's closure. A Finding corrects a
                        premise across tasks and is permanent.
                      - a bus message: "A message is a nudge, not an archive" (bus.py).
Identity              a declared id. "Matching is by declared id, not by keyword" (findings.py:8).
Lifecycle             OPEN -> ADOPTED | REJECTED | SUPERSEDED  (findings.py:43)
                      ⭐ A DESIGN finding with no status is an insight nobody decided about.
                      "Silence has to mean decided, the same way NOTHING TO REPORT has to mean
                      checked." (findings.py:41-42)
Relationships         measured by -> Instrument
                      affects -> any canonical object (free-text today)
                      supersedes -> Finding (0..1)
Persistence           durable, in git, one file per finding under docs/findings.d/.
Runtime owner         the repository. Findings merge with the branch — that is the point.
User-facing label     "what we got wrong", or "lesson learned" in AAR chrome.
API/schema identifier finding ; required: BELIEVED, ACTUALLY, MEASURED BY, AFFECTS
                      optional: KIND, CHANGES, STATUS
Example               findings.py:35-36 — "INSTRUMENT: a tool lied, or could not see — changes
                      what a measurement is worth". Note this KIND is the Instrument term under
                      another name, already in the code.
Counterexample        A progress note. Nothing was believed and then found false; there is no
                      BELIEVED line to write. findings.nothing_to_report() (:152) exists precisely
                      to count the difference between silence-as-measurement and
                      silence-as-nobody-looked.
```

---

#### 9. `Run`

```text
Canonical name        Run
Definition            One execution episode of an agent or lane, recorded with what happened and
                      how strongly that is known.
Why it exists         "A lane with no record is NOT a lane that did not run" (runs.py:16-18). It
                      is the only object that can carry a NOT-RECORDED past honestly.
Aliases               execution; session (the machine-local sense, sessions.py); attempt
                      (deploy.py, the retry sense)
Deprecated synonyms   Operation — "a runtime execution of a mission" IS this. Do not create a
                        second object for it.
Not the same as       - Task: the Task is the work and survives the Run. Several Runs, one Task.
                      - Evidence: a Run record says work happened; it says nothing about whether
                        the work was right. finish.py:8-10 makes the same cut — it "only knows
                        whether the work is complete", not whether it is correct.
Identity              (lane or agent, started-at). ⚠ Not (task, …) — the ledger is lane-keyed and
                      no join to Task exists today. Stating this rather than papering it.
Lifecycle             started -> FINISHED | REFUSED | ABANDONED   (runs.py:41)
                      outcome may be None for a reconstructed run — deliberately: "Neither can say
                      whether the lane finished — only that work happened" (runs.py:218-220).
Relationships         attributed to -> job, team, team_version, agent_versions  (runs.py:274)
                      ⛔ "Attribution is NEVER reconstructible" (runs.py:241). Today
                      unattributed() reports that ALL of the ledger is unjoinable — "nothing
                      executes a TeamSpec and no Job exists". The term is real; the joins are not.
                      produced by -> Configuration (aspirationally; NOT-RECORDED today)
Persistence           durable ledger, in the primary worktree (repo.py:22-24 — state shared
                      between lanes must resolve to the primary worktree or it is not shared).
Runtime owner         the run ledger.
User-facing label     "run".
API/schema identifier run ; outcome enum: FINISHED | REFUSED | ABANDONED | null
                      basis enum: RECORDED | RECONSTRUCTED | NOT-RECORDED
                      ⚠ Attribution keys record NOT-RECORDED, never omission (runs.py:154-157) —
                      an absent key reads as "this ledger does not ask", an explicit NOT-RECORDED
                      reads as "nobody answered it". This is the Instrument rule applied to a
                      join key, and it is the cleanest instance of it in the codebase.
Example               runs.py:22 — "RECONSTRUCTED: derived after the fact from git + the session
                      transcripts."
Counterexample        A `sessions.py` state. That is a machine-local liveness reading, computed
                      now, never persisted. Persisting one would be the staleness bug
                      claims.py:83-87 already caught once.
```

---

### CONFIGURATIONAL — must carry a model binding, and re-validated when it changes

⚠ Every term below is **downstream of the model binding**. A certification of any of them under one
binding does not transfer to another. `readiness.py:1206` `VERSION_DIMENSIONS` already includes
`model` in agent identity; this tier states the consequence.

---

#### 10. `Configuration`

```text
Canonical name        Configuration
Definition            The pinned set of choices that decide what a run IS: its agents, their
                      topology, their prohibitions, the repo, the contract that certifies it — and
                      the model binding all of that was validated against.
Why it exists         "An agent is not a name — it is a (prompt, model, effort, tools, retry
                      policy) tuple. Change any element and it is a different agent, whose
                      certification does not transfer." (blueprint.py:3-5)
Aliases               TeamSpec (the code's class, blueprint.py:43); blueprint (the YAML)
Deprecated synonyms   OrganizationVersion — same idea, wrong scope. Nothing organization-sized
                        exists to version. Use this name until something does.
                      Organization Definition, Org-IR — Org-IR presupposes a compiler with source
                        semantics (R00 D7). Deleted.
                      Team — ⚠ AMBIGUOUS IN CODE (Finding 7b). TeamSpec is a Configuration;
                        roadmap.TEAMS is an objective. "Team" is a field here, never a term.
Not the same as       - Agent: an Agent is a member of a Configuration.
                      - Contract: a Configuration is certified BY a Contract; it does not contain
                        one, it names one (blueprint.py:47).
Identity              a hash over every field EXCEPT a two-element deny-list (blueprint.py:39,
                      NOT_IDENTITY = ("purpose", "agents")), plus each agent by its own version.
                      ⭐ Deny-list, never allow-list: "a new field is identity by default and must
                      be argued out, because the failure mode of forgetting to add one is a
                      certification that transfers silently" (blueprint.py:36-38).
Lifecycle             authored -> pinned -> certified (against ONE binding) -> superseded
                      ⛔ A binding change demotes a certification to uncertified. This is R00's N4
                      and IMACS's finding, made structural.
Relationships         contains -> Agent (1..n)
                      certified by -> Contract (0..1)   [absent => UNGATED, never 0%]
                      produces -> Run (0..n)
                      binding -> (model family, model version)   ⚠ MANDATORY
Persistence           source-controlled YAML.
Runtime owner         a human. Configurations are authored, not derived — and the estate keeps a
                      REJECTED one on purpose (blueprints/orchestrator_team.yaml:24-30: "It is a
                      hypothesis that was tested and rejected, and the rejection is worth more
                      than the file's absence would be"), with its unlock threshold stated.
User-facing label     "setup" / "team setup".
API/schema identifier configuration ; fields: name, purpose, agents, topology, contract, repo,
                      prohibition, binding
                      topology enum: manager_to_agent   (blueprint.py:79 — one value, enforced at
                      :86-89, "until a second team demonstrably needs another")
Example               blueprint.py:58-61 — a team certified against one repo under "must not
                      deploy to production" kept the IDENTICAL version when repointed at another
                      repo with the prohibition deleted. The deny-list exists because of that.
Counterexample        roadmap.TEAMS. It has intent / gates / blocked_on and no agents, no
                      topology, no version. It is an objective wearing the word "team".
```

---

#### 11. `Agent`

```text
Canonical name        Agent
Definition            A locus of decision with a budget and the ability to refuse, whose identity
                      IS its configuration.
Why it exists         Because "agent" as a name is the thing the estate most needs not to believe
                      in: certifications transfer silently along names and never along configs.
Aliases               AgentSpec (blueprint.py:19); worker; unit (Army label)
Deprecated synonyms   Role — DELETED as an object (Finding 6). Survives ONLY as AgentSpec.role, a
                        free-text string with no template, registry or validation — and as a
                        routing position, which is configurational.
                      Skill — do not model. Agent Skills is an open cross-vendor standard.
Not the same as       - a Run: an Agent is a spec; there is NO running-agent-instance object in
                        the codebase at all. The nearest live thing is a sessions.py session,
                        which is a machine-local process reading. Stating this because the draft's
                        "An executing decision-making worker instance" (00-core-ontology.md:26)
                        names something that does not exist.
Identity              a hash over (prompt, model, effort, tools, max_turns, budget_usd,
                      prohibition, …). 15 dimensions are NAMED at readiness.py:1206; six are
                      hashed today. The gap is a known, stated hole, not a discovery.
Lifecycle             authored -> pinned -> budgeted -> retired.
                      An Agent is not "created at runtime". Nothing spawns one from a spec today
                      (runs.py:277 — "nothing executes a TeamSpec").
Relationships         member of -> Configuration (exactly one)
                      owns -> Task (0..n, one at a time)
                      receives -> ContextPack
                      bounded by -> Mandate (aspirational; prose today)
Persistence           source-controlled, as part of a Configuration.
Runtime owner         a human authors it; the harness runs it.
User-facing label     the agent's name — but the name must never appear without its version in any
                      context where a certification is claimed.
API/schema identifier agent ; fields: name, role, model, effort, prompt, tools, max_turns,
                      budget_usd, prohibition
                      ⚠ `tools` and `tool_implementation` are DIFFERENT dimensions
                      (readiness.py:1206). A flat "Tool" object would lose that distinction, which
                      is why Tool is not a canonical term.
Example               blueprint.py:28 — "prohibition: str = ''  # every agent carries an explicit
                      'must not'".
Counterexample        "the reviewer agent". A name with no config behind it. Two runs under that
                      name on different models are two different agents and their results may not
                      be pooled.
```

---

#### 12. `ContextPack`

```text
Canonical name        ContextPack     (with ContextRef as its member type)
Definition            The ordered set of context refs assembled for ONE task or lane, where every
                      ref names its source, its freshness and its confidence.
Why it exists         "Text that has already been concatenated cannot be filtered per lane, cannot
                      say where it came from, and cannot carry a date." (context.py:5-6)
Aliases               pack; briefing (Army label)
Deprecated synonyms   ContextPackage — DELETE. It is a rename of a built, tested object that would
                        break factory/lanes.py:100-112 and specifies none of the three properties
                        ContextPack already enforces. (Agreeing with the crawl; the decisive
                        reason is in Finding 5 and it is not the crawl's reason.)
                      Knowledge Cache, Cognitive Supply Line — metaphors, no state (test (d)).
Not the same as       - Evidence: Evidence is what came OUT of work; a ContextPack is what went IN.
                      - a prompt: a prompt is a string; a pack is queryable, per-lane filterable
                        and inspectable before it is rendered.
Identity              name + the ordered ref list.
Lifecycle             assembled -> handed to an Agent -> superseded. Not persisted as truth; it is
                      a projection, and "a projection that cannot point back at its origin is a
                      second source of truth" (context.py:96-112).
Relationships         contains -> ContextRef (1..n)
                      handed to -> Agent
                      derives from -> Artifact / wiki page / repo file (via ContextRef.source)
Persistence           assembled per run. The REFS are durable; the pack is not.
Runtime owner         whatever assembles the lane.
User-facing label     "what this agent was given".
API/schema identifier context_pack ; context_ref
                      ref fields: kind, source (REQUIRED, non-empty), status, checked, confidence
                      kind enum:       CompanyContext | RepoContext | ClientContext |
                                       SourceContract | DatasetContract | MetricContract |
                                       TaskContext | OperatorAnswer      (context.py:47)
                      status enum:     CURRENT | STALE | UNVERIFIED      (context.py:54)
                      confidence enum: MEASURED | DERIVED | STATED | ASSUMED  (context.py:63)
                      ⛔ UNVERIFIED is the DEFAULT status, not CURRENT (context.py:21-24), and
                      status=CURRENT requires a `checked` date — "Freshness is a measurement;
                      without the date it is an assertion wearing a measurement's label."
Example               context.py:56-58 — the module's own statement that freshness and trust are
                      orthogonal. That sentence is the ontology's `window` and `basis` axes,
                      discovered locally before anyone named them.
Counterexample        A 40,000-token concatenated prompt preamble. Not filterable, no sources, no
                      dates — and therefore not inspectable, which is the whole point.
```

---

#### 13. `Mandate` — NEXT, not NOW

```text
Canonical name        Mandate
Definition            What an Agent or Configuration is permitted to do: an authority set, a
                      depleting budget, an explicit prohibition, and an escalation rule. Checked
                      continuously at a boundary, never folded into a Verdict.
Why it exists         Because the draft's IntentContract holds two kinds of predicate at once
                      (Finding 3), and permissions are not falsifiable. Splitting them keeps
                      Contract's fold meaningful and gives authority a home that can actually be
                      enforced.
Aliases               authority envelope; rules of engagement (Army label); commander's intent
                      (the objective half lives on Task, not here)
Deprecated synonyms   IntentContract — REJECTED (Finding 3)
                      Policy — "Operational rule" (00-core-ontology.md:81) fails test (a) outright,
                        and R01 rates the term as colliding with Ponder/Rei/KAoS/XACML/OPA.
                      Doctrine — BLOCKING collision + no mechanism. A promoted Mandate carrying
                        its binding; not a term.
Not the same as       - Contract: required vs permitted; end-of-run vs continuous; falsifiable vs
                        not. This is the load-bearing distinction of Finding 3.
                      - Prohibition (blueprint.py:28,50): that is ONE FIELD of a Mandate, and
                        today it is prose in a prompt.
Identity              (subject, version). Part of the subject's identity hash — a weakened Mandate
                      must change the Configuration version, or a certification transfers across
                      a loosened permission. blueprint.py:58-61 records exactly that defect.
Lifecycle             authored -> enforced at a boundary -> violated | expired -> superseded
                      ⛔ authored -> enforced is the ONLY edge that makes it a Mandate. Without
                      it the object is a prompt string and must not use this word.
Relationships         bounds -> Agent | Configuration
                      escalates to -> a human   (operator.py:54 is the existing record type)
                      consumes -> Budget (a depleting counter, not a policy — R00 is right here
                      and it is worth restating: "A policy is checked; a budget is consumed.")
Persistence           source-controlled with the Configuration.
Runtime owner         the tool/store boundary. NOT the agent, and NOT the prompt.
User-facing label     "what this agent may do".
API/schema identifier mandate ; fields: authority, budget_usd, max_turns, prohibition, escalate_to
                      ("mandate" is free — zero occurrences in factory/, evaluator_service/,
                      tests/. Verified.)
Example               (none in code yet — this is why it is NEXT.) The nearest existing thing that
                      IS a Mandate by behaviour: tasks.py:163, where the STORE raises
                      EvidenceRequired. That is a rule enforced at a boundary. Generalising that
                      shape to authority is the work.
Counterexample        blueprint.prohibition today: a prose "must not" carried into a prompt and
                      enforced nowhere. It is part of the version hash, which makes a weakening
                      ATTRIBUTABLE (R00's N7) — but attributable is not enforced, and calling it a
                      Mandate would claim a property it does not have.
⛔ HARD GATE          If nothing in this harness can enforce authority at a tool boundary, demote
                      this term to RESEARCH ONLY and keep `prohibition` under its honest name. Do
                      not ship the word ahead of the mechanism. §Open questions Q1.
```

---

### Derived, not canonical — each is a fold, and storing it creates a second source of truth

| Derived thing | How it is computed | Why it is not a term |
|---|---|---|
| `Organization` | the fold of Configurations + Runs + Findings | Nothing organization-sized exists to store. Agreeing with R00. |
| `Mission` | a `Task` with `parent is None` | A label with a one-line test. Adding an object would double the store. |
| `Team` | the `agents` field of a `Configuration` | And the word is ambiguous in code (Finding 7b) — always qualify it. |
| `Capability` | `Evidence` grouped by task class, **with a sample size** | Never authored. R01 §D4 is right that `sampleSize` is the part that survives novelty review. A capability row with no evidence must be *unrepresentable*, not discouraged. |
| `Coverage` | four classes × three states, folded from `Evidence` | `evidence.py:131-139` already computes it. |
| `Knowledge` | `Finding`s with `STATUS=ADOPTED` | |
| `Decision` | a `Finding` with a STATUS, or a roadmap `Action` state | `roadmap.py:57` DECIDED / SHIPPED / SUPERSEDED. |
| `Board` / `Readiness` | non-passing gates of a `Contract`, plus authored `DEPENDS` edges | `board.py:5-8` — "There is no task list in this file." The only authored thing is the dependency graph, because no probe can infer "this must happen before that". |
| `Corpus` | an `Artifact` (hashed) that an `Instrument` scores against | Folding it in is what makes `stamp()` (corpus.py:105) legible: it is artifact attribution. |

---

## Deliverable 2 — Relationship diagram

Deliberately sparse. The draft's map (`01-relationship-map.md`) draws edges for objects that do not
exist and gives `Claim` four edges that are meaningless for the object the code calls `Claim`. This
map draws only edges that something today reads, writes or enforces — **and marks the ones that do
not exist yet**.

```text
                        ┌──────────────────┐
                        │  Configuration   │  binding: (model family, version)   ⚠ CONFIGURATIONAL
                        │  identity = hash │  deny-list: NOT_IDENTITY
                        └───┬──────────┬───┘
              contains      │          │  certified by
                  ┌─────────┘          └──────────┐
                  ▼                               ▼
            ┌───────────┐  bounded by      ┌────────────┐  contains   ┌────────────┐
            │  Agent    │◄╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌│  Mandate   │             │ Assertion  │
            │ ⚠ CONFIG  │   (NOT BUILT)    │ ⚠ NOT BUILT│             │            │
            └──┬────┬───┘                  └────────────┘             └─────┬──────┘
     receives  │    │  owns (1 at a time)                                   │ answered by
               ▼    ▼                                              ┌────────┴────────┐
      ┌──────────────┐   ┌──────────┐                              ▼                 │
      │ ContextPack  │   │   Task   │──── gated by ───►┌──────────────────┐          │
      │ ⚠ CONFIG     │   │          │                  │    Contract      │──────────┘
      └──────────────┘   └──┬───┬───┘                  │  = GreenContract │
                     has    │   │  produces            └─────────┬────────┘
                  ┌─────────┘   └──────────┐                     │ folds to
                  ▼                        ▼                     ▼
           ┌────────────┐            ┌───────────┐         ┌───────────┐
           │  Evidence  │            │ Artifact  │────────►│  Verdict  │
           │ class+basis│            │ uri+sha256│ scored  │  5 values │
           └─────┬──────┘            └───────────┘   by    └─────▲─────┘
                 │ produced by                  ▲                │ produces
                 │                              │ scores against │
                 │                    ┌─────────┴────────────────┴──┐
                 └───────────────────►│        Instrument           │
                                      │  standing: LIVE|DARK|UNPROVEN│  ⭐
                                      │  window · cause             │
                                      └─────────────┬───────────────┘
                                                    │ measured by
                                                    ▼
                                             ┌─────────────┐
                    Run ──── attributed to ──│   Finding   │  (attribution NOT-RECORDED today)
                    (lane-keyed; no join      │ BELIEVED/   │
                     to Task exists)          │ ACTUALLY    │
                                              └─────────────┘

    ╌╌╌╌  edge does not exist in code today
    ⚠     configurational: carries a model binding; certification does not transfer across bindings
    ⭐     the term this pass adds
```

**Four edges deliberately absent, each for a stated reason:**

- `Agent → Run`. Nothing executes a Configuration (`runs.py:277`). Drawing it would assert a
  capability the estate does not have.
- `Run → Task`. The ledger is lane-keyed; there is no join. `runs.unattributed()` reports that
  *all* of it is unjoinable, and that honesty is worth preserving in the diagram.
- `Agent → Field` (the draft's `01-relationship-map.md:33`). `Field` is deleted.
- `Doctrine → OrganizationCompiler` (the draft's `:44`). Neither object exists.

---

## Deliverable 3 — Glossary

One line each. Canonical terms in **bold**; derived and rule terms in plain.

- **Agent** — a locus of decision with a budget and the ability to refuse; its identity is its
  configuration, not its name.
- **Artifact** — a produced thing addressed by URI and sha256. If it cannot be hashed it is not one.
- **Assertion** — one falsifiable statement, answered by an Instrument, yielding one Verdict.
- Basis — how strongly a value is believed: `MEASURED | DERIVED | STATED | ASSUMED`.
- **Blind Zero** — a zero, "none", "never" or blank published from an Instrument that was `DARK` or
  `UNPROVEN`. The defect the Live-Instrument Rule prevents.
- Capability — Evidence grouped by task class, with a sample size. Derived, never authored.
- **Configuration** — the pinned choices that decide what a run is, plus the model binding they were
  validated against.
- **Contract** — a named set of Assertions defining "done", folding to one Verdict. Carries no
  authority and no objective, deliberately.
- **ContextPack** — the ordered set of context refs given to one agent, each naming its source,
  freshness and confidence.
- Coverage — four evidence classes × three states, folded from Evidence rows.
- **Evidence** — one recorded observation with a mandatory basis and a class; an unclassified row
  counts toward nothing.
- **Finding** — a corrected premise, addressable and permanent, that merges with the branch.
- **Instrument** — a named procedure that produces a value, with the window it covers and the proof
  it could have said otherwise.
- **Live-Instrument Rule** — an absence may be reported as a zero only from an Instrument whose
  standing is `LIVE` for that window.
- **Mandate** — what an agent may do: authority, budget, prohibition, escalation. Not a Mandate
  until enforced at a boundary. NEXT, not NOW.
- Mission — a Task with no parent. A label, not an object.
- **Run** — one execution episode, with what happened and how strongly that is known.
- Standing — whether an Instrument saw: `LIVE | DARK | UNPROVEN`.
- **Task** — one unit of work with an append-only history whose closure is gated on evidence.
- **Verdict** — `NOT_RUN | PASS | UNMEASURABLE | FAIL | REFUSED`. Five, never collapsed.
- Window — the period a reading covers. A freshness claim without a date is an assertion.

---

## Deliverable 4 — Developer / API naming guide

**Nine rules. The first four are prohibitions on identifiers that are already taken.**

1. **`contract` means `GreenContract`.** In seven importing modules and in `TeamSpec.contract`
   (`blueprint.py:47`), which puts it in every serialized blueprint. Never introduce a second
   `contract`, never qualify your way around it (`intent_contract`, `mission_contract` — no). If
   you need permissions, the identifier is `mandate`.
2. **`claim` means a lease.** `claims.Claim(lane, since, who, note)` — a filesystem
   mutual-exclusion record with no truth value. Never use `claim` for a proposition; use
   `assertion`. Never add a sixth meaning to `lane` (`claims.py:52-57` refused a fifth once
   already, for these reasons).
3. **`task` is ambiguous inside the code.** `tasks.Task` is persisted, claimable, evidence-gated;
   a `board` task is a derived view of a failing gate. In identifiers use `task` only for the
   stored kind; in prose always qualify.
4. **`artifact_uri` / `artifact_sha256` are taken** by `SUBMISSION_FIELDS` (`evaluator.py:55`), and
   that vocabulary is frozen on purpose: *"every field added here is one more thing the graded
   party gets to influence about its own grading."*

**Three rules about shape.**

5. **Every closed vocabulary is a module-level constant tuple, validated on write, raising on an
   unknown value.** `bus.py:48` + `:74-75` is the pattern (`UnknownClass` in `evidence.py:76` is
   the same shape). ⚠ The counterexample is in the codebase: `tasks.py:81-84` dispatches event
   kinds with `if kind ==` and no constant, and an unknown kind falls through silently at `:103`.
   That is the one closed set here that is not enforced, and it should be given a `KINDS` tuple.
6. **Every state vocabulary must contain a value meaning "the instrument did not see", and it must
   be derivable from `standing`.** If you are writing a third value and cannot say which of `LIVE /
   DARK / UNPROVEN` it is, you are collapsing two axes — check whether you actually need `basis` or
   `window` as a separate field. `context.py:51-63` is the worked example.
7. **New identity fields are identity by default.** Deny-list, never allow-list (`blueprint.py:39`
   `NOT_IDENTITY`, with the reason at `:36-38`).

**Two rules about honesty in identifiers.**

8. **Record `NOT-RECORDED`, never omit a key.** `runs.py:154-157` — an absent key reads as *"this
   ledger does not ask that question"*; an explicit `NOT-RECORDED` reads as *"nobody answered it"*.
   These are different claims and the schema must be able to say both.
9. **No Army word in an identifier, ever.** Not `mission_id`, not `squad`, not `battle_rhythm`, not
   `sensor`. §Deliverable 6 is display-layer only. The test: if it appears in a JSON key, a column
   name, a Python symbol or an enum member, it must be the canonical name.

---

## Deliverable 5 — User-facing language guide

The audience is a client or a non-specialist operator. The rule is: **the user-facing label may be
simpler than the canonical term, never stronger than it.**

| Canonical | Say | Never say | Why |
|---|---|---|---|
| `Verdict.UNMEASURABLE` | "couldn't check" | "failed", "warning", "0" | It is not a failure and not a degree of one. |
| `Verdict.NOT_RUN` | "not checked yet" | "passed", "n/a" | |
| `Verdict.REFUSED` | "we didn't score this" + the reason | "failed" | The apparatus, not the work. |
| standing `DARK` | "we couldn't look" | "nothing found" | This is the Blind Zero in one sentence. |
| standing `UNPROVEN` | "this check has never been seen to fail" | anything reassuring | *"A control never watched refusing is decoration."* |
| `Coverage.ABSENT` | "nobody looked" | "no issues" | `evidence.py:20-23`. |
| `Coverage.ASSERTED` | "claimed, not measured" | "verified" | The fix for ABSENT is to go and measure; for ASSERTED it is to stop calling a claim a proof. |
| `UNGATED` | "nothing can be measured yet" | "0%", "no progress" | `teamplan.py:24-26` — rendering it as an empty list reads as *nothing to do*. |
| basis `ASSUMED` | "our assumption" | omit it | Every published figure carries its basis. |
| a missing measure | "not measured" | "0", "0.00", blank-that-looks-like-zero | `pbi_contract.py:84-88` — *"A 0 reads as 'we measured none'; that is a claim about the client's business that we did not measure."* |

**Four presentation rules.**

1. **Colour is never the only carrier of a verdict.** `flow.py:41` `VERDICT_MARK` gives each verdict
   a glyph (`PASS ●  FAIL ■  UNMEASURABLE ◆  NOT_RUN ○`). Accessibility and honesty at once.
2. **Blocked is drawn differently from unbuilt** (`flow.py:16`).
3. **Every number carries the command that regenerates it.** This is a house rule and R00's N5, and
   the W0 note is what its absence costs.
4. **Never publish an Army label next to a number.** A "mission readiness: 82%" reads as a
   measurement of something that does not exist. The metaphor is for navigation and chrome.

---

## Deliverable 6 — Army-theme mapping

**Enforcement rule, stated first because the mapping is otherwise dangerous:** an Army label may
appear in page chrome, navigation, section headings and marketing prose. It may **never** appear in
a schema identifier, an API field, an enum member, a log line, a definition, or a sentence that
contains a number. If a reader can reach the number by reading only the label, the label has
replaced the definition and it must be removed.

| Technical primitive | Optional Army label | Notes |
|---|---|---|
| `Contract` | Mission Contract | Never in an identifier; `contract` is taken. |
| `Task` (parent=None) | Mission | The one label with a state test behind it (`parent is None`). |
| `Task` (child) | Task / Order | |
| `Run` | Operation | This is where "Operation" belongs — as a label, not an object. |
| `Configuration` | Task Organization / Order of Battle | |
| `Agent` | Unit | |
| `Configuration.agents` | Element | Not "squad", not "cell" — those imply distinct types that do not exist. |
| `Mandate` | Commander's Intent + Rules of Engagement | ⚠ Only once the mechanism exists. Labelling a prompt string "Commander's Intent" is the exact failure the enforcement rule above exists to stop. |
| `Instrument` | Sensor / ISR | |
| `Evidence` | Report | |
| `Coverage` | Situation Report | |
| `Finding` | Lesson Learned | Output of an After Action Review. |
| `ContextPack` | Logistics / Resupply | R00's Finding 4 makes this the best-evidenced law in the set; the label is apt. |
| `Verdict.PASS` from a LIVE instrument | "negative contact" (for an observed absence) | ⭐ The military idiom is exactly right and worth borrowing: a patrol reporting **negative contact** (we went, we looked, we saw nothing) is a different report from a patrol that **never reported**. That is the Live-Instrument Rule in the metaphor's own words, and it is the one place the Army theme genuinely clarifies rather than decorates. |
| `Verdict.UNMEASURABLE` | "no report" | |

**Labels explicitly refused**, with the reason:

| Refused | Why |
|---|---|
| Echelon | Means a level of command, not a time horizon. R01 Finding 5 — the literature wins; the term for what we mean is *planning horizon*. |
| Staff Mesh | Our staff functions are centralised; "mesh" asserts decentralisation. R01 calls this "the single most embarrassing item" in its report and it is right. |
| Doctrine | BLOCKING collision (PHP ORM) and no mechanism (no truce). |
| Command World | A UI metaphor with no state behind it. Rejection test (b). |
| Battle Rhythm | Names a cadence nothing schedules. Rejection test (d). |
| Federated Agent Armies | Nothing federates. Revisit if a second estate exists. |

---

## Deliverable 7 — Deprecated-term list

All 37 candidates from `foundations/R02:22-60`, plus the terms the drafts add. Column **T** is the
rejection test failed: (a) two teams will use it differently · (b) UI metaphor only · (c) another
canonical term covers it · (d) cannot be mapped to state or behaviour · (e) creates false novelty.

| Candidate | Verdict | T | Use instead / why |
|---|---|---|---|
| Organization | DERIVED | c | A fold over Configurations, Runs and Findings. Storing it makes a second source of truth. |
| OrganizationVersion | RENAMED | c | `Configuration`. Nothing organization-sized exists to version. |
| Intent | DEPRECATED | a,d | Today it is a free-text label on a launch record (`roadmap.py:183`). Splits into `Task.title` + `Contract` + `Mandate`. |
| IntentContract | **REJECTED** | a,c | Highest-risk collision in the set. `contract` resolves to GreenContract in 7 modules and in `TeamSpec.contract`. See Finding 3. |
| Mission | LABEL | c | A `Task` with `parent is None`. |
| Operation | DEPRECATED | c | `Run` (the record) or the Army label. |
| Task | **CANONICAL** | — | Bound to `tasks.Task`; qualify against `board` tasks. |
| Role | DELETED as an object | d | A free-text string with no template, registry or validation. Configurational, so it cannot have stable identity across bindings (Finding 6). |
| Agent | **CANONICAL** | — | Configurational. |
| Team | FIELD | a | Two live code objects wear it (Finding 7b). A field on `Configuration`; always qualified in prose. |
| Squad | DELETED | c,d | A Team with a different adjective. |
| Cell | DELETED | c,d | A Team with a shorter life. No distinct behaviour, no distinct storage. Agreeing with R00. |
| StaffFunction | RESEARCH ONLY | e | PROSA's *staff holon* (1998) is the exact precedent — same word. No LLM-era evidence it pays its coordination cost. |
| RunningEstimate | RESEARCH ONLY | d | No counterpart; `runs.py` is retrospective, not continuously revised. Do not map the two. |
| Artifact | **CANONICAL** (narrowed) | — | Hashable only. Tickets and deployments are TARGETs, not Artifacts. |
| Tool | FIELD | c | `AgentSpec.tools`. And a flat "Tool" would lose the `tools` vs `tool_implementation` split (`readiness.py:1206`). |
| Resource | DELETED | c,d | The fundamental thing is `Budget`, a depleting counter on Agent and Task. |
| Capability | DERIVED | c | Evidence grouped by task class, with a sample size. Never authored. |
| Readiness | DELETED as a term | a | Same word, different subject (estate vs unit) — Finding 7c. Plus TRL/CMMI/DRRS/K8s collisions. Use `Contract` + `Verdict`. |
| Skill | DO NOT MODEL | e | Agent Skills is an open cross-vendor standard. Reference it. |
| Procedure | DELETED | c | A Skill (external) or a Finding with `KIND=PROCESS`. |
| Observation | DELETED | c | An `Evidence` row with `basis=MEASURED`. |
| Claim | **DELETED** | a,c | Four live senses in one codebase (Finding 4). Use `Assertion`. |
| Evidence | **CANONICAL** | — | The code's typed meaning, not the draft's loose one (Finding 7a). |
| Knowledge | DERIVED | c | `Finding`s with `STATUS=ADOPTED`. |
| Experience | DELETED | c,d | |
| Lesson | DELETED | c | `Finding.KIND` is a finer cut. Keep "Lesson Learned" as an Army label only. |
| Policy | DEPRECATED | a | "Operational rule" is a definition two teams will read differently, and the word collides with Ponder/Rei/KAoS/XACML/OPA. Split into `Mandate` (enforced) and `Finding` (ADOPTED). |
| Doctrine | DELETED | a,e | BLOCKING collision (PHP ORM — every code search returns PHP) and no mechanism (no truce; R00 Finding 7). |
| Decision | DERIVED | c | A `Finding` with a status, or `roadmap.Action` state. |
| Outcome | DEPRECATED | a | Two live senses in code already (`metrics.py:21` vs `runs.py:41`). Use `Verdict`, or qualify as `run.outcome`. |
| Event | NESTED TYPE | c | A `Task` mutation record. ⚠ Explicit disagreement with R00, which made Event fundamental object #1: two typed event systems exist in code and *neither is an organizational event log* — naming Event canonically invites building one before there is anything to log. |
| Signal | **DELETED** | b,d | Zero occurrences. Wrong agent-count regime. |
| Field | **DELETED** | b,d | Same. |
| ContextPackage | DELETED | c | `ContextPack` — built, tested, and the only object already shaped correctly (Finding 5). |
| OrgIR | DELETED | e | Presupposes a compiler with source semantics; there is none. |
| Simulation | DELETED | c | A `Run` with a `REPLAYED` label, scored against a Corpus (an `Artifact`). |
| Belief, Pattern, Expertise (`vision/01:85-99`) | DELETED | c,d | Each is Evidence, a Finding, or Capability under a nicer word. |
| Knowledge Cache, Cognitive Supply Line (`vision/01:105-107`) | DELETED | b,d | Metaphors with no state. |

**Count check.** 37 candidates → 13 canonical (2 of which are renames of code objects that already
exist), 9 derived, 3 field-or-label demotions, 12 deleted or research-only. Regeneration command for
the candidate count is in §Metadata.

---

## Deliverable 8 — Unresolved vocabulary questions

**Q1. Can a `Mandate` be enforced at a boundary in this harness at all?** ⭐ The highest-stakes one.
If not, the term is a wish and `prohibition` keeps its honest name. Nobody has tested prompt-level
versus boundary-level compliance; R00's A7 proposes the experiment and it has not been run.

**Q2. Where does `REFUSED` sit in the verdict lattice, and does it belong in the enum?** I recommend
`NOT_RUN < PASS < UNMEASURABLE < FAIL < REFUSED` (TTCN-3's ordering with our names), but this is a
design choice the estate has never had to make because `REFUSED` cannot currently reach the
aggregator. Deciding it is cheap; discovering it by accident in the first path that has to fold one
is not.

**Q3. Three-value or four-value `basis`?** `tasks.py:136` accepts `MEASURED | DERIVED | ASSUMED`;
`context.py:63` accepts those plus `STATED` (*"a human said so"*). Nothing reconciles them. I lean
four everywhere, because `STATED` is exactly what `evidence.ASSERTED` exists to catch — but widening
a validated enum has a migration cost I did not measure.

**Q4. Should `Unmeasurable` be one exception class or three?** It is defined three times with three
docstrings (`contract.py:63`, `readiness.py:42`, `schedule.py:54`) and they are not the same class
object; `plan_gates.py:39` imports readiness's. A caller cannot catch "unmeasurable" generically
today.

**Q5. Should `roadmap.TEAMS` be renamed?** It is an objective, not a team (Finding 7b). Low cost —
a dict in one module — but it is an agent-factory change and not mine to make.

**Q6. Should `claims.Claim` become `Lease`?** Correct end state, non-urgent, touches a race-tested
store. Recorded so it is a decision rather than a drift.

**Q7. What is the `window` for a `Run`?** `runs.py` has no explicit window field, and
`MEASURED_SINCE = "2026-08-22"` (`readiness.py:100`) is a module constant rather than a property of
a reading. If windows become first-class, that constant should move onto the Instrument.

**Q8. Does `Configuration.binding` need a granularity below "model family"?** IMACS's result is at
family granularity. Whether a point-release invalidates a certification is unmeasured, and the
answer decides how often certifications expire.

**Q9. Who else will use this vocabulary?** — `NOT-SUPPLIED`. Rejection test (a) is *"two teams will
plausibly use it differently"*, and I could only apply it against one codebase. If a second team or
a client-facing surface is planned, the test must be re-run against them.

---

## Failure modes

*What breaks if the recommendation is wrong?*

1. **If `Instrument` is the wrong abstraction** — i.e. if the nine vocabularies are genuinely nine
   different concepts and I have over-unified — then a tenth module will find `standing / basis /
   window` insufficient and add a fourth axis. Cost: a paragraph. This is the cheapest failure in
   the set and it is why I recommend naming rather than refactoring.
2. **If `Mandate` cannot be enforced** — the term ships, gets used in prose, and an unenforceable
   permission acquires the authority of a named object. This is the *expensive* failure, because
   the whole point of R00's N3 is that a prompt-level constraint that looks like a constraint is
   worse than no constraint. Mitigation: the hard gate in the term's own schema, and NEXT status.
3. **If deleting `Claim` is wrong** — we lose a word people will keep using anyway, and prose gets
   clumsier. Cheap. Reversal is a rename, not a redesign.
4. **If the structural/configurational cut is wrong** — i.e. if configuration turns out to be
   binding-stable after all — we carried a `binding` field nobody needed and expired certifications
   too often. Cost: over-caution. The failure in the other direction (a certification that silently
   transfers across a model change) has already happened once in this estate at the repo/prohibition
   level (`blueprint.py:58-61`), which is why I take this asymmetry.
5. **The most dangerous way to be wrong.** This ontology is **more agreeable to the code than an
   outside model would be**. I read the code closely and I found it good, and a pass that runs at
   `INDEPENDENCE_RISK: HIGH` and then endorses nine of the estate's own vocabularies should be read
   with that in mind. The single strongest counterweight I can offer is that I went and found the
   one thing that *damages* the estate's novelty claim (Finding 1) rather than leaving the gap W0
   named. A second pass by an outside model on §Deliverable 1 alone would be worth its cost.

---

## Data-model implications

- **13 tables/types, not 30.** Nine structural, four configurational. Four of the thirteen already
  exist as code (`Contract`, `Assertion`, `Evidence`, `Task`); three more exist under exactly these
  names (`ContextPack`, `Finding`, `Run`); two are renames (`Configuration` ← `TeamSpec`, `Agent` ←
  `AgentSpec`); one is narrowed (`Artifact`); one is an enum (`Verdict`); one is new
  (`Instrument`); one is unbuilt (`Mandate`).
- **`standing` is computed, never persisted.** Persisting it recreates `claims.py:83-87`'s bug: age
  is a clock reading, liveness is a measurement.
- **Every configurational row carries `binding`, and it is part of the identity hash.**
- **Every state enum needs a value derivable from `standing`.** Rule 6 of the naming guide.
- **`NOT-RECORDED` over omission, everywhere** (`runs.py:154-157`).
- **Capability is unrepresentable without evidence rows.** Not discouraged — unrepresentable. R00
  says this and it is right.

## Runtime implications

- The `Instrument` lifecycle edge `declared → proven → live` is the only enforcement this ontology
  adds at runtime, and it already has two working precedents:
  `test_every_gate_can_refuse` and `test_every_assertion_has_been_proved_able_to_fail`. Generalising
  is a test-shape change, not an architecture change.
- `REFUSED` in the enum means `ContractResult.verdict` must gain a branch. Small, and it forces Q2.
- Nothing here requires an organizational event log, an org compiler, a runtime or a debugger. That
  is deliberate: R00 §D7 rates the two the vision leads with as the two that survive worst.

## UI implications

- The highest-value screen is the **coverage view** (four evidence classes × three states), and R00
  is right that `evidence.py:143-152` already renders it in text. The second is a **standing view**:
  for each Instrument, is it LIVE, DARK or UNPROVEN, and since when.
- **No visual element may encode a quantity the system does not measure** (R00, strengthening
  ADR-0004). The Instrument term gives this teeth: a pulsing node is a rendering of a reading, and a
  reading from a DARK instrument must render as absent, not as still.
- Army labels live in chrome. §Deliverable 6's enforcement rule is the UI's rule.

## Performance implications

None material. This pass adds one computed field (`standing`) and one enum member. The only cost is
that computing standing per window requires the negative-control result to be *available at read
time*, which today lives in a test suite rather than in a store. That is the one place where naming
the concept implies a small amount of plumbing.

## Security/governance implications

- **`Instrument`'s runtime owner is the evaluator, never the agent** — this makes grader separation
  (`corpus.py:9`) a property of a *term* rather than of one module's docstring. That is the main
  governance gain from this ontology.
- **`Mandate` is a security object.** If it ships as prose it becomes a governance claim with no
  enforcement, which is worse than an honest `prohibition` field. Hence the hard gate.
- **`Configuration.binding` is a governance control**: it is what makes "this was certified" a
  time-and-model-bounded statement rather than an unqualified one.
- Unchanged and still the top open item: separation is *evident* and *attributed*, not *enforced*
  (`corpus.py:24-26`). The ontology does not fix that; it names why it matters.

## Experiments required

**E1 — Does naming the concept stop the tenth vocabulary?** *Falsifiable:* over the next N modules
that need a "could not see" value, count how many use `standing` versus invent a new three-value
ladder. If ≥1 invents a new one after the term is documented, the naming intervention failed and the
answer is enforcement (a shared constant), not documentation.

**E2 — Q1, the Mandate experiment.** Adversarial trials of prompt-level versus boundary-level
prohibition compliance. *Falsified by:* indistinguishable compliance rates, which would mean
`prohibition` is already a Mandate and the term is free. This is R00's A7 and it gates a canonical
term, which raises its priority.

**E3 — Is `standing` sufficient, or is there a fourth axis?** Take the nine vocabularies, express
each in `(standing, basis, window)`, and have someone who did not do the mapping try to reconstruct
the original semantics from the triple. Any value that cannot be reconstructed is a fourth axis.

**E4 — Q8, binding granularity.** Run one certified contract under two point-releases of the same
model family. If verdicts differ, `binding` needs version granularity, not family.

**E5 — The rejection-test-(a) gap.** Give the 13-term glossary to one person outside this estate and
ask them to define each term cold. Every term two readers define differently fails test (a) and must
be renamed. This is the test I could not run (§NOT-SUPPLIED).

---

## Recommendation

```text
NOW
```

- **Adopt `Instrument`, `standing`, the Live-Instrument Rule and `Blind Zero`** into
  `ontology/00-core-ontology.md` at synthesis. Documentation only, blast radius zero. This is the
  single highest-value item in the pass.
- **Adopt the 13-term canonical list** and the deprecated list. Delete `Claim`, `Signal`, `Field`,
  `Cell`, `Squad`, `Readiness`, `Doctrine`, `ContextPackage`, `OrgIR`, `Simulation` from the
  ontology.
- **Decide `contract` explicitly** (Finding 3): `Contract` = `GreenContract`; no `IntentContract`;
  authority lives in a separate object.
- **Adopt `ContextPack` / `ContextRef` verbatim.**
- **Rewrite `ontology/01-relationship-map.md`** to §Deliverable 2, which draws only edges something
  reads and marks the ones that do not exist.
- **Correct R01's novelty claim** to the narrowed composition (Finding 1). It is currently the
  programme's headline claim and it is overstated as written.

```text
NEXT
```

- **`REFUSED` into the `Verdict` enum**, with the lattice decided (Q2).
- **`KINDS` tuple + validation for task-store event kinds** (`tasks.py:81-103`) — the one
  unenforced closed set.
- **`Mandate`**, gated on E2. Do not ship the word first.
- **Reconcile the basis ladders** (Q3).

```text
LATER
```

- `binding` as a first-class field on every configurational row, gated on E4.
- `roadmap.TEAMS` rename (Q5); `claims.Claim` → `Lease` (Q6). Both agent-factory changes.
- `window` promoted from a module constant to an Instrument property (Q7).

```text
RESEARCH ONLY
```

- `StaffFunction` — PROSA's staff holon is the precedent and there is no LLM-era evidence it pays.
- `RunningEstimate` — no counterpart in code; do not map it onto the retrospective run ledger.
- Everything in `vision/01`'s "UI lenses" list until each lens names the field it reads.

```text
DO NOT BUILD
```

- An organizational event log, an Org-IR, an organizational compiler, a field engine.
- A second `contract` object under any name.
- **A refactor of the nine vocabularies into one enum.** Explicitly listed here because it is the
  obvious next move after reading Finding 1 and it is the wrong one: every one is validated, several
  are tested, and the rename buys no behaviour.

---

## Claims ledger

| Claim | Evidence tier | Primary support | Counterevidence | Confidence |
|---|---|---|---|---|
| `contract` resolves to GreenContract in 7 non-test modules | ESTABLISHED | grep enumeration at a090f6f, listed in §Evidence | none | HIGH |
| `TeamSpec.contract` binds the word in every blueprint | ESTABLISHED | `blueprint.py:47` re-read | none | HIGH |
| `claim` has four live senses | ESTABLISHED | `claims.py:69`, `tasks.py:26`, `bus.py:50`, `contract.py:42` | none | HIGH |
| The nine vocabularies collapse three orthogonal axes, differently each | ESTABLISHED (repo) / DERIVED (the axis model) | nine-row table, every row re-checked | The axis decomposition is mine; nobody has validated it. E3 tests it. | MEDIUM-HIGH |
| `context.py` is the only module that separated two axes | ESTABLISHED | `context.py:51-63` + `:56-58` | none | HIGH |
| ISO/IEC 9646 (1991) and TTCN-3 standardise a five-verdict vocabulary with an instrument/subject split | EMERGING | TTCN-3 tutorial literature, two independent sources `SECONDARY` | Primary standards text NOT read (403 / unparseable PDF). If the tutorials misstate it, the *strength* of the prior art changes but not its existence. | MEDIUM-HIGH |
| Therefore R01's novelty claim as stated is prior art | EMERGING | above | R01's claim survives in narrowed form; I am correcting scope, not deleting it. | MEDIUM-HIGH |
| "mandate" is unused in agent-factory | ESTABLISHED | grep, zero hits | none | HIGH |
| "instrument" appears in prose in 15 modules and as a type in none | ESTABLISHED | `grep -rc` | none | HIGH |
| Permissions cannot be members of a falsifiable assertion set | DERIVED | `contract.py:42`, `:73-85` — the fold's meaning | Someone could define a permission-check assertion evaluated continuously; that would be a different object with the same name. | MEDIUM-HIGH |
| Configuration terms are model-binding-dependent | EMERGING | IMACS via W0 (verified by another session, not by me) | One paper, one experimental setup, generalised by me to a whole tier. | MEDIUM |
| 13 is the right number of terms | EXPERIMENTAL | applying four rejection tests to 37 candidates | No experiment. E5 is the test and it needs a person outside the estate. | LOW-MEDIUM |
| `Mandate` is buildable | SPECULATIVE | none | R00's N3 says prompt constraints are not constraints; nothing here is at a boundary. | LOW |

---

## Changed-my-mind section

**1. I expected the answer to `IntentContract` to be a rename. It is a split.** I went in assuming
the crawl's framing — pick a different head noun — and R00's — merge into GreenContract. Reading
`contract.py:42` and `:73-85` closely changed it: the fold over assertions is only meaningful
because every member is falsifiable, and authority is not. The collision is the visible symptom; the
type error underneath it is the real finding, and neither R00 nor the crawl states it.

**2. I expected the nine vocabularies to be nine names for one thing.** They are not. Building the
mapping table row by row, I found that **no two of the nine cover the same subset of axes** — which
explains why they were never unified and why `context.py`'s two ladders have never been reconciled
with `tasks.py`'s one. That reframed the deliverable from "pick a winning name" to "name the axes".

**3. I expected to endorse R01's novelty claim.** W0 had already flagged that it rested on an unrun
search, and I ran the search expecting to find nothing. TTCN-3's `inconc`/`error` split, with a
dominance lattice and an explicit "error indicates an error in the test devices", is a much closer
prior art than I expected — and the aggregation ordering `factory/contract.py:73-85` re-derived is
the same ordering. The claim survives, narrowed. This is the finding I would least have predicted at
the start of the pass.

**4. I expected to agree with R00 on `Claim` and `Event`.** I do not, on either, and for the same
underlying reason: both are terms whose *research* meaning is clean and whose *code* meaning is
already contested or absent. R00 kept them; I think keeping a term whose identifier is already taken
four ways is exactly what rejection test (a) exists to prevent.

---

## Open questions

Beyond §Deliverable 8's nine (which are the vocabulary-specific ones):

- Does anything in this estate actually *read* a `standing`-shaped value and change behaviour on it,
  or is every one of the nine currently only rendered? If rendering is all, the concept is a
  reporting convention, not a control — an important downgrade.
- `Run` has no join to `Task`. Is that a gap to close or a deliberate separation? `runs.py:241`
  ("Attribution is NEVER reconstructible") suggests closing it later is impossible, which makes it
  urgent rather than deferrable.
- Is `Artifact`'s narrowing to hashable-only too tight for a Power BI model, which is a live mutable
  object rather than bytes? `pbi_contract`'s `baseline` and `rollback_path` suggest the estate
  already models this as "a hash of a capture", but I did not verify.
- The brief asks for the *smallest precise* language. Thirteen may still be too many. The two I
  would cut first under pressure are `Run` (fold into Evidence about execution) and `Assertion`
  (fold into Contract). I did not, because both are live dataclasses with distinct stores, and
  cutting a term the code has is a different act from cutting one it does not.

---

## Proposed architecture changes

1. `Instrument` as a type in `factory/`, with `standing` computed from (a) whether the probe ran in
   the window and (b) whether the negative-control test for it has passed. The second input lives in
   the test suite today and would need to be readable at runtime — that is the only real plumbing
   this pass implies.
2. `REFUSED` into `Verdict`; `ContractResult.verdict` gains a branch (Q2).
3. `KINDS` tuple + raise for task-store event kinds.
4. `binding` field on `TeamSpec`, inside the identity hash.
5. *(Not now)* `Mandate` enforced at the tool boundary, generalising the `tasks.py:163` shape.

## Proposed ADRs

- **ADR — `contract` means `GreenContract`; authority lives in `Mandate`.** Records Finding 3,
  including why merging into GreenContract was rejected. Without this written down, `IntentContract`
  returns.
- **ADR — the Live-Instrument Rule.** Records `standing`, the three axes, the nine-vocabulary
  mapping, and the explicit decision *not* to refactor the nine.
- **ADR — structural vs configurational terms.** Records the IMACS-driven split and the consequence
  that certifications are binding-bounded.
- **ADR — `Claim` is deleted from the ontology.** Records the four senses and the `claims.py:52-57`
  precedent, so the word does not drift back in.

---

## NOT-SUPPLIED

Named rather than inferred, per §8 of the brief.

1. **Primary standards text for ISO/IEC 9646-1 and ETSI ES 201 873-1.** iso.org is paywalled; the
   ETSI PDF returned HTTP 403; the Grabowski tutorial PDF was compressed beyond my fetcher's ability
   to parse. The TTCN-3 verdict semantics in Finding 1 are `SECONDARY`, from two independent
   academic/tutorial sources that agree. If Finding 1 is going to be used to rewrite R01's headline
   novelty claim, **someone should open ES 201 873-1 §"verdict" and confirm the five values and the
   lattice from the standard itself.** I would not want that rewrite to rest on a tutorial.
2. **Anyone outside this estate to test rejection test (a) against.** The test is *"two teams will
   plausibly use it differently"* and I could apply it against exactly one codebase. E5 is the
   experiment and it needs a person.
3. **Any product or UI specification for Agent Army.** Every "User-facing label" field in
   §Deliverable 1 is therefore a proposal, not a validated label. No user has seen any of them.
4. **A list of the consumers of this vocabulary** — other repos, clients, a public site. Without it
   I cannot say which terms need to survive contact with a non-technical reader.
5. **Measured migration cost for widening `tasks.py`'s basis enum** (Q3). I recommend four values
   without having counted the call sites.
6. **Whether any harness boundary can enforce authority** (Q1). This is unmeasured and it gates a
   canonical term.

---

## Sources

**Repository (primary, read directly by me at agent-factory HEAD `a090f6f`):**
`factory/contract.py`, `evidence.py`, `tasks.py`, `claims.py`, `context.py`, `runs.py`, `bus.py`,
`board.py`, `blueprint.py`, `findings.py`, `evaluator.py`, `flow.py`, `pbi_contract.py`,
`connector_contract.py`, `readiness.py`, `lanes.py`, `sessions.py`, `goals.py`, `launch.py`,
`teamplan.py`, `deploy.py`, `roadmap.py`, `corpus.py`, `metrics.py`, `presets.py`,
`evaluator_service/service.py`.

**Repository (this repo):** `foundations/R02-canonical-ontology-and-vocabulary.md`,
`ontology/00-core-ontology.md`, `ontology/01-relationship-map.md`,
`vision/01-vocabulary-and-primitives.md`, `research/ANSWER_TEMPLATE.md`,
`research/sources/agent-factory-vocabulary-crawl.md`,
`research/sources/W0-citation-verification-partial.md`,
`research/answers/R00-answer-foundations-of-aoe.md`,
`research/answers/R01-answer-prior-art-and-novelty-boundary.md`.

**External (all `SECONDARY` — see NOT-SUPPLIED item 1):**
- ISO/IEC 9646-1:1991 / :1994, *Information technology — OSI — Conformance testing methodology and
  framework — Part 1: General concepts*. https://www.iso.org/standard/17472.html (existence and
  scope confirmed; verdict definitions not read)
- Grabowski, Hogrefe, Réthy, Schieferdecker, Wiles, Willcock, *An Introduction to the Testing and
  Test Control Notation (TTCN-3)* (2003), and the TTCN-3 User Conference 2004 tutorial.
  https://ttcn-3.etsi.org/ttcn-3uc04/cd/Programme/EducationTrack/20030426-TTCN-3-Introduction.pdf
- Grafana Labs, *No Data and Error states*.
  https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rule-evaluation/nodata-and-error-states/
- Altman DG, Bland JM, *Absence of evidence is not evidence of absence*, BMJ 1995;311:485.
  https://pubmed.ncbi.nlm.nih.gov/7647644/
- ITRC, *5.7 Nondetects*.
  https://projects.itrcweb.org/gsmc-1/Content/GW%20Stats/5%20Methods%20in%20indiv%20Topics/5%207%20Nondetects.htm
- US EPA, *Regional Guidance on Handling Chemical Concentration Data Near the Detection Limit*.
  https://www.epa.gov/risk/regional-guidance-handling-chemical-concentration-data-near-detection-limit
- IMACS: Chen, Song, Jin, Ren, Zhang, arXiv:2607.25446 — quoted via
  `W0-citation-verification-partial.md:148-151`, verified there by direct fetch. **Not re-fetched by
  me.**

---

## Closing question

> **What is the minimum vocabulary Agent Army needs today, and which terms should remain
> research-only until their mechanisms are validated?**

**Today, Agent Army needs nine words.** Not thirteen — nine. These are the terms that name something
the running system already does, where the word is currently missing or contested and the absence is
costing something:

```text
Instrument   Verdict   Assertion   Contract   Evidence   Task   Artifact   Finding   Run
```

Eight of the nine already exist as code under these or adjacent names, which is the test that they
are real. The ninth — `Instrument` — is the one this pass adds, and it is the only genuinely new
word in the whole answer. It earns its place on a count: the concept it names is implemented **nine
times under nine vocabularies**, which means the estate has paid for it nine times and cannot yet
say it once.

**Four more are needed as soon as anything actually runs**, and not before:
`Configuration`, `Agent`, `ContextPack`, `Mandate`. All four are **configurational** — their correct
values are downstream of the model binding — and `Mandate` additionally carries a hard gate: it is
not a Mandate until it is enforced at a boundary, and until then the honest word is `prohibition`.

**Research-only until their mechanisms are validated:**

| Term | Waiting on |
|---|---|
| `StaffFunction` | evidence that a persistent advisory unit pays its coordination cost at team sizes ≤5. PROSA named it in 1998; nobody has measured it with LLM agents. |
| `RunningEstimate` | anything that continuously revises an assessment. The run ledger is retrospective; mapping the two would be a false claim. |
| `Mandate` | E2 — boundary enforcement. Canonical in shape, unbuilt in fact. |
| `Capability` (as an authored thing) | never. It is derived from Evidence with a sample size, permanently. |
| Every `vision/01` UI lens | each naming the field it reads. |

**And the terms that should never come back:** `Claim`, `Signal`, `Field`, `Cell`, `Squad`,
`Doctrine`, `Readiness`, `IntentContract`, `ContextPackage`, `OrgIR`. Each fails at least two of the
brief's four rejection tests, and three of them (`Claim`, `Readiness`, `IntentContract`) fail against
identifiers that are *already taken by running code* — which is the only kind of vocabulary failure
that cannot be argued away.

**The sentence I would keep if the rest were thrown away:** the estate's most repeated design
decision is the refusal to report a zero from an instrument that has not been shown able to see a
non-zero. It is implemented nine times, named zero times, and prior art for it is thirty-five years
old in conformance testing and older still in metrology. Give it one name — `Instrument`, with
`standing` — cite the prior art rather than claiming the idea, and stop paying for it a tenth time.
