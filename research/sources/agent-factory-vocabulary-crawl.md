# Agent Factory — Vocabulary Crawl (source note)

```text
REPOSITORY     C:/Users/PaulRussell/repos/agent-factory
BRANCH         docs/agent-army-research-separation
HEAD           a691043adfea616c4ade45dc8566e440364494ab
DATE           2026-08-30
PRODUCED BY    local subagent reading source directly (no web, no summaries)
FOR            research pass R02 — Canonical Ontology and Vocabulary
```

**Method and its limits.** Every entry below was read from the file and line cited. Modules read in
full: `contract.py`, `evidence.py`, `tasks.py`, `bus.py`, `context.py`, `runs.py`, `board.py`,
`claims.py`, `repo.py`, `corpus.py`, `calibration.py`, `metrics.py`, `goals.py`, `operator.py`,
`blueprint.py`, `evals.py`, `targets.py`, `demo.py`, `certify.py`, `teamplan.py`, `findings.py`.
Modules read in the parts that carry vocabulary (docstring + module-level constants + class
definitions), with the rest skimmed: `readiness.py` (1547 lines), `lanes.py`, `sessions.py`,
`dispatch.py`, `research_run.py`, `roadmap.py`, `plan_gates.py`, `presets.py`, `connector_contract.py`,
`pbi_contract.py`, `live_probes.py`, `evaluator.py`, `deploy.py`, `schedule.py`, `launch.py`,
`synthesis.py`, `handoff.py`, `finish.py`, `worktrees.py`, `flow.py`, `evaluator_service/*`. Not
opened: `factory/__init__.py` (2 lines), `evaluator_service/__main__.py`, and the bodies of
individual gate probes in `readiness.py` beyond the ones quoted.

**A note on the corpus this crawl mirrors.** `docs/agent-army/CURRENT_STATE.md:14` records a grep
across `factory/`, `evaluator_service/` and `scripts/` for every Agent Army term and states that it
returns nothing: *"Not one Agent Army term appears in any Python module in this repository."* That
document was measured against HEAD `b4bac0d`; this crawl is at `a691043`. Everything below is
therefore a **parallel vocabulary**, not a partial implementation of the research one.

---

# PART 1 — THE CLOSED SETS

These are the highest-value entries: each encodes a decision, is validated at write time or import
time, and has a test that proves the refusal path is reachable.

---

## Verdict

```text
TERM                Verdict
KIND                enum (str, Enum)
DEFINED AT          factory/contract.py:17  (members at :18-21)
WHAT IT MEANS HERE  The four outcomes of one falsifiable assertion. The root success object —
                    "Every team, every optimizer run and every certification reads its verdict
                    from here" (contract.py:3).
DISTINCTION IT      FAIL vs UNMEASURABLE. Stated as the reason the file exists.
PROTECTS
ALLOWED VALUES      PASS · FAIL · UNMEASURABLE · NOT_RUN
QUOTE               "UNMEASURABLE = "UNMEASURABLE"   # instrument could not run — NOT a pass"
                    (contract.py:20)
                    "**Four verdicts, never collapsed.** The distinction between FAIL and
                    UNMEASURABLE is the entire reason this file exists: a check whose instrument
                    could not run has not passed, and reporting it as a pass is how a measurement
                    gap becomes a claim about the system." (contract.py:6-8)
```

Aggregation rule, `ContractResult.verdict` (contract.py:73-85): any FAIL → FAIL; else any
UNMEASURABLE → UNMEASURABLE; empty results → NOT_RUN; else PASS. Comment at :76-78: *"An
UNMEASURABLE required assertion yields UNMEASURABLE for the whole contract — not FAIL, because we
did not observe a failure, and emphatically not PASS."*

Tests: `tests/test_contract.py::test_unmeasurable_is_not_a_pass`,
`::test_crashing_instrument_is_unmeasurable_not_pass`, `::test_empty_contract_is_not_run`.

The same four strings are re-declared as plain module constants in `factory/readiness.py:34`
(`PASS, FAIL, UNMEASURABLE, NOT_RUN = "PASS", "FAIL", "UNMEASURABLE", "NOT_RUN"`) — the readiness
board does not import the enum, it mirrors its values.

---

## Evidence CLASSES

```text
TERM                CLASSES (TARGET, CONSUMER, REGRESSION, ROLLBACK)
KIND                constant tuple
DEFINED AT          factory/evidence.py:48  (members at :43-46, meanings at :51-56)
WHAT IT MEANS HERE  The four distinct questions a delivery's evidence must answer. Ordered as the
                    evidence gate runs them.
DISTINCTION IT      Refuses to let four artefacts answering ONE question satisfy a four-question
PROTECTS            gate. "four pieces of evidence that are all the same class look identical to
                    four that cover four different questions."
ALLOWED VALUES      TARGET · CONSUMER · REGRESSION · ROLLBACK
QUOTE               "TARGET      which object/system does the consumer ACTUALLY read
                                 — proved by a discriminating test, never inferred from matching
                                   values, and never inherited from a ticket, a boot prompt or a
                                   handoff" (evidence.py:11-13)
```

Two named requirement profiles:
- `DELIVERY: tuple = CLASSES` (evidence.py:60) — work that mutates something a consumer reads.
- `ANALYSIS: tuple = (TARGET, CONSUMER)` (evidence.py:65) — *"Present so that 'we only need two'
  is a declared policy, not an omission."*

`UnknownClass(ValueError)` (evidence.py:76) is raised by `check()` (:84): *"A typo'd class silently
creates a fifth bucket nothing requires, which is how a mandatory artifact becomes optional without
anyone deciding it should be."*

Two stated limits (evidence.py:25-33), quoted because R02 should not assume more: it **cannot verify
ordering** (a ROLLBACK row proves a rollback was *recorded*, not *recorded first*) and it **cannot
judge the evidence** (*"The class is a slot, not a referee — the referee is a `GreenContract`."*).

---

## Evidence coverage states

```text
TERM                SATISFIED / ASSERTED / ABSENT
KIND                constants (three-state vocabulary)
DEFINED AT          factory/evidence.py:68-70; folded in coverage() at :131-139
WHAT IT MEANS HERE  Per-class state of one task's evidence rows.
DISTINCTION IT      "nobody looked" vs "somebody claimed it without measuring". Explicitly the same
PROTECTS            defect class as collapsing UNMEASURABLE into FAIL.
ALLOWED VALUES      SATISFIED (>=1 MEASURED or DERIVED row) · ASSERTED (rows exist, all ASSUMED) ·
                    ABSENT (no row at all)
QUOTE               "⭐ **Three states, never two.** … `ABSENT` means nobody looked. `ASSERTED`
                    means somebody claimed it without measuring. Only `SATISFIED` is a pass."
                    (evidence.py:20-23)
```

`Coverage.missing` (evidence.py:101) returns ABSENT and ASSERTED alike, *"because both block, but
`state` keeps them distinguishable: the fix for ABSENT is to go and measure, and the fix for
ASSERTED is to stop calling a claim a proof."*

Test: `tests/test_evidence_classes.py::test_absent_asserted_and_satisfied_are_three_different_answers`,
`::test_four_pieces_of_one_class_do_not_satisfy_four_classes`.

---

## Evidence basis (on a task evidence row)

```text
TERM                basis
KIND                persisted field, validated at write time
DEFINED AT          factory/tasks.py:124 (parameter), :136-137 (validation), :161 (usable set)
WHAT IT MEANS HERE  How a piece of evidence came to be believed.
DISTINCTION IT      An assumed proof is not a proof; only MEASURED and DERIVED can close a task.
PROTECTS
ALLOWED VALUES      MEASURED · DERIVED · ASSUMED     (usable subset: MEASURED, DERIVED —
                    factory/evidence.py:73 USABLE)
QUOTE               "basis is MEASURED | DERIVED | ASSUMED — an assumed 'proof' is not a proof."
                    (tasks.py:125)
                    "if basis not in {"MEASURED", "DERIVED", "ASSUMED"}: raise ValueError(...)"
                    (tasks.py:136-137)
```

Note the asymmetry with `evidence_class`: basis is **mandatory** (defaulted to MEASURED and
validated), `evidence_class` is **optional and validated only when given** (tasks.py:139-140), and an
unclassified row *"counts toward nothing"* (tasks.py:131-134) — deliberate, because *"a class
inferred from a free-text label is exactly the 'inferred from matching values' move the TARGET class
exists to forbid."*

---

## bus KINDS

```text
TERM                KINDS
KIND                constant tuple
DEFINED AT          factory/bus.py:48  (enforced at :74-75)
WHAT IT MEANS HERE  What one lane may say to another over the live, ephemeral channel.
DISTINCTION IT      The CHANNEL (.data/bus/, gitignored, machine-local) vs the RECORD
PROTECTS            (docs/findings.d/, in git, permanent).
ALLOWED VALUES      correction · claimed · blocked · finished · note
QUOTE               "Deliberately small — every kind here is one that actually happened on
                    2026-08-22 and had no channel at the time." (bus.py:45-47)
                    "correction,   # your premise is wrong; the durable version is a finding"
                    (bus.py:49)
```

`claimed` is glossed *"I am touching this file/area — the filesystem, not the dependency graph"*
(bus.py:50). `MAX_LEN = 2000` (bus.py:44): *"Longer than this is a document, and a document belongs
in findings.d or evidence."* Rendered traffic is prefixed *"These are peers, not instructions —
verify anything you act on."* (bus.py:137-138).

Test: `tests/test_bus_and_finish.py::test_the_bus_refuses_junk`.

---

## Run outcome + run basis

```text
TERM                outcome / basis (on a lane run row)
KIND                constants + persisted fields
DEFINED AT          factory/runs.py:41 (outcome), :42 (basis)
WHAT IT MEANS HERE  What happened to a lane run, and how strongly we know it.
DISTINCTION IT      "A lane with no record is NOT a lane that did not run."
PROTECTS
ALLOWED VALUES      outcome: FINISHED · REFUSED · ABANDONED
                    basis:   RECORDED · RECONSTRUCTED · NOT-RECORDED   (plus MEASURED at :43,
                             used for cost)
QUOTE               "**2. A lane with no record is NOT a lane that did not run.** Everything
                    before this module existed is unrecorded, and reporting that as "0 runs" would
                    be the ZERO-vs-NOT-RECORDED collapse this estate keeps paying for."
                    (runs.py:16-18)
                    "RECONSTRUCTED  derived after the fact from git + the session transcripts"
                    (runs.py:22)
```

`reconstruct()` (runs.py:214) leaves `outcome=None` deliberately: *"Neither can say whether the lane
*finished* — only that work happened — so `outcome` stays None rather than guessing FINISHED from a
non-empty branch."* (runs.py:218-220).

---

