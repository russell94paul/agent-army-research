# Product Boundary — agent-factory and the Agent Army runtime

## Status

**DESIGN SKETCH — not researched, not decided.**

This document assumes both sides eventually ship as products. That is a *premise*, not a
finding. It is written now because the seam between them is cheap to design today and
expensive to retrofit, and because the schemas below are the part that gets re-derived.

Distinguish from [[repo-boundary/RESEARCH-VS-PRODUCT]], which divides **repositories**
(where a document lives). This divides **products** (what each tool does at runtime).

Everything asserted about agent-factory here was measured against the code on 2026-08-30.
Everything asserted about the runtime is drawn from `architecture/` and is speculative by
definition — none of it is built.

---

## Function of each

### agent-factory — the build-time product

**Function: it produces capability and proves it works.**

Its unit of output is *a blueprint certified against a contract, graded by an instrument the
blueprint does not control.* It answers one question:

```text
Does this work, and how do we know?
```

It owns blueprints, eval corpora, the grader, contracts and verdicts, readiness gates,
findings, and the cost ledger. It is finished with a capability the moment that capability is
certified. It has no opinion about what the capability is then used for.

### Agent Army runtime — the run-time product

**Function: it directs certified capability at changing intent.**

Its unit of work is *a mission delegated with bounded authority.* It answers a different
question:

```text
What is happening, and why?
```

It owns intent contracts, missions, the staff mesh, temporal echelons, world state, the
durable event log, doctrine, the organizational debugger and the evolution chamber. It never
decides whether a capability is good — it cannot.

### Said as one sentence

> agent-factory decides **whether a thing works**.
> The runtime decides **what to do with the things that work**.

---

## The invariant that makes the split principled

`factory/corpus.py` and `factory/certify.py` enforce a rule at agent scale:

> An agent that can edit its own grader is not graded.

`--calibrate` scores in-process under the caller's own identity and is documented as
*"worthless as evidence that an agent did not grade itself"* (`factory/certify.py:15-17`).
`--remote` submits to a separate service with a separate identity.

Scaled up, that rule **is** the product boundary:

> **An organization that can certify its own capabilities is not certified.**

This is why the two must be separate products rather than two modules of one, and it is what
makes the evolution chamber safe to build: **evolution proposes, the factory disposes.** The
organization may generate structural variants freely; it may not bless them.

---

## The interface

Three artifacts cross the boundary. Nothing else does.

### 1. The capability record — factory writes, runtime reads

```yaml
capability: {id: connector.windsorai.client_a, version: 3, blueprint_sha: ...}
contract:   {verdict: PASS}            # PASS | FAIL | UNMEASURABLE | NOT_RUN
grading:
  corpus_sha: ...                      # verified against evals/MANIFEST.sha256
  route:      remote                   # remote | calibrate
  grader:     evaluator_service@...    # NOT the submitting agent's identity
evidence:   {target: SATISFIED, consumer: SATISFIED,
             regression: SATISFIED, rollback: SATISFIED}
cost:       {basis: RECORDED, p50_tokens: ..., p50_wall_s: ...}
limits:     {unmeasured: [...]}        # what the corpus could not exercise
```

Every field already has a producer in agent-factory: `contract.py:17-21` (verdict),
`corpus.py` (corpus hash), `evidence.py:48,68-70` (classes and states), `runs.py:42` (cost
basis). The record is a join, not a new subsystem.

`limits.unmeasured` is load-bearing and must never be omitted. A capability record that does
not say what the corpus *failed to exercise* invites the runtime to use it outside the
envelope it was graded in.

### 2. `admit()` — the gate

```text
admit(mission, registry) -> ADMITTED | DEGRADED(missing) | BLOCKED(reason)
```

Refusal rules, each inherited from an existing mechanism rather than invented:

| Condition | Result | Why |
|---|---|---|
| `grading.route: calibrate` | BLOCKED | self-graded is not graded |
| `contract.verdict: UNMEASURABLE` | BLOCKED for privileged work | a dark instrument is not a pass |
| `evidence.rollback: ABSENT` | BLOCKED for any mutating mission | no rollback, no mutation |
| request outside `limits.unmeasured` | DEGRADED, escalate to human | ungraded territory |
| capability absent from registry | DEGRADED, demand signal | the factory's work queue |

`DEGRADED` is not an error state. `staffing.unstaffable` is the runtime telling the factory
what to build next.

### 3. The field record — runtime writes, factory reads

Same shape as the capability record, measured in production instead of in the corpus. The
factory diffs certified-vs-field:

- field score below certified score, corpus gap, new eval case, re-certify
- capability exercised outside its graded envelope, boundary finding
- failure mode absent from the corpus, new test

**This diff is what makes the two tools one system rather than two products that ship
alongside each other.** Without it the arrow points only one way and the runtime never
improves the factory.

---

## Ownership

