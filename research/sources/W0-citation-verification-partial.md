# W0 — citation verification (partial)

**Status: PARTIAL.** This covers the single most load-bearing external citation in Wave 0, verified
by hand against the primary source. A full audit of R00 and R01 across all citations is still
outstanding and should follow `claude-skills/evidence-auditor/SKILL.md`.

```yaml
verified_by: orchestrating session (local), by direct WebFetch of the primary source
verify_date: 2026-08-30
method: fetched the arXiv abstract page and compared it against what our own artefacts claim
verdict_vocabulary: SUPPORTED | PARTIALLY SUPPORTED | UNSUPPORTED | MISLEADING | NEEDS REPLICATION
```

Why this one first: it is the only external experimental result the estate had already promoted
into a **product decision** (`agent-factory/blueprints/orchestrator_team.yaml`) and then into a
**bridge document** (`agent-factory/docs/agent-army/CURRENT_STATE.md`). It was quoted forward three
times before anyone opened the paper.

---

## The source

**arXiv:2512.08296** — *Towards a Science of Scaling Agent Systems*, Kim, Gu, Park, Park,
Schmidgall, Heydari, Yan, Zhang, Zhuang, Liu, Malhotra, Liang, Park, Yang, Xu, Du, Patel, Althoff,
McDuff, Liu. DOI `10.48550/arXiv.2512.08296`.

Versions: **v1** 9 Dec 2025 · **v2** 17 Dec 2025 · **v3** 8 Apr 2026.

---

## Claim-by-claim

| # | Claim | Made by | Verdict |
|---|---|---|---|
| 1 | The study exists and is the one our blueprint cites | R01 | **SUPPORTED** — title, author list and the sequential-degradation pole all match |
| 2 | 180 configurations, 5 architectures, 3 model families, 4 benchmarks | `orchestrator_team.yaml:17-18` | **PARTIALLY SUPPORTED** — accurate for **v1**; superseded. v3 is **260 configurations, six benchmarks**, five architectures, three LLM families |
| 3 | Multi-agent averaged −3.5% vs single-agent | `orchestrator_team.yaml:18`, and this repo's migration report | **MISLEADING AS PRESENTED** — see below |
| 4 | …with 95% CI [−18.6%, +25.7%] | `agent-factory/docs/research/answers/R2-answer-topology.md:15` | **SUPPORTED at source, DROPPED downstream** — the answer states it; the blueprint header and the first version of `CURRENT_STATE.md` both omitted it |
| 5 | Sequential tasks degrade 39–70% | `orchestrator_team.yaml:18` | **SUPPORTED** — v3's abstract names **−70.0% on sequential planning** as one pole |
| 6 | A centralised system improved a parallelisable financial task by +80.9% | `R2-answer-topology.md:15` | **SUPPORTED** — v3 abstract says **+80.8%** (version drift of 0.1pp, consistent) |
| 7 | "Landed in Nature MI 2026", paywalled, NOT-ACCESSIBLE | R01 | **UNSUPPORTED** — the arXiv record shows **no journal reference**. And the expanded version is *not* paywalled: it is arXiv v3, free |

### On claim 3

The v3 abstract does not lead with an aggregate at all. It frames the result as:

> "Relative performance change compared to single-agent baseline ranges from **+80.8%** on
> decomposable financial reasoning to **−70.0%** on sequential planning, demonstrating that
> **architecture-task alignment determines collaborative success**."

So "multi-agent averages −3.5%" is a v1 aggregate, with an interval spanning zero, extracted from a
paper whose own conclusion is *it depends on architecture–task fit*. Quoting the mean as the
finding is a selective read of the source.

**Two further v3 results neither of our artefacts carries**, and both are useful:

- a **capability-saturation effect** — coordination yields diminishing returns once single-agent
  baselines exceed a threshold;
- **architectures without centralized verification propagate errors more** than those with it.

The second is an independent external argument for the non-LLM authoritative verifier
`agent-factory/evaluator_service/` already implements.

---

## What this episode demonstrates

The figure travelled **answer → blueprint header → bridge document** and got *more* confident at
every hop:

```text
R2-answer-topology.md:15   -3.5%, CI [-18.6%, +25.7%], "OPEN RESEARCH, not production evidence",
                           +80.9% on the other pole
        ↓  interval dropped, +80.9% dropped, caveat dropped
orchestrator_team.yaml:18  "multi-agent averaging -3.5% against single-agent baselines"
        ↓  promoted to a headline
CURRENT_STATE.md           "the strongest existing prior-art result against ... Agent Army"
```

Nothing here was fabricated. Every hop was a faithful *summary* of the hop above it, and the
uncertainty fell out anyway. That is the mechanism, and it is reproducible.

**Consequence for the research programme:** this is a worked example for R21 (collective cognition)
and R43 (knowledge economy), not a hypothetical. It is also the strongest available argument for
the estate's own rule that **every published figure carries its basis** — a rule that existed, in
writing, while this happened.

**Consequence for the decision:** none. The blueprint's rejection of the three-agent topology
survives, and v3 supports it *better* than v1 did — connector migration is sequential shared-state
work, the −70.0% pole named in the paper's own abstract.

---

---

## Resolved: R00 and R01 disagreed about whether the −3.5% exists at all

The two Wave 0 lanes ran in parallel and could not see each other. They returned **contradictory**
verdicts on the same figure, which is exactly what independent lanes are for.

| Lane | Verdict |
|---|---|
| **R01** | Found it verbatim in the full text, with the interval |
| **R00** | *"in no abstract of any version and I could not extract it from the body: `NOT-VERIFIED`"* |