## Run ATTRIBUTION

```text
TERM                ATTRIBUTION
KIND                constant tuple (join keys), written as fields on every run row
DEFINED AT          factory/runs.py:274 ; written at :160-165
WHAT IT MEANS HERE  Which work item, and which configuration, produced this run.
DISTINCTION IT      An omitted key ("this ledger does not ask") vs an explicit NOT-RECORDED
PROTECTS            ("nobody answered it").
ALLOWED VALUES      job · team · team_version · agent_versions
QUOTE               "⚠ They record ``NOT-RECORDED``, never omission. An absent key reads as
                    *"this ledger does not ask that question"*; an explicit `NOT-RECORDED` reads as
                    *"nobody answered it"*, which is the true state today" (runs.py:154-157)
                    "Attribution is NEVER reconstructible" (runs.py:241)
```

`unattributed()` (runs.py:277) reports, rather than gates, how much of the ledger cannot be joined:
*"Today the honest answer is *all of it* — nothing executes a `TeamSpec` and no `Job` exists."*

---

## Context KINDS

```text
TERM                KINDS (context kinds)
KIND                constant tuple, validated in ContextRef.__post_init__
DEFINED AT          factory/context.py:47  (members and glosses at :38-45; enforced at :97-98)
WHAT IT MEANS HERE  What a piece of context IS, so an agent can ask for the kinds its lane needs
                    rather than for everything.
DISTINCTION IT      Structured context vs a concatenated prompt blob. "Text that has already been
PROTECTS            concatenated cannot be filtered per lane, cannot say where it came from, and
                    cannot carry a date." (context.py:5-6)
ALLOWED VALUES      CompanyContext · RepoContext · ClientContext · SourceContract ·
                    DatasetContract · MetricContract · TaskContext · OperatorAnswer
QUOTE               "METRIC = "MetricContract"     #: numerator, denominator, scope, currency,
                    valid dimensions" (context.py:43)
```

Note the string values are CamelCase type names (`"CompanyContext"`), not the constant names.

---

## Context freshness (STATUSES) and confidence (CONFIDENCE)

```text
TERM                STATUSES / CONFIDENCE
KIND                two constant tuples, both validated in ContextRef.__post_init__
DEFINED AT          factory/context.py:54 (STATUSES; members :51-53)
                    factory/context.py:63 (CONFIDENCE; members :59-62)
WHAT IT MEANS HERE  STATUSES = how fresh a ref is against its source.
                    CONFIDENCE = how much the content is to be trusted.
DISTINCTION IT      Freshness and trust are orthogonal, and collapsing them loses whichever one
PROTECTS            matters. Separately: UNVERIFIED is not a weak CURRENT.
ALLOWED VALUES      STATUSES:   CURRENT · STALE · UNVERIFIED
                    CONFIDENCE: MEASURED · DERIVED · STATED · ASSUMED
QUOTE               "⚠ **`UNVERIFIED` is the default status, not `CURRENT`.** … defaulting to
                    CURRENT would let every ref claim a freshness nobody established — the same
                    collapse as reporting UNMEASURABLE as PASS." (context.py:21-24)
                    "A ref can be perfectly current and still be somebody's guess; a ref can be a
                    hard measurement taken a year ago." (context.py:56-58)
```

