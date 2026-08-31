# Research Answer — R00: Foundations of Artificial Organization Engineering

## Metadata

```yaml
research_id: R00
title: Foundations of Artificial Organization Engineering
run_date: 2026-08-30
status: complete
researcher_or_model: Claude Opus 5 (1M context), running as a LOCAL SUBAGENT inside
  C:/Users/PaulRussell/repos/aldc-launchpad, with read access to agent-army-research and
  agent-factory.
independence_declaration: |
  This ran as a local subagent, not an outside model. Both halves stated honestly:
  WEAKER than an external reviewer on independence — I read this estate's drafts, I run on
  its conventions, and the pull toward agreeing with its vocabulary is real. I countered it by
  reading the primary literature for each prior discipline BEFORE reading the repo's framing of
  it, and by hunting a counterexample for every candidate law before evaluating it. That is a
  mitigation, not a cure.
  STRONGER than an external reviewer on file-and-line claims — every repository claim below was
  re-executed or re-read by me, including independently re-running the CURRENT_STATE.md term
  sweep rather than inheriting its result.
repository_access: read-only. No file other than this answer was created, edited, staged or
  committed. No branch created.
repositories_inspected:
  - agent-army-research @ main, HEAD 5b8c4bf (read: ontology/, foundations/, vision/, research/,
    architecture/00 and 08, adr/ listing)
  - agent-factory @ docs/agent-army-research-separation. HEAD was a691043 at session start and
    ed89cb3 by the end of this pass — another session committed to that branch WHILE this pass
    ran. All agent-factory line citations below were read at a691043 or later and re-verified.
web_access: yes — WebSearch + WebFetch. ~40 searches/fetches.
primary_sources_read: 31 (listed in §Sources; those marked NOT-ACCESSIBLE were not read)
evidence_limitations:
  - Four primary PDFs are scanned images or FlateDecode streams my fetcher could not read:
    Erman et al. Hearsay-II (1980), Wooldridge et al. Gaia (JAAMAS 2000) limitations section,
    Jennings "Agent-Based Computing: Promise and Perils" (IJCAI-99), Galbraith (1974).
    For these I used secondary summaries and have tiered the claims DOWN accordingly and marked
    them `SECONDARY`. I did not quote them as if I had read them.
  - Springer and Nature both returned auth redirects. The Workflow Resource Patterns exact
    pattern count and the Nature Machine Intelligence collaboration paper are NOT-ACCESSIBLE.
  - The `-3.5%` average effect that this estate quotes ~10 times is NOT in the abstract of any
    version of its source paper and I could not extract it from the body PDF. See Finding 3.
  - I did not run any agent, team or benchmark. Every performance number here is REPORTED by
    someone else; none is MEASURED by me. The only things I MEASURED are repository facts.
```

---

## Executive conclusion

**Artificial Organization Engineering, as defined in the brief, is not a new engineering
discipline. It is a rename of an existing one — organisation-oriented multi-agent systems /
multi-agent oriented programming — which has a metamodel (Moise+, 2002), an enforcing runtime
(ORA4MAS/JaCaMo), a methodology family (Gaia, Tropos, INGENIAS), a normative layer (electronic
institutions), and an MIT Press textbook (2020). Every one of the ~17 concerns in the working
hypothesis has a named home in that literature. That discipline exists, is 25 years old, and did
not reach industry.**

That is the headline, and it is the answer to the falsification question the brief asked for. But
the honest conclusion is not a flat "no", and three things stop it being one:

**What appears true.**

1. **The problem AOE points at is real and is measured.** MAST (arXiv:2503.13657) classifies 1,642
   annotated multi-agent traces across 7 frameworks (κ=0.88) into 14 failure modes and three
   categories: *system design*, *inter-agent misalignment*, *task verification*. None of those
   three is a model-capability problem. They are specification, communication-structure and
   evidence problems — i.e. organisational ones. `ESTABLISHED`.
2. **Two substrate properties are genuinely new and they are not in the prior literature.**
   (a) *Context is a measurable, monotonically degrading resource.* Every one of 18 frontier models
   tested degrades as input length grows. Galbraith's 1974 information-processing view of
   organisation design was a qualitative theory about human cognitive limits; here the limit has a
   meter. (b) *The members have no interests.* No careers, no politics, no agency costs, no truce.
   That removes the mechanism behind a large fraction of human organisation-theory results — which
   means most of them do **not** transfer, and importing them as "laws" is a category error.
   `EMERGING` / `DERIVED`.
3. **Organisational design has become cheap and reversible**, so for the first time it can be run
   as a controlled experiment rather than a decade-long natural one. Somebody is already doing
   exactly this: IMACS (arXiv:2607.25446, July 2026) makes Belbin roles, Mintzberg coordination
   and RACI accountability *executable, independently swappable configuration* and ablates them.

**What remains uncertain, and it is the load-bearing uncertainty.** The best available evidence
says designed multi-agent structure usually *hurts* on the work this estate does. The scaling study
this repo already leans on found every multi-agent architecture degrading sequential planning by
39–70% (v1) / up to −70.0% (v3). IMACS found the winning organisational configuration **flips
across model families**. Dochkina (arXiv:2603.28990) found self-selected roles beating designed
roles. If the object of the proposed discipline is *designed structure*, the discipline's own
subject matter is the thing most likely to be harmful.

**What we should do.**

- Build the **measurement half** and only the measurement half. It is the half this estate has
  already built well (`factory/contract.py`, `factory/evidence.py`, `factory/corpus.py`,
  `evaluator_service/`, `factory/metrics.py`), it is the half with no adequate prior art that I
  could find, and it is the half that MAST says is a third of all observed failures.
- Cut the ontology from 30 objects to **9**, and delete `Role`, `Cell`, `Signal` and `Field`
  outright. Merge `Intent Contract` into `GreenContract` — the estate currently has two contract
  objects, and the repository one is better and is running.
- Replace the ten-stage "compile → execute → learn → new version" lifecycle with a **level-triggered
  reconciliation loop plus a promotion ladder**. The pipeline as drafted is a waterfall with no
  failure edge and no `UNMEASURABLE` exit.

**What we should explicitly NOT do.**

- **Do not adopt "Artificial Organization Engineering" as a public category.** Three independent
  reasons in §Deliverable 15, the strongest being that the term is effectively taken: *Artificial
  Organisations* (Waites, arXiv:2602.13275, Feb 2026) already publishes under it with a different
  meaning, and using a new name severs us from the prior art rather than positioning against it.
- **Do not build the organisational compiler or the organisational debugger.** These are the two
  analogies the vision leads with and the two that survive scrutiny worst (§Deliverable 7).
- **Do not build the field engine / stigmergy layer.** Zero code, zero LLM-agent evidence, and it
  is drawn from a regime — thousands of cheap agents — that is the opposite of ours.
- **Do not write another ontology before one team is certified.** The documented cause of death of
  AOSE was "no common understanding of key concepts, no common notations, no industrial-strength
  tools". A 30-object ontology written before a single certified team is a symptom of that disease,
  not a treatment for it.

---

## Question decomposition

The subquestions actually investigated, in the order they were worked:

1. Does an existing discipline already own the ~17 concerns in the working hypothesis? (§Prior art)
2. If so, why did it not reach industry, and do LLMs remove those causes? (F1, F2)
3. What does the one real system in scope actually implement, measured rather than claimed? (F5)
4. Is the estate's central empirical claim — the 180-configuration study — real, current and
   dereferenceable? (F3)
5. Where is the workflow/organisation boundary, and is it a real boundary? (§Deliverable 3+, D-boundary)
6. Which of the 30 candidate objects survive a reduction test? (§Deliverable 4)
7. Is the compile/run/debug analogy load-bearing or decorative? (§Deliverable 7)
8. Does each of the 10 candidate laws survive a deliberate counterexample hunt? (§Deliverable 8)
9. What can honestly be measured about an artificial organisation, and what cannot? (§Deliverable 9)
10. Under strict novelty rules, what is actually new? (§Deliverable 13/14, §Novelty map)
11. Should "AOE" be used publicly? (§Deliverable 15)

---

## Prior art

The brief named ~19 disciplines. Several turned out to be poor fits and saying so was requested;
I say so. Format per the template: *primary object / abstractions / tooling / what failed to become
mainstream / what applies to LLM agents / what changes because agents reason over unstructured
information.*

### 1. Organisation-oriented MAS / multi-agent oriented programming — **the direct ancestor**

- **Primary object:** the *organisation*, as a first-class programmable artefact separate from the
  agents that populate it.
- **Abstractions:** Moise/Moise+ splits the organisation into a **structural specification**
  (groups, roles, links, compatibilities, cardinalities), a **functional specification** (social
  schemes, missions, goals) and a **deontic specification** (obligations and permissions binding
  roles to missions). AGR/AALAADIN (Ferber & Gutknecht) reduces it further to Agent–Group–Role and
  is explicitly a *meta*-model able to express market-like and hierarchical organisations alike.
  OperA separates organisational aims from the agents that fill them, which is precisely the
  "roles outlive agents" property the brief proposes.
- **Tooling:** real and still maintained. Moise ships inside **JaCaMo**, which integrates three
  programming dimensions — agents (Jason), environment (CArtAgO), organisation (Moise) — with
  organisational artifacts and a Normative Programming Language enforcing the specification at
  runtime. MadKit implements AGR. ISLANDER + AMELI implement electronic institutions, where AMELI
  is a *domain-independent* middleware that mediates every interaction and enforces institutional
  rules. There is an MIT Press textbook: Boissier, Bordini, Hübner & Ricci, *Multi-Agent Oriented
  Programming* (2020).
- **What failed to become mainstream:** essentially all of it, outside academia. The AOSE
  retrospective literature is blunt about why: no common understanding of key multi-agent concepts,
  no common set of notations and models, no flexible industrial-strength tools, and — the one that
  matters most — MAS platforms "require the adoption of design paradigms fundamentally different
  from industry practices and do not integrate well with modern software engineering tool chains".
  `SECONDARY` (retrospective survey summaries; the Wooldridge/Jennings primaries were
  NOT-ACCESSIBLE as text).
- **Applies directly to LLM agents:** the entire deontic layer. Obligation/permission/prohibition
  bound to a *role* rather than an agent instance is exactly what an LLM agent estate needs and
  does not have. The separation of organisational aims from agent instances survives intact.
- **What changes with LLMs:** the reason the old stack needed heavy formalism was that agents could
  not read prose. An LLM can be handed the organisational specification in natural language. That
  removes the *authoring* cost that killed adoption — and removes the *enforcement* guarantee at
  the same time, because prose read by a stochastic reader is a suggestion. This is the single most
  important transfer question in the whole survey and it cuts both ways.
- **Novelty risk for AOE: SEVERE.** This discipline is AOE, under an older name, with better formal
  foundations and worse ergonomics.

### 2. Agent-oriented software engineering (Gaia, Tropos, INGENIAS)

- **Primary object:** the *development methodology* — how you get from requirements to a MAS.
- **Abstractions:** Gaia views a MAS as a computational organisation of interacting roles, with a
  role model, interaction model, agent model, services model and acquaintance model. A Gaia role
  carries **responsibilities** (as liveness and safety properties), **permissions**, **activities**
  and **protocols**. Zambonelli, Jennings & Wooldridge later added *organisational rules* as a
  first-class abstraction.
- **Tooling:** editors and code generators, largely academic.
- **What failed:** adoption. Methodologies covered particular lifecycle phases rather than the full
  lifecycle industry demands. `SECONDARY`.
- **Applies to LLM agents:** the *role-as-liveness-and-safety-properties* framing is better than
  anything in modern agent frameworks. "This role must eventually do X" and "must never do Y" is
  directly expressible as contract assertions.
- **What changes:** nothing structural. The failure was economic, not representational.
- **Novelty risk: SEVERE** for anything role-shaped.

### 3. Computational organisation theory

- **Primary object:** the organisation as a *simulable* object, to derive theory about human firms.
- **Abstractions/tooling:** Carley & Prietula's *Computational Organization Theory* (1994);
  **ORGAHEAD** (Lee & Carley) simulating organisational learning and structural adaptation under
  task-environment complexity; Levitt's **Virtual Design Team** simulating how structure and
  information tools affect project performance.
- **What failed:** it did not fail — it succeeded as *science* and was never intended as
  engineering. It produces validated theory about structure, not deployable systems.
- **Applies to LLM agents:** the *method*. Sweep a structural parameter, hold task constant,
  measure. That is exactly what the scaling study and IMACS now do.
- **What changes:** the simulated agents can now be the real agents. COT had to model cognition;
  we can run it. This is a real methodological upgrade and the strongest positive transfer in the
  survey.
- **Novelty risk: HIGH** for "Simulation" and "organisational search" as proposed objects.

### 4. Organisation theory proper (Simon, Galbraith, Mintzberg, March, Nelson & Winter)

- **Galbraith (1974):** the greater the task uncertainty, the more information must be processed
  between decision makers during execution. Four design strategies: create *slack resources* and
  *self-contained tasks* to reduce the information-processing **need**; invest in *vertical
  information systems* and *lateral relations* to increase **capacity**. `SECONDARY`.
- **Mintzberg:** five configurations, each with a dominant coordinating mechanism — direct
  supervision, standardisation of work processes, of skills, of outputs, and mutual adjustment.
