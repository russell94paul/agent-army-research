# Agent Factory — pre-migration inventory

State of `agent-factory` as measured on **2026-08-30**, before anything was moved.

```text
toplevel   C:/Users/PaulRussell/repos/agent-factory
branch     feat/readiness-generator          (HEAD b4bac0d)
remote     personal  https://github.com/russell94paul/agent-factory.git  (fetch + push)
status     ?? docs/agent-army-research-pack/
           ?? docs/agent-army-research-pack-v3/
           — nothing else; no modified tracked files
```

⚠ **The only two Agent Army artefacts in the repository were untracked.**
`git log --all -- docs/agent-army-research-pack*` returns nothing: neither pack was ever committed,
so neither has a commit provenance to cite. This is recorded rather than glossed because it means
agent-factory's history contains **no** Agent Army research at all — the entire body of it lived in
an uncommitted working tree, one `git clean` away from gone.

`docs/agent-army/` **did not exist.** It is created by this migration, not cleaned by it.

---

## Method

Every file below was read, not classified from its name. Term sweep run across the whole tree for:

```text
Agent Army · Artificial Organization · Artificial Organization Engineering · Mission Command
Intent Contract · Running Estimate · Organizational Compiler · Org-IR · Collective Cognition
stigmergy · morphogenetic · Evolution Chamber · Doctrine · Capability Readiness
Cognitive Logistics · Command World
```

Outside the two packs the sweep returned **19 hits in 6 tracked files** (plus identical copies in
four `.worktrees/` checkouts of the same repo, which are not separate artefacts). Every one is
inventoried below.

---

## The inventory

### 1. The research packs — MOVE

| | |
|---|---|
| **PATH** | `docs/agent-army-research-pack/` (39 md + 1 nested zip, ~71 KB) |
| **PURPOSE** | Self-described "Agent Army Research Pack v2": vision, vocabulary, target architecture, intent-contract schema, staff mesh, cognitive logistics, event/world-state model, design system, Command World layout, R20–R34 Deep Research prompts, roadmap, ADR-0001. |
| **CURRENT PRODUCT FACT?** | No. Nothing in it describes code that exists. |
| **RESEARCH / SPECULATIVE?** | Entirely. |
| **ACTION** | **MOVE** |
| **DESTINATION** | Superseded by the v5 baseline at the vault root. 33 of 39 files are byte-identical to v5 and were not duplicated; the 6 divergent files are at `legacy/research-pack-v2/`; the complete pack is archived byte-exact at `legacy/archives/agent-army-research-pack-v2.zip`. |
| **RATIONALE** | This is the definition of speculative organizational architecture. Its own README even proposed the folder layout this migration replaces (see collision C1). |

| | |
|---|---|
| **PATH** | `docs/agent-army-research-pack-v3/` (17 md, ~4 KB) |
| **PURPOSE** | "Agent Army Research Pack v3": adds R00 Foundations, a 3-wave execution order, and 14 one-line prompt stubs pointing back at the v2 pack. |
| **CURRENT PRODUCT FACT?** | No. |
| **RESEARCH / SPECULATIVE?** | Entirely. |
| **ACTION** | **MOVE** |
| **DESTINATION** | 3 substantive files at `legacy/research-pack-v3/`; complete pack archived at `legacy/archives/agent-army-research-pack-v3.zip`. |
| **RATIONALE** | Superseded by v5, which contains the full R00 and a 6-wave manifest. The 14 stubs each say only that the reader should use the expanded prompt from the *v2* pack instead — a dependency on a pack this repository does not carry, and the exact sentence `scripts/validate_repo.py` rejects. They live only in the archive, byte-exact. |

### 2. `BRAIN-DUMP.md` — SPLIT

| | |
|---|---|
| **PATH** | `BRAIN-DUMP.md` (10,091 B, tracked) |
| **PURPOSE** | Verbatim recovery of the 2026-08-20 request that produced `docs/research/agent-factory-research-prompts.md`, after a VS Code crash. Two versions, 18:47 and 20:04. Mixes Agent Army organizational ideas (11 term hits) with agent-factory product scope — Agentic Gym, AgnosticOptimizer, connector pipeline team, dashboard, technical diagrams. |
| **CURRENT PRODUCT FACT?** | Yes — it is the origin record of the factory's live research programme. |
| **RESEARCH / SPECULATIVE?** | Partly. |
| **ACTION** | **SPLIT (by extraction; original retained intact)** |
| **DESTINATION** | Stays at `agent-factory/BRAIN-DUMP.md`. Agent Army fragments excerpted with line references and provenance to `research/context/03-origin-brain-dump-agent-army-excerpt.md`. |
| **RATIONALE** | The file's value *is* that it is verbatim and recovered; cutting it in half destroys that. So the original is untouched and the research repo takes a cited excerpt, not a move. This is the only genuine SPLIT in the migration. |

### 3. `docs/research/` — KEEP (and it is code, not documentation)

| | |
|---|---|
| **PATH** | `docs/research/` — 28 files at top level, `answers/` 25, `sources/` 2 (~3.6 MB incl. evidence packs) |
| **PURPOSE** | agent-factory's **own** research programme: R1–R19 prompts, their answers, `SYNTHESIS.md` (219 KB, the decision record), evidence packs, concept inventory, UI surface inventory. |
| **CURRENT PRODUCT FACT?** | **Yes — load-bearing.** |
| **RESEARCH / SPECULATIVE?** | No. Different programme, different subject (eval harness, topology, control plane, optimizer, build velocity, session manager, data engineering). |
| **ACTION** | **KEEP** |
| **DESTINATION** | — |
| **RATIONALE** | ⛔ **The package imports and validates against this directory.** `factory/dispatch.py` globs `docs/research/*.md` for prompt ids and parses each file's `**Status:**` declaration; `factory/synthesis.py` reads `docs/research/SYNTHESIS.md` and `docs/research/answers/`; `factory/readiness.py` gates on `docs/research/answers/R*-followup*.md` and on `SYNTHESIS.md` §5. Moving any of it breaks imports and gates. Two incidental term hits (*stigmergy* in R8/R16 data-engineering answers, *"agent army"* in R13) are quotations inside an unrelated survey, not Agent Army research. |