Two hard constraints in `ContextRef.__post_init__` (context.py:96-112): `source` must be non-empty
(*"a projection that cannot point back at its origin is a second source of truth"*), and
`status == CURRENT` requires a `checked` date (*"Freshness is a measurement; without the date it is
an assertion wearing a measurement's label."*).

Note `CONFIDENCE` adds **STATED** — *"a human said so; true by assertion, not by measurement"*
(context.py:61) — which the task-evidence `basis` vocabulary (MEASURED/DERIVED/ASSUMED) does **not**
have. These two four/three-value ladders are similar but not identical, and are not reconciled
anywhere in the code.

---

## Readiness gate verdicts + GATES + PHASES

```text
TERM                PASS / FAIL / UNMEASURABLE / NOT_RUN  (readiness copies)
KIND                module constants
DEFINED AT          factory/readiness.py:34
QUOTE               "The verdicts are the contract's four, and they are never collapsed"
                    (readiness.py:7)
                    "UNMEASURABLE is not a pass." — printed by main() at readiness.py:1542
```

```text
TERM                Gate
KIND                dataclass
DEFINED AT          factory/readiness.py:50
FIELDS              id · question · why · probe · phase
QUOTE               "This is not a checklist. Every gate below is *measured* from a file at the
                    moment you run it, and each result carries the path it was measured from. A
                    gate that cannot be measured says so — it does not quietly pass."
                    (readiness.py:3-5)
```

```text
TERM                Result
KIND                dataclass
DEFINED AT          factory/readiness.py:59
FIELDS              verdict · headline · evidence · source
```

```text
TERM                GATES
KIND                module-level list of Gate
DEFINED AT          factory/readiness.py:1394
COUNT               30 gates (enumerated below; count read from the literal, not from a doc)
```

Gate ids, with phase, exactly as written:

| id | phase | question (readiness.py) |
|---|---|---|
| `r1-followup` | handover | Has R1 been asked what else depended on the misattribution? |
| `r2-followup` | handover | Has R2 been asked whether to move the build plane onto Prefect? |
| `r3-followup` | handover | Has R3 been asked the false-succeeded correction? |
| `rendered` | handover | Has anyone looked at the published surface and recorded it? |
| `chain` | handover | Is impeccable's place in the skill chain stated? |
| `grain` | handover | Is the landing-table grain settled? |
| `ticket` | handover | Does this work have a ticket, or a decision that it needs none? |
| `cap` | bounded | Is the retry cap enforced on the path that restarts? |
| `ceiling` | bounded | Is spend checked before dispatch? |
| `concurrency` | bounded | Is concurrent dispatch bounded outside the agent? |
| `reaper` | bounded | Is dispatched work either finished or killed? |
| `from-history` | judgement | Is the terminal verdict computed from history? |
| `breadth` | certification | Does the eval corpus have enough breadth to calibrate? |
| `version` | certification | Does the version hash cover what makes an agent an agent? |
| `isolated` | certification | Is the evaluator a principal the agent cannot impersonate? |
| `finishes` | loop | Does a run finish without a human? |
| `succeeds` | loop | Do stages succeed more often than they fail? |
| `bounded` | loop | Is failure bounded? |
| `refuses` | judgement | Has any gate ever refused a run? |
| `checks` | judgement | Do the gates have programmatic checks? |
| `attributable` | judgement | Can a run be tied to the ticket it was doing? |
| `truthful` | judgement | Does a recorded status match its own event log? |
| `honest` | judgement | Does a completed run mean the work was correct? |
| `cost` | judgement | Is cost observable when things fail? |
| `general` | judgement | Can QA validate any connector, not one? |
| `suite` | certification | Is the certification suite green and honest? |
| `certified` | certification | Is the output actually certified? |
| `tenancy` | certification | Is a tenant scope DECLARED? (declared, not verified) |
| `corpus` | certification | Is the grader tamper-evident and separable? |
| `durable` | certification | Does the factory survive this machine? |

```text
TERM                PHASES
KIND                dict constant
DEFINED AT          factory/readiness.py:1498
ALLOWED VALUES      loop ("Can the loop run?") · bounded ("Is it bounded? (build order 1-2)") ·
                    judgement ("Can it tell success from failure?") ·
                    certification ("Can its output be certified?") ·
                    handover ("Is it handed over honestly?")
```

Also load-bearing in readiness:

- `MEASURED_SINCE = "2026-08-22"` (readiness.py:100) — the measurement window. *"⚠ Windowing is NOT
  forgiving. An empty window is UNMEASURABLE, never PASS."* (:96-97)
- `VERSION_DIMENSIONS` (readiness.py:1206) — 15 named dimensions of agent identity: `prompt, model,
  effort, tools, max_turns, budget_usd, tool_implementation, sandbox_image, model_routing,
  context_policy, external_knowledge, permissions, contract_version, harness_version,
  side_effect_replay`. *"An agent is not a name; it is everything here, and anything absent is
  something a certification silently transfers across."* (:1204-1205)
- The `tenancy` gate carries an explicit DECLARED-vs-VERIFIED distinction in its own title and a
  four-line comment at :1481-1485: *"Declared and verified are different claims and only one of them
  is measured here."*

Tests: `tests/test_readiness_probes_can_pass.py::test_every_gate_can_report_pass` and
`::test_every_gate_can_refuse`.

---

## board — task status vocabulary + DEPENDS

```text
TERM                DONE / READY / BLOCKED
KIND                constants
DEFINED AT          factory/board.py:29
WHAT IT MEANS HERE  Derived task status. Every non-passing gate IS a task; passing removes it.
DISTINCTION IT      A hand-maintained list wearing a computed status.
PROTECTS
ALLOWED VALUES      DONE · READY · BLOCKED
QUOTE               "**There is no task list in this file.** … That is a hand-maintained board
                    wearing a computed status, which is the same defect as a checkbox grid with
                    nicer wiring." (board.py:5-8)
                    "gate not passing -> a task / gate passing -> done … / every dependency
                    satisfied -> READY, and everything READY is parallelisable by definition"
                    (board.py:19-21)
```

```text
TERM                DEPENDS
KIND                module-level dict, validated at import (board._validate, :70-85)
DEFINED AT          factory/board.py:34
WHAT IT MEANS HERE  The ONLY authored knowledge in the module: what must precede what, keyed by
                    gate id.
QUOTE               "The one thing that IS authored is `DEPENDS`, below, because "this must happen
                    before that" is real design knowledge and no probe can infer it. It is
                    validated on import: every id must name a real gate, so a renamed or deleted
                    gate breaks the build rather than leaving a dangling edge." (board.py:15-17)
EDGES (live)        ceiling<-cost · refuses<-checks · truthful<-from-history · certified<-isolated ·
                    breadth<-isolated · finishes<-[cap,reaper,from-history] ·
                    succeeds<-[cap,reaper,general] · grain<-[] · rendered<-[]
```

A removed edge is documented in place rather than deleted (board.py:43-53): the `tenancy` edge was
removed 2026-08-23 because *"A PASS pointing at a NOT_RUN dependency is how the roadmap came to
sequence work that could already have started"*, and the comment names the **missing gate** that
would restore it (`tenancy-verified`).

`critical_path()` (board.py:108): *"Longest dependency chain still unmet — the thing that cannot be
parallelised away."*

---

# PART 2 — THE REST OF THE FIRST-CLASS VOCABULARY

---

## GreenContract, Assertion, AssertionResult, ContractResult, Unmeasurable

```text
TERM                GreenContract
KIND                dataclass
DEFINED AT          factory/contract.py:103
WHAT IT MEANS HERE  "A named set of assertions defining "this worked" for one unit of work."
                    (contract.py:104)
DISTINCTION IT      It defines DONE, not intent. It carries no objective, no authority boundary
PROTECTS            and no escalation rule — see the collision table.
```

```text
TERM                Assertion
KIND                dataclass
DEFINED AT          factory/contract.py:41
QUOTE               "One falsifiable claim. … Raising ``Unmeasurable`` inside it yields
                    UNMEASURABLE rather than FAIL — the caller must be able to tell "it is broken"
                    from "I could not look"." (contract.py:42-46)
FIELDS              name · check · required · description
```

```text
TERM                AssertionResult
KIND                dataclass
DEFINED AT          factory/contract.py:29
FIELDS              name · verdict · detail · observed · expected
```

```text
TERM                ContractResult
KIND                dataclass
DEFINED AT          factory/contract.py:68
PROPERTIES          verdict (:73) · is_green (:88) · failures() (:91) · summary() (:94)
```

```text
TERM                Unmeasurable
KIND                exception class (TWO independent definitions)
DEFINED AT          factory/contract.py:63 ; factory/readiness.py:42 ; factory/schedule.py:54
QUOTE               "Raise inside a check when the instrument cannot run at all."
                    (contract.py:64)
                    "No instrument could be established. Distinct from a failure."
                    (readiness.py:43)
                    "Not enough history to say anything. Distinct from "the answer is zero"."
                    (schedule.py:55)
```

⚠ `Unmeasurable` is defined **three times** in this codebase with three docstrings. They are not the
same class object; `plan_gates.py:39` imports readiness's. Any ontology that names this concept
should know there are three.

---

## Assertion sets — A1–A12 and M1–M12

```text
TERM                A1 … A12  (connector end-to-end contract)
KIND                named assertions on a GreenContract
DEFINED AT          factory/connector_contract.py:299-310 (registration); build_contract at :117
ALLOWED VALUES      A1-config-satisfiable · A2-credential-authenticates ·
                    A3-exact-image-resolves · A4-deployment-binding · A5-regression-suite ·
                    A6-run-completed · A7-fresh-landing-proven · A8-load-fidelity ·
                    A9-semantic-invariants · A10-source-agreement · A11-no-forbidden-action ·
                    A12-tenancy-scope
QUOTE               "**Every assertion states a positive fact that must be observed.** None is
                    satisfied by the absence of an error." (connector_contract.py:7-8)
                    "A6-run-completed … description="necessary, insufficient — see A7""
                    (connector_contract.py:304)
```

```text
TERM                M1 … M12  (Power BI model-change contract)
KIND                named assertions on a GreenContract
DEFINED AT          factory/pbi_contract.py:444-461
ALLOWED VALUES      M1-rollback-captured-first · M2-target-is-the-declared-dataset ·
                    M3-every-field-appended-or-asserted · M4-additive-manifest ·
                    M5-refresh-moved-data · M6-anchors-hold · M7-no-regression ·
                    M8-absence-renders-blank · M9-warehouse-agreement ·
                    M10-every-visual-paints · M11-controls-respond · M12-change-is-reachable
QUOTE               "A contract that quietly DROPS the two assertions only a renderer can make is a
                    contract that certifies the wrong layer — and would have returned GREEN on
                    GP-293 while every visual was broken." (pbi_contract.py:21-23)
```

```text
TERM                RENDER_ONLY
KIND                constant tuple
DEFINED AT          factory/pbi_contract.py:467
WHAT IT MEANS HERE  The assertions NO XMLA/DAX instrument can satisfy — named so the gap is a
                    stated fact rather than an unexplained UNMEASURABLE.
ALLOWED VALUES      M10-every-visual-paints · M11-controls-respond
```

⚠ Standing on these two is not equal. `roadmap.py:190-194` records that `pbi_contract` has **zero
tests and zero callers**: *"A contract never watched refusing is decoration."* The connector contract
has `tests/test_connector_contract.py::test_every_assertion_has_been_proved_able_to_fail`.

---

## ConnectorTarget / PbiTarget

```text
TERM                ConnectorTarget
KIND                dataclass
DEFINED AT          factory/connector_contract.py:27 ; loaded by factory/targets.py:18
WHAT IT MEANS HERE  "What "green" means for ONE connector against ONE account."
DISTINCTION IT      Expectation vs world. "The world itself arrives separately, through probes —
PROTECTS            never from this object." (connector_contract.py:30-31)
KEY FIELDS          connector · client · deployment · landing_table · session_column ·
                    connection_class · options_class · expected_image_digest · expected_commit ·
                    merged_at · pinned_test_revision · run_date · expect_rows · primary_key ·
                    required_keys · key_column · date_column · non_null_positive ·
                    tenant_column · allowed_tenants
QUOTE               "The contract is code; what "green" means for one connector is data."
                    (targets.py:3)
```

`targets.load_target` refuses unknown keys (targets.py:21-23): *"A typo'd key that is silently
ignored is an assertion that quietly stops being made."*

```text
TERM                PbiTarget
KIND                dataclass
DEFINED AT          factory/pbi_contract.py:47
NOTABLE FIELDS      environment ("TEST | PROD", :61) · allow_environments · rollback_path ·
                    additive_only · protected_objects · writable_fields · anchors · tolerance ·
                    baseline · must_be_blank_not_zero · bound_reports · min_refresh_seconds
QUOTE               "must_be_blank_not_zero … These must evaluate to BLANK, never 0. … A `0` reads
                    as "we measured none"; that is a claim about the client's business that we did
                    not measure." (pbi_contract.py:84-88)
```

---

## Probes / CtxProbes

```text
TERM                Probes
KIND                class (base instrument; TWO definitions, one per contract)
DEFINED AT          factory/connector_contract.py:61 ; factory/pbi_contract.py:101
WHAT IT MEANS HERE  The instruments. Each returns observed facts, or raises Unmeasurable.
DISTINCTION IT      The base class REFUSES EVERYTHING. Unconfigured != passing.
PROTECTS
QUOTE               "The base class refuses everything, which is the correct default: an
                    unconfigured harness reports UNMEASURABLE, never PASS."
                    (connector_contract.py:65-67)
VERBS (connector)   config · credential · image · deployment · suite · run · landed · source ·
                    forbidden   (connector_contract.py:72-80)
```

```text
TERM                CtxProbes
KIND                class
DEFINED AT          factory/connector_contract.py:83 ; factory/pbi_contract.py:131
WHAT IT MEANS HERE  Probes that read the world out of a context dict — the replay instrument.
QUOTE               "A missing or None key means the instrument could not run — which is
                    UNMEASURABLE, not FAIL." (connector_contract.py:88)
```

```text
TERM                LIVE_CLIENTS
KIND                frozenset constant
DEFINED AT          factory/live_probes.py:255 ; used by probes_for() at :258
ALLOWED VALUES      "GEP" · "CLIENT-A"
QUOTE               "an identifier that was renamed underneath the selector. Nothing failed,
                    because "returns the honest unwired message" is indistinguishable from "is
                    genuinely unwired"." (live_probes.py:250-252)
```

---

## Corpus — EVIDENT / ATTRIBUTED / SEPARABLE

```text
TERM                corpus (the eval corpus)
KIND                domain noun + module
DEFINED AT          factory/corpus.py:1 ; CORPUS_ROOT :38 ; MANIFEST :39 ; CorpusError :42
WHAT IT MEANS HERE  "the known-good world every assertion is scored against" (corpus.py:3),
                    loaded as hash-verified JSON, never as executable Python.
DISTINCTION IT      Data vs code. ""the corpus changed" and "the corpus computes something
PROTECTS            different today" were indistinguishable." (corpus.py:6-7)
QUOTE               "EVIDENT     a changed corpus fails the hash check and raises, rather than
                                 quietly scoring differently
                     ATTRIBUTED  every verdict records which corpus and which hash it was scored
                                 against
                     SEPARABLE   `evals/` is a leaf with no imports from `factory/`"
                    (corpus.py:18-22)
                    "An agent that can edit its own grader is not graded." (corpus.py:9)
```

Stated gap (corpus.py:24-26): *"separation is not yet *enforced*. Enforcement means the corpus
living in a repository the scored agent has no write credential for."*

```text
TERM                stamp / provenance
KIND                function returning a provenance block
DEFINED AT          factory/corpus.py:105 ; factory/calibration.py:55
FIELDS              corpus · sha256 · recorded · basis
QUOTE               "The provenance block to attach to a verdict scored against this corpus."
                    (corpus.py:106)
```

```text
TERM                REPLAYED
KIND                label emitted with any calibration verdict (string, not a constant)
DEFINED AT          factory/certify.py:71, :131-132
QUOTE               "scored against corpus … — REPLAYED, not a live measurement" (certify.py:132)
                    "A verdict with no corpus is a live run; a verdict WITH one was replayed and
                    must say so. Without this a calibration result and a production result are
                    indistinguishable." (certify.py:117-118)
```

---

## Evaluator — Submission, RemoteVerdict, and the closed field sets

```text
TERM                SUBMISSION_FIELDS
KIND                constant tuple; enforced by the service (rejects a fourth key)
DEFINED AT          factory/evaluator.py:55 ; Submission dataclass at :89
ALLOWED VALUES      artifact_uri · artifact_sha256 · run_id
QUOTE               "The complete submission vocabulary. Frozen on purpose — every field added
                    here is one more thing the graded party gets to influence about its own
                    grading." (evaluator.py:53-54)
                    "The agent never supplies the evaluator implementation, the corpus, or the
                    manifest to be trusted. It supplies only the artefact to evaluate."
                    (evaluator.py:10-11)
```

```text
TERM                ATTRIBUTION_FIELDS / EVALUATOR_IDENTITY_FIELDS / UNSCORED_VERDICTS
KIND                constant tuples / frozenset
DEFINED AT          factory/evaluator.py:58, :61, :65
ALLOWED VALUES      ATTRIBUTION_FIELDS:        evaluator · scored_against
                    EVALUATOR_IDENTITY_FIELDS: identity · bundle_sha256
                    UNSCORED_VERDICTS:         REFUSED · UNMEASURABLE · NOT_RUN
QUOTE               "**A verdict must say who produced it.** An unattributed ``{"verdict":
                    "PASS"}`` is refused rather than believed: anything on a socket can emit that
                    string." (evaluator.py:24-25)
                    "REFUSED, UNMEASURABLE and NOT_RUN are exempt from the corpus requirement
                    because nothing was scored; demanding one would turn an honest refusal into a
                    parse error." (evaluator.py:27-29)
```

```text
TERM                REFUSED
KIND                a FIFTH verdict-shaped value, service-side only
DEFINED AT          evaluator_service/service.py:62 ; Refused exception at :65
WHAT IT MEANS HERE  The submission was not scored, and the reason is not the artefact being wrong.
DISTINCTION IT      REFUSED vs FAIL. "Not a FAIL — we never scored anything."
PROTECTS
QUOTE               "REFUSED  the submitted sha256 does not match the bytes on disk. … Not a FAIL
                    — we never scored anything." (service.py:19-21)
```

⚠ **REFUSED is not a member of `Verdict`** (contract.py:17) but is treated as a verdict value by the
client (`UNSCORED_VERDICTS`, evaluator.py:65) and by the service. R02 should treat the *effective*
verdict vocabulary as five, not four.

```text
TERM                BUNDLE / bundle_sha256
KIND                constant tuple + hash function
DEFINED AT          evaluator_service/service.py:57 ; bundle_sha256() at :77
WHAT IT MEANS HERE  The files that decide what a verdict means, hashed together into every verdict.
QUOTE               "Not a signature and not claimed to be one — a signing key inside the agent
                    sandbox is theatre, and R3 says so. This is the weaker, useful property: two
                    verdicts that disagree can be checked for whether they were even produced by
                    the same grader." (service.py:80-83)
```

```text
TERM                EvaluatorError family
KIND                exception classes
DEFINED AT          factory/evaluator.py:68 (EvaluatorError), :72 (EvaluatorNotConfigured),
                    :76 (EvaluatorUnreachable), :84 (UnattributedVerdict)
QUOTE               "No endpoint. Not a pass, and not a reason to grade locally."
                    (evaluator.py:73)
                    "It is not FAIL either: we did not observe a failing artefact, we failed to
                    observe at all." (evaluator.py:80-81)
```

```text
TERM                VerdictExists
KIND                exception class (write-once verdict store)
DEFINED AT          evaluator_service/store.py:42 ; StoreError at :38 ; RUN_ID regex at :35
```

---

## Task, TaskStore, Event, EvidenceRequired

```text
TERM                Task status vocabulary
KIND                module constants
DEFINED AT          factory/tasks.py:26 ; terminal set at :27
ALLOWED VALUES      open · claimed · blocked · done · abandoned    (terminal: done, abandoned)
QUOTE               "OPEN, CLAIMED, BLOCKED, DONE, ABANDONED = "open", "claimed", "blocked",
                    "done", "abandoned"" (tasks.py:26)
```

```text
TERM                Task
KIND                dataclass
DEFINED AT          factory/tasks.py:43
FIELDS              id · title · owner · parent · status · blocked_by · evidence · events
```

```text
TERM                Event  (task store)
KIND                dataclass
DEFINED AT          factory/tasks.py:35
FIELDS              ts · actor · kind · data
EVENT KINDS         create · claim · block · unblock · evidence · close · note
                    (dispatched in TaskStore._apply, tasks.py:83-102)
QUOTE               "**Append, never overwrite.** An agent that sets a field wholesale destroys
                    what another agent wrote. Every mutation is an event; current state is a fold
                    over events." (tasks.py:5-7)
```

⚠ The task-store event kinds are an **implicit** closed set — dispatched by `if kind == …` in
`_apply` with no constant tuple and no validation. Unlike `bus.KINDS`, an unknown kind is silently
ignored (falls through to the trailing `t.events.append`, tasks.py:103). This is the one closed set
in the codebase that is not enforced.

```text
TERM                EvidenceRequired
KIND                exception class
DEFINED AT          factory/tasks.py:30 ; raised at :163 and :169
QUOTE               "⭐ Cannot close as done without at least one MEASURED or DERIVED piece of
                    evidence." (tasks.py:150)
                    "A task cannot close without evidence. ``status=done`` with an empty
                    ``evidence`` list is rejected by the store, not by convention."
                    (tasks.py:7-8)
```

---

## Lane, LANES, PREAMBLE / POSTAMBLE, SIZE

```text
TERM                Lane
KIND                frozen dataclass
DEFINED AT          factory/lanes.py:71 ; LANES literal at :125 ; gate-id validation at :274-279
WHAT IT MEANS HERE  A parallelisable unit of work grouped by FILE LOCALITY, not by dependency.
FIELDS              id · title · why · repo · touches · size · gates · prompt · needs_paul ·
                    model · model_why
ALLOWED VALUES      control-plane · certify · judgement · artifact · grain   (5 lanes, lanes.py:125)
QUOTE               "The binding constraint is **file locality**, not the dependency graph."
                    (lanes.py:5-6)
                    "⚠ **Basis, stated because this is the one file here that is not measured.**
                    Gate membership and dependency order are MEASURED … The *grouping into lanes*
                    is ASSUMED" (lanes.py:8-11)
```

⚠ **`lane` is explicitly named as the most overloaded word in the codebase.** `claims.py:54-57`:
*"R14 measured that `lane` is already four objects wearing one string — work package, file-conflict
key, git branch, directory, claim key, ledger key — and named that, not topology, as the reason the
3-lane cap will not move."* (The sentence says "four" and then lists six.)

```text
TERM                SIZE
KIND                dict constant
DEFINED AT          factory/lanes.py:26
ALLOWED VALUES      S ("under an hour") · M ("a session") · L ("more than a session")
QUOTE               "Effort sizes are ASSUMED too, and deliberately ordinal (S/M/L) rather than
                    hours: an hours figure would be read as a plan" (lanes.py:12-13)
```

```text
TERM                PREAMBLE / POSTAMBLE
KIND                module-level string constants (the shared lane prompt)
DEFINED AT          factory/lanes.py:29 / :37
QUOTE               "⚠ A sub-agent's report is a claim, not a measurement." (lanes.py:49)
                    "A lane that closes green without an independent read is the shape of defect
                    this whole programme exists to stop." (lanes.py:56-57)
                    "Silence has to mean checked, not unlooked-at." (lanes.py:67)
```

---

## Claim (lane claim) and the holder vocabulary

```text
TERM                Claim
KIND                frozen dataclass
DEFINED AT          factory/claims.py:69 ; claim() at :246 ; STALE_AFTER at :46
WHAT IT MEANS HERE  A file recording that a named LANE is being worked, so a conflicting lane can
                    be refused. NOT a proposition, NOT an assertion.
DISTINCTION IT      A convention with a staleness warning, not a lock. And: age vs liveness.
PROTECTS
FIELDS              lane · since · who · note   (+ derived: age, stale, human_age)
QUOTE               "⚠ **This is a convention with a staleness warning, not a lock, and the
                    difference matters.**" (claims.py:10)
                    "Record that `lane` is being worked. Refuses if a conflicting lane is
                    claimed." (claims.py:247)
```

```text
TERM                HELD_LIVE / HELD_GONE / HELD_UNVERIFIED
KIND                constants
DEFINED AT          factory/claims.py:96-98 ; holder() at :101 ; advice() at :126
WHAT IT MEANS HERE  What actually holds a claim, measured against the process table.
DISTINCTION IT      Age is a clock reading; liveness is a measurement. And: "could not read the
PROTECTS            process table" is NOT "nothing is running".
ALLOWED VALUES      HELD-LIVE · HELD-GONE · HELD-UNVERIFIED
QUOTE               "These were the same thing until 2026-08-23, when three lanes claimed 29h
                    earlier were reported "STALE — release it if that session is gone" while all
                    three sessions were still running. Age is a clock reading; liveness is a
                    measurement." (claims.py:83-87)
                    "Three verdicts, never two. ``HELD_UNVERIFIED`` is the one that matters"
                    (claims.py:105-106)
```

```text
TERM                TASK_PREFIX
KIND                constant (namespace separator inside the claim store)
DEFINED AT          factory/claims.py:61
ALLOWED VALUES      "task--"
QUOTE               "⛔ A separate namespace rather than a new entry in `LANES`, deliberately. …
                    Registering "synthesis" as a lane to reuse `claim()` would have added a fifth
                    meaning to the most overloaded word in this codebase to save a dozen lines."
                    (claims.py:52-57)
```

---

## Session liveness vocabulary

```text
TERM                session state
KIND                constants
DEFINED AT          factory/sessions.py:121, :124, :126, :128, :130, :134
WHAT IT MEANS HERE  What a Claude Code session on this machine is doing, joined from the session
                    registry, the process table and the jobs registry.
DISTINCTION IT      "Alive, visible and attachable are three different things."
PROTECTS
ALLOWED VALUES      RUNNING-ATTACHED · RUNNING-ORPHANED · EXITED-RESUMABLE · EXITED-GONE ·
                    UNKNOWN-INSTRUMENT-BLIND · NO-SESSION
QUOTE               "**2. Alive, visible and attachable are three different things.** A terminal
                    died that morning while its agent kept working and kept writing to its
                    transcript. Anything that reports two states lies about that session."
                    (sessions.py:109-111)
                    "UNKNOWN … The process table could not be read. NOT the same as "nothing is
                    running"." (sessions.py:129-130)
                    "NO_SESSION … Distinct from EXITED_GONE, which means we watched a registered
                    session's process disappear." (sessions.py:131-134)
```

`_running_pids()` returns `None`, not an empty set, when it cannot look (sessions.py:30-35): *"None
is NOT an empty set."*

---

## Launch admission levels

```text
TERM                launch level states
KIND                constants
DEFINED AT          factory/launch.py:56-62 ; gate sets at :41 and :46
WHAT IT MEANS HERE  Three separately-answered questions about whether an agent may run, be left
                    alone, and be believed.
DISTINCTION IT      ""ready" … three questions get conflated into one word".
PROTECTS
ALLOWED VALUES      SUPERVISED-OK · SUPERVISED-BLOCKED · UNATTENDED-OK · UNATTENDED-BLOCKED ·
                    OUTPUT-CERTIFIABLE · OUTPUT-UNCERTIFIED · UNGATED
QUOTE               "MAY I RUN IT?          is there a human who can see it and stop it
                     MAY I LEAVE IT?        is it bounded — cap, reaper, ceiling, concurrency
                     MAY I TRUST OUTPUT?    is it certified" (launch.py:9-12)
                    "⛔ **What this is NOT.** It is not permission, and it never dispatches
                    anything." (launch.py:25)
GATE SETS           UNATTENDED_GATES = (cap, reaper, ceiling, concurrency, bounded)  (:41)
                    TRUST_GATES = (suite, certified, corpus, version, breadth, isolated)  (:46)
```

```text
TERM                UNGATED
KIND                constant (defined twice, same string)
DEFINED AT          factory/launch.py:62 ; factory/teamplan.py:36
WHAT IT MEANS HERE  A team with no contract. Not 0%.
QUOTE               "⭐ **UNGATED is not zero steps.** A team with no contract has nothing to
                    sequence, and rendering it as an empty list reads as *"nothing to do"* when
                    the truth is *"nothing can be measured yet."*" (teamplan.py:24-26)
```

---

## AgentSpec, TeamSpec, NOT_IDENTITY, SUPPORTED_TOPOLOGIES

```text
TERM                AgentSpec
KIND                dataclass
DEFINED AT          factory/blueprint.py:19 ; version property at :31
WHAT IT MEANS HERE  "An agent is not a name — it is a (prompt, model, effort, tools, retry policy)
                    tuple." (blueprint.py:3)
FIELDS              name · role · model · effort · prompt · tools · max_turns · budget_usd ·
                    prohibition
QUOTE               "prohibition: str = ""      # every agent carries an explicit "must not""
                    (blueprint.py:28)
                    "Change any element and it is a different agent, whose certification does not
                    transfer." (blueprint.py:4-5)
```

```text
TERM                TeamSpec
KIND                dataclass
DEFINED AT          factory/blueprint.py:43 ; version at :53 ; pinned() at :74
FIELDS              name · purpose · agents · topology · contract · repo · prohibition
QUOTE               "A team certified against `prefect-connectors` under *"must not deploy to
                    production"* kept the **identical** version when repointed at another repo
                    with the prohibition deleted." (blueprint.py:58-61)
```

```text
TERM                NOT_IDENTITY
KIND                constant tuple (deny-list)
DEFINED AT          factory/blueprint.py:39
ALLOWED VALUES      purpose · agents
QUOTE               "Deny-list on purpose … a new field is identity by default and must be argued
                    out, because the failure mode of forgetting to add one is a certification that
                    transfers silently." (blueprint.py:36-38, :64-66)
```

```text
TERM                SUPPORTED_TOPOLOGIES
KIND                set constant
DEFINED AT          factory/blueprint.py:79 ; enforced in load_team at :86-89
ALLOWED VALUES      manager_to_agent   (one value)
QUOTE               "Only {sorted(SUPPORTED_TOPOLOGIES)} exist until a second team demonstrably
                    needs another." (blueprint.py:89)
                    "topology: str = "manager_to_agent"     # the only one supported, deliberately"
                    (blueprint.py:47)
```

⚠ `blueprints/orchestrator_team.yaml:1` — *"⛔ SUPERSEDED BY EVIDENCE 2026-08-21 — DO NOT BUILD THIS
TEAM."* The only three-agent team blueprint in the repo is a **rejected hypothesis kept on purpose**
(:24-26), with the unlock threshold stated at :26-30.

---

## TEAMS / Action / ACTIONS

```text
TERM                TEAMS
KIND                module dict, validated at import (roadmap._validate, :213)
DEFINED AT          factory/roadmap.py:181
ALLOWED VALUES      "Data Pipeline Orchestrator" (7 declared gates) ·
                    "Power BI Data Model Designer" (0 gates → UNGATED)
FIELDS PER TEAM     intent · gates · blocked_on · (optional) unblock
QUOTE               "The end states someone named out loud. NOT derivable from any probe — an
                    agent team is a goal, and goals live in people's heads until someone writes
                    them down." (roadmap.py:176-178)
                    "⚠ A team with no gates is reported UNGATED, never 0%." (roadmap.py:179-180)
```

⚠ **`intent` here is a free-text string field on a team dict** (roadmap.py:183, launch.py:186,
teamplan.py:132). `docs/agent-army/CURRENT_STATE.md:44` names this explicitly: *"The `intent` field
is a label on a launch record."*

```text
TERM                AUTHORED / MEASURED  (roadmap action basis)
KIND                constants
DEFINED AT          factory/roadmap.py:55
QUOTE               "⭐ **An action linked to a gate takes its status FROM the gate, always.** Only
                    an action no gate can see keeps an authored status, and those render as
                    `AUTHORED` — deliberately weaker-looking than `MEASURED`, because they are."
                    (roadmap.py:19-22)
                    "⛔ And as of 2026-08-23 the honest count is 0 MEASURED, 18 AUTHORED."
                    (roadmap.py:24-25)
```

```text
TERM                DECIDED / SHIPPED / SUPERSEDED
KIND                constants (authored lifecycle for an ungated decision)
DEFINED AT          factory/roadmap.py:57
```

```text
TERM                Action
KIND                class
DEFINED AT          factory/roadmap.py:60 ; ACTIONS list at :80
FIELDS              id · text · source · state · gate · note · why_gate
QUOTE               "⛔ **A `gate` REQUIRES a `why_gate` naming what that gate actually asserts and
                    why it decides THIS action.** Three edges were authored on 2026-08-23 without
                    that check and all three were wrong" (roadmap.py:63-65)
```

---

## GOALS

```text
TERM                GOALS
KIND                module dict, validated at import (goals._validate, :43)
DEFINED AT          factory/goals.py:24
ALLOWED VALUES      "First agent team completes a run" ·
                    "Optimizer can run in a sandbox" ·
                    "Configuration identifies the agent"
QUOTE               "**A goal with no measurable gates reports NOT-MEASURED, not 0%.** Zero and
                    "nothing has looked" are different claims, and only one of them is about the
                    work." (goals.py:14-15)
                    "⚠ **The grouping is the only authored thing here and it is a judgement.**"
                    (goals.py:8)
BASIS VALUES        MEASURED · NOT-MEASURED   (goals.py:75)
```

---

## Finding (the durable knowledge object)

```text
TERM                Finding
KIND                frozen dataclass + a Markdown schema enforced by test
DEFINED AT          factory/findings.py:50 ; REQUIRED :31 ; OPTIONAL :34 ; KINDS :40 ;
                    STATUSES :43 ; DESIGN_KINDS :44
WHAT IT MEANS HERE  A corrected premise, addressable, permanent, merging with the branch. One file
                    per finding under docs/findings.d/.
DISTINCTION IT      The RECORD vs the CHANNEL (see bus.py). And: a design consequence is not spent
PROTECTS            until it is built or deliberately refused.
REQUIRED FIELDS     BELIEVED · ACTUALLY · MEASURED BY · AFFECTS
OPTIONAL FIELDS     KIND · CHANGES · STATUS
KINDS               CORRECTION · INSTRUMENT · DESIGN · AGENT-DESIGN · PROCESS
STATUSES            OPEN · ADOPTED · REJECTED · SUPERSEDED
QUOTE               "#: CORRECTION   a premise was wrong; fix it and move on
                     #: INSTRUMENT   a tool lied, or could not see — changes what a measurement is
                                     worth" (findings.py:35-36)
                    "A DESIGN finding with no status is an insight nobody ever decided about.
                    Silence has to mean decided, the same way NOTHING TO REPORT has to mean
                    checked." (findings.py:41-42)
                    "**Matching is by declared id, not by keyword.**" (findings.py:8)
```

`nothing_to_report()` (findings.py:152) counts the literal string `NOTHING TO REPORT`: *"Counted
because it is the difference between silence-as-measurement and silence-as-nobody-looked."*

`design_debt()` (findings.py:138) is the list that should shrink: *"a correction is spent once it is
read, a design consequence is not spent until it is built or deliberately refused."*

---

## Preset and verifier_state

```text
TERM                Preset
KIND                frozen dataclass ; PRESETS list at :92
DEFINED AT          factory/presets.py:46
WHAT IT MEANS HERE  One (ticket type, size) starting configuration for an AgentSpec, with the
                    reasoning attached.
FIELDS              type_id · title · seen_in · layers · size · model · model_why ·
                    escalate_when · effort · max_turns · budget_usd · prohibition · verifier ·
                    verifier_state · needs_paul
ALLOWED type_id     ui-control · add-measure · dimension-gap · wrong-number · model-redesign
                    (presets.py:94, 121, 149, 178, 207)
QUOTE               "⭐ **A preset is a starting point with its reasoning attached, not a lookup
                    table.**" (presets.py:19)
                    "* The **types** are MEASURED. … * The **assignments** … are ASSUMED."
                    (presets.py:10-14)
```

```text
TERM                verifier_state
KIND                persisted field with a closed vocabulary
DEFINED AT          factory/presets.py:40-42
ALLOWED VALUES      wired · available · unbuilt
QUOTE               "A verifier that exists and runs today, versus one this row asserts *should*
                    apply but which nobody has wired. The distinction is the difference between a
                    preset and a wish." (presets.py:38-39)
```

---

## Research-pass vocabulary (dispatch + research_run)

```text
TERM                dispatch states
KIND                constants
DEFINED AT          factory/dispatch.py:61-65
WHAT IT MEANS HERE  What is true about one research prompt, and who is being waited on.
DISTINCTION IT      "waiting on Paul" vs "waiting on the researcher". Named as the same error as
PROTECTS            collapsing UNMEASURABLE into FAIL.
ALLOWED VALUES      ANSWERED · UNDISPATCHED · IN_FLIGHT · STALE_STATUS · UNKNOWN
QUOTE               "⚠ **"No answer yet" is two different states and they need different actions.**
                    A prompt nobody has sent is waiting on *Paul*; a prompt in flight is waiting
                    on *the researcher*." (dispatch.py:8-10)
                    "Queue depth is **reported**; only self-contradiction (``STALE_STATUS``) is
                    **gated**" (dispatch.py:30-32)
```

```text
TERM                PASS_TYPES
KIND                constant tuple, DECLARED in a prompt header, never inferred
DEFINED AT          factory/research_run.py:61 (members :54-58; UNDECLARED at :59)
ALLOWED VALUES      EXTERNAL_SURVEY · SOURCE_CRAWL · STRUCTURE_CRITIQUE · DECISION_REVIEW ·
                    NARROW_REPAIR    (+ UNDECLARED, outside the tuple)
QUOTE               "⭐ **What a prompt declares now is its PASS TYPE, because that is what
                    configures the run.**" (research_run.py:13)
                    "Both facts are DECLARED in the prompt header, never inferred. A prompt that
                    does not declare gets no button and says why. Fail closed."
                    (research_run.py:36-37)
```

```text
TERM                INDEPENDENCE_RISK
KIND                dict constant
DEFINED AT          factory/research_run.py:81
ALLOWED VALUES      LOW (EXTERNAL_SURVEY, SOURCE_CRAWL) · MEDIUM (NARROW_REPAIR) ·
                    HIGH (STRUCTURE_CRITIQUE) · SEVERE (DECISION_REVIEW)
QUOTE               "⚠ **A local run trades independence for sources, and the record must say
                    so.** … A local agent reading our repo, our conventions and our conclusions is
                    pulled toward agreement; the outside model at least started from nowhere."
                    (research_run.py:23-26)
```

```text
TERM                research eligibility states
KIND                constants
DEFINED AT          factory/research_run.py:67
ALLOWED VALUES      READY · WAITING · NOT-ELIGIBLE · ALREADY-SENT
```

```text
TERM                IN_REPO
KIND                constant (the runner recorded on a research run)
DEFINED AT          factory/research_run.py:65
QUOTE               "Everything runs in one place now. Kept as a named constant so the run log
                    records it and a future outside-model run can be recorded as something else."
```

---

## deploy — attempt limit vocabulary

```text
TERM                LIMIT_HIT / LIMIT_NONE / UNDETERMINED
KIND                constants (an attempt's `limit` field)
DEFINED AT          factory/deploy.py:33-35
WHAT IT MEANS HERE  "did it run out of room", asked separately from "did it work".
DISTINCTION IT      Never assert "not a cap" from an absence of signal.
PROTECTS
ALLOWED VALUES      hit · none · undetermined
QUOTE               "UNDETERMINED = "undetermined"    #: no signal either way — never assert
                    "none" on this basis" (deploy.py:35)
                    "Modelled on ``inspect_ai``'s EvalSample.limit, which exists because a run
                    ended by a turn or cost ceiling is neither a pass nor a failure of the
                    approach." (deploy.py:31-32)
```

```text
TERM                AttemptLedger
KIND                class
DEFINED AT          factory/deploy.py:38 ; keyed by "agent:worktree"
QUOTE               "In-memory counters do not survive a restart, and a cap that resets on restart
                    is not a cap." (deploy.py:41)
                    "A retry that knows only that it is attempt 2 repeats attempt 1"
                    (deploy.py:44-45)
```

```text
TERM                Deployment / RepoDeployer
KIND                dataclass / class
DEFINED AT          factory/deploy.py:181 / :188
```

---

## Metric / MetricSet / GoodhartViolation

```text
TERM                Metric.kind
KIND                field with a two-value vocabulary (enforced by MetricSet.activity)
DEFINED AT          factory/metrics.py:21 ; enforcement at :40-50
ALLOWED VALUES      activity · outcome
QUOTE               "this module refuses to register an activity metric that has no paired outcome
                    metric: the pairing is enforced, not documented." (metrics.py:5-6)
                    "An activity metric with no outcome anchor is how 234 escalations looked like
                    progress." (metrics.py:47)
```

`MetricSet.suspicious()` (metrics.py:68): *"Activity climbing while its outcome stays at zero — the
234/0 signature."* `Metric` also carries a `basis` field defaulting to `"MEASURED"` (metrics.py:24).

---

## EvalCase / EvalReport / EvalSuite / mutate_and_expect_failure

```text
TERM                EvalCase
KIND                dataclass
DEFINED AT          factory/evals.py:21
FIELDS              name · setup · expect (a Verdict) · tags
QUOTE               "One scenario: a world state, and the contract that should judge it."
```

```text
TERM                mutate_and_expect_failure
KIND                function — the negative control
DEFINED AT          factory/evals.py:63
QUOTE               "⭐ The negative control. For each mutation, break one thing in the world and
                    assert the contract stops being green. A mutation that leaves the contract
                    GREEN is a hole in the contract" (evals.py:65-69)
                    "An eval nobody has proved can fail is decoration." (evals.py:3)
```

⚠ `README.md:29-34` corrects the standing of this file: *"That gate passes today, and it is weaker
than its reputation … it proves the *mutation harness* works, nothing more."* Cite
`tests/test_connector_contract.py::test_every_assertion_has_been_proved_able_to_fail` instead.

---

## Worktree / repo resolution

```text
TERM                primary (worktree) / data()
KIND                functions — the single resolver for shared state
DEFINED AT          factory/repo.py:37 (primary), :70 (data), :58 (in_worktree), HERE at :33
WHAT IT MEANS HERE  Where the repository actually is. One resolver, so the estate cannot disagree
                    with itself.
DISTINCTION IT      Per-worktree state vs estate-wide state.
PROTECTS
QUOTE               "**State shared between lanes must resolve to the primary worktree, or it is
                    not shared.** Claims, the worktree list and the run ledger are all that kind of
                    state: a claim taken in one worktree that another cannot see is not a claim."
                    (repo.py:22-24)
```

```text
TERM                BRANCH_PREFIX / .worktrees
KIND                constants
DEFINED AT          factory/worktrees.py:39 (BRANCH_PREFIX = "lane/") ; ROOT at :38
QUOTE               "⛔ **Removal is never automatic.**" (worktrees.py:14)
                    "across ~33,000 agent-generated PRs, *different-agent* PRs in flight conflicted
                    **41.7%** of the time" (worktrees.py:3-5)
```

---

## Schedule vocabulary

```text
TERM                Snapshot / Velocity / scope_settled
KIND                frozen dataclasses + property
DEFINED AT          factory/schedule.py:59 / :96 / :117 ; SETTLED_HOURS at :51
WHAT IT MEANS HERE  Programme velocity measured from git history of the generated artifact's own
                    headline, and the criterion for refusing to project a completion date.
DISTINCTION IT      "the denominator moves". Refuses an ETA rather than flattering one.
PROTECTS
QUOTE               "**⭐ The finding that governs everything else: the denominator moves.** …
                    Gates passed went 1 → 9. The gate set went 13 → 30. **Remaining went 12 → 21.**"
                    (schedule.py:12-17)
                    ""Ahead or behind schedule" needs a target, and there isn't one. … the schedule
                    report says NOT-SET rather than inventing a baseline to be ahead of."
                    (schedule.py:26-29)
```

---

## plan_gates — a SECOND gate set

```text
TERM                PLAN_GATES / PLAN_PHASES
KIND                list of Gate / dict constant
DEFINED AT          factory/plan_gates.py:235 / :50
WHAT IT MEANS HERE  "how far along is the platform build?" — measured against THIS repo, not
                    against prefect-connectors.
DISTINCTION IT      Must never be summed with the 30 readiness gates.
PROTECTS
PHASES              land · surface · trace · retry
QUOTE               "⛔ **These are NOT the thirty readiness gates, and must never be summed with
                    them.** … Adding the two scores together produces a number about nothing. That
                    conflation has already been made once in this estate and had to be corrected"
                    (plan_gates.py:13-18)
```

---

## Other named vocabulary worth recording

```text
TERM                UNSCORED / scored_against
KIND                verdict payload field
DEFINED AT          factory/certify.py:119 ; factory/evaluator.py:58, :111
MEANING             Which world produced this verdict. Absent = a live run; present = a replay.
```

```text
TERM                job (a Claude Code job record)
KIND                external artefact this code reads, with a `needs` field
DEFINED AT          factory/sessions.py:117 (JOBS), :161 (_job)
QUOTE               "**3. `jobs/<id>/state.json` carries a `needs` field, in English, that nothing
                    reads.** Four jobs were blocked on written questions while the operator had no
                    surface showing them. That is not alarm fatigue, it is alarm absence"
                    (sessions.py:112-114)
```

```text
TERM                operator answer / needs_paul
KIND                persisted record / Lane field
DEFINED AT          factory/operator.py:54 (record) ; :77 (block) ; factory/lanes.py:80
MEANING             A decision only a human can make, declared up front so a session does not
                    launch and then block on it.
QUOTE               "`Lane.needs_paul` names a decision only a human can make … It is knowable
                    before the session starts, so a session that launches and then blocks on it has
                    wasted the trip." (operator.py:3-5)
                    "Treat it as Paul's decision. If it does not actually resolve the blocker, say
                    so and stop rather than improvising around it." (operator.py:83-85)
```

```text
TERM                VERDICT_MARK
KIND                dict constant (non-colour carrier per verdict)
DEFINED AT          factory/flow.py:41
ALLOWED VALUES      PASS ● · FAIL ■ · UNMEASURABLE ◆ · NOT_RUN ○
QUOTE               "**Four verdicts, and colour is never the only carrier.** … `UNMEASURABLE` is
                    not a worse `FAIL` — it is "the instrument could not see", a different claim
                    entirely" (flow.py:11-14)
                    "**Blocked is drawn differently from unbuilt.**" (flow.py:16)
```

```text
TERM                LANE handoff vs SESSION handoff
KIND                two documented senses of one word
DEFINED AT          factory/handoff.py:5-8
QUOTE               "Two different things wear the word "handoff" and they want different homes:
                       LANE     one lane finishing …
                       SESSION  everything that moved while you were here, across lanes"
NOTE                Boot prompts are written to `aldc-launchpad/boot-prompts` (handoff.py:39),
                    NOT into this repo: "Writing them here instead would create the fifth artefact
                    home CLAUDE.md warns of."
```

```text
TERM                NotFinished
KIND                exception class
DEFINED AT          factory/finish.py:29
QUOTE               "`finish()` does the five that are safe to automate and refuses the sixth. **It
                    does not merge.** A merge is a judgement about whether the work is right, and
                    this module only knows whether the work is *complete*." (finish.py:8-10)
```

---

# PART 3 — COLLISION ANALYSIS

Compared against `ontology/00-core-ontology.md`, `ontology/01-relationship-map.md` and the
candidate-terms list in `foundations/R02-canonical-ontology-and-vocabulary.md:22-60`.

## The table

| RESEARCH TERM | AGENT-FACTORY TERM | RELATIONSHIP | RISK |
|---|---|---|---|
| **Intent Contract** (`00-core-ontology.md:87`) | `GreenContract` (`contract.py:103`) | **DIFFERENT THING, SAME NAME** (the head noun "Contract") | ⚠⚠⚠ **HIGHEST.** See below. |
| **Evidence** (`:75`) | `evidence.py` CLASSES + `tasks.py` evidence rows | SAME THING, SAME NAME — but the code's is far narrower and *typed* | ⚠⚠ Research def ("an observation or artifact that supports or contradicts a claim") has no class, no basis, no coverage state. Adopting the loose definition would silently retire a working four-class gate. |
| **Claim** (`:71`) | `claims.py` `Claim` (`:69`) | **DIFFERENT THING, SAME NAME** — a pure homonym. **VERIFIED, not assumed.** | ⚠⚠⚠ See below. |
| **Claim** (`:71`) | `Assertion` (`contract.py:41`) | SAME THING, DIFFERENT NAME | ⚠ Low, but the mapping must be stated or R02 will think `claims.py` is the claim store. |
| **Agent** (`:24`) | `AgentSpec` (`blueprint.py:19`) | SAME THING, DIFFERENT NAME (spec vs instance) | ⚠ The code has **no running agent instance object at all** — only a spec and a `session`. Research "Agent" = "an executing decision-making worker instance"; the nearest live thing is `sessions.py`. |
| **Team** (`:32`) | `TeamSpec` (`blueprint.py:43`) and `TEAMS` (`roadmap.py:181`) | SAME THING, SAME NAME — but **two different code objects wear it** | ⚠⚠ `TeamSpec` is a versioned config; `TEAMS` is an authored goal dict with `intent`/`gates`/`blocked_on`. Nothing executes a `TeamSpec` (`runs.py:157`). |
| **Mission** (`:16`) | — | **NO COUNTERPART IN CODE** | `CURRENT_STATE.md:38`: *"The word appears in this codebase only inside `submission` and `PermissionError`."* Nearest analogues are a **lane brief** and a **gate**, and neither is a mission. |
| **Operation** (`:20`) | `runs.py` run row; `Deployment` (`deploy.py:181`) | SAME THING, DIFFERENT NAME (partial) | ⚠ A run row is retrospective and lane-keyed, not a mission execution. |
| **Task** (R02 candidate) | `Task` (`tasks.py:43`) **and** `board` task (`board.py:19`) | **DIFFERENT THINGS, SAME NAME — inside the code itself** | ⚠⚠ `tasks.Task` is a persisted, claimable, evidence-gated work item. A `board` "task" is a *derived view of a non-passing gate* with no id, no owner and no store. R02 must not merge them. |
| **Role** (`:28`) | `AgentSpec.role` (`blueprint.py:21`) | SAME THING, SAME NAME — but a free-text string, not an object | ⚠ No role template, no registry, no validation. |
| **Capability** (`:59`) | — | **NO COUNTERPART IN CODE** | The code measures **readiness of the factory**, never of an agent. `goals.py` groups gates by goal; nothing claims an agent can do a class of work. |
| **Readiness** (R02 candidate) | `readiness.py` GATES / PHASES / `Result` | SAME NAME, **DIFFERENT SUBJECT** | ⚠⚠ Research readiness is a property of a unit/capability. Code readiness answers *"can an agent team run a connector migration unattended?"* (`readiness.py:1`) — a property of the whole estate. Named in `CURRENT_STATE.md:47`. |
| **Skill** (`:63`) | — | **NO COUNTERPART IN CODE** | Skills appear only as **probe targets**: `readiness.py` gate `chain` reads `~/.claude/skills/living-systems-ui/SKILL.md`. No skill object, registry or version. |
| **Knowledge Object** (`:67`) | `Finding` (`findings.py:50`) + `docs/findings.d/` | SAME THING, DIFFERENT NAME | ⚠ Findings have a mandatory four-field schema, KINDS and STATUSES; they lack provenance schema, confidence and cross-repo reuse. |
| **Doctrine** (`:83`) | — | **NO COUNTERPART IN CODE** | One prose mention at `live_probes.py:226`, about *measurement* doctrine, not organizational doctrine. |
| **Policy** (`:79`) | `AgentSpec.prohibition` / `TeamSpec.prohibition` (`blueprint.py:28`, `:50`) | SAME THING, DIFFERENT NAME (a very thin slice) | ⚠ A prohibition is one free-text "must not" string, and it is part of the version hash. |
| **Event** (`:91`) | `bus.KINDS` (`bus.py:48`) **and** `tasks.Event` (`tasks.py:35`) | SAME NAME, **TWO DIFFERENT CODE OBJECTS, NEITHER ORGANIZATIONAL** | ⚠⚠ `CURRENT_STATE.md:40`: *"Two typed event systems exist and **neither is an organizational event log.**"* The bus is ephemeral and gitignored by design (`bus.py:11-16`); task events are per-task. |
| **Signal** (`:95`) / **Field** (`:99`) | — | **NO COUNTERPART IN CODE** | Zero occurrences. |
| **Running Estimate** (`:103`) | `runs.py` ledger | **NO COUNTERPART** — `runs` is retrospective, not continuously revised | ⚠ Do not map. `CURRENT_STATE.md:48` states this. |
| **Organization / OrganizationVersion** (`:3`, `:107`) | `TeamSpec.version` (`blueprint.py:53`) | SAME IDEA one level down (a team, not an organization) | ⚠ The version-hash *discipline* is real and worth lifting; the scope is not. |
| **Artifact** (`:44`) | `artifact_uri` / `artifact_sha256` (`evaluator.py:96-97`); `docs/artifacts/agent-factory.html` | SAME NAME, **NARROWER AND ALREADY OVERLOADED** | ⚠⚠ In this repo "artifact" means (a) the thing submitted for grading and (b) the generated HTML board that `schedule.py` reads its history from. Neither matches the research list (file/repo/table/API/document/ticket/deployment/test). |
| **Cell** (`:36`) / **Squad** / **Staff Function** (`:40`) | — | **NO COUNTERPART IN CODE** | Zero occurrences. |
| **ContextPackage** (R02 candidate) | `ContextPack` (`context.py:121`) + `ContextRef` (`:71`) | **SAME THING, ALMOST SAME NAME** | ⚠⚠ *Adopt the existing name or explicitly deprecate it.* `ContextPack` is built, tested (`tests/test_context_pack.py`, 9 tests) and carries a required `source`, a freshness state and a confidence — all of which `ContextPackage` in the candidate list does not yet specify. Renaming it `ContextPackage` breaks `factory/lanes.py:100-112`. |
| **Observation** (R02 candidate) | probe return values; `AssertionResult.observed` (`contract.py:33`) | SAME THING, DIFFERENT NAME | ⚠ Low. |
| **Decision** (R02 candidate) | `Action` + DECIDED/SHIPPED/SUPERSEDED (`roadmap.py:57-60`) | SAME THING, DIFFERENT NAME | ⚠ Low, but note the code's `Action` requires `why_gate` when it claims measurement. |
| **Outcome** (R02 candidate) | `Metric.kind == "outcome"` (`metrics.py:21`) **and** `runs.outcome` (`runs.py:41`) | **DIFFERENT THINGS, SAME NAME — inside the code itself** | ⚠⚠ A metric outcome is the anchor for an activity metric. A run outcome is FINISHED/REFUSED/ABANDONED. |
| **Simulation** (R02 candidate) | — | **NO COUNTERPART IN CODE** | `corpus.py` loads a hashed known-good **world**, which is a fixture, not a simulator. Note "world" is the code's own word (`corpus.py:3`, `calibration.py:50`). |
| **Tool** / **Resource** (R02 candidates) | `AgentSpec.tools` (`blueprint.py:25`) | SAME NAME, list-of-strings only | ⚠ `readiness.VERSION_DIMENSIONS` distinguishes `tools` from `tool_implementation` — a distinction R02's flat "Tool" would lose. |
| **Experience** / **Lesson** (R02 candidates) | `Finding.kind` values (`findings.py:40`) | PARTIAL, DIFFERENT NAME | ⚠ `CORRECTION` vs `DESIGN` vs `PROCESS` is a finer cut than "Lesson". |
| **Procedure** (R02 candidate) | — | **NO COUNTERPART IN CODE** | |
| **OrgIR** (R02 candidate) | — | **NO COUNTERPART IN CODE** | |
| **Knowledge vs memory** (required distinction) | `docs/findings.d/` vs `.data/bus/` | The code has already made this cut, under different names | ⚠ RECORD (in git, permanent) vs CHANNEL (gitignored, ephemeral) — `bus.py:11-16`. Worth adopting rather than re-deriving. |

---

## The three dangerous redefinitions, spelled out

### 1. "Intent Contract" vs `GreenContract` — DIFFERENT THING, SAME HEAD NOUN

`factory/contract.py` is the **root object of the whole codebase**. Its module docstring line 1 is
*"GreenContract — what "done" means, and what "I could not tell" means."* Line 3: *"The root success
object. Every team, every optimizer run and every certification reads its verdict from here."*

A `GreenContract` is a **named set of falsifiable assertions with a four-verdict outcome**
(contract.py:103-115). It carries no objective, no end state, no invariant, no authority boundary and
no escalation rule — none of the five things `00-core-ontology.md:89` lists for an Intent Contract.

`docs/agent-army/CURRENT_STATE.md:44` states this in the repo's own words, and it is the clearest
existing statement of the collision:

> *"Easy to mistake, so stated plainly: `contract.py` defines what *done* means
> (`Verdict.PASS/FAIL/UNMEASURABLE/NOT_RUN`, `contract.py:17-21`). An Intent Contract as researched —
> bounded authority, commander's intent, acceptable variation — has no representation. The `intent`
> field is a label on a launch record."*

**The specific hazard.** `TeamSpec.contract` (blueprint.py:48) is *"name of the GreenContract that
certifies it"*. `roadmap.TEAMS` entries carry both an `intent` string and a `gates` list, and the
"Power BI Data Model Designer" entry's `unblock` text (roadmap.py:190) argues about whether *"a
contract exists for what its output must satisfy"*. If R02 introduces `IntentContract` without a
disambiguating rule, a reader of `TeamSpec.contract` cannot tell which of the two is meant, and the
word "contract" in this repo already resolves to the certification object in every one of its
~15 uses I read.

**Recommendation for R02 to consider (not a decision):** either keep `GreenContract` as a distinct
canonical term (it is the more established of the two — it exists, is tested, and is imported by
seven modules), or name the research concept something that does not share the head noun.

### 2. "Claim" vs `claims.py` — VERIFIED HOMONYM, not a guess

I checked this rather than assuming it. `factory/claims.py:69`:

```python
@dataclass(frozen=True)
class Claim:
    lane: str
    since: _dt.datetime
    who: str
    note: str = ""
```

and `claims.py:247`: *"Record that `lane` is being worked. Refuses if a conflicting lane is
claimed."* The module docstring (`claims.py:1`) is *"Which lanes are being worked right now, so a
conflicting one can be refused."* Claims are files under `.data/claims/`, gitignored (`claims.py:22`),
protected by a filesystem lock (`_exclusive`, `claims.py:214`) and tested by
`tests/test_claim_race.py`.

**This is a mutual-exclusion lease, not a proposition.** It has no truth value, no supporting
evidence, no derivation and no decision. It is a **pure homonym** of `00-core-ontology.md:73`'s
*"A proposition whose truth is not assumed."*

The research `Claim` maps to `factory/contract.py:41` `Assertion` — *"One falsifiable claim"* — which
is the codebase's own gloss and uses the research word in prose while naming the class something
else.

**The specific hazard.** `01-relationship-map.md:35-39` gives `Claim` four edges (`supported by →
Evidence`, `contradicted by → Evidence`, `derived from → Claim`, `used by → Decision`). None of those
edges is meaningful for a lane claim. A schema that reuses the identifier `claim` will collide with a
live, race-tested, filesystem-backed store, and `claims.py:54-57` already records that adding a fifth
meaning to `lane` was rejected on exactly this reasoning.

Note also that `bus.KINDS` includes `claimed` (bus.py:50) with a *third* sense: *"I am touching this
file/area — the filesystem, not the dependency graph"* — and `tasks.py:26` has a task status
`claimed` with a *fourth* (a task has an owner). Four senses of claim/claimed already exist in this
codebase.

### 3. "Evidence" — SAME NAME, and the code's version is strictly stronger

`00-core-ontology.md:77` defines Evidence as *"An observation or artifact that supports or
contradicts a claim."* That is compatible with the code, but far weaker than it.

`factory/evidence.py` requires an evidence row to carry a **basis** (MEASURED/DERIVED/ASSUMED,
validated at write time, tasks.py:136) and optionally a **class** (one of four, validated when given,
tasks.py:140), and it folds rows into a three-state per-class coverage (SATISFIED/ASSERTED/ABSENT).
`tasks.TaskStore.close(require=…)` refuses a close that does not satisfy the named classes
(tasks.py:166-171). `tests/test_evidence_classes.py` has 12 tests including
`test_four_pieces_of_one_class_do_not_satisfy_four_classes`.

**The hazard is not renaming — it is dilution.** An ontology entry that says "Evidence: an
observation or artifact that supports or contradicts a claim" and stops there, adopted as the
canonical definition, would make the four-class gate look like an implementation detail rather than
part of the term's meaning. `CURRENT_STATE.md:42` calls this *"The strongest Agent-Army-adjacent
thing in the repo."*

---

# PART 4 — WHAT THE CODE HAS THAT THE RESEARCH ONTOLOGY LACKS ENTIRELY

Ordered by how much would be lost by not adopting them.

### 1. UNMEASURABLE as a first-class verdict — `contract.py:20`

No term in `00-core-ontology.md` or the R02 candidate list can express *"the instrument could not
run"*. `CURRENT_STATE.md:67` states that R30's metric lists *"have no way to say 'the instrument was
dark'"*. Every measurement concept the research ontology proposes (Evidence, Observation, Signal,
Running Estimate, Capability, Readiness) is silently two-valued.

