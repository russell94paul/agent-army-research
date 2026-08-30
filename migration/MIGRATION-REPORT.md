# Migration report — separating Agent Army research from Agent Factory

**Date:** 2026-08-30 · **Outcome:** complete, with one incident (§Incident) and eight open
collisions (§Content collisions).

---

## Research repository

| | |
|---|---|
| **path** | `C:/Users/PaulRussell/repos/agent-army-research` |
| **branch** | `main` |
| **remote** | see §GitHub below |
| **file count** | **167 tracked** files, 146 markdown. 175 on disk — the extra 8 are gitignored personal Obsidian state (`appearance.json`, `themes/`, `workspace.json`) |
| **v5 baseline** | 150 files, 132 markdown — unmodified |
| **added by migration** | 17 tracked files: `legacy/` 13 · `migration/` 3 · `research/context/03-…` 1. Modified: `.gitignore`, `INDEX.md`, and two `.obsidian/` files Obsidian rewrote on first open |
| **commit hashes** | `8f1c276` bootstrap · migration commit recorded in `git log --oneline` |
| **validation** | `python scripts/validate_repo.py` → `{"markdown_files": 146, "research_prompts": 29, "errors": 0, "warnings": 0}`, exit 0 |

Regenerate the counts above with:

```bash
git ls-files | wc -l                                   # tracked
find . -name '*.md' -not -path './.git/*' | wc -l      # markdown
git status --ignored --short | grep '^!!'              # what is deliberately not tracked
python scripts/validate_repo.py
```

### Validation detail

- **All v5 content present** — 150/150 files copied byte-exact; `manifest.json` (the v5 per-file
  sha256 attestation) was **deliberately not regenerated**, so it still attests the pristine
  baseline. Migration additions are indexed in `INDEX.md`, not in `manifest.json`.
- **Research prompts substantive** — 29 prompts, none under 1,000 chars.
- **No empty markdown** — 0.
- **Obsidian links resolve** — 0 unresolved wikilinks. Two links written during migration pointed
  outside the vault (`docs/agent-army/CURRENT_STATE`) or at a `.yaml` (`RESEARCH-MANIFEST`); both
  were converted to plain code spans rather than left as broken links.
- **No dependency on older packs** — 0. The v3 stubs that *do* carry such a dependency were kept
  out of the tracked markdown and archived instead (§Files moved).
- **No secrets** — swept for `gh[pousr]_`, `xox[baprs]-`, `AKIA`, PEM headers, JWTs and
  `key/secret/token/password = "…"` assignments. Clean.
- **No machine-specific absolute paths** in the vault content. The two occurrences in this
  migration folder are deliberate provenance records of where agent-factory was measured.

---

## Agent Factory

| | |
|---|---|
| **path** | `C:/Users/PaulRussell/repos/agent-factory` |
| **branch created** | `docs/agent-army-research-separation`, from `feat/readiness-generator` @ `b4bac0d` |
| **remote** | `personal → https://github.com/russell94paul/agent-factory.git` — **unchanged** |

### Files moved

| From | To | Files |
|---|---|---|
| `docs/agent-army-research-pack/` ("v2") | superseded by v5 root; 6 divergent files at `legacy/research-pack-v2/`; complete pack at `legacy/archives/agent-army-research-pack-v2.zip` | 39 md + 1 nested zip |
| `docs/agent-army-research-pack-v3/` | 3 substantive files at `legacy/research-pack-v3/`; complete pack at `legacy/archives/agent-army-research-pack-v3.zip` | 17 md |

Both were **untracked** — `git log --all -- docs/agent-army-research-pack*` returns nothing, so
neither has a commit provenance to cite. Recorded in
[[migration/agent-factory-inventory-before|the inventory]] because it means agent-factory's history
never contained any Agent Army research at all.

33 of the v2 pack's 39 markdown files are byte-identical to their v5 counterparts (verified by
`cmp`) and were not duplicated into the vault. Archive integrity: `legacy/archives/SHA256SUMS.txt`.

### Files retained

Everything else. Specifically kept, with reasons in the inventory:

- **`docs/research/`** (55 files, ~3.6 MB) — **imported by the package.** `factory/dispatch.py`
  globs it at module scope, `factory/synthesis.py` reads `SYNTHESIS.md` and `answers/`,
  `factory/readiness.py` gates on both. It is code that happens to be Markdown.
- `docs/specs/`, `docs/findings.d/`, `docs/artifacts/`, `docs/evidence/`, `docs/board/` — read by
  `readiness.py`, `findings.py`, `schedule.py`, `build_board_artifact.py`.