- **Nelson & Winter:** routines are the firm's genes and play three roles — *routine as memory*,
  *routine as truce*, *routine as goal*.
- **Walsh & Ungson (1991):** organisational memory as acquisition, retention and retrieval across
  storage "bins".
- **Malone (MIT CCI):** the collective-intelligence "genome" — building blocks derived from 200+
  examples, organised as answers to **what / who / why / how**. This is a four-slot minimal
  organisational ontology derived empirically, and it is smaller than the brief's thirty.
- **What applies:** Galbraith transfers *exactly*, and better than it transfers to human firms,
  because the capacity term is now instrumented (see F4). Mintzberg's coordinating mechanisms are a
  usable taxonomy for topology choice. Malone's four questions are a better starting ontology than
  the brief's list.
- **What does NOT apply — and this is a finding, not a caveat.** *Routine as truce* has no
  analogue. Human routines are sticky because changing them re-opens a political settlement between
  people with careers and conflicting interests. Artificial agents have none of that. Any law whose
  mechanism is agent self-interest — most of agency theory, much of transaction-cost economics,
  the entire stability-of-doctrine argument — does not transfer. See F7.
- **Novelty risk: SEVERE** for "organizational memory", "doctrine", "institutional memory".

### 5. Blackboard systems (Hearsay-II)

- **Primary object:** a shared, structured, multi-level hypothesis space that independent knowledge
  sources read and write, with a scheduler and focus-of-attention control.
- **Tooling:** Hearsay-II (1971–76), BB1, GBB. `SECONDARY` — the Erman 1980 PDF is a scanned image
  and I could not read it; I did not quote it.
- **What failed:** control complexity. The hard part was never the blackboard, it was deciding
  which knowledge source runs next; the architecture became a niche.
- **Applies to LLM agents:** directly, and it is being reinvented under other names. "Shared
  understanding is a runtime asset" (draft Law 11) is the blackboard model restated.
- **What changes:** the blackboard no longer needs a rigid level structure, because the readers can
  parse prose. That is a real simplification.
- **Novelty risk: SEVERE** for "Collective Cognition Fabric" and "shared world state".

### 6. Autonomic computing (MAPE-K) and self-adaptive systems

- **Primary object:** the *managed element plus its autonomic manager* — a control loop, not an
  organisation. Kephart & Chess (2003): Monitor, Analyse, Plan, Execute over shared Knowledge.
- **Tooling / status:** the field is alive and the reference model is stable. Weyns's survey work
  reports "evidence that the principles of architecture-based adaptation are widely applied in
  industry", and models-at-runtime (Blair et al. 2009) is the direct ancestor of every "digital
  twin of the system" proposal.
- **What failed / what is still open:** assurance. The recent state-of-the-art essay
  (arXiv:2511.06352) states plainly that existing approaches emphasise estimated *benefit* and that
  "estimated risk in the decision-making process of self-adaptive systems has been largely ignored
  so far".
- **Applies to LLM agents:** MAPE-K is the correct shape for the runtime. It is level-triggered and
  continuous; the brief's lifecycle is edge-triggered and one-shot.
- **What changes:** the P in MAPE can now be an LLM, which is why assurance got *harder*, not
  easier.
- **Novelty risk: SEVERE** for the runtime and adaptation layers.

### 7. Workflow / BPM / process mining

- **Primary object:** the *process*, plus — and this is the part usually forgotten — the *resource*.
- **Abstractions:** the Workflow Patterns initiative catalogues patterns across control-flow, data,
  resource and exception perspectives. The **resource patterns** (Russell, van der Aalst, ter
  Hofstede & Edmond, CAiSE 2005) explicitly cover role-based distribution, authorisation,
  separation of duties, delegation, escalation, and capability-based distribution — grouped as
  creation, push, pull, detour, auto-start, visibility and multiple-resource patterns. The exact
  pattern count is `NOT-ACCESSIBLE` (workflowpatterns.com fails TLS SNI; Springer requires auth).
- **Process mining** discovers models from event logs, and **conformance checking** replays history
  against a model to find deviations.
- **Organisational mining** (Song & van der Aalst, *Decision Support Systems*, 2008) discovers
  *organisational models and social networks from event logs* — i.e. it derives roles from
  behaviour.
- **What failed:** nothing. This is the most industrially successful item in the survey.
- **Applies to LLM agents:** conformance checking is the honest form of the "organisational
  debugger": replay history against the declared organisation and report deviations.
- **Novelty risk: SEVERE** for "capability from outcomes not role names" (organisational mining,
  2008), for "Organizational Trace", and for the whole resource/authority/delegation cluster.

### 8. Actor systems and durable execution

- **Hewitt's actor model** (and Open Information Systems Semantics, 1991) gives isolated
  state, message passing and inherent indeterminacy in message ordering.
- **Erlang/OTP** gives the engineering answer: supervision trees, workers and supervisors,
  "let it crash", separation of normal operation from error recovery (Armstrong, 2003 thesis).
- **Temporal** gives durable execution: the event history is logged and the workflow re-executed
  deterministically after failure; on replay the worker's emitted commands are compared against the
  recorded history, and determinism is the *precondition* for that working.
- **Applies to LLM agents:** the supervision tree is a better model for "team topology" than any
  organisational metamodel — it is about *who restarts whom*, which is a decision the estate will
  have to make and has not. AutoGen v0.4's runtime is literally an actor model.
- **What does NOT apply:** deterministic replay. An LLM policy is stochastic, so a recorded history
  can be *shown* but not *re-executed with a change* to attribute the difference. This is the reason
  the "debugger" analogy fails (§Deliverable 7).
- **Novelty risk: SEVERE** for runtime, replay and supervision.

### 9. Cybernetics — Beer's Viable System Model

- **Primary object:** the viable system; five recursive subsystems (operations, coordination,
  control, intelligence, policy) with Ashby's requisite variety as the governing constraint, and
  every S1 unit itself a viable system.
- **What failed:** operationalisation. Beer himself said the five subsystems "work recursively and
  cannot be isolated from each other, so attempts in the literature to identify them separately
  with managerial names are ill-conceived" — which is precisely what a "staff mesh" of named
  cognition services does.
- **Applies:** requisite variety is a genuinely useful constraint — a controller must have at least
  as much variety as what it controls. It gives a principled reason why a single supervisor agent
  over many workers fails: the supervisor's context window bounds its variety.
- **Verdict on fit: PARTIAL, and the brief over-rates it.** VSM is a diagnostic language, not an
  engineering method, and the estate's own ADR-0004 ("no random agent animation") suggests it
  already senses that the recursive-diagram aesthetic is the seductive part.
- **Novelty risk: MODERATE** — VSM is a good source of constraints, a bad source of architecture.

### 10. Artificial life, stigmergy, swarm — **poor fit, and I am saying so**

- Stigmergy (Grassé 1959) is indirect coordination via environmental traces; ACO (Dorigo, 1996–97)
  formalises it. It works in a specific regime: very many, very cheap, near-identical agents,
  with a cheap shared medium and no need to explain any individual decision.
- Our regime is five expensive, heterogeneous, individually-auditable agents whose decisions must
  be explainable to a client. **The mechanism does not transfer.** Pheromone fields buy you
  emergent global behaviour at the price of per-decision explainability, which is the one thing
  this estate refuses to trade.
- **Verdict: the `Signal` and `Field` objects, the "field engine" and the "morphogenetic" language
  should be cut, not deferred.** This is the clearest "poor fit" in the brief's list.

### 11. Digital twins — **poor fit as used**

- ISO 23247 defines a digital twin as "a fit for purpose digital representation of an observable
  manufacturing element with synchronization between the element and its digital representation",
  and the distinction that does the work is *bidirectional* sync — a *digital shadow* is one-way,
  a *digital model* is manual. The standard is criticised for not addressing verification,
  validation and uncertainty quantification, and for lacking a formal ontology.
- **What "Organizational Digital Twin" would actually be:** a digital *shadow*, because nothing
  proposed writes back to the organisation. Using "twin" for a read-only projection imports a
  synchronisation claim the design does not make. Call it what it is: a **materialised projection**.

### 12. Orchestration systems

- **Kubernetes** contributes the one design principle that most needs importing: **level-triggered
  reconciliation**. Controllers do not react to single events; they periodically compare actual
  state to declared desired state and act until convergence, and reconciliation must be idempotent.
  This is strictly more robust than the brief's edge-triggered pipeline.
- **Infrastructure-as-Code** contributes plan/apply/diff and drift detection, which is exactly the
  proposed "Organization Definition" + "Organization Diff".
- **Novelty risk: SEVERE** for the organisation-as-versioned-config artefacts.

### 13. Modern LLM-agent layer

- **Frameworks.** LangGraph = state graph (nodes, edges, reducers, checkpointers). AutoGen v0.4 =
  actor model, async messaging, `SelectorGroupChat`/`RoundRobin`/`Swarm` policies. CrewAI = role
  model (Agent + Task + Process, sequential or hierarchical crews). **None of the three has an
  organisation object, a norm, an obligation, an authority boundary or inter-mission persistence.**
  CrewAI's "role" is a prompt string, not a deontic construct. This is a real gap — and it is
  exactly the gap Moise filled in 2002.
- **Protocols.** A2A (Google, Apr 2025; Linux Foundation, Jun 2025) gives Agent Card, Task with a
  lifecycle (`SUBMITTED / WORKING / INPUT_REQUIRED / AUTH_REQUIRED / COMPLETED / FAILED / CANCELED /
  REJECTED`), Message, Part, Artifact. This is FIPA's Directory Facilitator and ACL, rebuilt on
  HTTP/JSON-RPC/OAuth2. Confirmed absent from the A2A spec: roles, authority hierarchy, teams,
  organisational units, norms, obligations.
- **Skills.** Anthropic's Agent Skills (Oct 2025; open standard 18 Dec 2025) is a folder with a
  `SKILL.md`, loaded by progressive disclosure, portable across Claude apps, Claude Code and the
  API. **The "Skill Package" artefact in the brief is a solved, standardised, cross-vendor problem.
  Do not design one.**
- **Observability.** OpenTelemetry GenAI semantic conventions define span shapes for model
  inference, embeddings, retrieval, memory operations, tool execution, agent invocation, workflow
  invocation and planning. Status: still *Development* as of mid-2026. **The "Organizational Trace"
  artefact is this, and it is nearly free.**
- **The organisational-science layer already exists.** IMACS (arXiv:2607.25446, 28 Jul 2026)
  separates *who is on the team* (organisation), *how members align* (coordination) and *which
  algorithm fuses their work* (collaboration protocol) into orthogonal swappable layers, makes
  Belbin/Mintzberg/RACI executable configuration, and learns protocol selection with a contextual
  bandit. **This is the AOE thesis, published, one month before this pass.**
- **Institutional design as a safety argument already exists.** Waites, *Artificial Organisations*
  (arXiv:2602.13275, 5 Feb 2026): "Multi-agent AI systems should follow this institutional model
  using compartmentalisation and adversarial review to achieve reliable outcomes through
  architectural design rather than assuming individual alignment", demonstrated over 474
  composition tasks with a Composer, a Corroborator *with* source access and a Critic *without*.

---

## Evidence

Tiers per `research/RESEARCH_PROTOCOL.md` (A–E), plus the pass's OBSERVED / DERIVED / ASSUMED /
MARKETED labels.

### ESTABLISHED (tier A–B)

| Claim | Support |
|---|---|
| Organisation-oriented MAS is a mature, tooled, textbook discipline whose object is the organisation | Moise+ (2002), AGR/AALAADIN, OperA, JaCaMo, MIT Press 2020 `OBSERVED` (site + book listing) |
| The workflow *resource* perspective already models role, authorisation, delegation, escalation, separation of duties | Russell et al., CAiSE 2005 `OBSERVED` (abstract/summary; full text NOT-ACCESSIBLE) |
| Roles can be discovered from event logs rather than authored | Song & van der Aalst, DSS 2008 `OBSERVED` |
| MAPE-K is the reference model for self-adaptive systems and architecture-based adaptation is applied in industry | Kephart & Chess 2003; Weyns survey via arXiv:2511.06352 `OBSERVED` |
| Level-triggered reconciliation beats edge-triggered event handling for convergence | Kubernetes controller/operator design `OBSERVED` |
| Durable execution with deterministic replay is a solved industrial problem *for deterministic workflows* | Temporal docs `OBSERVED` |
| Supervision trees are the mature answer to "who restarts whom" | Armstrong 2003 `SECONDARY` |
| Contract Net gives announce/bid/award/report task allocation, and is inappropriate when subproblems are interdependent | Smith 1980 `OBSERVED` (PDF read) |
| Multi-agent LLM failures cluster into system design, inter-agent misalignment, and task verification | MAST, arXiv:2503.13657 `OBSERVED` |
| Every frontier model degrades as input length grows | Chroma 2025 (18 models); Liu et al. 2023 `SECONDARY` |
| Agent Skills is an open, cross-vendor standard as of 18 Dec 2025 | claude.com/blog/skills `OBSERVED` |
| A2A defines Agent Card / Task / Message / Part / Artifact and defines **no** organisational concepts | a2a-protocol.org spec `OBSERVED` |
| Anthropic's multi-agent research system beat single-agent Opus 4 by 90.2% on an internal *breadth-first research* eval, at ~15× chat token cost, and coding is explicitly called a poor fit | anthropic.com/engineering `OBSERVED` |