### 4. `docs/specs/`, `docs/findings.d/`, `docs/artifacts/`, `docs/evidence/`, `docs/board/` — KEEP

| | |
|---|---|
| **PATH** | `docs/specs/` (7), `docs/findings.d/` (16), `docs/artifacts/` (4), `docs/evidence/` (~30 incl. screenshots), `docs/board/` (4) |
| **PURPOSE** | Current architecture (`architecture-v0.md`, `control-room.md`, `product-end-state.md`, `golden-workflow-fit.md`, `terminal-configuration.md`), corrected-premise findings F20–F82, the generated tracker/board artifacts, and render/probe evidence. |
| **CURRENT PRODUCT FACT?** | Yes, all of it. |
| **RESEARCH / SPECULATIVE?** | No. |
| **ACTION** | **KEEP** |
| **DESTINATION** | — |
| **RATIONALE** | Zero Agent Army term hits. `factory/readiness.py` reads `docs/specs/`, `docs/findings.d/` and `docs/artifacts/`; `factory/schedule.py` regenerates `docs/artifacts/agent-factory.html`; `factory/findings.py` reads `docs/findings.md` as data. Code-linked documentation by the strictest test: moving it breaks something. |

### 5. `README.md` — KEEP

| | |
|---|---|
| **PATH** | `README.md` line 93 |
| **PURPOSE** | Scope table row: `\| Agent Army / supervisor tiers \| One certified team, plus evidence a tier helps \|` |
| **CURRENT PRODUCT FACT?** | **Yes.** It is a record of a deliberate *cut*, and states the condition for revisiting it. |
| **RESEARCH / SPECULATIVE?** | No. |
| **ACTION** | **KEEP** |
| **DESTINATION** | — |
| **RATIONALE** | A decision not to build something is a product fact and belongs beside the product. Removing it would delete the reason Agent Army is absent from the codebase. |

### 6. `docs/research/agent-factory-research-prompts.md`, `docs/DEEP-REVIEW-PROMPT.md` — KEEP

| | |
|---|---|
| **PATH** | `docs/research/agent-factory-research-prompts.md` L17, L55 · `docs/DEEP-REVIEW-PROMPT.md` L228 |
| **PURPOSE** | The prompts record that "Agent Army (level 5)" was **Cut for now** — *"Crucible already asked whether levels 4–5 are real structure or ceremony. With zero certified teams…"* — and the review prompt encodes the unlock rule: *"agent army ← one certified team"*. |
| **CURRENT PRODUCT FACT?** | **Yes**, and the most important ones in this table. |
| **RESEARCH / SPECULATIVE?** | No — these are gating decisions about speculative work, which is a different thing. |
| **ACTION** | **KEEP** |
| **DESTINATION** | Cited in `docs/agent-army/CURRENT_STATE.md` and `APPROVED_CONCEPTS.md`. |
| **RATIONALE** | This is the answer to "why is none of this built": it was scoped out on purpose, with a named precondition. `docs/research/` is also import-validated (see §3). |

### 7. Application source and tests — KEEP, untouched

| | |
|---|---|
| **PATH** | `factory/` (44 modules), `evaluator_service/`, `tests/` (33 files), `scripts/`, `blueprints/`, `evals/`, `pyproject.toml` |
| **PURPOSE** | The product. |
| **CURRENT PRODUCT FACT?** | Yes. |
| **RESEARCH / SPECULATIVE?** | No. |
| **ACTION** | **KEEP** |
| **DESTINATION** | — |
| **RATIONALE** | Zero Agent Army term hits in any `.py` file across `factory/`, `evaluator_service/` and `scripts/`. Nothing in the product implements Agent Army vocabulary, which is itself the central finding — see `docs/agent-army/CURRENT_STATE.md`. |

### 8. `.worktrees/` — REVIEW (no action)

| | |
|---|---|
| **PATH** | `.worktrees/artifact/`, `certify/`, `control-plane/`, `cp-rename/` |
| **PURPOSE** | Four live git worktrees on lane branches. Each carries its own copy of `BRAIN-DUMP.md`, `README.md`, `docs/artifacts/agent-factory.html` and `docs/research/agent-factory-research-prompts.md`, producing duplicate term hits. |
| **CURRENT PRODUCT FACT?** | They are checkouts, not artefacts. |
| **RESEARCH / SPECULATIVE?** | n/a |
| **ACTION** | **REVIEW — no action taken** |
| **DESTINATION** | — |
| **RATIONALE** | Editing a worktree edits another branch. The bridge documents land on a branch off `feat/readiness-generator` and reach the lane branches when those merge. Deliberately out of scope. |

---

## Summary

| Action | Items | Files |
|---|---|---|
| **MOVE** | 2 research packs | 56 (39 + 17) |
| **SPLIT** | `BRAIN-DUMP.md` | 1 (retained; excerpt created) |
| **KEEP** | product source, tests, `docs/research/`, `docs/specs/`, `docs/findings.d/`, `docs/artifacts/`, `docs/evidence/`, `docs/board/`, `README.md` | everything else tracked |
| **REVIEW** | `.worktrees/` | 4 checkouts, untouched |

**Nothing tracked in agent-factory was moved or deleted by this migration.** The only files that
left the repository were the two untracked packs, and both are archived byte-exact here first.