- `README.md` line 93, `docs/research/agent-factory-research-prompts.md`, `docs/DEEP-REVIEW-PROMPT.md`
  — these record the decision to **cut** Agent Army and the precondition to revisit it. A decision
  not to build something is a product fact.
- All application source: `factory/` (42 modules), `evaluator_service/`, `tests/` (32 files),
  `scripts/`, `blueprints/`, `evals/`.

### Files split

One: **`BRAIN-DUMP.md`** — split by *extraction*, original untouched. Its Agent Army fragments are
quoted with line references and full provenance in
`research/context/03-origin-brain-dump-agent-army-excerpt.md`. The file is a verbatim crash
recovery; cutting it in half would destroy the property that makes it worth keeping.

### Files removed after verified migration

**None removed by this migration.** See §Incident — the two packs were removed by a concurrent
process, recovered, and archived here before anything else proceeded.

### Bridge files created

`agent-factory/docs/agent-army/` — the directory did not previously exist:

| File | Contents |
|---|---|
| `README.md` | The boundary, the one rule (*research does not imply implementation*), and what did not move |
| `RESEARCH_REPO.md` | Pointer to the sibling repo + a seven-row source-of-truth hierarchy |
| `CURRENT_STATE.md` | 20 concepts classified with file:line evidence — **the important one** |
| `APPROVED_CONCEPTS.md` | Empty, with the four reasons it is empty and the bar for a first entry |
| `IMPLEMENTATION_HANDOFFS.md` | Empty, with the promotion path and lifecycle |

### Links repaired

- 2 wikilinks in this repository (above).
- **0 links broken in agent-factory** — nothing tracked moved, so no reference could break.
- `INDEX.md` extended with `legacy/`, the new `migration/` documents and the new research context
  note, plus a regeneration command so the index can be checked rather than trusted.

### Tests / builds run

| Check | Result |
|---|---|
| `factory/` source present | 42 modules, 32 test files — unchanged |
| Import-time doc validation (`dispatch`, `synthesis`, `readiness`, `board`, `goals`, `teamplan`, `evidence`, `tasks`, `contract`, `corpus`) | **pass** — 30 gates, 5 lanes resolve |
| `git status` after bridge creation | only `?? docs/agent-army/` |
| `python -m pytest -q` (full suite) | **15 failed, rest passed** — all 15 in `tests/test_mutation_anchors_still_match.py`, and all 15 **reproduce at `b4bac0d`**, the parent commit, verified in a detached worktree. Pre-existing, not caused by this migration |
| Docs-dependent subset (`dispatch`, `synthesis_current`, `findings`, `evidence_classes`, `tasks`, `contract`, `corpus`, `repo_root`, `tracker_is_current`, `research_run`, `research_safeguards`) | **96 passed, 0 failed** |
| `python scripts/validate_repo.py` (research repo) | 0 errors, 0 warnings |

⚠ **The suite is not green, and was not green before this migration either.** The 15 failures are
`mutate_readiness_probes.py` anchors that no longer match their target — e.g.
`MAX_TERMINATION_ATTEMPTS = 4` *"appears 0 time(s) in orchestrator/pipelines.py, so the mutation
cannot be applied and that control is UNTESTED"*. They belong to the readiness-generator work on
the parent branch, touch no file this migration created, and are reported here rather than
absorbed into a claim of success.

The suite is also slow: repeated foreground runs were still going at 8–9 minutes. The full result
above comes from a run that was allowed to finish in the background.

---

## Incident — the packs were deleted mid-migration

Between the pre-migration inspection and the copy step, both
`docs/agent-army-research-pack/` and `docs/agent-army-research-pack-v3/` **disappeared from
agent-factory**, and `git status` went fully clean. They were untracked, so git could not recover
them.

- **Cause:** a concurrent Claude Code session on the same repository (`agent-factory-17`, started
  ~19 minutes before the deletion) appears to have been running the same brief and removed them.
  A freshly extracted `Downloads/agent-army-research-v5/` appeared at the same time.
- **Recovery:** all content was found intact in the Windows Recycle Bin and copied out. The
  recovered v2 tree was verified **byte-identical** to a `agent-army-research-pack-v2.zip` also
  found there, and the nested v3 zip was verified to hold the same 17 files as the recovered v3
  tree.
- **Bonus:** the Recycle Bin held a `agent-army-research-pack-v2.zip` that was never on disk during
  the inspection. It is archived here too.
- **Net loss:** none.

**Lesson, and it is the same one the inventory already makes:** the entire prior Agent Army
research corpus existed only as untracked working-tree files. It survived by luck — a delete that
happened to route through the Recycle Bin. Everything is now committed.

---

## Content collisions