### 2. ZERO vs NOT-RECORDED vs NOT-VISIBLE vs NOT-RETAINED — `runs.py:19-23`

The run ledger's basis vocabulary (RECORDED / RECONSTRUCTED / NOT-RECORDED) exists precisely so *"a
lane with no record is NOT a lane that did not run"*. The same distinction recurs, independently, in
at least six other modules with different value names:

| Where | Values | The zero it refuses |
|---|---|---|
| `runs.py:42` | RECORDED / RECONSTRUCTED / NOT-RECORDED | "0 runs" for an unrecorded past |
| `evidence.py:68-70` | SATISFIED / ASSERTED / ABSENT | "no evidence" for an assumed claim |
| `context.py:51-53` | CURRENT / STALE / UNVERIFIED | "fresh" for never-checked |
| `claims.py:96-98` | HELD-LIVE / HELD-GONE / HELD-UNVERIFIED | "free" for an unreadable process table |
| `sessions.py:130` | UNKNOWN-INSTRUMENT-BLIND | "nothing running" for a blind instrument |
| `goals.py:75` | MEASURED / NOT-MEASURED | "0%" for an unmeasured goal |
| `launch.py:62` / `teamplan.py:36` | UNGATED | "0%" for a team with no contract |
| `deploy.py:35` | UNDETERMINED | "not a cap" from an absence of signal |
| `readiness.py:96-97` | empty window → UNMEASURABLE | "controls work" for "nothing has run" |