### EMERGING (tier B–C)

| Claim | Support |
|---|---|
| Multi-agent architectures average *worse* than single-agent, with strong task-structure dependence | arXiv:2512.08296 `OBSERVED` — but see Finding 3, the version matters |
| Sequential/planning tasks degrade most under multi-agent decomposition (39–70% v1; up to −70.0% v3) | ibid. `OBSERVED` |
| Coordination returns diminish or go negative once a single-agent baseline exceeds ~45% (β=−0.408, p<0.001) | ibid. v1 `OBSERVED` |
| Error amplification is topology-dependent: 17.2× independent vs 4.4× centralised | ibid. v1 `OBSERVED` |
| The winning organisational configuration flips across model families | IMACS, arXiv:2607.25446 `OBSERVED` (abstract) |
| Preserving inherited intent across decomposition/revision is the binding long-horizon difficulty | TaskWeave, arXiv:2606.01199 `OBSERVED` |
| Architecturally enforced information asymmetry produces behaviours not individually instructed | Waites, arXiv:2602.13275, 474 tasks, explicitly observational `OBSERVED` |
| Benchmark-based capability claims are substantially inflated by leakage and weak tests | SWE-bench audit literature: 32.7% solution leakage reported; ~12.5% → ~4% after correction `SECONDARY` |

### EXPERIMENTAL (tier C–D)

| Claim | Support |
|---|---|
| Self-selected roles with a fixed sequence beat both centralised coordination and full autonomy | Dochkina, arXiv:2603.28990 — **treat with caution**: LLM judges, synthetic tasks, judge model changed mid-series (GPT-4o → GPT-5.4), no multiple-comparison correction, and a reported Cohen's *d* of 22.9 that is not a credible effect size. Directionally interesting, quantitatively not usable. |
| An organisational control layer (policy / authority / budget / escalation) at the execution boundary is the right enforcement point | arXiv:2606.04306 `OBSERVED` (abstract; results not extractable) |
| Interaction count grows ~n^1.724 with team size, bounding useful teams to 3–4 agents | Quoted in `agent-factory/docs/research/answers/R2-answer-topology.md:158`; I could **not** verify it in the source PDF. `NOT-VERIFIED` |

### SPECULATIVE (tier D)

- That a persistent artificial organisation outperforms a per-mission assembled one. No evidence
  either way was found. This is the central untested claim of the whole thesis.
- That doctrine promotion (experience → knowledge → skill → doctrine) improves outcomes.
- That a staff mesh (persistent non-task cognition services) pays for its coordination cost.

### METAPHORICAL ONLY (tier E)

- **Organisational fields / stigmergy / morphogenesis.** Wrong agent-count regime (§Prior art 10).
- **"Digital twin"** as applied to an organisation. It is a shadow, not a twin (§Prior art 11).
- **"Compiler"** for mission-intent → organisation. No source semantics, no preservation theorem
  (§Deliverable 7).
- **"Command World"** as a design driver. A UI metaphor is not an architecture.

---

## Findings

### Finding 1 — The discipline already exists, under a different name, and it failed for reasons LLMs do not fix

**Mechanism.** Organisation-oriented programming took the organisation as its primary object,
decomposed it into structural/functional/deontic specifications, built a runtime that enforces the
specification through organisational artifacts and a normative programming language, and published
a textbook. Everything in the brief's working-hypothesis list — roles, teams, capabilities, skills,
knowledge, policies, communication structures, authority, history, evaluation, topology — has a
named construct there.

**Evidence.** Moise+ structural/functional/deontic split `OBSERVED`; JaCaMo integrating agent,
environment and organisation dimensions with Moise + NPL `OBSERVED`; AGR as an organisational
meta-model `OBSERVED`; MIT Press 2020 `OBSERVED`. Documented adoption obstacles: no common concepts,
no common notation, no industrial-strength tooling, poor toolchain integration `SECONDARY`.

**Counterevidence.** Two of the four obstacles are genuinely weakened by LLMs: authoring cost (an
LLM can read a prose specification) and notation (natural language is the common notation). That is
real and it is the strongest pro-AOE argument available. It is not sufficient, because the third
and fourth obstacles — industrial tooling and toolchain integration — are economic, and are
currently being solved by *other* people's standards (A2A, Agent Skills, OTel GenAI) that contain no
organisational concepts at all.

**Agent Army implication.** Position Agent Army as *organisation-oriented programming for LLM
agents* and cite Moise, not as a new discipline. That framing is defensible, gives us 25 years of
formal foundations for free, and immediately tells us what to build: the deontic layer, which
neither LangGraph nor AutoGen nor CrewAI nor A2A has.

---

### Finding 2 — The brief's 17 concerns and the running system disagree, and the running system is right

**Mechanism.** The brief lists ~17 concerns an artificial organisation "may" contain. I
independently re-ran the CURRENT_STATE term sweep against `agent-factory` and confirm it returns
**nothing** — not one Agent Army term appears in any Python module (`grep` exit status 1, verified
by me at HEAD a691043). Beyond that: `blueprints/orchestrator_team.yaml` is a three-agent team that
was designed, tested and **rejected on measurement**, and deliberately kept.

**Evidence.** Term sweep `OBSERVED (re-executed by me)`. `factory/lanes.py:125` `LANES` is a literal
authored list. `factory/teamplan.py` sequences a team's steps but does not staff one.
`factory/bus.py:48` `KINDS` is a five-kind ephemeral machine-local bus, not an organisational event
log. Zero occurrences of `federat*` or `simulat*` in `factory/`. The blueprint header states the
rejection and the unlock threshold.

**Counterevidence.** Absence is a scope decision, not a refutation: `README.md` §"What is
deliberately absent" gates Agent Army on "one certified team, plus evidence a tier helps", and no
team is certified. So the thesis has not been *tested and failed* here; it has been *declined
pending evidence*.

**Agent Army implication — and this is the conflict the brief asked me to report explicitly.** The
estate's best engineering did not come from the organisational half. It came from the measurement
half: `factory/contract.py` (four verdicts, never collapsed), `factory/evidence.py` (four typed
evidence classes, three states, refusal in the store), `factory/corpus.py` (hashed, verified,
separable grader world), `evaluator_service/service.py` (three submission fields and a body with a
fourth is *refused*, and the corpus tenants come from the service, never from the submission),
`factory/metrics.py` (a `GoodhartViolation` if an activity metric is registered with no outcome
metric to anchor it). **If AOE is a discipline, the evidence from the only running system says its
subject matter is the instrument, not the org chart.**

---

### Finding 3 — The estate's most load-bearing empirical claim is cited from a superseded preprint and could not be checked

**Mechanism.** The number that killed the three-agent team, and that is repeated in at least ten
files across `agent-factory/docs/`, is cited as `citeturn3view0` — a ChatGPT Deep Research
citation token with no dereferenceable URL. Nobody in this estate has been able to open the source.

**Evidence.** I found the source: **"Towards a Science of Scaling Agent Systems", Kim et al.,
arXiv:2512.08296**. Version history and content, all `OBSERVED`:

| | v1 (9 Dec 2025) | v3 (8 Apr 2026, current) |
|---|---|---|
| Configurations | **180** | **260** |
| Benchmarks | 4 (Finance-Agent, BrowseComp-Plus, PlanCraft, Workbench) | **6** |
| Predictive model R² | **0.513** | **0.373** (0.413 with task-grounded capability) |
| Capability coefficient | β = −0.408, p<0.001 | not in abstract |
| Error amplification | 17.2× independent vs 4.4× centralised | not in abstract |
| Parallelisable gain | +80.9% | +80.8% |
| Sequential degradation | 39–70% | up to −70.0% |