Eight documents differ materially between the old packs and v5 and **require synthesis**. Full
write-ups with recommended actions in [[migration/content-collisions]].

| # | Document | Priority | One-line summary |
|---|---|---|---|
| C1 | `README.md` | **DECIDED** | v2 argued for the *same* repo; v5 and ADR-0001 argue for separate. Decided in v5's favour — but v2's reason (research drifts from code) is real and now rests on `CURRENT_STATE.md` staying fresh |
| C2 | `INDEX.md` | low | v5 supersedes; no research content at stake |
| C3 | R28 Governance | **high** | v5 dropped v2's four-layer `CONSTITUTION/POLICY/STRATEGY/PREFERENCE` model **and** the eight-item operator control surface (emergency stop, quarantine knowledge, rollback organization version…) |
| C4 | R29 Repo integration | **high** | v5 dropped v2's numbered 12-step substrate ordering. Recommend promoting it to a falsifiable hypothesis, not pasting it back into the prompt |
| C5 | R30 Evaluation | medium | Six concrete metrics lost, including **false-confidence rate** — the one metric that measures the system claiming success it cannot support |
| C6 | R31 Frontier primitives | medium | v5 dropped the ≥25-concept search quota (restore) and the `value × feasibility × novelty ÷ complexity` formula (do **not** restore — four unmeasured scores multiplied produce a number with no units) |
| C7 | R00 Foundations | low | v3 skeleton fully subsumed by v5; two residuals covered by R31 and R02 |
| C8 | Execution order | low | v3's 3 waves → v5's 6 waves; they disagree on where R20/R21/R28/R31 sit. v5's ordering (product thesis later) is more defensible |

---

## Stale research — assumptions that conflict with the current implementation

Kept, not deleted. Each needs a correction pass before the prompt it sits in is dispatched.

| Assumption | Where | Reality in agent-factory |
|---|---|---|
| The repo is an `apps/` + `packages/` monorepo with a frontend, backend, realtime transport and UI components | v5 `research/prompts/R29` audit schema; v2 R29 "Inspect" list; v2 `README.md` folder sketch | **It is a single Python package.** `factory/` (42 modules) + `evaluator_service/` + `tests/`. No `apps/`, no `packages/`, no frontend, no realtime transport. The UI is three generated static HTML files |
| A session manager, team schemas, task/mission schemas, tool abstraction and sandboxing exist to be inspected | v2 R29 "Inspect" list | `factory/sessions.py` reads Claude Code's own registry — it does not manage sessions. There are **no** team, task-schema, tool-abstraction or sandbox subsystems. There is no mission object at all |
| A durable event log can be the organizational source of truth | `adr/ADR-0002-event-log-as-organizational-source` | The only cross-agent channel, `factory/bus.py`, is **deliberately** ephemeral, gitignored, machine-local and one-file-per-writer — designed that way after F70/F71. ADR-0002 must either argue against that design or scope itself to a new log |
| World state can be materialized from that log | `adr/ADR-0003-materialized-world-state` | Nothing is materialized. `board.py` derives tasks from live gate measurement on every render, on purpose, so drift is structurally impossible. A materialized projection would reintroduce the failure mode `board.py:1-21` was written to remove |
| Agent Army is the direction of travel | v2 `README.md`; `vision/00-agent-army-master-context` | `README.md` in agent-factory lists **Agent Army / supervisor tiers** under *"What is deliberately absent"*, unlocked by *"one certified team, plus evidence a tier helps"*. The precondition is unmet |
| Research must live beside the code to stay grounded | v2 `README.md` §"Why same repo?" | Superseded by ADR-0001, but see C1 — the objection survives the decision |

---

## Product discoveries — facts the research programme currently misunderstands

These came out of reading the code, and none of them is in the research corpus. **Feed them into
Wave 0 rather than discovering them again in Wave 5.**

### 1. Multi-agent organization has already been tested here — and rejected on measured evidence

`blueprints/orchestrator_team.yaml` is a three-agent team that was designed, evaluated and killed.
Its header records a 180-configuration study (5 architectures, 3 model families, 4 agentic
benchmarks) finding multi-agent **averaging −3.5% against single-agent baselines**, with
**sequential tasks degrading 39–70%** — and connector migration is sequential shared-state work,
the class that did worst. It also notes every measured failure in this estate was a *seam* failure,
so adding mandatory LLM-to-LLM handoffs treats the wrong variable.

The file was **kept, not deleted**: *"a hypothesis that was tested and rejected, and the rejection
is worth more than the file's absence would be."*

It even states the unlock threshold, quantified: a same-budget A/B on the same tasks with the same
authoritative verifier showing **≥10pp absolute terminal-success gain**, or **≥20% lower cost at
indistinguishable success**, with no increase in side effects and every mandatory handoff **≥99%
accepted-and-correctly-consumed**.