**This is the single most repeated design decision in the codebase, and the research ontology has no
name for it.** It appears nine times under nine different vocabularies, which is itself a finding:
R02 could give it one name and let the nine be its instances.

### 3. Basis labelling on every published figure — `MEASURED | DERIVED | ASSUMED`

`tasks.py:136`, `context.py:63` (which adds `STATED`), `metrics.py:24`, `presets.py:10-14`,
`lanes.py:8-13`, `roadmap.py:55`, `blueprints/windsorai_client_a.yaml:8-9`. The blueprint file
carries a per-field basis in comments and records a case where the label paid for itself
(windsorai_client_a.yaml:28-36): a DERIVED class name was wrong, caught the moment a real instrument
arrived, *"because the guess was recorded AS a guess"*.

The research ontology's `Claim`/`Evidence` pair has no confidence or provenance axis.

### 4. DECLARED vs VERIFIED — `readiness.py:1486`, `blueprints/windsorai_client_a.yaml:78-82`

The `tenancy` gate's title literally contains the disambiguation: *"Is a tenant scope DECLARED?
(declared, not verified)"*, with the comment *"Declared and verified are different claims and only
one of them is measured here."* The blueprint carries the staleness deliberately: *"a PASS on A12
means 'the landing matched what we declared', not 'what we declared is still correct'."*