**Resolution: R01 is correct.** Fetched `https://arxiv.org/html/2512.08296v1` directly:

> "Aggregating across all benchmarks and architectures, the overall mean MAS improvement is
> **−3.5% (95% CI: [−18.6%, +25.7%])**, reflecting substantial performance heterogeneity with
> **high variance (σ=45.2%)**."

Both lanes were *partly* right and the distinction matters: the figure is **in the body of v1, not
in any abstract**. R00 searched abstracts and reported honestly that it could not extract it from
the body — a correct `NOT-VERIFIED` given what it actually did, not a fabrication. R01 went to the
body and found it.

**σ=45.2% is new** — neither our blueprint header nor `R2-answer-topology.md` carries it, and it is
the most informative number in the sentence. A standard deviation of 45.2 points around a mean of
−3.5 is the whole finding: the effect is enormous in both directions and the average is nearly
meaningless.

v1 parameters confirmed: **180 configurations · 4 benchmarks** (Finance Agent, BrowseComp-Plus,
PlanCraft, Workbench) · 5 architectures · **R²=0.513**. v3: 260 configurations · 6 benchmarks ·
**R²=0.373**. R00's claim that the model's explanatory power *fell* between versions is
**SUPPORTED**.

---

## Resolved: the category name is taken, twice — both CONFIRMED

R00 recommended not launching "Artificial Organization Engineering" publicly. Both supporting
citations were checked directly and **both are real and on point**.

**`arXiv:2602.13275` — "Artificial Organisations", William Waites, 5 Feb 2026. CONFIRMED.**
Publishes under the name, with a thesis close to ours:

> "Human institutions achieve reliable collective behaviour differently: they mitigate the risk
> posed by misaligned individuals through organisational structure. Multi-agent AI systems should
> follow this institutional model using **compartmentalisation and adversarial review** to achieve
> reliable outcomes through **architectural design rather than assuming individual alignment**."

**`arXiv:2607.25446` — "Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling
Who, How, and Which Algorithm", Chen, Song, Jin, Ren, Zhang, 28 Jul 2026. CONFIRMED.**
IMACS makes Belbin roles, Mintzberg coordination and RACI accountability into *executable,
independently swappable configuration* — the organizational-compiler thesis, published five weeks
ago. Its ablation finding is a direct hit on **"intent before topology"**:

> "Accountability placement changes outcomes exactly when the protocol routes the deliverable
> through the accountable agent, and **the winning placement flips across model families, so
> organizational design cannot be hard-coded; it must be revalidated, or learned, for each model
> binding.**"

If organizational design must be re-validated per model binding, then a compiler from intent to a
fixed topology is compiling against a target that moves whenever the model does. That is a
mechanism-level objection, not a naming objection, and it should be carried into R02 and R23.

---

## New finding: the estate's external research corpus has no resolvable citations

R00 reported the `−3.5%` source was cited as `citeturn3view0` — an opaque ChatGPT citation
token. Verified and **larger than reported**:

```bash
# in agent-factory
grep -roh "turn[0-9]*\(view\|search\)[0-9]*" --include="*.md" . | grep -v worktrees | sort -u | wc -l
```

| File | Token occurrences |
|---|---|
| `docs/research/R16-evidence-pack.md` | 526 |
| `docs/research/R8-evidence-pack.md` | 336 |
| `docs/research/answers/R3-answer-control-plane.md` | 133 |
| `docs/research/answers/R2-answer-topology.md` | 111 |
| `docs/research/answers/R4-answer-agnostic-optimizer-run2.md` | 103 |
| `docs/research/answers/R1-answer-eval-harness.md` | 92 |
| `docs/research/answers/R4-answer-agnostic-optimizer.md` | 87 |
| **total** | **1,388 occurrences · 215 distinct tokens · 7 files** |

`R2-answer-topology.md` contains **no arXiv id, no DOI and no URL** — its only citations are these
tokens. They resolve inside the ChatGPT session that produced them and nowhere else.

**This is the mechanism behind the whole −3.5% episode.** The figure did not lose its provenance
through carelessness downstream; there was never a resolvable citation to walk back to. Anyone who
wanted to check it had to re-run the literature search, which is what R00 and R01 each independently
did today — four and a half months late, and only because they were told to.

**Recommendation (agent-factory, not this repo):** a lint that fails on `turn\d+(view|search)\d+`
in `docs/research/`, plus a back-fill pass resolving the tokens that support load-bearing claims.
Filed here rather than fixed — it is a product-repo change and belongs to whoever owns that corpus.

---

## Still outstanding

- **R01's seven CRITICAL novelty verdicts rest on citations nobody has opened.** KB-ORG (Sims,
  Corkill & Lesser, JAAMAS 2008), ODML, Organization Self-Design (Ishida/Gasser/Yokoo, IEEE TKDE
  1992), Co-Fields/TOTA (ACM TOSEM 2009), PROSA's "staff holons" (1998). Until these are opened,
  treat the CRITICAL verdicts as `PLAUSIBLE`, not `CONFIRMED`.
- **R00's Moise+/JaCaMo/electronic-institutions lineage** is unaudited on the same basis.
- R00 marked **four primary PDFs `NOT-ACCESSIBLE`** (scanned images). Correctly declared, still a gap.
- The search **R01 says it did not run**: `UNMEASURABLE` as a first-class verdict in the
  **metrology and software-testing** literatures. R01's narrowest-defensible-novelty claim rests
  entirely on that gap, so **the one surviving novelty claim is the least verified thing in Wave 0.**
