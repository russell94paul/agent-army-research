# Origin brain dump — the Agent Army fragments

## Provenance

| | |
|---|---|
| Source | `agent-factory/BRAIN-DUMP.md` |
| Source status | **tracked and retained in agent-factory** — this is an excerpt, not a move |
| Original capture | 2026-08-20, sessions 18:47 and 20:04, recovered verbatim after a VS Code crash |
| Extracted | 2026-08-30, during the research/product repository split |

`BRAIN-DUMP.md` is the recovered verbatim record of the request that produced agent-factory's own
research programme (`docs/research/agent-factory-research-prompts.md`). It stays in agent-factory
because it is that programme's origin document and splitting a *verbatim recovered* file would
destroy the thing that makes it worth keeping.

What follows is the subset that concerns Agent Army as an organizational idea, quoted exactly,
with the line numbers it occupies in the source. Read it as **the earliest statement of intent**,
predating every prompt in `research/prompts/`.

---

## The fragments

> **L33 / L144** — We should clearly define what Agent Army, Agent Team Agents consist off how the
> can be configured, communicate with eachother
>
> **L34 / L145** — maybe there should be an agent or agent team responsible for picking the correct
> team members for a specific task
>
> **L36 / L147** — the agent army agent team or agent should iterate on the task until the optimal
> configuration is found - then deploy the team on the real run.
>
> **L38** — should each army, team, agent store run data to allow agent versioning
>
> **L56** — Agentic Gym to train Agent Army, Agent Team Manager, Agent Team and Agents
>
> **L60–64** — Agent Communication Module:
> Agent to Agent / Agent Team Manager to Agent / Agent Team Manager to Agent Team Manager /
> Agent Army to one or many Agent Team Managers / Agent Army to Agent Army
>
> **L73 / L174** — There should be a simulator tool for constructing the optimal agent
> army/agent manager/agent for the task/project
>
> **L85 / L186** — identify all repos/infrastructure/access/credentials required and the proces of
> deploying an agent army, agent team manager, agent team, agent

---

## Why this matters to the research programme

Five of this repository's canonical concerns are already present in the origin dump, in a
pre-theoretical form. Tracing them keeps the programme honest about what is genuinely new:

| Brain-dump fragment | Concept it anticipates | Where it now lives |
|---|---|---|
| "an agent or agent team responsible for picking the correct team members" | adaptive / morphogenetic team formation | [[research/prompts/R22-organizational-os-stigmergy-morphogenesis]] |
| "iterate until the optimal configuration is found — then deploy on the real run" | offline evolution before live deployment | [[adr/ADR-0007-evolution-offline-first]] |
| "store run data to allow agent versioning" | organizational genome / versioned organization | [[research/prompts/R23-organizational-compiler-genome-governance]] |
| "simulator tool for constructing the optimal army" | counterfactual organization simulation | [[research/prompts/R24-evolution-simulation-counterfactuals]] |
| five-tier communication module | staff mesh / echelon addressing | [[architecture/02-organizational-staff-mesh]] |

## The tension worth recording

The dump repeatedly frames the goal as **"the optimal configuration"** — a search for a best
team shape. This repository's governing principle is that Agent Army must optimize for **verified
outcomes, not activity** ([[CLAUDE]]), and R30/R35 both insist a primitive earns its place only
against a declared baseline.

Those are not the same objective. "Optimal configuration" is a property of the organization;
"verified outcome" is a property of the work it delivers. A configuration search that is not
anchored to an outcome measure is exactly the architecture-by-metaphor failure
[[research/prompts/R30-evaluation-benchmarks-experiments]] exists to prevent.

**Open question for R00/R02:** is "optimal organization" a well-formed objective at all, or only
ever a derived statistic of verified mission success?