`00-core-ontology.md:59` defines Capability as *"Evidence-backed statement that an agent/team/
organization can reliably perform a class of work"* with no way to mark it declared-but-unverified.

### 5. Negative control — "a control never watched refusing is decoration"

`evals.mutate_and_expect_failure` (evals.py:63); the standing rule in gate `refuses`
(readiness.py:1453: *"A gate never observed refusing is decoration. Same rule as an eval."*);
`tests/test_readiness_probes_can_pass.py::test_every_gate_can_refuse`;
`tests/test_connector_contract.py::test_every_assertion_has_been_proved_able_to_fail`; and
`roadmap.py:190-194` refusing to give the PBI contract standing because *"nothing has ever watched it
refuse."*

The research ontology has `Simulation` (tests Doctrine) but nothing that requires a control to have
been **observed refusing**.

### 6. Grader separation and the submission floor — `corpus.py`, `evaluator.py`, `evaluator_service/`

*"An agent that can edit its own grader is not graded"* (corpus.py:9). Three enforcement layers: the
corpus is hashed JSON not Python (corpus.py:1-14); the submission vocabulary is three frozen fields
(evaluator.py:55); the service enforces a target floor and refuses a weakened blueprint
(service.py:23-24, `tests/test_evaluator_isolation.py::test_a_weakened_blueprint_is_refused`). The
remaining hole is named rather than hidden (service.py:28-35).