Every figure this estate quotes matches **v1 exactly**. The paper has since been substantially
expanded and its predictive model's R² has **fallen from 0.513 to 0.373**. Separately: the `−3.5%
average` with 95% CI `−18.6% to +25.7%` — quoted in `R2-answer-topology.md:15` and repeated
throughout — **is not in the abstract of v1, v2 or v3**, and I could not extract it from the body
PDF. It is `NOT-VERIFIED`. It may be in the paper's body; I am not asserting it is absent, only
that it is currently uncheckable from the repository.

**Counterevidence.** The *decision* survives the version change intact. Sequential planning still
degrades catastrophically in v3, and the capability-saturation and topology-dependence findings are
unchanged in direction. The three-agent team should still not be built.

**Agent Army implication.** This is a live instance of the "counts must carry their regeneration
command" rule applied to citations rather than counts. Recommendation (I am not editing the file):
`blueprints/orchestrator_team.yaml`'s header and `docs/agent-army/CURRENT_STATE.md` should carry
`arXiv:2512.08296v1` explicitly, note that v3 supersedes it with different numbers, and state that
the rejection rests on the *direction*, which survives. A second recommendation: every `citeturn`
token in `docs/research/` is an unresolvable citation and should be treated as `NOT-VERIFIED` until
dereferenced.

---

### Finding 4 — Context as an instrumented logistics resource is the strongest genuinely-new thing here

**Mechanism.** Galbraith's information-processing view says organisational form is a response to
task uncertainty, and gives four levers: reduce the *need* (slack resources, self-contained tasks)
or increase the *capacity* (vertical information systems, lateral relations). In a human firm the
capacity term is unmeasurable — you infer it from outcomes. In an LLM organisation it has a meter:
tokens in, tokens out, and a measurable accuracy-versus-length curve that degrades in every model
tested.

**Evidence.** Context degradation across 18 frontier models `SECONDARY`; position-dependence
changing character above ~50% context fill `SECONDARY`; Anthropic's own ~15× token multiple for
multi-agent vs chat `OBSERVED`; Agent Skills' progressive disclosure — load ~80 tokens of metadata,
then instructions, then resources — is the industry's operational answer `OBSERVED`.

**Counterevidence.** The measurement is of a *model*, not an *organisation*. Nobody has shown that
allocating context as a budget across agents improves organisational outcomes. The link from
"context degrades" to "therefore allocate it as logistics" is `DERIVED`, not measured.

**Agent Army implication.** "Context is Logistics" (draft Law 4) is the best-supported law in the
set and should be promoted to the first thing built after the instrument. Its operational form:
*every agent has a declared context budget, and the organisation can report context spend per
mission the way it reports dollars.* That is buildable today and nothing in the prior art does it.

---

### Finding 5 — The estate has an unnamed design doctrine that is better than several of its named laws

**Mechanism.** Three separate modules solve the same problem the same way, and the pattern has no
name in either repository: **when you cannot make a weakening impossible, make it attributable.**

**Evidence, all `OBSERVED`:**
- `factory/corpus.py:12-14` — the corpus is hashed and verified on load; tampering "is still
  *possible* … but it is no longer *silent*, and the corpus id and hash travel with every verdict".
- `evaluator_service/service.py:28-35` — names the weakness it does not close (the graded party
  writes the blueprint that parameterises its own contract) and answers with two partial controls:
  the artefact hash travels with the verdict "so a weakened blueprint is attributable rather than
  silent", plus a small `_enforce_target_floor`.
- `factory/blueprint.py:41-70` — `NOT_IDENTITY` is a **deny-list, not an allow-list**, after a
  proven defect: `repo` and team-level `prohibition` were outside the version hash, so "a team
  certified against `prefect-connectors` under *must not deploy to production* kept the identical
  version when repointed at another repo with the prohibition deleted".

**Counterevidence, and it is important.** Attribution is only a control if somebody reads it. An
unread hash is a log line. And the same repository shows the limit of prompt-level constraint:
`prohibition` is a prose field carried into the agent's prompt (`factory/blueprint.py:28,50`) and
enforced nowhere at the tool boundary. It is now part of the team's *identity*, which makes a
weakening attributable — it does not make the deploy impossible.

**Agent Army implication.** Promote this to a stated law (see N7 below), *with* its limit stated,
and pair it with the harder law: **a constraint that lives in a prompt is not a constraint**
(N3). The right enforcement point is the one the OCL paper independently identifies — the execution
boundary — not the prompt.

---

### Finding 6 — "Role" should be deleted from the ontology

**Mechanism.** `Role` is the most load-bearing object in every prior organisational metamodel and
the least supported object in the modern evidence. Three independent lines converge on it.

**Evidence.**
- Organisational mining derives roles from behaviour rather than authoring them (Song & van der
  Aalst 2008) `OBSERVED`.
- Self-selected roles outperformed a coordinator that assigns them (Dochkina, arXiv:2603.28990)
  — direction only, effect sizes not credible `EXPERIMENTAL`.
- IMACS finds accountability placement matters *only when the protocol routes the deliverable
  through the accountable agent*, and the winning placement flips across model families
  `OBSERVED`. A role label with no routing consequence changes nothing.
- The running system has no role object at all, and its capability model measures the factory, not
  a role `OBSERVED`.

**Counterevidence.** Gaia's role — responsibilities as *liveness and safety properties*, plus
permissions, activities and protocols — is a genuinely useful construct, and Moise's deontic
binding of missions to roles is how you get obligation without naming an instance. If role is
deleted entirely, obligations have to attach to something.

**Agent Army implication.** Keep `Role` as an **attribute of an Agent within a Task**, carrying only
what has consequences: an authority set, a budget, a prohibition enforced at the tool boundary, and
a routing position. Delete it as an ontological object with its own identity and lifecycle. This is
Law 5 ("capability is earned") made structural rather than aspirational.

---

### Finding 7 — Most organisation-theory results do not transfer, because the members have no interests

**Mechanism.** A large fraction of organisation theory explains structure as a response to *human
motivational* facts: opportunism, career incentives, information hoarding, politics, coalition
maintenance. Nelson & Winter's *routine as truce* is the cleanest example — routines are stable
partly because changing them re-opens a settlement between people with conflicting interests.
Williamson's transaction-cost account rests explicitly on bounded rationality *and opportunism*.

Artificial agents have bounded rationality (measurably — Finding 4) and **no opportunism**. Remove
opportunism and you remove the mechanism behind agency costs, monitoring hierarchies, most of the
case for authority, and the stickiness of doctrine.

**Evidence.** Nelson & Winter's three roles of routine `SECONDARY`; Williamson's three determinants
(asset specificity, uncertainty, frequency) resting on bounded rationality and opportunism
`SECONDARY`; Coase's boundary condition — internalise when internal cost < market cost `SECONDARY`.

**Counterevidence.** Two motivational analogues do exist and should not be dismissed. (a) *Reward
hacking* is a real behavioural analogue of opportunism, and it is exactly why grader separation
matters. (b) *Sycophancy toward the requester* is a real analogue of political deference. So the
correct statement is not "no interests" but "**different** interests, arising from training rather
than from careers".

**Agent Army implication.** Every borrowed law must name its mechanism and say whether the mechanism
exists in this substrate. Draft Law 8 ("doctrine changes slower than strategy") fails this test
outright: its human mechanism is the truce, which does not exist here, while the actual
doctrine-invalidating force — a model version change — has no analogue in human firms and arrives
every few months. See N4.

---

### Finding 8 — The lifecycle in the brief is edge-triggered, and it has no way to say "I could not tell"

**Mechanism.** The proposed lifecycle runs `DEFINE INTENT → COMPILE → ESTABLISH SHARED
UNDERSTANDING → EXECUTE → OBSERVE → VERIFY → AAR → UPDATE → SIMULATE → NEW VERSION`. It is a
one-shot pipeline: every stage is entered once per mission, on an event, and the only feedback is
at the end.

**Evidence.** MAPE-K and Kubernetes reconciliation are both *level-triggered* and continuous —
periodically compare actual to desired and act until convergence, idempotently `OBSERVED`. Level-
triggering exists precisely because edge-triggered systems lose state when an event is missed.
Separately: `factory/contract.py:74-85` shows the missing exit — an `UNMEASURABLE` required
assertion yields `UNMEASURABLE` for the whole contract, "not FAIL, because we did not observe a
failure, and emphatically not PASS". The brief's `VERIFY` stage has no such branch.

**Counterevidence.** There is one genuinely edge-triggered, genuinely sequential thing in the
lifecycle and it should be kept: the **promotion ladder** (draft Law 12) — experience → knowledge →
skill → doctrine, each transition gated on accumulated evidence. That is not a control loop; it is
a ratchet, and ratchets are correctly edge-triggered.

**Agent Army implication.** Replace the pipeline with: a level-triggered reconciliation loop
(observe → compare to intent → act → record) whose verdict vocabulary is the four-verdict contract,
*plus* an orthogonal promotion ladder with explicit evidence thresholds per rung. See §Deliverable 5.

---

## Failure modes

*What breaks if this recommendation is wrong?*

1. **If I am wrong that AOE is a rename**, we under-claim: we publish under "organisation-oriented
   programming" and someone else names the category. Cost: positioning only. Recoverable.
2. **If I am wrong that the measurement half is the valuable half**, we build a very good
   instrument for a system nobody wants to organise, and the organisational insight goes to
   whoever built IMACS. Cost: a year of the wrong emphasis. Partly recoverable — the instrument is
   a prerequisite for the organisational work either way, so the sequencing is robust even if the
   emphasis is wrong.
3. **If I am wrong to cut `Role`**, obligations lose their attachment point and we rediscover
   Moise's deontic layer the hard way. Mitigated by keeping role as an *attribute with
   consequences*. Cheap to reverse.
4. **If I am wrong to cut fields/stigmergy**, we miss an emergent-coordination mechanism at large
   agent counts. Given that our teams are 1–5 agents and the mechanism needs hundreds, the risk is
   near zero at current scale and the decision should be revisited only if agent count crosses ~50.
5. **The most dangerous way to be wrong:** treating this survey's tiering as licence to stop
   looking. Four primary PDFs were unreadable to me. A pass that says "prior art exists" on
   secondary sources can miss the specific formulation that would have changed the design.
   `NOT-ACCESSIBLE` items in §Sources are a work list, not a footnote.

---

## Data-model implications

- **9 fundamental objects, not 30** (§Deliverable 4). `Organization` is a *projection*, not a
  stored row — it is the fold of events over an `OrganizationVersion`. Storing it invites two
  sources of truth, which ADR-0002/0003 already sense.
- **One contract object, not two.** `architecture/01-intent-contract-schema.md` defines an Intent
  Contract while `factory/contract.py` defines a GreenContract. Per the conflict rule, the
  repository wins. Merge: an Intent Contract is a GreenContract *stated before execution*, with
  authority and escalation as additional assertion kinds.
- **Every projection carries a basis and a staleness stamp.** `MEASURED | DERIVED | ASSUMED`, plus
  an explicit `NOT-MEASURED` distinct from `0` — the discipline already present in
  `factory/goals.py` and `factory/tasks.py:137`.
- **Capability is never authored.** It is a derived view over `Evidence` grouped by task class,
  with a count and a recency. A capability row with no supporting evidence rows must be
  unrepresentable, not merely discouraged.
- **Budgets are depleting counters on Agent and Task**, not policies. A policy is checked; a budget
  is consumed. Conflating them is how "budget_usd: 5.0" becomes decoration — which is what it
  currently is in `blueprints/orchestrator_team.yaml`.

## Runtime implications

- **Level-triggered reconciliation**, idempotent, converging on a declared desired state. Not an
  event-driven pipeline.
- **Supervision, not management.** The first real topology decision is not "who plans" but "who
  restarts whom, and how many times before escalating to a human" — Erlang/OTP's question, and one
  neither repository has answered. `factory/launch.py` admission control is the nearest thing.
- **Enforcement at the execution boundary, not in the prompt.** Authority, budget and prohibition
  belong at the tool/store boundary. `factory/tasks.py:163` (`EvidenceRequired` raised *by the
  store*) is the pattern to generalise; `blueprint.prohibition` is the anti-pattern to retire.
- **Replay is a recording, not a debugger.** Keep `certify.py`'s honesty label — "REPLAYED, not a
  live measurement" — and never build a UI that implies stepping-with-modification.
- **Do not invent a comms protocol.** A2A exists, is at the Linux Foundation, and already has Task
  lifecycle and Artifact. If a second team ever needs to talk to the first, speak A2A and add the
  deontic layer above it.

## UI implications

- The honest name for the world view is a **materialised projection**, not a digital twin. One-way
  sync is a shadow (ISO 23247's own distinction).
- The single highest-value screen is not a world map. It is a **coverage view**: for each mission,
  which of the four evidence classes are `SATISFIED` / `ASSERTED` / `ABSENT`, rendered so that
  ASSERTED never looks like SATISFIED. `factory/evidence.py:143-152` already renders this in text.
- Every number on screen carries its basis and the command that regenerates it. Finding 3 is what
  happens when it does not.
- ADR-0004 ("no random agent animation") is correct and should be strengthened: **no visual element
  may encode a quantity the system does not measure.** A pulsing node with no metric behind it is
  the UI equivalent of an activity metric with no outcome anchor.

## Performance implications

- Coordination cost is superlinear in team size, and token cost is ~15× chat for multi-agent
  (`OBSERVED`, Anthropic). Any structural addition must be justified against a same-budget
  single-agent baseline, which is exactly the threshold `orchestrator_team.yaml` already states.
- Context is the scarce resource, not compute. Progressive disclosure (~80 tokens of skill metadata
  at rest) is the reference technique and it is free — Agent Skills already implements it.
- The instrument must be cheap enough to run on every delivery. A contract that costs more than the
  work is a contract that gets skipped.

## Security/governance implications

- **Grader separation is a security property, not a quality property.** "An agent that can edit its
  own grader is not graded" (`factory/corpus.py:8-10`). The stated gap — separation is *evident*
  and *attributed*, not *enforced* — is the single most important open security item, and
  `CORPUS_ROOT` honouring `$AGENT_FACTORY_EVALS` means closing it is a config change.
- **The graded party writes the target.** `evaluator_service/service.py:28-35` names this honestly:
  an agent that softens its own blueprint softens its own grading wherever the evaluator runs.
  `_enforce_target_floor` is a partial answer; a per-connector evaluator-pinned target is the real
  one and nobody has written the policy.
- **Human-owned constitution is a policy decision, not a discovered law.** Say so. It should be
  enforced by the substrate (no credential, no permission), not by a law in a document.
- **Escalation is a first-class object.** The OCL paper independently arrives at policy / authority
  / budget / escalation; adopt that vocabulary rather than inventing one.

---

## Deliverable 1 — Definition of Artificial Organization Engineering

> **Artificial Organization Engineering** is the design, instrumentation and empirical evaluation
> of *persistent structural constraints* on populations of stochastic autonomous agents, where the
> structure — who exists, what each may do, what each can see, and what counts as done — is a
> versioned artefact that outlives any single mission and is changed only on evidence.

Four clauses, each doing work, each falsifiable:

- **"persistent … outlives any single mission"** distinguishes it from orchestration, whose
  structure is per-run.
- **"structural constraints … what each can see"** is the mechanism claim, and it is the one with
  independent support (Waites' enforced information asymmetry; MAST's topology-dependent error
  amplification). Structure that does not change what an agent can see or do is decoration.
- **"stochastic"** is why this is not distributed systems. You cannot re-run and attribute.
- **"changed only on evidence"** is what makes it *engineering* rather than organisational design
  opinion, and it is the clause this estate can actually already discharge.

## Deliverable 2 — Reasons to reject that definition

Nine, ordered by strength. I hold 1–3 to be currently decisive.

1. **It is a rename.** Organisation-oriented programming has owned this object since 2002, with a
   metamodel, an enforcing runtime and a textbook (Finding 1).
2. **The prior discipline failed for reasons unrelated to representation**, and the reasons persist:
   tooling and toolchain integration. Renaming it does not fix them.
3. **The evidence says the object is usually harmful.** Multi-agent structure averages worse than
   single-agent; sequential work degrades up to 70%; the best configuration flips per model family;
   self-selected roles beat designed ones. A discipline whose subject matter usually hurts is a
   research programme, not an engineering discipline.
4. **No certified team exists.** `README.md` gates this work on one, and the gate has not opened.
   Founding a discipline before the first working instance is how you get a 30-object ontology and
   no users.
5. **The name is taken.** Waites, *Artificial Organisations*, Feb 2026, with a different meaning.
6. **"Engineering" implies predictive design rules**, and IMACS's central mechanism finding is that
   the rules are not portable across model bindings. Prediction that must be re-derived per binding
   is measurement, not engineering.
7. **Most of the borrowed theory does not transfer** because the members have no interests
   (Finding 7).
8. **The artefacts are already owned by other standards**: Skill Package → Agent Skills; trace →
   OTel GenAI; capability advertisement → A2A Agent Card; definition/diff → IaC; runtime → Temporal
   / Kubernetes.
9. **The two lead analogies fail** — compiler and debugger (Deliverable 7). A discipline whose
   central metaphors mislead is under-specified.

**The strongest defence against 1–3**, stated fairly: the prior discipline assumed agents that could
not read. Every organisational construct had to be formal, and that formality was the adoption cost.
LLM agents can be handed a prose organisation. That is a genuine substrate change and it deserves a
research programme. It does not yet deserve a discipline name.

## Deliverable 3 — Prior-art lineage

See §Prior art above (13 clusters covering the brief's ~19 named disciplines; artificial life,
digital twins and cybernetics were assessed and reported as poor or partial fits, as requested).

### The boundary definitions the brief asked for (§3 of the brief)

| Term | Proposed definition | Discriminating test |
|---|---|---|
| **Agent** | A locus of decision with an identity, a budget and the ability to refuse. | Can it decline the work it is handed? A prompt that cannot refuse is a function call. |
| **Agent System** | One agent plus its tools, memory and verification. | Exactly one locus of decision. |
| **Multi-Agent System** | ≥2 loci of decision that can produce different outcomes from the same input. | Count *loci*, not processes. Two chained prompts where the second cannot refuse is one locus — most "multi-agent" systems fail this test. |
| **Workflow** | A structure that is an input to execution. | Its topology is not in its own state space. |
| **Team** | A set of agents bound to one mission, dissolved with it. | Does membership survive mission completion? |
| **Organization** | **A workflow whose topology is in its own state space** — the structure is both input and output, modified by the same system that executes it, on the basis of its own recorded history. | Has the topology ever changed as a function of the system's own recorded history? If never, it is a workflow. |
| **Artificial Organization** | An organisation whose members are non-human loci of decision, whose structure is a versioned artefact, and whose members have no personal interests. | The third clause is what makes borrowed human theory suspect (Finding 7). |
| **AO Runtime** | The component that enforces the structure at the execution boundary — authority, budget, visibility, escalation — and records the events from which the organisation is projected. | Can an agent violate the structure by writing a different prompt? If yes, there is no runtime. |
| **AO Engineering** | Deliverable 1. | Is any structural change ever rejected on measurement? If not, it is design, not engineering. |

**Answering the brief's example question — when does a workflow become an organisation?** Not at
persistent roles (workflow resource patterns have those), not at reusable knowledge (BPM has
that), not at resource allocation (that is scheduling), not at organisational memory (event logs
are that), not at governance (OPA is that). It becomes an organisation **when its own structure
enters its state space** — when the thing that executes can change the thing that decides who
executes, on evidence it produced itself.

Two consequences, and the second is uncomfortable:
- The candidate properties in the brief (persistent roles, adaptive authority, reusable knowledge,
  resource allocation, organisational memory, dynamic topology, capability development, governance,
  inter-mission persistence) are **all satisfied by mature workflow and BPM systems** except one:
  *dynamic topology decided by the system itself*. So eight of the nine do not discriminate.
- By this definition, **agent-factory is a workflow, not an organisation.** `factory/lanes.py:125`
  `LANES` is a literal list validated on import; `factory/teamplan.py` takes membership as given.
  That is the honest classification and I would rather have a definition that classifies our own
  system correctly than one that flatters it.

## Deliverable 4 — Canonical ontology proposal

Reduced from 30 candidates to **9 fundamental objects**. The reduction is the deliverable; the list
is the easy part.

| # | Object | Identity | Lifecycle | Owner | Mutability | Persistence | Observability | Versioning | UI importance |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Event** | ULID + stream | append-only, never deleted | runtime | immutable | durable, forever | total — it *is* the observation | none (the log is the version) | low (raw), total (derived) |
| 2 | **Agent** | stable id + config hash | created, budgeted, retired | human | config immutable per version | durable | budget spend, verdicts produced | config hash = version (`factory/blueprint.py:31-33`) | high |
| 3 | **Task** | id + parent | open → claimed → closed(verdict) | agent, one at a time | append-only event history | durable | full | none | high |
| 4 | **Artifact** | URI + sha256 | created outside the system | external | external | external | hash only | external | medium |
| 5 | **Claim** | id | asserted → supported / contradicted / stale | any agent | immutable text, mutable status | durable | full | supersession chain | high |
| 6 | **Evidence** | id + class | recorded once | agent | immutable | durable | class + basis + ref | none | **highest** |
| 7 | **Contract** | name + assertion-set hash | authored → calibrated → run | human | immutable once calibrated | durable | four verdicts per assertion | hash | high |
| 8 | **Policy** | id | authored → enforced → retired | human | versioned | durable | every check logged | semver | medium |
| 9 | **OrganizationVersion** | deny-list hash over config | pinned per run | human | immutable | durable | diffable | it *is* the version | high |

**Derived, not stored** (each is a fold over Events, and storing any of them creates a second source
of truth): `Organization`, `Mission` (a Task with no parent), `Operation` (an event range),
`Team` (the agent set on a task tree), `Capability` (Evidence grouped by task class), `Knowledge`
(Claims with SATISFIED evidence), `Outcome` (a Contract verdict), `Decision` (an Event kind),
`RunningEstimate` (a projection + staleness + basis), `Observation` (= Evidence).

**Cut outright, with reasons:**

| Cut | Reason |
|---|---|
| **Role** | Finding 6. Survives only as an attribute with consequences (authority, budget, prohibition, routing position). |
| **Cell** | A Team with a shorter life. No distinct behaviour, no distinct storage. |
| **Signal**, **Field** | Wrong regime (§Prior art 10). Tier E. |
| **Intent** as a separate object | Merge into Contract. An intent contract is a contract stated before execution. Two contract objects is the conflict in Finding/Data-model. |
| **Skill** as an owned object | Agent Skills is an open standard. Reference it; do not model it. |
| **Doctrine** as an object | A Policy that survived a promotion threshold. The promotion is an Event; doctrine is a Policy with a flag. |
| **Simulation** | Not an object. A run with a flag, scored against a **Corpus** — and Corpus (hashed, verified, separable) is the object worth having, per `factory/corpus.py`. |
| **StaffFunction** | `RESEARCH ONLY`. PROSA's *staff holon* (1998) is the exact precedent — an advisory unit alongside order/product/resource holons — so it is not new; and there is no LLM-era evidence it pays for its coordination cost. |
| **Resource**, **Tool** | Substrate attributes. What is fundamental is **Budget**, which is an attribute of Agent and Task, not an object. |

**Sanity check against the smallest empirically derived organisational ontology I found:** Malone's
collective-intelligence genome reduces 200+ real examples to four questions — *what, who, why, how*.
Nine objects is already an order of magnitude more than that. Thirty was not an ontology, it was a
vocabulary list.

## Deliverable 5 — Lifecycle

**Rejected: the brief's ten-stage pipeline.** It is edge-triggered, has no failure edge, no abort,
no `UNMEASURABLE` exit, and puts learning only at the end (Finding 8).

**Proposed: a reconciliation loop, a ratchet, and a gate.**

```text
                      ┌──────────── DECLARE ─────────────┐
                      │  intent as a contract, stated     │
                      │  BEFORE execution; authority,     │
                      │  budget, escalation, prohibitions │
                      └───────────────┬───────────────────┘
                                      │
        ┌─────────────────────────────▼──────────────────────────────┐
        │  RECONCILE   (level-triggered, idempotent, continuous)     │
        │                                                            │
        │   OBSERVE ──► COMPARE to declared ──► ACT ──► RECORD       │
        │      ▲                                          │          │
        │      └──────────────────────────────────────────┘          │
        │                                                            │
        │   exits with ONE of four verdicts, never collapsed:        │
        │     PASS · FAIL · UNMEASURABLE · NOT_RUN                   │
        └─────────────────────────────┬──────────────────────────────┘
                                      │
                          ┌───────────▼────────────┐
                          │  PROMOTION LADDER      │  ← edge-triggered ratchet
                          │  (evidence thresholds) │
                          │                        │
                          │  experience            │  1 occurrence
                          │     ↓ provenance       │
                          │  knowledge             │  ≥2 independent sources
                          │     ↓ reuse            │
                          │  skill                 │  reused ≥N times, ≥1 repo
                          │     ↓ generality       │
                          │  doctrine              │  survived ≥M missions
                          └───────────┬────────────┘
                                      │
                          ┌───────────▼────────────┐
                          │  HUMAN GATE            │
                          │  new OrganizationVersion│
                          └────────────────────────┘
