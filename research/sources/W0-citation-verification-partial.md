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

## Still outstanding

- Full citation audit of **R01**'s remaining sources — in particular KB-ORG (Sims, Corkill & Lesser,
  JAAMAS 2008), ODML, Organization Self-Design (Ishida/Gasser/Yokoo, IEEE TKDE 1992), Co-Fields/TOTA
  (ACM TOSEM 2009), and PROSA's "staff holons" (1998). These carry R01's seven CRITICAL novelty-risk
  verdicts and **none of them has been independently opened yet.**
- Full citation audit of **R00** once it completes.
- The search R01 says it did **not** run: `UNMEASURABLE` as a first-class verdict in the
  **metrology and software-testing** literatures. R01's narrowest-defensible-novelty claim rests on
  that gap, so the claim is unconfirmed until someone looks there.