| | agent-factory | Agent Army runtime |
|---|---|---|
| Unit | certified blueprint | delegated mission |
| Time | before deployment | during operation |
| Grader / corpus | **owns** | must not have |
| Contracts and verdicts | **owns** | consumes |
| Durable event log | deliberately absent | **owns** |
| Materialized world state | deliberately absent | **owns** |
| Intent, authority, doctrine | none | **owns** |
| Evolution / morphogenesis | grades the output | **proposes** |
| Human surface | board, gates, tracker (*what is proven*) | Command World (*what is live*) |

The two "deliberately absent" rows are measured, not assumed: `factory/bus.py:1-27` documents
its event bus as ephemeral, machine-local, gitignored and one-file-per-writer, and
`docs/agent-army/CURRENT_STATE.md` records that nothing in the factory is materialized as
organizational state. The runtime is not duplicating the factory there; it is building what
the factory chose not to.

---

## Where the boundary blurs

Five known soft spots. Each needs a decision before either side hardens.

1. **Two evidence schemas.** `factory/evidence.py` defines four classes and three states;
   [[architecture/06-knowledge-evidence-model]] defines its own. **If these diverge, the field
   record cannot be diffed against the capability record and the feedback loop silently stops
   working.** Highest-priority convergence.
2. **Teams.** `factory/teamplan.py` sequences a team's steps; the staff mesh forms teams.
   Proposed rule: the factory certifies a team *blueprint*; the runtime instantiates and
   staffs from it.
3. **Skills.** [[architecture/07-skill-capability-doctrine-model]] versions and evaluates
   skills; the factory certifies them. Proposed rule: shared registry, asymmetric write —
   factory certifies, runtime applies and contributes after-action evidence.
4. **Measurement vs certification.** The runtime will want to score live missions. It may
   **measure**; it may never **certify**. Keep that verb distinction in the schema itself.
5. **Two dashboards.** The board/flow surfaces and the organizational debugger overlap.
   Unresolved.

---

## What else the ecosystem needs

Two products do not make an ecosystem. Below is what sits between and beneath them.
**Status is measured**: `EXISTS` means it is in agent-factory today; `PARTIAL` means something
real is there but not ecosystem-grade; `ABSENT` means nothing anywhere.

### Layer 1 — Trust: who says this is true

| Component | Function | Status |
|---|---|---|
| **Evaluator service** | The independent grader. The certificate authority of the ecosystem. | `PARTIAL` — `evaluator_service/` exists, single-tenant, three routes |
| **Identity and attestation** | Signs capability and field records. Without it a record is an unverifiable claim. | `ABSENT` |
| **Capability registry** | Stores, versions and resolves capability records. Must support **revocation** — the CVE story for a capability later found unsafe. | `ABSENT` |
| **Corpus store** | Hosts and hashes graded task worlds. | `PARTIAL` — `evals/` + `MANIFEST.sha256`, repo-local |

Identity is the quiet blocker. Every refusal rule in `admit()` depends on trusting
`grading.grader`, and nothing today can prove that field.

### Layer 2 — Control: what makes authority real

| Component | Function | Status |
|---|---|---|
| **Policy enforcement point** | Enforces `may` / `may_not` against real systems. Without it, bounded authority is advisory. | `ABSENT` |
| **Credential broker** | Issues scoped, short-lived credentials per mission. | `ABSENT` |
| **Cost metering** | Live budget caps and chargeback, not retrospective. | `PARTIAL` — `runs.py` is retrospective and repo-local |

⚠ The enforcement point is the largest single gap. `authority.may_not: [mutate prod]` is a
*sentence in a YAML file* until something sits in the request path and refuses. Everything the
governance layer promises rests on a component nobody has built.

### Layer 3 — Memory: what the organization knows

| Component | Function | Status |
|---|---|---|
| **Event store** | Durable, replayable, cross-entity event log. | `ABSENT` — `bus.py` is deliberately ephemeral |
| **World-state store** | Materialized organizational state at time T. | `ABSENT` |
| **Knowledge store** | Typed, provenance-carrying findings and evidence. | `PARTIAL` — `docs/findings.d/` is untyped Markdown, repo-local |

### Layer 4 — Human: how a person stays in the loop

| Component | Function | Status |
|---|---|---|
| **Escalation channel** | Delivers a `DEGRADED` or a bounded-authority breach to a human, and proves it arrived. | `ABSENT` |
| **Command World** | The live organizational surface. | `ABSENT` |
| **After-action review** | Turns a closed mission into doctrine and eval cases. | `ABSENT` |

An escalation path nobody has proven can fire is the failure mode H7 warns about: observability
must exist *before* structural autonomy.

### Layer 5 — Safety: where variants run before production

| Component | Function | Status |
|---|---|---|
| **Simulation / staging substrate** | Runs an organizational variant somewhere that is not production. | `ABSENT` |

H8 makes replay and simulation the precondition for safe optimization. The evolution chamber
cannot be built before this exists, or it evolves against live systems.

### The honest tally