```

**Why this shape, against the alternatives compared:**

| Alternative lifecycle | What it contributes | Why not adopted wholesale |
|---|---|---|
| MAPE-K | the loop, and shared Knowledge | no promotion semantics; assurance is its own open problem (arXiv:2511.06352) |
| Kubernetes reconciliation | level-triggering, idempotence, declarative desired state | no learning at all |
| OODA | speed of the loop, orientation as the hard step | no artefacts, no evidence discipline |
| PDCA / Shewhart | Check→Act ratchet | pre-dates any notion of an instrument that can be dark |
| Spiral (Boehm) | risk-first ordering | per-project, not per-run |
| Temporal workflow | durable state, deterministic replay | replay requires determinism we do not have |
| **Brief's pipeline** | names the right *stages* | edge-triggered; no failure edge; no UNMEASURABLE |

The two non-negotiables: **four verdicts at the exit of every loop**, and **the promotion ladder has
thresholds that are numbers, not adjectives.** Draft Law 12 already states the ladder; what it
lacks is the thresholds, and a ladder without thresholds is a metaphor.

## Deliverable 6 — Core engineering artifacts

| Artefact | Keep? | Source-controlled / generated / runtime state | Notes |
|---|---|---|---|
| **Intent Contract** | **merge into GreenContract** | source | Two contract objects today. Repo wins. |
| **GreenContract** | **keep — the root object** | source | `factory/contract.py`. Everything reads its verdict. |
| **Org-IR** | **cut** | — | An IR presupposes a compiler with source semantics. There is none (D7). |
| **Organization Definition** | keep | source | It is IaC. Deny-list identity hash per `blueprint.py:39-42`. |
| **Capability Graph** | keep, **generated** | generated | Never authored. Derived from Evidence. |
| **Skill Package** | **do not build** | external | Agent Skills, open standard, 18 Dec 2025. |
| **Knowledge Graph** | keep, **generated** | generated | Claims with SATISFIED evidence. `docs/findings.d/` is the working prototype. |
| **Policy Bundle** | keep | source | Enforced at execution boundary, not in a prompt. |
| **Doctrine Bundle** | keep as a *flag* | source | A Policy that cleared a promotion threshold. |
| **Verification Contract** | = GreenContract | source | Do not create a second one. |
| **Simulation Scenario** | rename → **Corpus** | source, hashed | `factory/corpus.py`: hashed, verified on load, separable. |
| **Organizational Test** | keep, and it is the *core* | source | Must include the negative control: every assertion proved able to fail. |
| **Organizational Trace** | keep, **do not invent** | runtime state | OTel GenAI semconv. |
| **Organization Diff** | keep, generated | generated | Diff of OrganizationVersion. |
| **After Action Review** | keep, generated + human | generated, then curated | Its output is *candidate* knowledge, not knowledge. |
| **Evidence Coverage Report** | **ADD — missing from the brief's list** | generated | Per-delivery: four classes × three states. `factory/evidence.py`. The most useful artefact in the estate and the brief does not list it. |
| **Verdict Record** | **ADD — missing** | runtime, write-once | Attribution: evaluator identity, bundle hash, corpus id + hash, artefact hash. `evaluator_service/`. |

## Deliverable 7 — Compiler / runtime / debugger model

Tested as the brief asked: where does the analogy help, where does it mislead? Ranked by how well
each survives.

| Analogy | Verdict | Where it helps | Where it misleads |
|---|---|---|---|
| **Version control** | **STRONGEST — keep** | An organisation genuinely is a versioned config. `blueprint.py` already gets the hard part right: identity is a **deny-list**, so a new field is identity by default. | Only if the diff is *semantic*. A hash diff tells you something changed, not what it means. |
| **Test framework** | **STRONG — keep, build first** | The whole discipline reduces to "did the structural change help, and can I tell?" Requires the negative control. | A green suite from an instrument that cannot fail is worse than no suite (`README.md`). |
| **Profiler** | **STRONG** | Cost/latency/token accounting per agent, per mission. Real, cheap, already standardised in OTel. | Profiling measures resource use; organisational inefficiency is often *redundancy*, which looks like healthy utilisation. |
| **Runtime / OS** | **MODERATE** | Scheduling, permissions, budgets, isolation — real OS concerns with real precedents (Erlang supervision, Kubernetes, Temporal). | "OS" implies preemption and hard isolation we cannot provide over a stochastic policy. |
| **Debugger** | **WEAK — do not build** | Causality *inspection* over a recorded trace is useful and is what conformance checking already does. | A debugger's defining power is *re-run with a change and observe the difference*. With a stochastic policy, one re-run tells you nothing; you need N runs and a statistical test. Calling it a debugger promises single-shot attribution the substrate cannot deliver. `factory/certify.py:71,132` already refuses the pretence: recorded values are labelled *"REPLAYED, not a live measurement"*. Honest name: **organisational conformance checker**. |
| **Compiler** | **WEAKEST — do not build** | The *pass structure* is a decent checklist for a planner (feasibility, capability, policy conflict). | A compiler is a **total, deterministic, semantics-preserving** map from a formal source language to a target, and correctness is provable relative to the source semantics. "Mission intent → executable organization" has (a) no formal source language, (b) no semantics to preserve, (c) no correctness theorem, and (d) — fatally — IMACS's finding that the right output flips across model families, meaning the map is not even a function of the input. Calling it a compiler makes people trust its diagnostics. Honest name: **Org Planner**, explicitly *partial* — it must be able to emit "no feasible organisation", which a compiler pipeline as drafted cannot. |

**The uncomfortable pattern:** the two analogies the vision leads with — compiler and debugger — are
the two that survive worst, and the two that survive best — version control and test framework —
are the two already implemented in `agent-factory`. That is a strong signal about which half of the
product is real.

## Deliverable 8 — Foundational design laws

Every law below was attacked before it was evaluated, as instructed. Verdicts: **HOLDS**,
**WEAKENED** (true but not as stated), **FALSIFIED** (mechanism absent), **POLICY** (a decision
dressed as a law), **VACUOUS**.

### The ten candidates, attacked

| # | Candidate law | Counterexample hunted | Verdict |
|---|---|---|---|
| 1 | Intent before topology | IMACS: winning configuration flips across model families, so topology is not derivable from intent. Dochkina: self-organised beat designed. Conway's law runs the other way — existing topology bounds expressible intent. | **WEAKENED** → replace with N2 |
| 2 | Evidence before autonomy | Evidence itself is unreliable: SWE-bench leakage 32.7%, corrected success ~12.5%→~4%; MAST makes *task verification* a whole failure category. Trusting a bad instrument is worse than none. | **HOLDS but insufficient** → must be paired with N1 |
| 3 | Knowledge without provenance is rumor | Model weights. Everything the LLM knows is provenance-free and it is the most useful knowledge in the system. A working fix is worth having whether or not you can cite why. | **WEAKENED** → *provenance gates promotion, not use* |
| 4 | Context is a resource, not a transcript | None found. Directly supported by measured degradation across 18 models and by the industry's own answer (progressive disclosure). | **HOLDS — best-evidenced law in the set** |
| 5 | Organizations should expose state before changing state | Kubernetes controllers change state continuously and derive observability from the same loop; there is no expose-first phase. And `README.md`'s own ordering is contract-first, not observability-first. | **WEAKENED** → applies to **self-modification only** |
| 6 | Doctrine should change slower than strategy | Nelson & Winter: human routine stability is partly *routine as truce* — a political settlement. No truce exists here. Meanwhile model versions change every few months and invalidate configurations. | **FALSIFIED as stated** → replace with N4 |
| 7 | Simulation should precede self-modifying optimization | The "simulation" is a corpus, and corpora leak and saturate. Optimising against a corpus optimises against the corpus. | **HOLDS, but needs N1's companion**: score against an instrument the optimiser cannot write to |
| 8 | Capability should be measured from outcomes, not role names | None found. Supported by organisational mining (2008), Dochkina, MAST. | **HOLDS — but not new**, attribute to Song & van der Aalst |
| 9 | Local autonomy requires global constraints | None — and that is the problem. Every bounded system has bounds; as stated it excludes nothing. | **VACUOUS as stated** → sharpen to N3 |
| 10 | Human-controlled constitutions bound machine-controlled execution | Not falsifiable; it is a choice we are making. | **POLICY, not law** — keep, label honestly |

### Laws worth keeping from `FOUNDATIONAL_LAWS_DRAFT.md`

- **L10 "Activity is not progress" — HOLDS, and is the best law in either document.** It is the only
  one with in-house empirical support: 233 diagnoses / 234 escalations / **0 fixes** over 81 days,
  and a loop that ran 965 times, recorded its own 1.6% success rate and never adjusted. It is also
  the only one already *enforced in code* — `factory/metrics.py` raises `GoodhartViolation` when an
  activity metric is registered with no outcome metric to anchor it.
- **L13 "Organizational structure has a cost" — HOLDS and is now quantified:** ~15× tokens for
  multi-agent vs chat `OBSERVED`; superlinear interaction growth `NOT-VERIFIED`.
- **L14 "An organization should know what it does not know" — HOLDS, and is this estate's
  distinctive contribution.** `UNMEASURABLE` ≠ `FAIL`; `ABSENT` ≠ `ASSERTED`; `NOT-MEASURED` ≠ `0%`.
- **L12 "Learning must have a promotion path" — HOLDS in form, incomplete in substance.** Needs
  numeric thresholds per rung or it is a metaphor.

### Better laws (proposed)

Each is stated so it can be falsified, and each names the observation that would kill it.

**N1 — The instrument precedes the organization.**
No structural change may be adopted on the strength of an instrument that has not been *proved able
to register its failure*. *Falsified by:* a case where adopting a change on an unproven instrument
caught the same regressions as adopting it on a proven one. *Already implemented:*
`tests/test_connector_contract.py::test_every_assertion_has_been_proved_able_to_fail`.

**N2 — Topology is empirical and binding-specific.**
Topology is a parameter to be measured per model binding, never derived from intent. No topology
ships without a same-budget A/B against one agent on the same tasks and the same authoritative
verifier. *Falsified by:* a topology that transfers across ≥3 model families with stable rank order.
*Source:* IMACS; `orchestrator_team.yaml`'s own unlock threshold is already the correct form.

**N3 — A constraint that lives in a prompt is not a constraint.**
Authority, budget and prohibition must be enforced at the store, the runtime or the tool boundary.
*Falsified by:* a measured compliance rate with prompt-only prohibitions indistinguishable from
boundary enforcement across adversarial trials. *Positive example:* `factory/tasks.py:163` raises
`EvidenceRequired` *in the store*. *Negative example:* `blueprint.prohibition` is prose in a prompt.

**N4 — A substrate change is a doctrine-invalidating event.**
Any promoted doctrine carries the model binding it was validated against, and is demoted to
candidate on a binding change until re-validated. *Falsified by:* doctrine whose measured benefit is
stable across model generations. *Source:* IMACS's flipping placements + Finding 7.

**N5 — Every organizational number carries the command that regenerates it.**
*Falsified by:* nothing — it is a hygiene rule, and Finding 3 is what its absence costs.

**N6 — Structure buys reliability only when it buys independence.**
Adding an agent that reads the same context as the agent before it adds cost and no information. The
gain from structure is proportional to the *independence* of the added view, not to the count.
*Falsified by:* a measured gain from adding an agent with strictly identical context and tools.
*Source:* Waites' architecturally enforced information asymmetry (Corroborator *with* sources /
Critic *without*), plus MAST's 17.2× vs 4.4× error amplification — independent agents amplify,
centralised validation contains. **I believe this is the single most useful output of this pass**:
it explains both the failures (redundant agents) and the successes (asymmetric review) with one
mechanism, and it makes "how many agents" answerable.

**N7 — When you cannot make a weakening impossible, make it attributable — and then read it.**
Hash it, carry it with the verdict, put it in the identity. *Falsified by:* an estate where
attribution existed and the weakening still went unnoticed — which is the standing risk, so the
second clause is not decoration. *Source:* Finding 5, three modules, `OBSERVED`.

## Deliverable 9 — Evaluation model

**Principle first:** the unit of evaluation is the **delivered artefact**, not the trace. A trace
tells you what happened; only the artefact tells you whether it was right. MAST's largest single
observed modes were *step repetition* and *unaware of termination* — both invisible in an
artefact-only view and both irrelevant to whether the artefact is correct. Measure both; never
substitute one for the other.

| Dimension | Metric | Instrument | How the instrument fails |
|---|---|---|---|
| Verified task success | terminal contract verdict per mission | GreenContract, run by a grader the agent cannot write to | corpus leakage; graded party writes the target (`service.py:28-35`) |
| Robustness | verdict variance over N≥5 identical runs | repeated runs, same binding | N=1 is not a measurement of a stochastic system — this is the most commonly skipped control |
| Cost | USD + tokens per *verified* success (never per run) | OTel GenAI spans | per-run cost flatters systems that fail cheaply |
| Latency | wall-clock to terminal verdict, p50/p95 | same | hides queueing behind agent count |
| Adaptability | Δ success on a held-out task class | held-out corpus | held-out only until it is used twice |
| Reproducibility | identical verdict from identical inputs + pinned version | corpus hash + bundle hash + org version | non-determinism makes this a *distribution* claim, not a boolean |
| Intervention | human interventions per mission, and per *unit of value delivered* | task store | a low rate can mean "trusted" or "unwatched" |
| Explainability | fraction of decisions traceable to a cited context ref | `factory/context.py:71` — `ContextRef` requires a non-empty `source` | a ref that points at a file saying "looks right" still counts (`evidence.py:31-32`) |
| Knowledge quality | share of promoted knowledge with ≥2 independent sources | promotion ladder | repeated claims from one source are not independent (draft Law 3) |
| Organizational stability | edits to OrganizationVersion per mission | version hash | stability can be stagnation |
| Intent alignment | drift between declared end state and delivered artefact, at mission end **and at each decomposition step** | contract re-check at each level | TaskWeave: intent decays across decomposition, so end-only checking is blind to the failure |

**Three rules that bind all of the above.**
1. **Every metric has a NOT-MEASURED state distinct from zero.** `factory/goals.py` already does
   this; a goal with no measurable gate reports `NOT-MEASURED`, never `0%`.
2. **Every activity metric is paired with an outcome metric, enforced.** `factory/metrics.py`.
3. **The grader must be an instrument the graded party cannot write to.** Currently *evident and
   attributed*, not *enforced* — the top open security item.

## Deliverable 10 — Research agenda

Ordered by what unblocks what.

- **A1. Certify one team.** Everything else in this estate is gated on it by explicit decision.
- **A2. The N6 independence experiment.** Does structure help only when it adds an independent view?
  This is cheap, decisive, and would produce a publishable result.
- **A3. Context-as-logistics.** Does an explicit per-agent context budget improve verified success
  at equal total tokens?
- **A4. Binding portability.** Does any organisational configuration hold rank order across ≥3 model
  families? IMACS says no; replicate on *our* task classes, which are sequential and shared-state.
- **A5. Intent preservation across decomposition.** TaskWeave names the failure; measure it on real
  tickets, not simulations.
- **A6. Promotion thresholds.** What N and M actually make doctrine promotion pay?
- **A7. Enforcement point.** Prompt-level vs boundary-level prohibition compliance, adversarially.
- **A8. Grader separation, enforced.** Move `evals/` to a repository the scored agent has no write
  credential for; `CORPUS_ROOT` already honours `$AGENT_FACTORY_EVALS`.
- **A9 (RESEARCH ONLY).** Does a staff function pay for itself? PROSA says the idea is 1998; nobody
  has measured it with LLM agents.

## Deliverable 11 — Glossary

- **Agent** — a locus of decision with identity, budget and the ability to refuse.
- **Artificial organization** — a workflow whose topology is in its own state space, staffed by
  agents without personal interests.
- **Attributable weakening** — a control that cannot prevent a softening of the contract but makes
  it visible and attached to the verdict (Finding 5).
- **Basis** — `MEASURED | DERIVED | ASSUMED` on any recorded figure.
- **Contract** — a named set of falsifiable assertions defining "done", evaluated to four verdicts.
- **Corpus** — a hashed, verified, known-good world an assertion is scored against.
- **Deontic specification** — the binding of obligations and permissions to roles (Moise).
- **Doctrine** — a policy that has cleared a promotion threshold, carrying the binding it was
  validated against.
- **Evidence class** — one of `TARGET | CONSUMER | REGRESSION | ROLLBACK`.
- **Evidence state** — `SATISFIED | ASSERTED | ABSENT`. Three, never two.
- **Grader separation** — the property that the scored party cannot write the instrument.
- **Level-triggered** — acting on a comparison of current to desired state, not on an event.
- **Locus of decision** — a point that can produce different outputs from the same input *and*
  refuse.
- **Materialised projection** — a read-only fold of the event log. Not a digital twin.
- **OrganizationVersion** — the pinned configuration a verdict is valid for; identity by deny-list.
- **Promotion ladder** — experience → knowledge → skill → doctrine, gated on numeric thresholds.
- **UNMEASURABLE** — the instrument could not run. Not a pass, not a fail.

## Deliverable 12 — Top 20 open questions

1. Does *any* designed topology beat one agent, at equal budget, on sequential shared-state work?
2. Is the benefit of structure proportional to added *independence* (N6), or to something else?
3. Do organisational configurations transfer across model bindings at all?
4. What is the actual shape of the context-degradation curve for *our* task classes?
5. Does an explicit context budget improve verified success at equal total tokens?
6. Where exactly does intent decay across decomposition, and can a re-check at each level stop it?
7. What promotion thresholds make doctrine pay, and how are they falsified?
8. Can a grader be separated *in practice* in a single-operator estate?
9. Is prompt-level prohibition measurably weaker than boundary enforcement? By how much?
10. Does a persistent organisation beat a per-mission assembled one? (Nothing tests this today.)
11. What is the right supervision policy — who restarts whom, how often, before escalating?
12. Is `UNMEASURABLE` genuinely absent from the prior art, or did I fail to find it?
13. Does an evidence-coverage gate change delivered quality, or only delivered paperwork?
14. What is the minimum team size at which stigmergic coordination beats explicit messaging?
15. Can conformance checking over agent traces find defects a contract misses?
16. Does a staff function pay for its coordination cost at team sizes ≤5?
17. What is the honest false-positive rate of an LLM-as-judge on our own deliverables?
18. Does the deny-list identity hash catch every certification-transferring edit, or only the two?
19. Is there a defensible cost model for "organisational structure" as a first-class budget line?
20. At what point does a human stop being able to audit the organisation's own account of itself?

## Deliverable 13 — The "NOT NEW" list

Strict. Everything here has prior art I read or read a credible summary of.

| Proposed concept | Prior art | Earliest |
|---|---|---|
| Organisation as a first-class programmable object | Moise / AGR / OperA / JaCaMo | 1998–2002 |
| Roles, groups, links, cardinality, compatibility | Moise+ structural specification; AGR | 2002 / 1998 |
| Obligations, permissions, prohibitions bound to roles | Moise+ deontic spec; electronic institutions | 2002 |
| Norm enforcement by a middleware that mediates interaction | AMELI / ISLANDER | ~2004 |
| Role as liveness + safety properties + permissions | Gaia | 2000 |
| Organisational rules as a design abstraction | Zambonelli, Jennings & Wooldridge | 2001 |
| Task announce / bid / award / report | Contract Net | 1980 |
| Shared structured workspace many specialists read and write | Hearsay-II blackboard | 1976 |
| Monitor–analyse–plan–execute over shared knowledge | MAPE-K | 2003 |
| Models at runtime / self-representation | Blair et al. | 2009 |
| Declarative desired state + convergent reconciliation | Kubernetes controllers | ~2015 |
| Durable event history + replay | Temporal; Erlang/OTP | 2003 / 2019 |
| Supervision, restart, escalation | Erlang/OTP supervision trees | 1998 |
| Role/authority/delegation/escalation/separation-of-duties in process work | Workflow resource patterns | 2005 |
| Deriving roles and social structure from event logs | Organisational mining (Song & van der Aalst) | 2008 |
| Replaying history against a model to find deviation | Conformance checking | ~2008 |
| Simulating organisational structure to predict performance | ORGAHEAD; Virtual Design Team | 1990s |
| Organisational memory as acquisition/retention/retrieval | Walsh & Ungson | 1991 |
| Routines as organisational memory and as goal | Nelson & Winter | 1982 |
| Information-processing view of structure; slack vs capacity | Galbraith | 1974 |
| Coordinating mechanisms taxonomy | Mintzberg | 1979 |
| A minimal organisational ontology (what/who/why/how) | Malone, CI genome | 2009 |
| Staff function alongside operational units | PROSA *staff holon* | 1998 |
| Recursive viable subsystems; requisite variety | Beer VSM; Ashby | 1972 / 1956 |
| Capability advertisement + discovery | FIPA Directory Facilitator → A2A Agent Card | 1997 → 2025 |
| Task lifecycle + artifact as protocol objects | A2A | 2025 |
| Skill packages with progressive disclosure | Agent Skills (open standard) | Oct/Dec 2025 |
| Agent/tool/planning traces as spans | OTel GenAI semconv | 2024– |
| Organisation-as-versioned-config, plan/diff/apply | Infrastructure as Code | ~2014 |
| Making org theory executable and ablatable for LLM agents | IMACS | Jul 2026 |
| Institutional structure as a substitute for individual alignment | Waites, *Artificial Organisations* | Feb 2026 |
| Policy / authority / budget / escalation at the execution boundary | Organizational Control Layer | Jun 2026 |
| Designing team structure as an engineering artefact | Team Topologies; Conway | 2019 / 1968 |

## Deliverable 14 — The "POSSIBLY NEW" list

Short, and each carries what would kill it.

1. **Context as an instrumented logistics resource.** Galbraith's capacity term now has a meter, and
   the degradation is monotone and measurable per model. *Killed by:* finding the same treatment in
   the cognitive-load or attention-economics literature. `C` — I did not find it; I did not
   exhaustively look.
2. **Organisations whose members have no personal interests.** Removes truce, agency costs, career
   politics — and therefore removes the mechanism behind a large slice of borrowed theory. I found
   no prior work that treats interest-free membership as the *defining* difference. *Killed by:*
   prior art in the normative-MAS literature making the same argument. `C`.
3. **Organisational design as a cheap, reversible, A/B-testable experiment.** COT simulated because
   it could not run the real thing; we can. IMACS is already exploiting this, which is evidence the
   window is *closing*, not that it is not new. `B`.
4. **The four-verdict discipline with `UNMEASURABLE` never collapsed.** I searched and did not find
   an equivalent in the MAS, workflow, self-adaptive or agent-eval literature I read. Self-adaptive
   systems research is only now naming *risk* as an ignored input; nobody I read separates "the
   instrument was dark" from "it failed". *Killed by:* one citation. `C` — and "I did not find it"
   is materially weaker than "it does not exist", which is why this is not tiered higher.
5. **Typed evidence classes with three states, enforced at the store boundary.** `TARGET / CONSUMER
   / REGRESSION / ROLLBACK` × `SATISFIED / ASSERTED / ABSENT`, with refusal in the store rather than
   in a convention. Adjacent to conformance checking and to DevOps change-management, but I found no
   equivalent typing. `C`.
6. **N6 — structure buys reliability only when it buys independence.** Stated as a design law with a
   falsification condition. The *ingredients* are published (Waites, MAST); the law is not. `D`.

Everything else in the working hypothesis is on the NOT-NEW list.

## Deliverable 15 — Recommendation on using "AOE" publicly

**Do not.** Three independent reasons, any one sufficient:

1. **The name is effectively taken and taken differently.** *Artificial Organisations* (Waites,
   arXiv:2602.13275, Feb 2026) already uses it for institutional design as an AI-safety mechanism.
   Publishing "Artificial Organization Engineering" six months later, meaning something adjacent but
   different, creates collision rather than category.
2. **A new name severs us from the prior art rather than positioning against it.** "Organisation-
   oriented programming" / "multi-agent oriented programming" has a metamodel, a runtime and an MIT
   Press textbook. Adopting that vocabulary and saying *"the LLM substrate changes three things
   about it, and here they are"* is a stronger, more credible claim than announcing a discipline.
3. **We cannot presently evidence the category.** No certified team, no A/B against one agent, and
   the estate's own most-cited number is from a superseded preprint nobody could open. Announcing a
   discipline from that position is a `MARKETED` claim, and this estate's own rules forbid a
   marketed claim as a design premise.

**Use instead:** *Organisation-oriented programming for LLM agents* externally; **AOE as an internal
research frame only**, in this repository, clearly labelled as a frame and not a claim. Revisit when
(a) one team is certified, and (b) one structural A/B has cleared the threshold
`orchestrator_team.yaml` already states.

---

## Experiments required

Every uncertain mechanism, with a falsifiable design. Predict the result before running — the
estate's own rule.

**E1 — Independence, not headcount (tests N6).**
Three arms at equal token budget on the same 30 real tickets: (a) one agent; (b) two agents,
identical context and tools; (c) two agents with *enforced asymmetry* — one holds sources, one is
denied them. Same authoritative verifier. **Falsifies N6 if** (b) ≥ (c). Predict: (c) > (a) > (b).

**E2 — Binding portability (tests N2/N4).**
Fix one organisational configuration. Run across three model families. Measure rank order of
configurations within each. **Falsifies N4 if** rank order is stable. Predict: it flips (IMACS).

**E3 — Context budget (tests Law 4 / Finding 4).**
Same total tokens, two arms: unmanaged context vs a declared per-agent budget with progressive
disclosure. **Falsifies "context is logistics" if** no difference in verified success. Predict:
budgeted wins on long missions, ties on short ones.

**E4 — Prompt vs boundary enforcement (tests N3).**
Same prohibition, expressed (a) in the prompt only, (b) at the tool boundary. 50 adversarial
attempts each. **Falsifies N3 if** compliance rates are indistinguishable. Predict: they are not.

**E5 — Intent decay (tests Finding 8 / TaskWeave).**
Decompose 20 real tickets to depth 3. Re-check the declared end state at each level. **Falsifies
the intent-decay concern if** drift at depth 3 is not greater than at depth 1.

**E6 — Instrument sensitivity (tests N1).**
For every assertion in the contract, mutate the world to make it fail. **Falsifies the contract if**
any assertion cannot be made to fail. Already implemented for the connector contract; generalise.

**E7 — Persistence (tests the central untested claim).**
Ten missions run by a fresh team each time vs ten run by a persistent organisation with a knowledge
store. **Falsifies the persistence premise if** the fresh teams match. Nothing currently tests this,
and it is the claim the whole thesis rests on.

**E8 — Verdict-vocabulary value.**
Over 3 months, count how often `UNMEASURABLE` fires and how many of those would have shipped as
`PASS` under a two-verdict scheme. **Falsifies the four-verdict claim if** the count is ~0.

---

## Recommendation

**NOW**
- Correct the citation of arXiv:2512.08296 wherever it appears; pin `v1`, note `v3` supersedes it,
  state that the *direction* survives (Finding 3). *(Recommendation only — I edited nothing.)*
- Merge Intent Contract into GreenContract. One contract object.
- Adopt the 9-object ontology; delete `Role`, `Cell`, `Signal`, `Field` from the drafts.
- Adopt N1, N3, N5, N6, N7 as stated laws; retire draft Law 8 in its current form.
- Run **E1** (independence) and **E6** (instrument sensitivity, generalised).

**NEXT**
- Level-triggered reconciliation loop + promotion ladder with numeric thresholds.
- Evidence Coverage Report and Verdict Record as first-class artefacts.
- Enforce grader separation by moving `evals/` behind a credential boundary (`$AGENT_FACTORY_EVALS`
  already permits it).
- Context budget per agent (**E3**).
- Speak A2A if a second team ever needs to talk to the first. Do not invent a protocol.

**LATER**
- Org Planner (explicitly partial, must be able to say "no feasible organisation"). Not a compiler.
- Organisational conformance checker over traces. Not a debugger.
- Federation. There is no second organisation.

**RESEARCH ONLY**
- Staff functions / staff mesh (PROSA precedent, no LLM evidence).
- Persistent vs per-mission organisation (**E7**) — the untested central claim.
- Adaptive team formation, gated behind **E1** and **E2** clearing.

**DO NOT BUILD**
- Organisational compiler and Org-IR.
- Organisational debugger implying step-and-modify.
- Field engine / stigmergy / morphogenesis.
- A skill package format (Agent Skills exists).
- A trace format (OTel GenAI exists).
- A comms protocol (A2A exists).
- Evolution Chamber before a working eval — this estate's own gate, and it has not opened.
- The public category "Artificial Organization Engineering".

### Required closing table (per RESEARCH_PROTOCOL)

| IDEA | EVIDENCE | USER VALUE | PERFORMANCE VALUE | COMPLEXITY | RISK | BUILD NOW? | EXPERIMENT? |
|---|---|---|---|---|---|---|---|
| Four-verdict contract | A (in-house, running) | high | neutral | low | low | **already built** | E8 |
| Typed evidence classes | A (in-house) | high | neutral | low | low | **already built** | — |
| Grader separation, enforced | B | high | neutral | med | **high if skipped** | **yes** | — |
| Context budget per agent | B | med | **high** | med | low | next | E3 |
| Level-triggered reconcile loop | A (K8s, MAPE-K) | med | med | med | low | next | — |
| Promotion ladder w/ thresholds | D | med | unknown | med | med | next | E-ladder |
| 9-object ontology | derived | high (clarity) | neutral | low | low | **yes** | — |
| Boundary enforcement of prohibition | C | high | neutral | med | high if skipped | **yes** | E4 |
| Independence-based team design (N6) | C | high | **high** | low | low | **experiment first** | **E1** |
| Adaptive team formation | D | unknown | unknown | high | high | **no** | E1→E2 first |
| Organisational compiler / Org-IR | E | low | negative | very high | high | **no** | — |
| Field engine / stigmergy | E | low | unknown | high | high | **no** | — |
| Evolution Chamber | D | unknown | unknown | very high | high | **no** | gated on eval |
| Public "AOE" category | E | negative | none | low | **reputational** | **no** | — |

---

## Claims ledger

| Claim | Evidence tier | Primary support | Counterevidence | Confidence |
|---|---|---|---|---|
| AOE's concerns are already owned by organisation-oriented MAS | A | Moise+, AGR, OperA, JaCaMo, MIT Press 2020 | LLMs remove the formal-authoring cost that killed adoption | **high** |
| That discipline failed on tooling/integration, not representation | B `SECONDARY` | AOSE retrospectives | primaries NOT-ACCESSIBLE as text | med-high |
| No Agent Army term appears in agent-factory code | A `OBSERVED (re-run by me)` | grep exit 1 at a691043 | — | **very high** |
| A three-agent team was tested and rejected on measurement | A `OBSERVED` | `blueprints/orchestrator_team.yaml` header | rejection cites a preprint version now superseded | **high** |
| The estate's 180-config figures are from arXiv:2512.08296 **v1**; v3 says 260/6/R²=0.373 | A `OBSERVED` | arXiv v1, v2, v3 abstracts | direction of finding unchanged | **very high** |
| The `−3.5%` average is not in any abstract and is uncheckable from the repo | A `OBSERVED` | all three abstracts read | may be in the body; PDF unreadable | **high** (about checkability) |
| Multi-agent LLM failures are structural, not model-capability | B | MAST (1,642 traces, 7 frameworks, κ=0.88) | distribution varies by framework | **high** |
| Every frontier model degrades with input length | B `SECONDARY` | Chroma 18-model study; Liu et al. | thresholds vary by task | **high** |
| Winning organisational configuration flips across model families | B | IMACS abstract | single study, abstract only | med |
| Self-selected roles beat designed roles | C | Dochkina | LLM judges, synthetic tasks, judge swapped mid-series, d=22.9 implausible | **low** |
| Intent decay across decomposition is the binding long-horizon failure | B | TaskWeave | simulation, not real tickets | med |
| Architecturally enforced information asymmetry produces uninstructed behaviour | C | Waites, 474 tasks, observational | authors call for controlled study | med |
| Skill Package / trace / protocol are solved by external standards | A `OBSERVED` | Agent Skills, OTel GenAI, A2A | OTel GenAI still "Development" | **high** |
| Role should be cut as an ontological object | derived | Finding 6 (4 lines) | Gaia/Moise role is genuinely useful for deontics | med |
| Human org theory transfers only where its mechanism exists | derived | Nelson & Winter truce; Williamson opportunism | reward hacking is an opportunism analogue | med-high |
| "Compiler" and "debugger" are the two weakest analogies | derived | compiler totality; stochastic replay | a probabilistic debugger is conceivable | med-high |
| `UNMEASURABLE` has no equivalent in the literature I read | C | absence of finding | absence of evidence, single searcher | **low-med** |

---

## Changed-my-mind section

Four positions the evidence moved.

1. **I started expecting to find AOE was mostly novel packaging of MAS. It is worse than that — it
   is a rename of a specific, named, textbook discipline, tool and all.** I did not expect Moise +
   JaCaMo to cover the deontic layer this completely, nor to find a 2020 MIT Press textbook. That
   moved my recommendation on the public category from "maybe" to "no".

2. **I started expecting the strongest counter-evidence to be theoretical. It was empirical, and it
   was in this estate's own file.** `blueprints/orchestrator_team.yaml` is a better falsification of
   the thesis than anything I found in the literature, because it is *our* topology, *our* task
   class, and *our* decision.

3. **I expected the citation chase on the 180-configuration study to be a formality.** It was not.
   The paper is real, the estate quotes it accurately — against a version that has since been
   superseded, with different numbers and a lower R². The claim survives; the *checkability* did
   not. That changed how much weight I put on any `citeturn`-cited figure in this estate: none,
   until dereferenced.

4. **I expected "Context is Logistics" to be the softest law and "Doctrine changes slower than
   strategy" to be among the firmest.** The opposite. Context is the best-evidenced law in either
   document; doctrine-slowness is falsified by the absence of the human mechanism (truce) plus the
   presence of a non-human one (model-version churn) that runs *faster* than strategy.

**What did NOT change:** I went in expecting to conclude that the measurement half is the valuable
half, and the evidence supported it. That is the one place a local subagent's bias most plausibly
shows, and I flag it rather than defend it: this is the estate's own emphasis, and I agreed with it.
An external reviewer should be asked specifically whether the four-verdict discipline and typed
evidence classes are as unprecedented as §Deliverable 14 items 4 and 5 claim.

---

## Open questions

See §Deliverable 12 (twenty). Two are for the parent rather than for research:

- Whether the estate wants a *falsifiable* research programme (which is what §Recommendation
  describes) or a *product narrative* (which is what the vision documents describe). These are
  compatible but they are not the same document, and the vision currently reads as the latter while
  being filed as the former.
- Whether `NOT-SUPPLIED` items in §Sources should become a work list. I would say yes: four
  unreadable primaries is a real gap in a foundational survey.

---

## Proposed architecture changes

*(Recommendations. I edited no file other than this one.)*

1. `ontology/00-core-ontology.md` — reduce to the 9 fundamental objects; move `Organization`,
   `Mission`, `Operation`, `Team`, `Capability`, `Knowledge`, `Running Estimate` to a "derived
   projections" section; delete `Cell`, `Signal`, `Field`; demote `Role` to an attribute; delete
   `Skill` as an owned object and reference Agent Skills.
2. `architecture/01-intent-contract-schema.md` — merge into the GreenContract; state explicitly that
   `factory/contract.py` is the implementation and this document is its pre-execution profile.
3. `architecture/08-organization-compiler-pipeline.md` — rename to **Org Planner**; make it
   explicitly partial; delete "Org-IR"; state that the pass list is a checklist, not a compilation.
4. `architecture/09-organizational-debugger-model.md` — rename to **conformance checker**; state
   that stochastic policies make single-run attribution invalid; require N-run statistics.
5. `architecture/02-organizational-staff-mesh.md` — mark `RESEARCH ONLY` and cite PROSA (1998) as
   prior art for the staff holon.
6. `foundations/FOUNDATIONAL_LAWS_DRAFT.md` — re-verdict per §Deliverable 8; add N1–N7; label
   Laws 10 and 15 as **policies**, not laws.
7. `vision/00-agent-army-master-context.md` — replace "Digital Twin" with "materialised projection";
   the mapping table's left column is a *source of hypotheses*, and should say so.
8. `agent-factory/blueprints/orchestrator_team.yaml` and `docs/agent-army/CURRENT_STATE.md` — pin
   `arXiv:2512.08296v1`, note v3.

## Proposed ADRs

- **ADR-0008 — Do not adopt "Artificial Organization Engineering" as a public category.**
  Publish as organisation-oriented programming for LLM agents. Revisit on one certified team plus
  one cleared structural A/B.
- **ADR-0009 — One contract object.** The GreenContract is the root; an Intent Contract is a
  GreenContract stated before execution.
- **ADR-0010 — Nine fundamental objects; everything else is a projection.**
- **ADR-0011 — Enforcement lives at the execution boundary, never in a prompt.**
- **ADR-0012 — Topology is an empirical parameter per model binding.** No topology ships without a
  same-budget A/B against one agent.
- **ADR-0013 — Every external citation must be dereferenceable.** `citeturn` tokens are
  `NOT-VERIFIED` until resolved to a URL and a version.

---

## Closing question, answered directly

> **If Artificial Organization Engineering is real, what are the irreducible primitives and design
> problems that distinguish it from ordinary multi-agent orchestration?**

Stated as plainly as the evidence allows: **on the current evidence it is not real as a discipline,
but there is an irreducible residue, and the residue is small, specific, and worth building.**

Orchestration and AOE share almost everything — agents, tasks, tools, messages, retries, state,
topology. Four things do not reduce to orchestration, and each is a design problem, not a feature:

**1. The instrument, and the state where the instrument was dark.**
Orchestration asks *did it run*. An organisation must ask *did it work, and can I tell*. That
requires a verdict vocabulary in which "I could not look" is not "I looked and it was fine", an
instrument proved able to register failure before its pass is admissible, and a grader the graded
party cannot write to. No orchestrator has any of this, and it is the one place I could not find
adequate prior art. **Irreducible primitives: `Contract`, `Evidence`, `Corpus`, and `UNMEASURABLE`.**

**2. Structure as an information-asymmetry decision, not a headcount decision.**
Orchestration adds workers for throughput. An organisation adds a member only when that member sees
something no existing member sees — because independence, not count, is what buys reliability
(N6). The design problem is *what each agent may see*, and it is a first-class, enforced,
architectural choice. **Irreducible primitive: visibility as a bounded, enforced attribute.**

**3. Context as an allocated, depleting, measurable supply.**
Orchestration treats context as a transcript. An organisation must treat it as logistics, because
its capacity term is now instrumented and monotonically degrading. This is Galbraith with a meter,
and it is the one place where the LLM substrate genuinely gives us something human organisation
theory never had. **Irreducible primitive: `Budget` — of tokens, of context, of authority.**

**4. Structure in its own state space — and the promotion ladder that gates entry to it.**
A workflow's topology is an input. An organisation's topology is also an output, and the design
problem is the *ratchet*: what evidence promotes an experience to knowledge, knowledge to skill,
skill to doctrine, and what demotes it — with a model-version change as a demotion event.
**Irreducible primitives: `OrganizationVersion` and the promotion thresholds.**

Everything else in the working hypothesis — roles, teams, cells, missions, staff functions, fields,
federation, compilers, debuggers, digital twins — is either already owned by a prior discipline,
already owned by an industry standard, or a metaphor.

**So: not a discipline. Four design problems, one of which (the instrument) this estate is already
unusually good at, one of which (independence) is a cheap decisive experiment away, and two of
which (context logistics, the promotion ratchet) are buildable now.** That is a research programme
with a name it can defend. It is not a category launch.

---

## Sources

**Repository (read directly, this session)**
- `agent-factory/docs/agent-army/CURRENT_STATE.md`; term sweep **re-executed by me**, returns nothing
- `agent-factory/blueprints/orchestrator_team.yaml`
- `agent-factory/factory/contract.py` (`:17-21`, `:52-60`, `:74-85`)
- `agent-factory/factory/evidence.py` (`:20-34`, `:43-73`, `:120-152`)
- `agent-factory/factory/corpus.py` (`:1-27`, `:74-109`)
- `agent-factory/evaluator_service/service.py` (`:1-36`, `:101-163`, `:203-216`)
- `agent-factory/factory/blueprint.py` (`:20-70`), `factory/metrics.py`, `factory/lanes.py:125`,
  `factory/bus.py:48`, `factory/readiness.py:1394`
- `agent-factory/README.md`
- `agent-army-research/`: `ontology/00-core-ontology.md`, `foundations/FOUNDATIONAL_LAWS_DRAFT.md`,
  `vision/00-agent-army-master-context.md`, `research/RESEARCH_PROTOCOL.md`,
  `research/ANSWER_TEMPLATE.md`, `architecture/00`, `architecture/08`, `adr/` listing

**Primary literature and specifications (fetched or read)**
- Kim et al., *Towards a Science of Scaling Agent Systems*, arXiv:2512.08296 — **v1 (9 Dec 2025)**,
  v2 (17 Dec 2025), **v3 (8 Apr 2026)** — https://arxiv.org/abs/2512.08296
- Cemri et al., *Why Do Multi-Agent LLM Systems Fail?* (MAST), arXiv:2503.13657
- Chen et al., *Toward an Organizational Science of Multi-Agent LLM Systems* (IMACS),
  arXiv:2607.25446
- Waites, *Artificial Organisations*, arXiv:2602.13275
- Zhu et al., *Can LLM Agents Sustain Long-Horizon Organizational Dynamics?* (TaskWeave),
  arXiv:2606.01199
- Shi et al., *Organizational Control Layer*, arXiv:2606.04306
- Dochkina, *Drop the Hierarchy and Roles*, arXiv:2603.28990 — **methodologically weak, see tiering**
- Weyns-lineage essay, *State of the Art on Self-adaptive Systems*, arXiv:2511.06352
- Smith, *The Contract Net Protocol*, IEEE Trans. Computers 29(12), 1980 — PDF read
- Anthropic, *How we built our multi-agent research system* — anthropic.com/engineering
- Anthropic, *Agent Skills* — claude.com/blog/skills (16 Oct 2025; open standard 18 Dec 2025)
- A2A Protocol Specification — a2a-protocol.org/latest/specification/
- Moise — moise-lang.github.io; JaCaMo — jacamo-lang.github.io
- Temporal documentation (workflows, event history, deterministic replay) — docs.temporal.io

**Read via credible secondary summary only (tiered down, marked `SECONDARY`)**
- Hübner, Sichman & Boissier, *Moise+* (2002) and *Developing organised MAS using Moise+* (2007)
- Ferber & Gutknecht, *AALAADIN* / AGR; MadKit
- Dignum, *OperA* / *OperettA*; Esteva et al., ISLANDER / AMELI
- Wooldridge, Jennings & Kinny, *Gaia* (JAAMAS 2000) — PDF unreadable, limitations NOT-ACCESSIBLE
- Boissier, Bordini, Hübner & Ricci, *Multi-Agent Oriented Programming*, MIT Press 2020
- Erman, Hayes-Roth, Lesser & Reddy, *Hearsay-II* (1980) — PDF is a scanned image
- Kephart & Chess, *The Vision of Autonomic Computing* (2003)
- Russell, van der Aalst, ter Hofstede & Edmond, *Workflow Resource Patterns*, CAiSE 2005
- Song & van der Aalst, *Towards comprehensive support for organizational mining*, DSS 2008
- Carley & Prietula, *Computational Organization Theory* (1994); ORGAHEAD; Levitt's VDT
- Armstrong, *Making reliable distributed systems…* (2003)
- Beer, *Brain of the Firm* (1972) / VSM; Ashby's requisite variety
- Van Brussel, Wyns, Valckenaers et al., *PROSA*, Computers in Industry 37(3), 1998
- Galbraith, *Organization Design: An Information Processing View*, Interfaces 4(3), 1974 — PDF scanned
- Mintzberg, five configurations; March, exploration/exploitation
- Nelson & Winter, *An Evolutionary Theory of Economic Change* (1982) — routine as memory/truce/goal
- Walsh & Ungson, *Organizational Memory*, AMR 16(1), 1991
- Malone, Laubacher & Dellarocas, *The Collective Intelligence Genome* (MIT SMR, 2010)
- Coase (1937); Williamson (1985)
- Skelton & Pais, *Team Topologies* (2019); Conway (1968)
- Grassé (1959); Dorigo, ACO
- ISO 23247-1 digital twin definition
- Kubernetes controller / operator reconciliation documentation
- OpenTelemetry GenAI semantic conventions
- SWE-bench audit literature (solution leakage, weak tests, contamination)
- Context-degradation literature (Liu et al. 2023; Chroma 2025, 18 models)

**NOT-ACCESSIBLE / NOT-SUPPLIED — named, not inferred around**
- Workflow Resource Patterns full text and exact pattern count — workflowpatterns.com fails TLS SNI;
  Springer requires authentication.
- *Capable language models can outgrow the benefits of collaboration*, Nature Machine Intelligence
  s42256-026-01268-y — auth redirect.
- Body text of arXiv:2512.08296 v1 — could not extract; the `−3.5%` / 95% CI and the `n^1.724`
  interaction-scaling figure remain **NOT-VERIFIED**.
- Gaia limitations section; Jennings, *Agent-Based Computing: Promise and Perils* (IJCAI-99);
  Wooldridge & Jennings, *Pitfalls of Agent-Oriented Development* (1998); Erman et al. Hearsay-II;
  Galbraith 1974 — all unreadable as text by this fetcher.
- No MAS or agent-eval source found that separates "the instrument could not run" from "it failed".
  This is a **failure to find**, not a demonstration of absence.