`01-relationship-map.md` has no evaluator, no grader and no separation-of-principal edge.

### 7. Configuration IS identity — `blueprint.py:3-5`, `readiness.py:1206`

*"An agent is not a name — it is a (prompt, model, effort, tools, retry policy) tuple. Change any
element and it is a different agent, whose certification does not transfer."* Fifteen named
dimensions at `readiness.py:1206`, of which the repo currently hashes six.

`00-core-ontology.md:107` has `Organization Version` but nothing at agent or team granularity, and
nothing that makes version a **deny-list** so a new field is identity by default (blueprint.py:36-38).

### 8. Goodhart pairing — `metrics.py:5-6`

*"this module refuses to register an activity metric that has no paired outcome metric: the pairing
is enforced, not documented."* Grounded in a measured incident: 233 diagnoses, 234 escalations, 0
fixes over 81 days (README.md:11).

No research term pairs a metric with an anchor.

### 9. The derived-board rule — `board.py:5-13`, `plan_gates.py:5-11`

*"a hand-maintained board wearing a computed status … Drift is not prevented here — it is
structurally impossible."* Stated twice in two modules, and `roadmap.py:5` restates it a third time.
The research ontology's world-state projections have no equivalent constraint.

### 10. The rejected-hypothesis artefact — `blueprints/orchestrator_team.yaml:24-30`