Of roughly fourteen components, **none is ecosystem-ready**, five are partial, and the two
load-bearing ones for safety — the **policy enforcement point** and the **simulation
substrate** — are entirely absent. Any roadmap that puts the evolution chamber before those
two is proposing to evolve an organization with no sandbox and no enforceable limits.

---

## Three ways to start an ecosystem

In order of how close each is to something that could ship.

### 1. The evidence commons — open the corpus format

**Bet:** the scarce thing in agentic software is not agents, it is *honest evaluation*.

Publish the eval corpus format, the `MANIFEST.sha256` hashing discipline, and the four-verdict
contract — in particular `UNMEASURABLE`, which has no equivalent in SWE-bench, HELM or OpenAI
evals and is the differentiator. Others contribute graded task worlds and failure cases.

- **Starts from:** what agent-factory already is. Little new to build.
- **Moat:** becoming the vocabulary for agent evidence. Standards are sticky.
- **Network effect:** each corpus contributed makes every certification more meaningful.
- **Risk:** eval commons are hard to bootstrap. Mitigation — seed with the corpora under
  `evals/`.
- **Precedent:** SWE-bench, HELM, OpenAI evals — none separates the grader from the graded,
  which is the opening.

### 2. The certified capability registry — open the capability record

**Bet:** a registry whose entries are *graded by an independent instrument* beats one whose
entries are self-described.

Publish the capability record schema and run the evaluator service as gatekeeper. Anyone may
submit a blueprint; only `route: remote` results are admissible.

- **Starts from:** `evaluator_service/` plus the schema above. **Blocked on identity and
  attestation** (Layer 1) — without signing, the registry's central claim is unverifiable.
- **Moat:** the grader and the corpora. The registry itself is the commodity.
- **Network effect:** more certified capabilities, more staffable missions, more demand for
  certification.
- **Risk:** you must operate grading infrastructure and cost scales with submissions. Needs an
  economic model before launch, not after.
- **Precedent:** Docker Hub, crates.io — none makes independent grading a precondition of
  publication.

### 3. The doctrine library — open skills, doctrine and after-action evidence

**Bet:** organizational know-how that has been *used and measured* beats know-how that was
merely written down.

Publish [[architecture/07-skill-capability-doctrine-model]] and let others share executable
doctrine, carrying the after-action evidence of every run. Doctrine accumulates a track record
rather than a star count.

- **Starts from:** nothing that exists. Furthest out.
- **Moat:** the evidence loop. A runbook with 400 measured executions cannot be copied by
  writing a better runbook.
- **Network effect:** strongest of the three, and compounding — usage improves the artifact.
- **Risk:** ⛔ depends on the runtime existing, and the evidence on whether multi-agent
  structure pays is *conditional*, not settled. Per
  [[research/sources/W0-citation-verification-partial]], the source
  (arXiv:2512.08296 v3, published as *"Capable language models can outgrow the benefits of
  collaboration"*, Nature MI 8(7), 2026) concludes **architecture–task alignment determines
  collaborative success** — ranging from **+80.8%** on decomposable financial reasoning to
  **−70.0%** on sequential planning. Two findings bear directly on this ecosystem: sequential
  shared-state work is the class that degrades worst, and a **capability-saturation effect**
  means coordination buys less as single-agent baselines improve.

  ⚠ Do **not** quote "multi-agent averages −3.5%" as the finding. That is a v1 aggregate with a
  95% CI of **[−18.6%, +25.7%]** — an interval spanning zero — drawn from a paper whose own
  conclusion is that it depends on fit. `blueprints/orchestrator_team.yaml` still carries the
  v1 figure and the superseded "180 configurations" (v3 is 260 across six benchmarks).
- **Precedent:** Ansible Galaxy, Terraform registry, Claude skills — all distribute know-how
  with no measurement attached.

### Recommendation

**Start with (1).** It is the only one that ships from what exists today, it is the honest
unmet need, and it produces the corpora that (2) requires in order to mean anything. (2)
follows once there is enough graded material to make a registry entry worth trusting, and once
Layer 1 identity exists. (3) is gated on the runtime being justified at all, which is a
research question rather than a product one.

---

## Open questions this sketch does not answer

- One product with two surfaces, or two products with separate buyers?
- Who operates the evaluator service in a multi-tenant world, and who pays for grading?
- Does the runtime ever run without a factory, in a degraded uncertified mode?
- What is the revocation story when a certified capability is later found unsafe?
- Does `admit()` live in the runtime, in the registry, or between them?

---

## Provenance

Written 2026-08-30, during the research/product repository separation. Derived from the
measured state of agent-factory in `docs/agent-army/CURRENT_STATE.md`, from
[[architecture/00-target-architecture]] and
[[architecture/08-organization-compiler-pipeline]], and from `PROGRAM_MANIFEST.md` H1-H10.

Related: [[repo-boundary/RESEARCH-VS-PRODUCT]] ·
[[repo-boundary/WHAT-STAYS-IN-AGENT-FACTORY]] ·
[[adr/ADR-0001-keep-agent-army-research-separate]]