**Implication.** This is the strongest existing prior-art result against the naive form of the
Agent Army thesis, and it is *our own*. R01 (prior art and novelty boundary) and R30 (evaluation)
should both start from it. R30's experiment design already has the right shape; what it lacks is
this baseline and this threshold.

### 2. The research corpus has no way to say "the instrument was dark"

`factory/contract.py:17-21` defines four verdicts and refuses to collapse them:
`PASS / FAIL / UNMEASURABLE / NOT_RUN`. *"A check whose instrument could not run has not passed."*
The same discipline recurs everywhere — `factory/runs.py:42` separates
`RECORDED / RECONSTRUCTED / NOT-RECORDED`; `factory/evidence.py:68-70` separates
`SATISFIED / ASSERTED / ABSENT`; `factory/goals.py` reports `NOT-MEASURED` rather than `0%`.

R30's metric taxonomy has no equivalent. A benchmark that cannot distinguish *"the mechanism did
not help"* from *"we could not measure it"* will report measurement gaps as negative results.

### 3. Grader independence is already engineered, and its remaining gap is already named

`factory/corpus.py` moved the eval corpus out of Python and into hashed JSON under `evals/`,
verified on every load, because *"an agent that can edit its own grader is not graded."*
`evaluator_service/` grades out of process — three routes, no fourth, and no route that writes a
verdict without scoring one. `factory/certify.py:19` is explicit that in-process `--calibrate`
scoring is *"worthless as evidence that an agent did not grade itself"*.

`corpus.py` also names what is still missing: separation is **evident and attributed, not
enforced** — enforcement means the corpus living where the scored agent has no write credential.

**Implication.** R44 (trust, reputation, epistemic independence) and R30's anti-gaming section
should extend this, not re-derive it. The `EVIDENT / ATTRIBUTED / SEPARABLE` triple is a better
starting vocabulary than anything currently in `governance/`.

### 4. Agent Army is gated, not merely unbuilt

`README.md`, `docs/research/agent-factory-research-prompts.md:55` and
`docs/DEEP-REVIEW-PROMPT.md:228` all encode the same rule: **agent army ← one certified team**.
The research programme is not currently aware it is operating behind a written precondition that
has not been met.

### 5. The prior research corpus was never under version control

Six weeks of Agent Army thinking lived entirely in untracked working-tree files, and was destroyed
and recovered during this migration (§Incident). That is a governance finding about how this
programme stores its own knowledge, and it belongs in R21/R43 (collective cognition, knowledge
economy) as a live example rather than a hypothetical.

---

## Open items

1. **15 pre-existing test failures in agent-factory** — `tests/test_mutation_anchors_still_match.py`,
   reproducing at `b4bac0d`. Not this migration's to fix, but they should be fixed before
   `feat/readiness-generator` merges, because they mean five readiness controls are currently
   **UNTESTED** rather than passing.
2. **Eight content collisions** — C3 and C4 should be resolved before W5 and before R29 is
   dispatched respectively.
3. **Push the research repository** — see §GitHub.
4. **Concurrent session** — `agent-factory-17` may hold its own view of this migration. Reconcile
   before merging anything.

---

## GitHub

`gh auth status` → authenticated as `russell94paul` (keyring), scopes
`gist, read:org, repo, workflow, write:packages`. The repository is created **private**; the
agent-factory remote is untouched.

If the create step did not run, the exact command is:

```bash
cd C:/Users/PaulRussell/repos/agent-army-research
gh repo create agent-army-research --private --source . --remote origin
git push -u origin main
```

---

## Recommended next action

**Do not start implementation.** Nothing is approved, and the product-side gate
(*one certified team*) is closed.

Begin the research programme with Wave 0, in this order:

```text
R00 — Foundations of Artificial Organization Engineering
      foundations/R00-foundations-of-artificial-organization-engineering.md

R01 — Prior Art and Novelty Boundary
      foundations/R01-prior-art-and-novelty-boundary.md

R02 — Canonical Ontology and Vocabulary
      foundations/R02-canonical-ontology-and-vocabulary.md
```

Attach to R01 the three product discoveries above — particularly the −3.5% multi-agent result and
its quantified unlock thresholds. R01 exists to find the strongest evidence against novelty, and
the strongest such evidence currently available was produced in-house and is not yet in the corpus.

Save answers to `research/answers/`, audit with `claude-skills/evidence-auditor`, synthesize to
`research/synthesis/W0-foundations.md`, and only then update `ontology/`, `architecture/` and
`governance/`. `START_HERE.md` steps 4–7.