*"THIS FILE IS KEPT, NOT DELETED. It is a hypothesis that was tested and rejected, and the rejection
is worth more than the file's absence would be."* — with the numeric threshold that would reopen it.
The research ontology has `Lesson` and `Doctrine` but no object for *a design that was tried,
rejected on evidence, and retained with its unlock condition*.

### 11. Independence risk on a research pass — `research_run.py:81`

LOW / MEDIUM / HIGH / SEVERE, keyed to pass type, with the reason at `research_run.py:23-26`: a local
agent reading our own conclusions is pulled toward agreeing with them. Directly relevant to R02
itself — this crawl is a `SOURCE_CRAWL`, risk LOW; a `DECISION_REVIEW` over the same material would
be SEVERE.

### 12. The RECORD/CHANNEL split — `bus.py:11-16`

*"the RECORD is `docs/findings.d/` — in git, reviewed, permanent … the CHANNEL is here — `.data/bus/`,
gitignored, ephemeral, machine-local … A message is a nudge, not an archive."* This is R02's required
"knowledge vs memory" distinction, already resolved in code, with a documented failure (F70/F71) that
forced it.

### 13. Anti-terms — words the codebase deliberately refuses

Worth recording because R02's naming-quality tests (`R02:127-133`) reject terms for exactly these
reasons:

- **No hours.** `lanes.py:12-13`, `presets.py:24-26`: sizes are ordinal S/M/L, *"an hours figure
  would be read as a plan"*.
- **No completion date.** `schedule.py:22-24`: refuses to project until scope velocity settles.
- **No second source of truth.** `context.py:10-17`: the factory-wiki must be a *derived projection*,
  and every ref must name its source or it *"is not a projection but a fork"*.
- **No supervisor tier, no second topology, no gym, no optimizer, no platform UI** — `README.md:88-98`
  lists each with its unlock precondition.

---

# PART 5 — SUMMARY FOR R02

**Three counts, each measured from the source literal, not from a document:**

- 30 gates (`readiness.py:1394`), 5 phases (`readiness.py:1498`), 9 keys / 11 authored dependency
  edges in `DEPENDS` (`board.py:34`) — note `flow.py:3` still says "twelve dependency edges", written
  before the `tenancy` edge was removed on 2026-08-23 (`board.py:43-53`).
- 5 lanes (`lanes.py:125`), 2 teams (`roadmap.py:181`), 5 preset types (`presets.py:92`).
- 4 verdicts in the enum (`contract.py:17`), **5 in effective use** once `REFUSED`
  (`evaluator_service/service.py:62`) is counted.

**The four terms R02 most needs to disambiguate before writing anything:**

1. `contract` — resolves to GreenContract everywhere in this repo. An `IntentContract` sharing the
   head noun is the highest-risk collision in the set.
2. `claim` — already has four senses in this codebase (lane lease, task status, bus kind, prose
   "falsifiable claim"). The research sense is the fourth, and the class named `Claim` is the first.
3. `lane` — self-documented at `claims.py:54-57` as the most overloaded word here; six meanings on
   one string.
4. `task` — `tasks.Task` (persisted, claimable, evidence-gated) vs `board` task (derived view of a
   failing gate). Both live, neither renameable cheaply.

**The one term R02 should probably adopt rather than rename:** `ContextPack` / `ContextRef`
(`context.py:121`, `:71`). It is built, tested, carries a mandatory `source`, a freshness state and a
confidence, and `ContextPackage` in the candidate list has none of those properties specified yet.

**The one concept the code has nine names for and the research has none:** the refusal to report a
zero from an instrument that has not been shown able to see a non-zero. Giving it one canonical name
would be the single highest-value output of R02 for this codebase.
