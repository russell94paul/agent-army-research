# Research Answer — R01 / Prior Art and Novelty Boundary

## Metadata

```yaml
research_id: R01
run_date: 2026-08-30
status: complete
researcher_or_model: >
  Claude Opus 5 (claude-opus-5[1m]) running as a LOCAL SUBAGENT inside Claude Code,
  spawned by the Agent Army research team lead. Independence disclosure below.
repository_commit:
  agent-army-research: 5b8c4bf (branch main)
  agent-factory: a691043 (branch docs/agent-army-research-separation)
repository_access: >
  Full read access to agent-army-research and agent-factory. No writes made outside this file.
web_access: yes — WebSearch + WebFetch, 32 searches, 5 direct artefact fetches
primary_sources_read: >
  FETCHED AND READ IN FULL OR SUBSTANTIALLY (tier OBSERVED):
    - arXiv:2512.08296 abstract page (v-latest)
    - arXiv:2512.08296v1 abstract page
    - arXiv:2512.08296v1 full HTML text (targeted extraction of aggregate statistics)
    - docs.crewai.com/en/concepts/processes
    - agent-factory: blueprints/orchestrator_team.yaml, docs/agent-army/CURRENT_STATE.md,
      docs/research/answers/R2-answer-topology.md (targeted extraction)
    - agent-army-research: foundations/R01, ANSWER_TEMPLATE, RESEARCH_PROTOCOL,
      ontology/00, vision/01, architecture/01,02,03,05,06,07,08,09,10,11,
      research/context/01,02, research/prompts/R22
  CITED FROM SEARCH-RESULT SYNTHESIS, NOT READ IN FULL (tier DERIVED — see research debt):
    ~40 further papers/specifications named in the Sources section.
repositories_inspected: >
  agent-factory (read), agent-army-research (read). No third-party source trees were cloned;
  the LLM-framework layer was assessed from official documentation, not from source. This is a
  stated limitation, not a claim of source-level verification.
evidence_limitations: >
  1. The Nature Machine Intelligence version of the load-bearing scaling study is PAYWALLED
     (303 redirect to idp.nature.com). NOT-ACCESSIBLE. The arXiv preprint was read instead.
  2. Most historical MAS/COT literature (1980–2010) is behind ACM/IEEE/Springer paywalls. I have
     verified BIBLIOGRAPHIC EXISTENCE and the substance of each system's claim as reported by
     multiple independent search syntheses, but I did not read those PDFs. Treat every pre-2015
     description in this document as DERIVED, not OBSERVED.
  3. I did not read the source of LangGraph, AutoGen, CrewAI, MetaGPT or the OpenAI/Claude agent
     SDKs. Only CrewAI's process documentation was fetched directly.
```

### Independence disclosure (required by the brief)

This pass ran as a **local subagent, not an outside model**. Both halves of that matter:

- **Less independent than an external deep-research tool.** I read the Agent Army drafts before
  I searched (I needed the concept definitions to search for them at all), so my search terms are
  contaminated by our vocabulary. I mitigated this by searching for *mechanisms* rather than our
  names, and by running exact-string collision checks on our coined terms last. But a genuinely
  blind reviewer would have started from the literature and never seen `vision/01`.
- **Stronger on file-and-line claims.** I can and did open `orchestrator_team.yaml`,
  `CURRENT_STATE.md` and `R2-answer-topology.md` and quote them exactly, verify the internal
  citation chain, and detect where a number lost its uncertainty between hops. An external model
  could not have done that.

I did **not** consult Zeus Memory or the wiki; this question is a literature question.

---

## Executive conclusion

**Agent Army is, at the concept level, overwhelmingly not new.** Of the 15 named concepts, my
assessment is:

| Novelty risk | Count | Concepts |
|---|---|---|
| **CRITICAL** — the idea exists, was implemented, was published, and in several cases was *named almost identically* | 7 | Organizational Compiler, Org-IR, Organizational OS, Stigmergic Fields, Morphogenetic Teams, Organizational Debugger, Staff Mesh |
| **HIGH** — strong direct precedent, differences are of substrate not of idea | 5 | Intent Contract, Collective Cognition Fabric, Executable Doctrine, Capability Readiness, Federated Agent Armies |
| **MEDIUM** — precedent exists in adjacent fields but the specific composition is thinly explored | 2 | Evolution Chamber, Cognitive Logistics |
| **LOW** — under-explored as posed | 1 | Temporal Echelons (and even here, "current ops / future ops / plans" and anytime-algorithm deliberation scheduling both precede us) |

The single most damaging finding for the programme's framing: **automated organization design for
multi-agent systems is a solved-and-published research problem from 2008.** KB-ORG (Sims, Corkill
& Lesser, *Autonomous Agents and Multi-Agent Systems*, 2008) takes situational parameters plus
application-level and coordination-level knowledge and *generates organization designs*, searching
a candidate space with pruning — which is the Organizational Compiler, including the diagnostics.
ODML (Horling & Lesser) is the organizational modelling language it searches over — which is
Org-IR. Organization Self-Design (Ishida, Gasser & Yokoo, IEEE TKDE 1992) supplies runtime
composition/decomposition of the agent population — which is Morphogenetic Teams. Field-based
coordination (Mamei & Zambonelli's Co-Fields, and the TOTA middleware, ACM TOSEM 2009) is
literally "computational fields" over a distributed substrate — which is Stigmergic Fields, and
it shipped as middleware. And PROSA (Van Brussel et al., 1998), the holonic manufacturing
reference architecture, already contains **"staff holons"** that "assist the basic holons with
expert knowledge" — which is the Staff Mesh, under the same word.

**What appears true.** The organizational abstraction layer Agent Army proposes was built between
1980 and 2010 for symbolic/BDI agents, was academically successful, and did not reach industry.
It failed on adoption, not on coherence. The LLM era changes exactly three input variables — the
agents are now general-purpose and cheap to instantiate, natural-language intent is now
machine-consumable without ontology engineering, and the failure distribution has moved from
"agents cannot do the task" to "agents do the task and nobody can tell whether it worked". None
of those three changes make the *organizational concepts* new. They make the *economics* of
building them different, and they make one specific sub-problem — verification — newly load-bearing.

**What remains uncertain.** Whether organizational structure helps at all at the LLM layer. The
strongest controlled evidence available says the average multi-agent effect is **−3.5%** against
single-agent baselines — but with a 95% interval of **[−18.6%, +25.7%]**, i.e. *not distinguishable
from zero*, which is a different and weaker statement than the one our own blueprint file makes.

**What we should do.** Keep every mechanism. Rename most of them. Stop claiming category
creation. Narrow the novelty claim to the one thing I could not find prior art for: **an
organizational runtime in which the unit of organizational truth is an evidence-gated, four-verdict
claim — where `UNMEASURABLE` is a first-class outcome that cannot be collapsed into pass or fail,
and where the refusal to close without evidence lives in the store rather than in agent
instructions.** That is defensible, small, already partially built in `agent-factory`, and I found
nothing in the organizational-MAS, process-mining, autonomic-computing or LLM-agent literature that
does it.

**What we should explicitly not do.** Do not use the words *compiler*, *OS*, *fabric*, *mesh*,
*doctrine*, *evolution chamber*, or *digital twin of the organization* in any external-facing
document without a prior-art footnote — each one is either a live trademark-adjacent product
category, an existing named research field, or a widely-used term meaning something else. Do not
claim stigmergy, morphogenesis or organizational compilation as inventions. Do not repeat the
−3.5% figure without its confidence interval. And do not build the Evolution Chamber, Stigmergic
Fields, Morphogenetic Teams or Federation before there is one certified team — a precondition
`agent-factory` already records as unmet.

Deliverable locations: **timeline** §Deliverable 1 · **lineage graph** §Deliverable 2 ·
**vocabulary collision table** §Deliverable 3 · **novelty risk map** §Deliverable 4 ·
**recommended terminology** §Deliverable 5 · **top 25 prior systems** §Deliverable 6 ·
**claims we must not make** §Deliverable 7 · **closing question** §Narrowest defensible claim.

---

## Question decomposition

The subquestions actually investigated:

1. For each of the 15 concepts, does a materially similar prior concept exist, and what is it called?
2. Does our *exact coined term* already denote something else? (String-level collision, run last
   and deliberately, because a term collision is a marketing failure independent of a design failure.)
3. Was the prior concept ever *implemented*, or only proposed? Implemented prior art is far more
   damaging to a novelty claim than a paper.
4. Why did the prior work stop? Was it refuted, superseded, or merely unadopted? These have
   opposite implications for us.
5. Which of the LLM era's changes are genuinely new *inputs*, and which are re-labelled old ones?
6. Is the in-house −3.5% claim real, and is our summary of it faithful?
7. Where the literature and our drafts disagree about a word's meaning, what is the literature's meaning?
8. What is the smallest claim that survives all of the above?

---

## Deliverable 1 — Historical timeline

```
1959   Grassé coins "stigmergie" — coordination via traces left in a shared environment
1967   Koestler coins "holon" — the part/whole unit later used for holonic manufacturing
1973   Hewitt: Actor model. 1986 Agha formalises it
1974   Forgy: Rete algorithm → the substrate of every later business-rules engine
1974   Sadin (NASA): Technology Readiness Levels — readiness as a graded, auditable scale
1976   Hearsay-II operational; 1980 Erman et al. publish → the blackboard architecture
1980   Smith: Contract Net Protocol — task announcement / bid / award, IEEE Trans. Computers
1982   Corkill: distributed problem solving; organizational structuring in DAI
1985   Gelernter: Linda tuple spaces. Wegner: transactive memory systems
1986   Nii: "Blackboard Systems" (AI Magazine, 2 parts) — the canonical control-loop account
        Meyer: Design by Contract. Minsky: Society of Mind
1987   Bratman: Intention, Plans and Practical Reason → BDI
1988   Dean & Boddy: anytime algorithms + deliberation scheduling (compute allocated over horizons)
1990s  Erlang/OTP supervision trees ship in production telecoms — "let it crash", restart strategies
1991   Walsh & Ungson: Organizational Memory. SEI: Capability Maturity Model
1992   Ishida, Gasser & Yokoo: ORGANIZATION SELF-DESIGN — runtime composition/decomposition of
        the agent population (IEEE TKDE 4(2))
1993+  Levitt et al. (Stanford): the VIRTUAL DESIGN TEAM — computational organization theory;
        simulate an organization, predict duration/cost/coordination quality before building it
1994   Carley & Prietula: Computational Organization Theory as a named field
1995   Hutchins: Cognition in the Wild — distributed cognition. WfMC workflow reference model
1996   Decker & Lesser: TÆMS task structures + GPGP coordination; "exploring organizational
        designs with TÆMS"
1997   Decker, Sycara & Williamson: MIDDLE-AGENTS — matchmakers/brokers over capability
        advertisements. Later LARKS matchmaker (2002)
1998   Ferber & Gutknecht: AALAADIN / AGR (Agent–Group–Role) organizational meta-model
        Van Brussel et al.: PROSA holonic reference architecture — includes STAFF HOLONS
1999   FIPA Abstract Architecture; agent platforms (AMS, DF, ACC) standardised
2000   Wooldridge, Jennings & Kinny: Gaia — first complete AOSE methodology; Brueckner:
        "Return from the Ant" — pheromone infrastructure for manufacturing control
2001   IBM autonomic computing manifesto. Foster, Kesselman & Tuecke: "Anatomy of the Grid" —
        VIRTUAL ORGANIZATIONS as the unit of federation
2002   Hübner, Sichman & Boissier: Moise+ organizational model
        Poutakidis, Padgham & Winikoff: DEBUGGING MAS USING DESIGN ARTIFACTS (AAMAS'02)
        Parunak & Brueckner: digital pheromone mechanisms (AAMAS'02)
2003   Kephart & Chess: The Vision of Autonomic Computing — the MAPE-K loop
        Esteva et al.: ISLANDER/AMELI electronic institutions — norms specified and enforced
2004   Mamei & Zambonelli: Co-Fields / TOTA — field-based coordination as middleware
        Dignum: OperA. van der Aalst: process mining takes off
2005   van der Aalst, Reijers & Song: discovering social networks from event logs →
        ORGANIZATIONAL MINING as a named subfield of process mining
2008   Sims, Corkill & Lesser: KB-ORG — FULLY AUTOMATED knowledge-based organization design
2008   ORA4MAS: organisational artifacts — the organization itself as first-class runtime objects
2012   Doursat, Sayama & Michel: MORPHOGENETIC ENGINEERING (Springer) — a named field
2013   Boissier et al.: JaCaMo — agents + environment + organization in one platform
2015   Mouret & Clune: MAP-Elites / quality-diversity — archives of diverse elites, not one fitness
2018   Gartner names DIGITAL TWIN OF AN ORGANIZATION (DTO) as a market category
2019   Dehghani: Data Mesh. W3C PROV-O already standard for provenance
2023   MetaGPT encodes SOPs into agent prompt sequences; Generative Agents; AutoGen; ChatDev
        MemGPT: OS-style virtual context paging for LLMs
2024   Hu, Lu & Clune: ADAS / Meta Agent Search — agents that program better agents
        AFlow, AgentSquare, GPTSwarm — automated agentic-workflow/topology search
        MCP (Nov). OpenTelemetry GenAI semantic conventions SIG forms (Apr)
2025   A2A protocol (Apr), donated to Linux Foundation (Jun) — agent cards, capability discovery
        Cemri et al.: MAST — 14 failure modes over 1,600+ traces, 7 frameworks
        Darwin Gödel Machine — empirical self-modifying agent lineage with an archive
        Karpathy popularises "context engineering". Anthropic publishes its multi-agent research
        system (90.2% internal-eval gain, ~15× tokens); Cognition publishes "Don't Build Multi-Agents"
        Dec: Kim et al., "Towards a Science of Scaling Agent Systems" — 180 configurations
2026   That study expands to 260 configurations and lands in Nature Machine Intelligence
        Aug: Agent Army research programme begins (this document)
```

---

## Deliverable 2 — Concept lineage graph

```
                     ┌──────────────── MILITARY / ORGANIZATION THEORY ────────────────┐
Prussian Generalstab ─→ Continental staff system (S1–S9) ─→ Running Estimates (FM 5-0)
        │                                                          │
        │                                            ┌─────────────┴─────────────┐
        │                                            ▼                           ▼
        │                                     [STAFF MESH]              [CAPABILITY READINESS]
        │                                            ▲                           ▲
        │                          PROSA staff holons (1998)          SORTS → DRRS (C-levels,
        │                          Middle-agents (Decker 1997)         METs, "ready for what?")
        │                          Blackboard control (1980)           TRL (1974) · CMM (1991)
        │                                                              K8s readiness probe (2015)
        │
Mission Command / Commander's Intent ──→ [INTENT CONTRACT] ←── BDI intentions (Bratman '87)
        │                                     ▲   ▲   ▲       ←── Design by Contract (Meyer '86)
        │                                     │   │   └────────── Deontic norms / e-institutions
        │                                     │   └──────────────  RFC 9315 intent-based networking
        │                                     └──────────────────  K8s declarative desired state
        │
Doctrine publications ──→ [EXECUTABLE DOCTRINE] ←── Rete (1974) → Drools → OPA/Rego "policy as code"
                                    ▲                ←── Ponder / Rei / KAoS / XACML
                                    └────────────────── MetaGPT: SOPs encoded into prompt sequences

Army logistics ─────────→ [COGNITIVE LOGISTICS] ←── Information Logistics (Deiters, Haftor, 2000s)
                                    ▲                ←── MemGPT virtual context paging (2023)
                                    └────────────────── "Context engineering" (2025)

Current ops / Future ops / Plans ─→ [TEMPORAL ECHELONS] ←── Anytime algorithms + deliberation
                                                              scheduling (Dean & Boddy 1988)
                                                          ←── Speculative execution / prefetch

Federated Mission Networking ──→ [FEDERATED AGENT ARMIES] ←── Grid VIRTUAL ORGANIZATIONS (2001)
                                            ▲                 ←── FIPA interoperability (1999)
                                            └───────────────────  A2A agent cards (2025) / MCP

                     ┌──────────────── COMPUTING / MAS LINEAGE ───────────────────┐
Actor model (1973) ──→ Erlang/OTP supervision trees ──┐
Blackboard (1980) ───→ shared workspace ──────────────┤
Linda tuple spaces (1985) ───────────────────────────┼─→ [ORGANIZATIONAL OS]
FIPA platform: AMS/DF/ACC (1999) ────────────────────┤        ▲
Moise+ → S-Moise+ → ORA4MAS → JaCaMo (2002–2013) ────┘        │ collides with EOS® (business),
                                                              │ DC/OS, "AI OS" marketing
Contract Net (1980) ──→ Middle-agents (1997) ──→ Matchmaking/LARKS ──→ A2A agent cards

AALAADIN/AGR (1998) ┐
Gaia (2000)         ├──→ organizational modelling languages ──→ ODML (Horling & Lesser)
Moise+ (2002)       │                                              │
OperA (2004)        ┘                                              ▼
                                                            [ORG-IR]  ← LLVM IR (metaphor source)
                                                                   │   ← BPMN/BPEL (executable
                                                                   │      process IR)
Organization Self-Design (1992) ──┐                                ▼
TÆMS/GPGP (1996) ─────────────────┼──→ KB-ORG (2008) ────→ [ORGANIZATIONAL COMPILER]
ODML search/pruning ──────────────┘        ▲                       ▲
                                           │                       └── ADAS / AFlow / AgentSquare
                                    "generating and choosing            (2024, LLM era)
                                     organisations for MAS" (2023)

Organization Self-Design (1992) ──→ [MORPHOGENETIC TEAMS] ←── Morphogenetic Engineering (2012)
Holonic/PROSA reorganisation ────────────▲                 ←── Amorphous computing / swarm
                                          └──────────────────── DyLAN/AgentVerse/EvoMAC (LLM era)

Grassé stigmergy (1959) → ACO (1992) → digital pheromones (Parunak/Brueckner 2000–2002)
                                                 │
Artificial potential fields (Khatib 1986) ───────┼──→ Co-Fields / TOTA (2004–2009)
                                                 │            │
                                                 └────────────┴──→ [STIGMERGIC FIELDS]

Genetic algorithms → Novelty search → MAP-Elites / quality-diversity (2015)
                          │                          │
                          └── AutoML / NAS ──────────┼──→ [EVOLUTION CHAMBER]
                                                     │        ▲
                          Shadow deployment / VDT ───┘        └── ADAS, DGM, self-evolving
                          organizational simulation                agents surveys (2024–25)

Omniscient/time-travel debugging ──┐
Distributed tracing (Dapper→OTel) ─┼──→ [ORGANIZATIONAL DEBUGGER]
W3C PROV-O provenance ─────────────┤          ▲
Process mining → ORGANIZATIONAL ───┘          └── Poutakidis/Padgham/Winikoff (2002):
  MINING (van der Aalst 2005)                     debugging MAS from design artifacts

Distributed cognition (1995) ┐
Transactive memory (1985)    ├──→ [COLLECTIVE COGNITION FABRIC] ←── "data fabric" (term collision)
Organizational memory (1991) │                 ▲
Blackboard / tuple spaces ───┘                 └── Generative Agents / MemGPT / knowledge graphs
```

---

## Prior art

Per the template's per-concept block format. `novelty risk` uses the scale in Deliverable 4.

```text
concept                     Intent Contract
earliest relevant precedent Contract Net Protocol (Smith 1980) for the word "contract" as a
                            task-allocation object; Design by Contract (Meyer 1986) for
                            pre/postcondition/invariant structure; Bratman (1987) + BDI for
                            "intention" as a persistent commitment that constrains later choice;
                            deontic-logic norms (permission/prohibition/obligation) as the
                            authority envelope, operationalised in ISLANDER/AMELI (2003–05).
modern precedent            RFC 9315 (IRTF NMRG, 2022): "intent" = "a set of operational goals
                            and outcomes, defined in a declarative manner without specifying how
                            to achieve or implement them" — that is our objective + desiredEndState,
                            standardised, four years ago, and the RFC exists *specifically* because
                            the word was being used loosely. Kubernetes' declarative desired state.
                            2026 O-RAN work already uses the exact phrase "intent contract".
what transfers              Invariants with severity + enforcement mode; the authority envelope
                            (allowed/forbidden/requires-approval) is standard deontic structure and
                            has 20 years of enforcement machinery behind it; escalation conditions.
what does not               Our schema's `verificationRequirements` + `requiredEvidenceTypes` is
                            NOT standard. RFC 9315 intent has no evidence contract; e-institution
                            norms are enforced by observing actions, not by requiring proof of
                            outcome. This is the one part that is ours.
novelty risk                HIGH on the object; LOW on the evidence-requirement field.
```

```text
concept                     Organizational Compiler
earliest relevant precedent Organization Self-Design (Ishida, Gasser & Yokoo, IEEE TKDE 1992):
                            formalised "organizational knowledge" and gave composition/decomposition
                            primitives that change the agent population and knowledge distribution.
modern precedent            ⛔ KB-ORG (Sims, Corkill & Lesser, JAAMAS 2008): "a fully automated,
                            knowledge-based organization design framework" that uses situational
                            parameters plus application-level AND coordination-level design
                            knowledge to prune and direct a search over candidate organizations.
                            ODML (Horling & Lesser) is the modelling language whose search space it
                            prunes. Also: "Generating and choosing organisations for multi-agent
                            systems" (JAAMAS 2023). In the LLM era: ADAS/Meta Agent Search (2024),
                            AFlow, AgentSquare — automated search over agent-system designs.
what transfers              Nothing needs to transfer; the thing exists. What transfers to us is
                            KB-ORG's key distinction — application-level vs coordination-level
                            design knowledge — which our 10-pass pipeline does not make and should.
what does not               KB-ORG targeted a distributed sensor network with known task structures
                            (TÆMS). Our input is natural-language mission intent, which is a genuinely
                            new front end; and our pass 8 (verification-plan generation) has no
                            counterpart in KB-ORG or ODML.
novelty risk                CRITICAL. "We built a compiler that turns intent into an organization"
                            is a 2008 paper with our name on it removed.
```

```text
concept                     Org-IR
earliest relevant precedent AALAADIN/AGR (Ferber & Gutknecht 1998) — a meta-model with notation
                            and vocabulary for MAS organizations; Gaia's role/interaction models
                            (2000).
modern precedent            ODML (an organization design *modelling language* whose whole purpose
                            is to be searched over), Moise+ organizational specification XML,
                            OperA, OMNI, ISLANDER's declarative institution language. Outside MAS:
                            BPMN/BPEL/XPDL are executable process IRs with 25 years of tooling;
                            ArchiMate is the enterprise-architecture equivalent.
what transfers              Everything. Moise+ separates structural / functional / deontic
                            specifications — a three-way split our single flat Org-IR lacks and
                            probably needs.
what does not               None of these carry evidence, capability-with-sample-size, or a
                            verification plan as first-class IR elements.
novelty risk                CRITICAL as a category. The name "Org-IR" is free; the artefact is not.
```

```text
concept                     Organizational OS
earliest relevant precedent FIPA Abstract Architecture (1999) — AMS, Directory Facilitator, ACC:
                            an agent platform is precisely a runtime substrate for agents,
                            directories and message transport. Erlang/OTP supervision trees are
                            the production-proven version of "the runtime owns team lifecycle,
                            failure and restart policy".
modern precedent            ORA4MAS (2008) is the sharpest hit: it reifies "the organisation and
                            the organisation infrastructure itself ... in terms of agents and
                            artifacts, as first-class basic abstractions" — an organizational
                            runtime, shipped, on the JaCaMo platform (2013).
what transfers              The A&A insight (organization as manipulable runtime artifacts, not as
                            a config file) is directly applicable and better than our draft.
                            OTP restart strategies (one-for-one / one-for-all / rest-for-one) are a
                            ready-made vocabulary for cell failure policy.
what does not               None of them had a durable, replayable, cross-entity event log as the
                            organizational source of truth (our ADR-0002). That is a real gap in
                            the prior art, though it is standard practice elsewhere (event sourcing).
novelty risk                CRITICAL, and the TERM is worse than the concept — see Deliverable 3.
```

```text
concept                     Collective Cognition Fabric
earliest relevant precedent Blackboard architecture (Hearsay-II 1976/1980; Nii 1986): a shared
                            structured workspace that multiple knowledge sources read and write
                            opportunistically, with a control component deciding what runs next.
                            Linda tuple spaces (1985). Transactive memory (Wegner 1985).
                            Organizational memory (Walsh & Ungson 1991). Distributed cognition
                            (Hutchins 1995).
modern precedent            Knowledge graphs with provenance (W3C PROV-O: entities, activities,
                            agents, wasDerivedFrom, wasAttributedTo). LLM-era memory systems:
                            MemGPT/Letta, Generative Agents' memory stream with retrieval +
                            reflection, Mem0, Zep/Graphiti.
what transfers              The blackboard's *control* problem is the unsolved half and we have not
                            addressed it: who decides which knowledge source fires. PROV-O gives us
                            a standard provenance vocabulary we should adopt rather than invent.
what does not               Our Observation→Claim→Evidence→KnowledgeObject promotion ladder with a
                            required `sourceRootId` for detecting duplicated evidence chains is not
                            in PROV-O and not in any LLM memory system I found. Independence-of-
                            evidence tracking is genuinely thin in the literature.
novelty risk                HIGH on the fabric; LOW-to-MEDIUM on the evidence-independence ladder.
```

```text
concept                     Stigmergic Fields
earliest relevant precedent Grassé (1959) coins stigmergy; Dorigo's ACO (1992) makes it algorithmic;
                            Khatib (1986) artificial potential fields gives the "field" half.
modern precedent            ⛔ Two direct hits, both implemented. (a) Parunak & Brueckner's digital
                            pheromone infrastructure (Brueckner's thesis "Return from the Ant",
                            2000; AAMAS'02) — deposit / propagate / evaporate over a distributed
                            substrate, deployed to unmanned-vehicle and manufacturing control.
                            (b) Co-Fields and the TOTA middleware (Mamei & Zambonelli;
                            ACM TOSEM 18(4), 2009) — "computational fields" as distributed tuples
                            propagated by application-specific rules. The phrase "stigmergic field"
                            is in active current use (e.g. dual-trail stigmergic coordination for
                            underwater swarms).
what transfers              All of it, including the failure knowledge: field-based coordination is
                            tunable-but-opaque, and Parunak's own line of work on entropy/self-
                            organization exists because the emergent behaviour needed a theory to
                            be predictable at all.
what does not               Nothing material. Our proposed signals (risk, uncertainty,
                            edit_contention, verification_demand, knowledge_density) are a
                            *domain* choice, not a mechanism invention.
novelty risk                CRITICAL. Claiming stigmergy or fields as new would be indefensible.
```

```text
concept                     Morphogenetic Teams
earliest relevant precedent Turing (1952) morphogenesis; Koestler's holon (1967) →
                            holonic manufacturing; Ishida/Gasser/Yokoo (1992) Organization
                            Self-Design gives composition and decomposition of the agent population
                            *at runtime* — which is spawn/merge/dissolve.
modern precedent            ⛔ "Morphogenetic Engineering: Toward Programmable Complex Systems"
                            (Doursat, Sayama & Michel, Springer 2012) is a NAMED FIELD with a
                            review article in Natural Computing. Also: adaptive reorganisation in
                            MAS, and the LLM-era dynamic-team line (DyLAN, AgentVerse, EvoMAC,
                            self-organized agents).
what transfers              The whole local-rule formulation. Also the field's central warning:
                            self-architecting systems are easy to specify and hard to bound.
what does not               Our ADR-0006 ordering (intent and authority BEFORE adaptive autonomy)
                            is a governance stance the morphogenetic-engineering literature does
                            not take, because it was not building governed production systems.
novelty risk                CRITICAL on the term (the field owns it); HIGH on the mechanism.
```

```text
concept                     Evolution Chamber
earliest relevant precedent Genetic algorithms / genetic programming; organizational simulation:
                            the Virtual Design Team (Levitt et al., Stanford, 1993+) simulated
                            project organizations to predict duration, cost and coordination quality
                            *before building them* — i.e. an evolution chamber for org designs,
                            thirty years ago, validated against real projects.
modern precedent            MAP-Elites / quality-diversity (Mouret & Clune 2015) — which is exactly
                            our "prefer multi-objective / quality-diversity views rather than one
                            opaque fitness score", published, named. ADAS/Meta Agent Search (2024),
                            AFlow, AgentSquare, Darwin Gödel Machine (2025) with parent lineage and
                            an archive. Shadow deployment / progressive delivery is standard practice.
what transfers              MAP-Elites' archive-of-elites is our Candidate Registry and we should
                            say so. DGM's archive + lineage is our candidate record.
what does not               The promotion gate chain (offline → replay → shadow → limited live →
                            production) with a *constitution/permissions/audit mutation prohibition*
                            is not in ADAS or DGM, which mutate agent code freely. That prohibition
                            is a real contribution and is the part worth naming.
novelty risk                MEDIUM on the composition; CRITICAL on the NAME (see Deliverable 3).
```

```text
concept                     Organizational Debugger
earliest relevant precedent ⛔ "Debugging multi-agent systems using design artifacts: the case of
                            interaction protocols" (Poutakidis, Padgham & Winikoff, AAMAS 2002) —
                            AUML protocols compiled to Petri nets, used to monitor live
                            conversations and emit precise errors when the organization deviates
                            from its design. That is an organizational debugger, named, in 2002.
modern precedent            ⛔ ORGANIZATIONAL MINING — a named subfield of process mining since
                            van der Aalst, Reijers & Song (2005), covering organizational-structure
                            discovery, social-network analysis from event logs, resource allocation
                            and role mining; OrgMining 2.0 (2020). Plus: W3C PROV-O for causality,
                            distributed tracing (Dapper → OpenTelemetry, whose GenAI semantic
                            conventions now cover agent spans, tool calls and evaluation metadata),
                            and time-travel/omniscient debugging for replay.
what transfers              Conformance checking is the mechanism our "why did the organization do
                            this?" question actually needs, and it has 20 years of algorithms.
                            `caused_by / used_evidence / verified_by` should be expressed in PROV-O
                            terms (`wasInformedBy` / `used` / `wasGeneratedBy`) rather than invented.
                            Emit OpenTelemetry GenAI spans rather than a bespoke trace format.
what does not               Our breakpoint model (pause-and-escalate on an *evidence-sufficiency*
                            predicate) has no counterpart. Process mining is post-hoc; tracing is
                            passive; neither halts the organization on an epistemic condition.
novelty risk                CRITICAL on the concept; LOW on the evidence-conditioned breakpoint.
```

```text
concept                     Executable Doctrine
earliest relevant precedent Rete (Forgy 1974) → production systems → business rules engines
                            (Drools). Policy languages for distributed systems: Ponder, Rei, KAoS,
                            XACML. Norms in electronic institutions with online enforcement and
                            sanctions (ISLANDER/AMELI, 2003–05).
modern precedent            "Policy as code" (Open Policy Agent / Rego) and "compliance as code"
                            are mature, named industry practices with the exact property we want:
                            policy stored, versioned, tested and evaluated as code. MetaGPT (2023)
                            encodes human SOPs into agent prompt sequences.
what transfers              OPA's decision model. e-institutions' distinction between norms that
                            are *regimented* (impossible to violate) and *enforced* (violable, then
                            sanctioned) — our `enforcement: block|warn|escalate` is a rediscovery of
                            it and should cite it.
what does not               Doctrine promotion gated on replay/simulation plus governance
                            (`candidate → shadow → active → retired`) is not how policy-as-code
                            works; policies are reviewed, not empirically promoted. That is ours.
novelty risk                HIGH on the mechanism; MEDIUM on evidence-gated promotion.
                            The WORD "doctrine" is heavily colonised — see Deliverable 3.
```

```text
concept                     Capability Readiness
earliest relevant precedent TRL (Sadin/NASA 1974) — readiness as a graded, auditable scale;
                            SORTS C-levels; CMM/CMMI (1991) for organizational capability maturity.
modern precedent            DRRS: explicitly reframes readiness from resource status to "ready for
                            WHAT" — mission-essential tasks assessed Y/Q/N under defined scenarios.
                            That is our `capability_readiness` block, including the idea that the
                            binding constraint is named (our `blocker: verification_capacity`).
                            In software: Kubernetes readiness probes, SRE Production Readiness
                            Reviews, agile "Definition of Ready". In MAS: capability advertisement
                            and matchmaking (Decker/Sycara/Williamson middle-agents 1997; LARKS 2002)
                            and FIPA's Directory Facilitator; in 2025, A2A Agent Cards.
what transfers              DRRS's "ready for what" framing is better than ours and should be
                            adopted verbatim as a design constraint: readiness is never a scalar
                            property of an agent, always a pair (capability, mission class).
what does not               Our Capability object carries `evidenceRefs`, `historicalSuccessRate`
                            AND `sampleSize`. A capability claim that must state its sample size is
                            not something I found in TRL, CMMI, DRRS, LARKS or A2A. Agent Cards in
                            particular are pure self-declaration — MARKETED by construction.
novelty risk                HIGH on readiness; LOW on evidence-backed capability with sample size.
```

```text
concept                     Cognitive Logistics
earliest relevant precedent Military logistics doctrine; ⛔ INFORMATION LOGISTICS — an established
                            research domain (Deiters/Fraunhofer, Haftor et al.) whose stated goal is
                            "timely providence of the right information ... tailored to the user's
                            need", i.e. right information / right time / right place. Same idea,
                            same metaphor, different decade.
modern precedent            "Context engineering" (Karpathy, June 2025) is now the industry term for
                            precisely this at the LLM layer: "the delicate art and science of filling
                            the context window with just the right information for the next step".
                            MemGPT (2023) applies OS virtual-memory paging to the context window.
                            Model routing / token budgeting (RouteLLM, FrugalGPT).
what transfers              Everything conceptual. The write/select/compress/isolate taxonomy from
                            the context-engineering literature is more actionable than our supply list.
what does not               Treating *verification capacity* and *human attention* as rationed
                            supplies alongside tokens and tools is unusual — I found no context-
                            engineering treatment that budgets the reviewer. That is a real seam.
novelty risk                MEDIUM. The TERM is taken (see Deliverable 3); the human-attention-as-
                            supply framing is thin in the literature.
```

```text
concept                     Temporal Echelons
earliest relevant precedent Army planning horizons — current operations / future operations /
                            future plans cells, synchronised by a battle rhythm (ADP 5-0).
                            Dean & Boddy (1988): deliberation scheduling allocates computation
                            across anytime algorithms based on expected performance — the
                            promotion-criteria problem, formalised, in 1988.
modern precedent            Speculative execution and prefetching in computer architecture (the
                            direct analogue of speculative NEXT/LATER work, including the crucial
                            requirement of a cheap cancellation path); rolling-wave planning;
                            hierarchical task networks; three-horizon models in strategy.
what transfers              Deliberation scheduling gives a principled way to set promotion
                            thresholds instead of hand-tuning them. Speculative execution's
                            hard-won lesson — speculation must be cancellable and its side effects
                            must not escape — maps exactly onto our guardrail list, and to Spectre
                            it adds a security lesson we should heed (speculative work leaves traces).
what does not               An explicit NOW/NEXT/LATER *organizational* horizon with budget, expiry,
                            relevance threshold and cancellation, applied to LLM agent preparation,
                            is thinly covered. This is the least-precedented of the 15.
novelty risk                LOW-to-MEDIUM. The mechanism is old; the application is open.
                            But "echelon" is the wrong word — see Deliverable 3.
```

```text
concept                     Staff Mesh
earliest relevant precedent The Prussian/continental general staff system; running estimates as
                            doctrine. In computing: blackboard *control* components; the
                            Hearsay-II scheduler is a non-task cognition service.
modern precedent            ⛔ PROSA (Van Brussel et al. 1998): three basic holon types (order,
                            product, resource) PLUS "staff holons [that] can be added to assist the
                            basic holons with expert knowledge". Same word, same role, 1998, in a
                            manufacturing reference architecture with 1,500+ citations.
                            Also middle-agents (Decker, Sycara & Williamson 1997): matchmakers,
                            brokers and facilitators as non-task infrastructure agents.
what transfers              PROSA's decoupling of control *structure* from control *algorithm* is
                            the property our staff mesh needs and does not state. PROSA also shows
                            staff functions can be advisory-only, which resolves our open question
                            about staff authority: in PROSA they have none.
what does not               Running estimates as *continuously revised structured projections with
                            declared coverage and critical unknowns* is not in PROSA or middle-agent
                            work. The coverage/critical-unknowns/contradictions triple is ours.
novelty risk                CRITICAL on the term and the role; LOW on the running-estimate schema.
```

```text
concept                     Federated Agent Armies
earliest relevant precedent ⛔ "The Anatomy of the Grid: Enabling Scalable Virtual Organizations"
                            (Foster, Kesselman & Tuecke, IJHPCA 2001) — federation defined as
                            "flexible, secure, coordinated resource sharing among dynamic
                            collections of individuals, institutions and resources", with
                            authentication, authorization, resource discovery as the named problems.
                            FIPA (1999) standardised cross-platform agent interoperability.
                            NATO Federated Mission Networking on the military side.
modern precedent            A2A (Google, Apr 2025; Linux Foundation, Jun 2025): Agent Cards
                            advertising capabilities, input/output modalities and auth requirements
                            over HTTP/JSON-RPC — our CapabilityAdvertisement, shipped, with 150+
                            organizations claiming support. MCP for tool/context federation.
what transfers              A2A is a real transport we should assume rather than design around.
                            The Grid's hard-won lesson is that federation dies on identity and
                            authorization, not on message formats — which validates our own
                            non-goal ("do not implement federation before permissions, provenance,
                            evidence contracts, audit and organization identity are mature").
what does not               A2A has no evidence contract and no provenance envelope; a 2026 analysis
                            ("Governance Gaps in Agent Interoperability Protocols") argues MCP, A2A
                            and ACP cannot express governance constraints at all. `EvidenceRequirement`
                            + `ProvenanceEnvelope` + `AuditReceipt` as *required* parts of a
                            cross-organization result package is a genuine gap.
novelty risk                HIGH on federation; LOW on the evidence-bearing result package.
```

---

## Evidence

```text
ESTABLISHED  (tier A — replicated / mature implementation)
  · Stigmergy and field-based coordination work as coordination mechanisms and were shipped as
    middleware and in defence/manufacturing control (ACO, digital pheromones, TOTA).
  · Blackboard architectures work for opportunistic multi-source problem solving (Hearsay-II).
  · Process mining reliably recovers organizational structure and social networks from event logs.
  · Policy-as-code enforcement (Rete lineage → OPA) is production infrastructure.
  · Supervision trees with declared restart strategies are production-proven fault-tolerance.
  · Readiness-as-graded-scale (TRL, CMMI, DRRS, K8s probes) is an established, auditable pattern.
  · Provenance modelling (W3C PROV-O) is a standard, not a proposal.
  · Automated organization design for MAS was demonstrated (KB-ORG, ODML) — established as
    RESEARCH; never established as industrial practice.

EMERGING  (tier B/C — multiple credible studies or one mature implementation)
  · LLM multi-agent topology has a measurable, task-dependent effect. ONE controlled study
    (Kim et al. 2025/2026) dominates the evidence base; see Finding 4 on source independence.
  · Automated search over agentic system designs improves benchmark scores (ADAS, AFlow,
    AgentSquare, DGM) — all benchmark-scale, none side-effecting production.
  · Multi-agent failures are dominated by system design and inter-agent misalignment rather than
    model capability (MAST: 1,600+ traces, 7 frameworks, κ=0.88 — one dataset, one team).
  · Context engineering as a discipline; OS-style context paging (MemGPT).
  · Agent interoperability protocols (A2A, MCP) — adoption is real; governance expressiveness is
    documented as absent.

EXPERIMENTAL  (tier C/D — promising or testable, unproven at our scale)
  · Morphogenetic / self-architecting organizations. A named field with demonstrations; no
    production governed deployment I could find.
  · Quality-diversity optimisation of organizational designs (MAP-Elites applied to org genomes).
  · Evidence-conditioned breakpoints that halt an organization on epistemic insufficiency.
  · Temporal echelons — speculative organizational preparation with budget/expiry/cancellation.

SPECULATIVE  (tier D — testable but unevidenced)
  · That an organizational abstraction layer improves LLM-agent outcomes AT ALL. This is the
    programme's load-bearing assumption and it is currently unevidenced in either direction.
  · That "capability readiness with sample size" changes routing behaviour usefully.
  · Federation of artificial organizations delivering value beyond a single org.

METAPHORICAL ONLY  (tier E)
  · "Organizational OS", "Collective Cognition Fabric", "Organizational Genome", "Organizational
    Immune System", "Organizational Cortex", "Agent City", "Causal Multiverse", "Fog of War".
    These are naming devices. None currently designates a mechanism that could not be described
    without them, and each imports a promise the system does not keep.
  · "Autopoiesis" as used in R22. In Maturana & Varela's sense it means a system that produces its
    own components and boundary; a loop from work → signals → policy adaptation is a control loop,
    not autopoiesis. Using the word invites a claim we cannot support.
```

---

## Findings

### Finding 1 — Organizational MAS did not fail; it was not adopted, and that distinction changes our strategy

**Mechanism.** Between 1992 and 2013 the organization-oriented MAS community produced a complete
stack: organizational meta-models (AGR, Moise+, OperA), a modelling language designed to be
searched (ODML), automated design over it (KB-ORG), runtime organizational infrastructure
(S-Moise+, ORA4MAS), a full platform (JaCaMo), norms with online enforcement (ISLANDER/AMELI),
and debugging from design artifacts (Poutakidis et al.). Every layer of the Agent Army
architecture has a counterpart there.

**Evidence.** KB-ORG is described by its own abstract as "fully automated"; ORA4MAS reifies the
organization infrastructure as first-class runtime abstractions; Moise remains published at
`moise-lang.github.io`. These are artefacts, not proposals. (DERIVED — bibliographic and abstract
level; I did not read the implementations.)

**Counterevidence.** Nothing in this stack reached industry. The plausible reason — which I can
support by absence rather than by a citation, so mark it ASSUMED — is that it required each agent
to be hand-built with an explicit ontology and capability model. The organizational layer was
cheap relative to the agents, and the agents were prohibitively expensive. That constraint is now
inverted: agents are near-free and the organizational layer is the expensive part.

**Agent Army implication.** We should *mine* this literature rather than compete with it, and say
publicly that we are doing so. Our differentiator is not that we thought of organizational
compilation; it is that the input to it is now natural language and the workers are now general.
Concretely: adopt Moise+'s structural/functional/deontic split for Org-IR, adopt KB-ORG's
application-vs-coordination knowledge distinction in the compiler, adopt PROSA's control-structure/
control-algorithm decoupling for the staff mesh, adopt ORA4MAS's organization-as-artifacts stance
for the Organizational OS, and adopt PROV-O for the debugger's causal edges.

### Finding 2 — Seven of our fifteen names are already taken, and four of those collide with commercial categories

Detailed in Deliverable 3. The pattern is that our most evocative names are the most colonised.
"Organizational OS" collides with EOS® (the Entrepreneurial Operating System, a trademarked
business-operating-system methodology claiming 250,000+ businesses) — the exact audience for a
product about running an organization. "Doctrine" is one of the largest PHP projects in existence.
"Evolution Chamber" is a StarCraft II Zerg building. "Cognitive Logistics" is a live term in
supply-chain (an EU H2020 project, COG-LO, is named for it). "Digital twin of the organization" is
a Gartner Magic Quadrant category with named vendors. A term collision is not a design flaw, but
it makes every one of our claims un-searchable and un-citable, which for a research programme is
close to fatal.

**Agent Army implication.** Rename before anything is published externally. Deliverable 5.

### Finding 3 — The −3.5% figure is REAL and our summary is faithful on the point estimate but drops the uncertainty, and the loss happens at a specific hop

I verified this rather than accepting it. The study is:

> Kim, Gu, Park, Park, Schmidgall, Heydari, Yan, Zhang, Zhuang, Liu, Malhotra, Liang, Park, Yang,
> Xu, Du, Patel, Althoff, McDuff, Liu — **"Towards a Science of Scaling Agent Systems"**,
> arXiv:2512.08296, submitted 9 Dec 2025.

`v1` matches our blueprint's description **exactly**: 180 configurations, 5 canonical architectures
(Single, Independent, Centralized, Decentralized, Hybrid), 3 LLM families, 4 agentic benchmarks
(Finance-Agent, BrowseComp-Plus, PlanCraft, Workbench); "for sequential reasoning tasks, all
multi-agent variants degraded performance by 39–70%". (OBSERVED — I fetched the v1 abstract page.)

The −3.5% appears in the v1 full text, verbatim:

> "Aggregating across all benchmarks and architectures, the overall mean MAS improvement is
> **−3.5% (95% CI: [−18.6%, +25.7%])**"

(OBSERVED — I fetched `arxiv.org/html/2512.08296v1` and extracted this sentence.)

So the summary is **faithful on the number and unfaithful on its meaning**. A mean of −3.5% with a
CI spanning −18.6% to +25.7% is *not evidence that multi-agent hurts*; it is evidence that the
average effect is indistinguishable from zero and that the variance is enormous — which is in fact
the paper's actual thesis (architecture–task alignment determines the outcome; the same study
reports **+80.9%** on parallelisable financial reasoning).

Tracing the internal chain: `docs/research/answers/R2-answer-topology.md:15` **does** carry the
interval — "a very wide 95% interval of −18.6% to +25.7%" — and also carries the +80.9%, the ~45%
capability-saturation threshold (β = −0.408, p<0.001), the 17.2× vs 4.4× error amplification, the
n^1.724 interaction growth and the 87% held-out prediction accuracy. All of those I independently
confirmed against the paper. **R2 is an excellent piece of work.** The interval is lost at the next
hop — `blueprints/orchestrator_team.yaml` and then `docs/agent-army/CURRENT_STATE.md` both quote
"−3.5%" and "39–70%" with no interval — and CURRENT_STATE.md is the file a new session reads.

Two further corrections to how the figure is being used:

- The study has since been **expanded to 260 configurations across 6 benchmarks** and published in
  *Nature Machine Intelligence* (2026), reporting a span of **+80.8% to −70.0%**. Our citation is
  to a superseded preprint version. The Nature version is **NOT-ACCESSIBLE** (paywall; 303 to
  `idp.nature.com`) so I cannot confirm whether the aggregate mean changed.
- The counterweight is a vendor claim: Anthropic reports **90.2%** improvement over single-agent
  Opus 4 on its **internal** research evaluation at ~15× tokens. That is `MARKETED` — unreproducible,
  non-public eval, vendor-run — and R2 already labels it "VENDOR ENGINEERING EVIDENCE". It must
  never be used as a design premise.

**Agent Army implication.** The decision the blueprint reaches (build the single-worker topology
first) is *still correct*, because it does not rest on the aggregate mean — it rests on the
sequential-task result (39–70% degradation) and on our own measured failure distribution (all seam
failures). But the *argument as written* is stronger than the evidence supports. Fix the two
downstream files to carry the interval, and cite arXiv:2512.08296 explicitly.

### Finding 4 — The evidence that "multi-agent doesn't work" is much thinner than the discourse suggests, and largely traces to one study

The brief asked me to flag when citations collapse to one source. They do here. Searching for
multi-agent-vs-single-agent evidence returns a large volume of blog posts, newsletters and
secondary analyses ("More Agents, Worse Results", "the 17x error trap", practitioner threads) — and
the quantitative content of essentially all of them traces back to **arXiv:2512.08296** or its
Nature successor. That is **one study, one team (Google/MIT/UW), one experimental design**. It is
a good study. It is not a literature.

The genuinely independent pieces of evidence I found are:
1. **MAST** (Cemri et al., arXiv:2503.13657) — 1,600+ annotated traces, 7 frameworks, 14 failure
   modes, κ=0.88. Independent of the scaling study. Also one team, one dataset.
2. **Anthropic's production report** — independent, opposite sign, vendor-run, unreproducible.
3. **Cognition's practitioner reports** — "Don't Build Multi-Agents", then a 2026 follow-up
   ("Multi-Agents: What's Actually Working") that *revises the position*: multi-agent works when
   "one main loop carries state, subagents are stateless workers with narrow scope". Qualitative,
   commercially motivated, but from operators.

Note that (3) has moved. Citing "Don't Build Multi-Agents" as the current industry position is
already out of date.

**Agent Army implication.** Do not build the programme's justification on "multi-agent
underperforms". That claim is under-evidenced in both directions. Build it on the two things that
*are* well-evidenced: coordination cost grows superlinearly, and failures concentrate at seams.

### Finding 5 — The literature disagrees with us about three words, and the literature wins

Reported explicitly per the brief's conflict rule.

- **"Echelon" is a hierarchy level, not a time horizon.** In military usage an echelon is a level
  of command (squad → platoon → company). The thing we mean — NOW/NEXT/LATER — is called a
  **planning horizon**, and the organizational structure that owns it is the current-operations /
  future-operations / plans cell split. "Temporal Echelons" reads to any military-literate reader
  as "time-based command levels", which is not what we mean. **The literature wins: use
  *planning horizons*.**
- **"Contract" already means a bid-based task allocation.** In MAS, "contract" has meant Contract
  Net task contracting since 1980. Our Intent Contract is not that — it is closer to an
  authority envelope plus an acceptance specification. Every MAS-literate reader will misread it.
- **"Fabric" and "mesh" both mean something specific and neither means ours.** A *data fabric* is
  a unified integration layer; a *data mesh* is decentralised domain ownership with federated
  governance; a *service mesh* is sidecar-mediated service-to-service networking. Our "Collective
  Cognition Fabric" is centralised shared knowledge (which makes it a fabric, not a mesh) and our
  "Staff Mesh" is a set of centralised cognition services (which makes it *not* a mesh at all —
  it is nearer a fabric, or simply a *staff*). **We have the two words swapped relative to their
  industry meanings.** That is the single most embarrassing item in this report.

### Finding 6 — What actually changes in the LLM era: three things, and only three

Answering sub-question 5 of the brief's required method, across all 15 concepts at once.

1. **Intent is now machine-consumable without ontology engineering.** Every prior organizational
   MAS required the mission, the task structure (TÆMS) and the capabilities to be formally
   specified by a human. This was the adoption killer. It is gone. This is the single biggest
   change and it is what makes the Organizational Compiler's *front end* new even though its
   *body* is 2008 work.
2. **Workers are general and cheap to instantiate.** Organization Self-Design's
   composition/decomposition primitives were expensive because each agent was hand-built.
   Spawning a research cell now costs a prompt. This makes morphogenesis *affordable* — and
   therefore makes bounding it, which the morphogenetic-engineering literature never had to do
   at production stakes, the actual hard problem.
3. **The failure mode moved from capability to verifiability.** In 1998 the question was "can the
   agent do the task". In 2026 the agent usually can, and the question is "did it, and how would
   we know". MAST's finding that 21% of failures are verification failures and 42% specification
   failures is the same shape as our own evidence-gate discipline. **This is where the novelty is,
   and it is the only one of the three that the prior organizational-MAS literature does not
   already have machinery for.**

What does **not** change: coordination overhead still grows superlinearly (n^1.724 in the scaling
study); indirect coordination via a shared environment still trades tunability for opacity;
organizational structure is still easier to specify than to govern; and an organization still
cannot be debugged without a durable event log.

### Finding 7 — Our strongest asset is not in the research corpus, and it is not an organizational idea

`agent-factory/docs/agent-army/CURRENT_STATE.md` names three mechanisms that exist in code and have
no counterpart in the research vocabulary: the **four-verdict contract** (`factory/contract.py:17-21`,
where `UNMEASURABLE` is never collapsed into PASS or FAIL), **grader separation** (`factory/corpus.py`,
`factory/certify.py:15-17,79,82` — `--calibrate` scoring is explicitly labelled "worthless as
evidence that an agent did not grade itself"), and **evidence-gated close** (`factory/evidence.py:48`
with classes TARGET/CONSUMER/REGRESSION/ROLLBACK, enforced in the store at `factory/tasks.py:163`).

I searched for equivalents and did not find them. Organizational MAS has norms and sanctions but not
epistemic verdicts. Process mining has conformance but not "the instrument was dark". OpenTelemetry
GenAI conventions carry evaluation metadata but no refusal semantics. MAST *diagnoses* verification
failure but proposes no primitive against it. ADAS and DGM optimise against scores their own agents
can influence — the exact thing grader separation forbids.

**Agent Army implication.** This is the novelty claim. It is small, it is real, and it is already
partly built. See §Narrowest defensible claim.

---

## Deliverable 3 — Vocabulary collision table

`Collision severity`: **BLOCKING** = the term already denotes a different, well-known thing in a
directly overlapping audience; **SERIOUS** = established prior meaning in an adjacent field;
**MINOR** = collision exists but audiences do not overlap.

| Our term | Already means | Owner / earliest | Severity | Effect on us |
|---|---|---|---|---|
| **Organizational OS** | EOS® — Entrepreneurial Operating System, a trademarked business methodology (Wickman, *Traction*), 250,000+ businesses claimed | EOS Worldwide, 2007 | **BLOCKING** | Same buyer, same words, opposite thing. Also collides with DC/OS and current "AI OS" marketing. Unsearchable. |
| **Executable Doctrine** | Doctrine — a major PHP ORM/DBAL project; separately, "doctrine" is US military publication series | doctrine-project.org, 2006 | **BLOCKING** | Every code search for `doctrine` returns PHP. Term is unusable in a software repo. |
| **Evolution Chamber** | A Zerg building in StarCraft/StarCraft II (plus an SC2 build-order optimiser of the same name) | Blizzard, 1998 | **SERIOUS** | Reads as a gaming reference. Undermines seriousness in exactly the audience we want. |
| **Cognitive Logistics** | An active logistics-industry term ("Logistics 5.0"); EU H2020 project **COG-LO** = *COGnitive Logistics Operations* | ~2017 | **SERIOUS** | Search results are dominated by supply-chain. The prior art we actually want to cite is *Information Logistics*. |
| **Staff Mesh** | *Mesh* = decentralised, peer-connected (service mesh; data mesh = decentralised domain ownership) | Istio 2017 / Dehghani 2019 | **SERIOUS** | Our staff functions are **centralised** cognition services. The name asserts the opposite of the design. |
| **Collective Cognition Fabric** | *Data fabric* = unified integration layer; *collective cognition* / *swarm cognition* = established terms in swarm-robotics and animal-behaviour research | Gartner; Trianni & Tuci, *Swarm Intelligence* 2011 | **SERIOUS** | Two collisions at once, and — see Finding 5 — "fabric" and "mesh" are swapped relative to their industry senses. |
| **Stigmergic Fields** | "Stigmergic field" / "virtual pheromone field" in active use in swarm-coordination papers; "computational fields" is the Co-Fields/TOTA term | Grassé 1959; Mamei & Zambonelli 2004 | **SERIOUS** | Not a collision so much as an *appropriation*. Use it, but cite it. |
| **Morphogenetic Teams** | **Morphogenetic Engineering** is a named research field with a Springer volume and a Natural Computing review | Doursat, Sayama & Michel, 2012 | **SERIOUS** | Same. Cite or be caught. |
| **Organizational Compiler** | No established term (checked). But the *function* is KB-ORG / automated organization design | Sims, Corkill & Lesser, 2008 | MINOR (term) / **BLOCKING** (concept) | The name is free; the claim is not. |
| **Org-IR** | No established term. The artefact is an organizational modelling language (ODML, Moise+, OperA) | Horling & Lesser; Hübner et al. | MINOR (term) / SERIOUS (concept) | Name is safe. Say "our organizational modelling language" in prose. |
| **Intent Contract** | "Intent" is standardised by **RFC 9315**; "contract" means Contract Net task contracting in MAS; "intent contract" is already in use in O-RAN/network-slicing agent papers (2026) | IRTF NMRG 2022; Smith 1980 | **SERIOUS** | Two established senses, both wrong for us, plus a live 2026 usage. |
| **Organizational Debugger** | **Organizational mining** is the named subfield of process mining for exactly this data | van der Aalst, Reijers & Song, 2005 | **SERIOUS** | Our name is free; the technique has a name and 20 years of algorithms. |
| **Capability Readiness** | Readiness is a defined term of art in DRRS/SORTS (C-levels, METs), TRL, CMMI, and Kubernetes (`readinessProbe`) | NASA 1974; DoD; K8s | MINOR | Safe to use, but must not be defined loosely — the prior art defines it precisely and better. |
| **Temporal Echelons** | **Echelon** = a level of command, not a time horizon. The correct term is *planning horizon* | Military usage | **SERIOUS** | The name means the wrong thing to the audience it borrows from. |
| **Federated Agent Armies** | *Virtual organizations* (Grid, 2001); *Federated Mission Networking* (NATO); A2A/MCP for the transport layer | Foster et al. 2001 | MINOR | "Federated" is correct and standard. "Army" is ours. |
| **Organizational Digital Twin** | **Digital Twin of an Organization (DTO)** — a Gartner market category with a Magic Quadrant and named vendors (Signavio, Ardoq, QualiWare) | Gartner, ~2018 | **BLOCKING** | We would be entering a defined analyst category, against funded incumbents, with no differentiator stated. |
| **Organizational Autopoiesis** | Autopoiesis (Maturana & Varela) means self-production of components and boundary | 1972 | **SERIOUS** | We describe a control loop. Using the word claims something stronger and false. |

---

## Deliverable 4 — Novelty risk map

Scale: **CRITICAL** — implemented, published prior art doing materially the same thing; any novelty
claim is indefensible. **HIGH** — strong precedent; differences are of substrate or degree.
**MEDIUM** — precedent in adjacent fields; the specific composition is thinly explored.
**LOW** — genuinely under-explored as posed.

| Concept | Risk | The specific thing that kills the claim | What survives as ours |
|---|---|---|---|
| Organizational Compiler | **CRITICAL** | KB-ORG (2008): fully automated knowledge-based organization design with pruned candidate search | Natural-language mission intent as the front end; verification-plan generation as a compiler pass |
| Org-IR | **CRITICAL** | ODML, Moise+, OperA, AGR; BPMN/BPEL outside MAS | Evidence, capability-with-sample-size and verification plan as first-class IR elements |
| Organizational OS | **CRITICAL** | FIPA platforms; ORA4MAS organisational artifacts; JaCaMo | Durable replayable event log as the single organizational source of truth |
| Stigmergic Fields | **CRITICAL** | Digital pheromone infrastructure (2000–02); Co-Fields/TOTA middleware (2004–09) | Nothing at the mechanism level. Domain signal choice only. |
| Morphogenetic Teams | **CRITICAL** | Organization Self-Design (1992); Morphogenetic Engineering as a named field (2012) | Intent-and-authority-before-autonomy ordering (ADR-0006) as a governance stance |
| Organizational Debugger | **CRITICAL** | Debugging MAS from design artifacts (2002); organizational mining (2005–); PROV-O; OTel | Breakpoints conditioned on **evidence sufficiency** rather than on state or protocol violation |
| Staff Mesh | **CRITICAL** | PROSA **staff holons** (1998, same word); middle-agents (1997) | The running-estimate schema: coverage + critical unknowns + contradictions + recommendation |
| Intent Contract | **HIGH** | RFC 9315 intent; deontic authority envelopes in e-institutions; Design by Contract | `verificationRequirements` with `requiredEvidenceTypes` inside the contract object |
| Collective Cognition Fabric | **HIGH** | Blackboard; transactive memory; distributed cognition; PROV-O; LLM memory systems | Observation→Claim→Evidence→Knowledge promotion with `sourceRootId` independence tracking |
| Executable Doctrine | **HIGH** | Rete→Drools; Ponder/Rei/KAoS/XACML; OPA policy-as-code; e-institution norms | Doctrine promotion gated on replay + simulation + governance (`candidate→shadow→active→retired`) |
| Capability Readiness | **HIGH** | TRL, CMMI, SORTS/DRRS, K8s readiness probes, LARKS matchmaking, A2A Agent Cards | Capability claims carrying `evidenceRefs` + `historicalSuccessRate` + **`sampleSize`** |
| Federated Agent Armies | **HIGH** | Grid virtual organizations (2001); FIPA; A2A agent cards (2025) | `EvidenceRequirement` + `ProvenanceEnvelope` + `AuditReceipt` as mandatory in the result package |
| Evolution Chamber | **MEDIUM** | MAP-Elites/QD; ADAS; DGM; VDT organizational simulation; shadow deployment | The mutation **prohibition** (constitution/permissions/audit are not in the genome) + gate chain |
| Cognitive Logistics | **MEDIUM** | Information Logistics (2000s); context engineering (2025); MemGPT | Verification capacity and human attention treated as rationed supplies with readiness blockers |
| Temporal Echelons | **LOW** | Anytime algorithms + deliberation scheduling (1988); speculative execution; planning horizons | Organizational speculative preparation with budget/expiry/relevance/cancellation, measured |

**Aggregate reading of the map.** Every surviving column entry is about **evidence, verification or
governance**. Not one is about organizational structure. That is the answer to the brief's question,
arrived at from the map rather than asserted.

---

## Deliverable 5 — Recommended terminology

Rule applied: prefer the term the literature already uses; coin only where nothing exists; never
coin a metaphor that promises a property we do not deliver.

| Current | Recommended | Why |
|---|---|---|
| Intent Contract | **Mission Contract** (or *Commander's Intent Record* internally) | Avoids RFC 9315's "intent" and Contract Net's "contract" simultaneously; keeps the doctrine lineage |
| Organizational Compiler | **Organization Synthesiser** — and cite KB-ORG in the same paragraph | "Compiler" over-promises determinism we do not have; synthesis is the honest word and the literature's |
| Org-IR | **Organization Specification** (structural / functional / deontic, after Moise+) | The three-way split is a design improvement, not just a rename |
| Organizational OS | **Organization Runtime** | Kills the EOS® collision and the "OS" over-claim in one move |
| Collective Cognition Fabric | **Knowledge and Evidence Store** | Says what it is. If a lyrical name is needed later, it must not be "fabric" |
| Stigmergic Fields | **Coordination Fields** (cite Co-Fields/TOTA and Parunak) | Keeps the mechanism, drops the implied invention |
| Morphogenetic Teams | **Adaptive Team Formation** (cite Organization Self-Design; Morphogenetic Engineering) | Plain, searchable, honest about lineage |
| Evolution Chamber | **Organization Design Lab** | Removes the StarCraft collision; "lab" correctly implies offline |
| Organizational Debugger | **Organizational Debugger** — keep, but describe the technique as *conformance and causal replay over the organizational event log* | The name is free and good; the *method* must cite process mining |
| Executable Doctrine | **Organizational Policy** (rules) + **Validated Practice** (promoted procedure) | Splits two things "doctrine" conflates, and dodges the PHP collision |
| Capability Readiness | **Capability Readiness** — keep, but always as a pair `(capability, mission class)` after DRRS's "ready for what" | Term is correct; our definition is looser than the prior art's |
| Cognitive Logistics | **Context Logistics** (cite Information Logistics + context engineering) | Keeps the metaphor, escapes the supply-chain search space |
| Temporal Echelons | **Planning Horizons** (NOW / NEXT / LATER) | "Echelon" means the wrong thing. The literature wins. |
| Staff Mesh | **Staff Functions** (or *Organizational Staff*) | Not a mesh. PROSA already calls them staff; agreeing is a feature |
| Federated Agent Armies | **Federated Organizations** (transport: assume A2A/MCP) | "Virtual organizations" is the 2001 term; "federated organizations" is close and unencumbered |
| Organizational Digital Twin | **Organization World State** (materialised projection) | Avoids walking into Gartner's DTO Magic Quadrant |
| Organizational Autopoiesis | *drop* | Claims a property we do not have |
| Organizational Cortex / Immune System / Genome / Agent City / Causal Multiverse | *drop, or mark VISUALIZATION ONLY* | Metaphors with no mechanism behind them; each imports an unearned promise |

**Category name.** "Artificial Organization Engineering" is currently unclaimed as a field name and
is a reasonable coinage — but only if we simultaneously acknowledge **Computational Organization
Theory** (Carley & Prietula, 1994) as the parent field. Positioning AOE as *the engineering
successor to COT for LLM-based workers* is defensible and citable. Positioning it as new is not.

---

## Deliverable 6 — The 25 highest-value prior systems, papers and repositories

Ordered by how much damage each does to a naive novelty claim. All links were returned by search;
those marked ‡ I fetched and read directly (`OBSERVED`). The rest are `DERIVED` — existence and
substance corroborated across independent search syntheses, full text not read.

| # | Work | What it actually is | Hits which concept |
|---|---|---|---|
| 1 | **Sims, Corkill & Lesser (2008), "Automated organization design for multi-agent systems"**, JAAMAS. [Springer](https://link.springer.com/article/10.1007/s10458-007-9023-8) · [UMass PDF](http://mas.cs.umass.edu/Documents/07-43.pdf) | KB-ORG: a fully automated knowledge-based organization designer that prunes a candidate-organization search using application- and coordination-level knowledge | **Organizational Compiler** (fatal) |
| 2 | **Ishida, Gasser & Yokoo (1992), "Organization self-design of distributed production systems"**, IEEE TKDE 4(2). Overview: [arXiv:1506.09032](https://arxiv.org/pdf/1506.09032) | Runtime composition/decomposition primitives that change the agent population and knowledge distribution | **Morphogenetic Teams**, Organizational Compiler |
| 3 | **Mamei & Zambonelli (2009), "Programming pervasive and mobile computing applications: the TOTA approach"**, ACM TOSEM 18(4). [ACM](https://dl.acm.org/doi/10.1145/1538942.1538945) · Co-Fields: [T&F](https://www.tandfonline.com/doi/full/10.1080/08839510500484264) | Field-based coordination as shipped middleware — computational fields as propagated distributed tuples | **Stigmergic Fields** (fatal) |
| 4 | **Parunak & Brueckner (2002), "Digital pheromone mechanisms for coordination of unmanned vehicles"**, AAMAS. [ACM](https://dl.acm.org/doi/10.1145/544741.544843) · [PDF](http://biomimetic.pbworks.com/f/Digital%20pheromone%20mechanisms%20for%20coordinationParunaK.pdf) | Deposit/propagate/evaporate pheromone infrastructure, deployed to vehicle and manufacturing control | **Stigmergic Fields** |
| 5 | **Van Brussel, Wyns, Valckenaers, Bongaerts & Peeters (1998), "Reference architecture for holonic manufacturing systems: PROSA"**, Computers in Industry. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S016636159800102X) · [ARTI update](https://www.sciencedirect.com/science/article/abs/pii/S0166361520302530) | Order/product/resource holons **plus staff holons** that assist with expert knowledge; decouples control structure from control algorithm | **Staff Mesh** (same word) |
| 6 | **Hübner, Sichman & Boissier — Moise / S-Moise+ / ORA4MAS**. [moise-lang.github.io](https://moise-lang.github.io/) · [ORA4MAS](https://link.springer.com/chapter/10.1007/978-3-540-79003-7_13) | Structural/functional/deontic organizational specification, and the organization infrastructure reified as runtime artifacts | **Org-IR**, **Organizational OS** |
| 7 | **van der Aalst, Reijers & Song (2005), "Discovering social networks from event logs"**, CSCW. [ACM](https://dl.acm.org/doi/10.1007/s10606-005-9005-9) · [OrgMining 2.0](https://arxiv.org/pdf/2011.12445) | Founds **organizational mining**: structure discovery, SNA, role mining and resource allocation from event logs | **Organizational Debugger** |
| 8 | **Poutakidis, Padgham & Winikoff (2002), "Debugging multi-agent systems using design artifacts"**, AAMAS. [ACM](https://dl.acm.org/doi/10.1145/544862.544966) | AUML protocols → Petri nets → live conformance monitoring with precise deviation messages | **Organizational Debugger** |
| 9 | **Kim et al. (2025), "Towards a Science of Scaling Agent Systems"**, [arXiv:2512.08296](https://arxiv.org/abs/2512.08296) ‡ | The source of our −3.5%. 180 configs (v1) → 260 (Nature MI 2026). Capability saturation ~45%; 17.2× vs 4.4× error amplification; n^1.724 interaction growth | Whole-programme premise |
| 10 | **Kephart & Chess (2003), "The Vision of Autonomic Computing"**, IEEE Computer. [Semantic Scholar](https://www.semanticscholar.org/paper/540e7510e92d8f24600eabd2e3ced700e31f1c23) | MAPE-K: monitor/analyse/plan/execute over shared knowledge, from high-level administrator objectives | **Organizational OS**, Intent Contract |
| 11 | **Foster, Kesselman & Tuecke (2001), "The Anatomy of the Grid"**, IJHPCA 15(3). [SAGE](https://journals.sagepub.com/doi/abs/10.1177/109434200101500302) · [PDF](https://dept-info.labri.fr/~denis/Enseignement/2008-IR/Articles/04-anatomy.pdf) | **Virtual organizations** as the unit of federated resource sharing; identity/authz as the hard part | **Federated Agent Armies** |
| 12 | **Erman, Hayes-Roth, Lesser & Reddy (1980), Hearsay-II** + **Nii (1986), "Blackboard Systems"**, AI Magazine 7(2)/(3). [AAAI](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/537) | Shared structured workspace, opportunistic knowledge sources, explicit control component | **Collective Cognition Fabric** |
| 13 | **Smith (1980), "The Contract Net Protocol"**, IEEE Trans. Computers C-29(12). [ACM](https://dl.acm.org/doi/10.1109/TC.1980.1675516) | Announce/bid/award task allocation — owns the word "contract" in MAS | **Intent Contract** (terminology) |
| 14 | **Levitt, Kunz et al., The Virtual Design Team**, CMOT. [Springer](https://link.springer.com/article/10.1007/BF00127273) · [J. Org. Design](https://www.jorgdesign.net/article/view/6345) | Computational organization simulation predicting duration, cost and coordination quality for real project organizations | **Evolution Chamber**, whole-programme |
| 15 | **Doursat, Sayama & Michel (2012), *Morphogenetic Engineering***, Springer. [Book](https://link.springer.com/book/10.1007/978-3-642-33902-8) · [Review](https://link.springer.com/article/10.1007/s11047-013-9398-1) | A named field for programmable self-architecting systems | **Morphogenetic Teams** (term) |
| 16 | **Decker, Sycara & Williamson (1997), "Middle-Agents for the Internet"**, IJCAI; **LARKS** (2002). [LARKS PDF](https://www.cs.cmu.edu/~softagents/papers/LARKS.pdf) | Matchmakers/brokers over capability advertisements — the ancestor of A2A Agent Cards | **Capability Readiness**, Staff Mesh |
| 17 | **Decker & Lesser, TÆMS + GPGP**. [AAAI ICMAS'96 PDF](https://cdn.aaai.org/ICMAS/1996/ICMAS96-036.pdf) · [AAMAS'02 evolution](https://dl.acm.org/doi/abs/10.1145/544741.544742) | Declarative task structures with quantified interrelations; modular coordination mechanisms; "exploring organizational designs" | **Org-IR**, Organizational Compiler |
| 18 | **RFC 9315 (2022), "Intent-Based Networking — Concepts and Definitions"**, IRTF NMRG. [RFC Editor](https://www.rfc-editor.org/rfc/rfc9315.html) | Standardises "intent" as declarative goals/outcomes without implementation; exists because the term was used loosely | **Intent Contract** (terminology) |
| 19 | **Cemri et al. (2025), "Why Do Multi-Agent LLM Systems Fail?"** [arXiv:2503.13657](https://arxiv.org/abs/2503.13657) | MAST: 14 failure modes over 1,600+ traces across 7 frameworks; ~42% specification, ~37% coordination, ~21% verification | Whole-programme; Organizational Debugger |
| 20 | **Hu, Lu & Clune (2024), "Automated Design of Agentic Systems"**, [arXiv:2408.08435](https://arxiv.org/abs/2408.08435) · [repo](https://github.com/ShengranHu/ADAS) | Meta Agent Search: a meta-agent programs progressively better agents in code, with an archive | **Evolution Chamber**, Organizational Compiler |
| 21 | **Mouret & Clune (2015), MAP-Elites / quality-diversity**, arXiv:1504.04909 | Archive of diverse elites instead of a single fitness score — precisely our stated evaluation preference | **Evolution Chamber** |
| 22 | **Esteva et al., ISLANDER / AMELI electronic institutions**. [AAMAS'05](https://dl.acm.org/doi/10.1145/1082473.1082575) | Declarative institution specification + runtime norm enforcement with sanctions; regimentation vs enforcement | **Executable Doctrine**, Intent Contract |
| 23 | **DoD DRRS / SORTS readiness reporting**. [DOT&E report](https://www.dote.osd.mil/Portals/97/pub/reports/FY2013/dod/2013drrs.pdf) · [CJCSI 3401.02B](https://www.jcs.mil/Portals/36/Documents/Doctrine/training/cjcsi3401_02b.pdf) | "Ready for what?" — capability assessed against mission-essential tasks under defined scenarios, not resource fill | **Capability Readiness** |
| 24 | **A2A protocol** (Google → Linux Foundation, 2025). [Repo/spec](https://github.com/a2aproject/A2A) · governance critique: [arXiv:2606.31498](https://arxiv.org/pdf/2606.31498) | Agent Cards advertising capabilities/modalities/auth over HTTP+JSON-RPC; the critique documents that MCP/A2A/ACP cannot express governance constraints | **Federated Agent Armies** |
| 25 | **Packer et al. (2023), MemGPT**, [arXiv:2310.08560](https://arxiv.org/pdf/2310.08560) + Karpathy's "context engineering" (2025) | OS virtual-memory paging applied to the context window; the industry name for context supply | **Cognitive Logistics** |

Runners-up worth reading, in order: JaCaMo (Boissier et al. 2013); Gaia (Wooldridge, Jennings &
Kinny 2000); AALAADIN/AGR (Ferber & Gutknecht 1998); MetaGPT ([arXiv:2308.00352](https://arxiv.org/abs/2308.00352));
Darwin Gödel Machine ([arXiv:2505.22954](https://arxiv.org/abs/2505.22954)); W3C PROV-O; OpenTelemetry
GenAI semantic conventions; Anthropic's multi-agent research system write-up; Cognition's
["Don't Build Multi-Agents"](https://cognition.com/blog/dont-build-multi-agents) and its 2026 revision
["Multi-Agents: What's Actually Working"](https://cognition.com/blog/multi-agents-working);
Gartner's Digital Twin of an Organization category.

---

## Deliverable 7 — Claims we must NOT make

Each item is a sentence we must not write, followed by the artefact that refutes it.

1. ❌ *"We invented the idea of compiling mission intent into an executable organization."*
   → KB-ORG (2008) does automated organization design end to end.
2. ❌ *"Organizational structure as a first-class, versioned, executable artefact is new."*
   → ODML, Moise+, OperA, AGR — and BPMN/BPEL outside MAS.
3. ❌ *"We are the first to give agents an organizational runtime."*
   → FIPA agent platforms (1999); ORA4MAS (2008); JaCaMo (2013).
4. ❌ *"Stigmergic coordination for software agents is a novel mechanism."*
   → Grassé 1959; ACO 1992; digital pheromone infrastructure 2000–02; Co-Fields/TOTA 2004–09.
5. ❌ *"Teams that grow, split, merge and dissolve by local rules is a new idea."*
   → Organization Self-Design (1992); Morphogenetic Engineering as a named field (2012).
6. ❌ *"We invented organizational debugging / causal replay of an organization."*
   → Poutakidis et al. (2002); organizational mining (2005–); PROV-O; time-travel debugging.
7. ❌ *"Persistent staff functions that maintain organizational awareness are novel."*
   → PROSA staff holons (1998); middle-agents (1997); blackboard control components (1980).
8. ❌ *"Declarative intent with bounded authority is a new contract type."*
   → RFC 9315; deontic norms in e-institutions; Design by Contract.
9. ❌ *"Policy that is executable and versioned is our contribution."*
   → Rete → Drools; Ponder/Rei/KAoS/XACML; OPA/Rego policy-as-code.
10. ❌ *"Readiness as a graded, evidence-backed measure is new."*
    → TRL (1974), CMMI (1991), SORTS/DRRS, Kubernetes readiness probes.
11. ❌ *"Treating context and tools as logistics is our framing."*
    → Information Logistics (2000s); context engineering (2025); MemGPT (2023).
12. ❌ *"Federated interoperating agent organizations is a frontier we opened."*
    → Grid virtual organizations (2001); FIPA (1999); A2A (2025, 150+ organizations).
13. ❌ *"Simulating an organization before running it is new."*
    → The Virtual Design Team, validated against real construction/engineering projects, 1990s.
14. ❌ *"Searching a space of organization designs against a fitness measure is new."*
    → ODML search, KB-ORG pruning, MAP-Elites, ADAS, AFlow, AgentSquare, DGM.
15. ❌ *"We are creating the field of artificial organization engineering."*
    → Computational Organization Theory (Carley & Prietula 1994) is the parent field. We may claim
    a successor position; we may not claim origination.
16. ❌ *"An organizational digital twin is a new product category."*
    → Gartner DTO, with a Magic Quadrant and funded vendors.
17. ❌ *"Research shows multi-agent systems underperform single agents."*
    → The mean is −3.5% with a 95% CI of [−18.6%, +25.7%] — **not distinguishable from zero** — from
    **one** study, which also reports +80.9% on a parallelisable task. The defensible statement is:
    *"multi-agent performance is dominated by architecture–task alignment; on sequential shared-state
    tasks every tested multi-agent architecture degraded performance by 39–70%."*
18. ❌ *"Anthropic's 90.2% result proves multi-agent works."*
    → `MARKETED`. Internal, unpublished eval, vendor-run, at ~15× tokens, with the vendor's own
    caveat that coding is less parallelisable.
19. ❌ *"Agent Army is implemented in agent-factory."* → `CURRENT_STATE.md`: the term sweep across
    `factory/`, `evaluator_service/` and `scripts/` returns nothing.
20. ❌ *"The organization is autopoietic."* → It is a control loop. Autopoiesis means something else.

---

## Failure modes

**If the recommendation is wrong — i.e. if the prior art is less relevant than I claim:**

- We rename and cite for nothing. Cost: low. Renaming costs a week; a plagiarism accusation or a
  reviewer who recognises KB-ORG costs the programme's credibility.
- We under-claim novelty and someone else claims the category. Cost: real but bounded — the
  narrow claim in §Narrowest defensible claim is the defensible core, and defending a small true
  claim beats losing a large false one.

**If the recommendation is right and we ignore it:**

- We spend months rebuilding ODML and KB-ORG under new names, with less rigour than the originals,
  and discover the prior art at review time.
- We publish something that is refuted by a 2008 JAAMAS paper.
- The whole-programme risk: the biggest failure mode is *building the organizational layer at all*.
  Every survivor in the novelty risk map is about evidence and verification, not structure. A
  programme that builds Stigmergic Fields before it builds evidence-gated capability claims will
  have built the part that already exists and skipped the part that does not.

**Specific measurement failure mode already present:** a real number (−3.5%) travelled three hops
and lost its confidence interval on hop two. The same mechanism will strip caveats off every other
number this programme produces unless the interval is carried in the same string as the estimate.

---

## Data-model implications

- **Adopt Moise+'s three-way split for the Organization Specification**: structural (roles, groups,
  links), functional (missions, schemes, goals), deontic (permissions, obligations). Our current
  Org-IR is flat and will need this seam later, when it is expensive to add.
- **Express the debugger's causal edges in W3C PROV-O terms.** `caused_by` → `wasInformedBy`,
  `used_evidence` → `used`, `produced` → `wasGeneratedBy`, `constrained_by` has no PROV analogue
  and is genuinely ours. This buys interoperability and standard tooling.
- **Keep `sourceRootId` and `independentSourceGroup` in the Evidence type** (`architecture/06`).
  These are the least-precedented fields in the entire ontology and are directly implicated by
  Finding 4 — the failure of six citations to be six pieces of evidence.
- **Keep `sampleSize` on Capability.** No prior capability model I found carries it. A2A Agent
  Cards are pure self-declaration; this is our differentiator against them.
- **Add a mission-class dimension to readiness.** Per DRRS: readiness is `(capability, mission
  class)`, never a scalar on an agent.
- **Add `verdict` as a four-value enum wherever a check result is stored**, mirroring
  `agent-factory/factory/contract.py:17-21` (PASS / FAIL / UNMEASURABLE / NOT_RUN). This does not
  exist anywhere in `architecture/` today and it is our strongest asset.

## Runtime implications

- **The event log is the load-bearing novelty in the Organizational OS, not the OS.** ADR-0002 is
  correct and should be defended; the rest of the "OS" framing should be dropped.
- **Steal OTP's restart-strategy vocabulary** (one-for-one / one-for-all / rest-for-one) for cell
  failure policy rather than inventing one.
- **Adopt PROSA's decoupling**: staff functions supply the control *algorithm*; the runtime owns
  the control *structure*. And follow PROSA in making staff advisory-only by default — that
  resolves the open authority question in `architecture/02` in the direction the prior art
  validated.
- **Emit OpenTelemetry GenAI spans** rather than a bespoke trace format. The conventions cover
  agent spans, tool calls and evaluation metadata; the agent/tool-orchestration parts are still
  settling, so treat them as provisional and version the mapping.
- **Assume A2A as federation transport.** Do not design a bespoke protocol. Our contribution is
  the evidence/provenance payload that A2A does not carry.

## UI implications

- The "lenses" list in `vision/01` is 17 items long and every one of them is a projection over the
  event log. The prior art here is process-mining visualisation and the **Common Operational
  Picture** — both worth studying before designing.
- **Drop "Organizational Digital Twin" from all UI copy** — Gartner owns the category. "Organization
  World State" or "Common Operational Picture" (which we already use in `vision/01` and which is
  the correct doctrinal term) both work.
- The UI's genuinely novel surface is the one that shows **which claims are unverified and which
  instruments were dark**. A lens that renders `UNMEASURABLE` distinctly from `FAIL` is something
  no observability product currently does, and it is the visual expression of our actual novelty.
- ADR-0004 (no random agent animation) is well judged and consistent with everything above:
  motion must encode a measured quantity.

## Performance implications

- **Coordination cost grows superlinearly.** The scaling study measures interaction count growing
  ~`n^1.724` under fixed budget, constraining useful teams to roughly 3–4 agents. Any Morphogenetic
  Teams rule that can grow a cell must be bounded by this, and the bound should be a configured
  constant with the citation next to it.
- **Error amplification is architecture-dependent**: 17.2× for independent multi-agent vs 4.4× for
  centralised. This is an argument *for* a coordinator and *against* free peer-to-peer messaging,
  and it should be recorded in `architecture/00` as a design constraint.
- **Capability saturation ~45%.** Once the single-agent baseline exceeds ~45% on a task class,
  coordination gains diminish or reverse (β = −0.408, p<0.001). This gives the Organization
  Synthesiser an actual admission test: measure the single-agent baseline first; if it is above
  ~45%, do not decompose.
- Multi-agent research at Anthropic costs ~15× the tokens of chat. Budget envelopes in the Intent
  Contract are therefore not optional.

## Security/governance implications

- **Permission topology outranks prompt topology** (R2's phrase, and I found nothing to contradict
  it). Prompt-based constraint is not an enforcement boundary; the e-institutions literature made
  the same distinction 20 years ago as *regimentation* vs *enforcement*, and we should adopt that
  vocabulary because it is precise.
- **Agent-declared capability is an attack surface.** A2A Agent Cards are self-asserted. Our
  evidence-backed capability model is a security property, not just an accuracy one — treat it as
  such in the threat model.
- **Speculative work leaves traces.** The Temporal Echelons guardrails cover budget, expiry and
  cancellation but not *information leakage from cancelled speculative work*. Spectre is the
  cautionary precedent; a LATER-horizon agent that reads production data and is then cancelled has
  still read it.
- **Federation must not ship before identity.** The Grid's history is the strongest available
  support for `architecture/10`'s own non-goal. Keep that non-goal; it is well-founded.
- **The evolution genome prohibition is the governance contribution.** ADAS and DGM mutate agent
  code freely. Our refusal to let constitution, hard permissions and audit rules into the genome is
  the part of the Evolution Chamber worth publishing.

---

## Experiments required

Falsifiable, each with a predicted result stated before running.

**E1 — Does organizational structure help at all, at our scale?**
Same tasks, same budget, same authoritative verifier: one worker vs a structured organization.
Threshold already set by `orchestrator_team.yaml`: ≥10pp absolute terminal-success gain, or ≥20%
lower cost at indistinguishable success, no increase in side effects, every mandatory handoff ≥99%
accepted-and-correctly-consumed. *Prediction: fails on our current sequential connector work; the
literature's sequential-task result predicts degradation.* This is the programme's crux experiment
and everything else is downstream of it.

**E2 — Does an evidence-gated close change outcomes, or only paperwork?**
A/B the `require=` argument on task close over N real deliveries. Measure: rate of deliveries later
found defective. *Prediction: measurable reduction, because this is the one mechanism with no prior
art and the MAST verification-failure share (21%) is the headroom.*

**E3 — Does `UNMEASURABLE` change behaviour, or is it a label?**
Count how often `UNMEASURABLE` is emitted and what happens next. If it is never emitted, the
instrument is not honest. If it is emitted and treated like FAIL, the distinction is decorative.
*Prediction: emitted at a low but nonzero rate; the risk is silent collapse into PASS.*

**E4 — Does capability-readiness-with-sample-size change routing?**
Compare routing decisions made with vs without `sampleSize` and `historicalSuccessRate` visible.
*Prediction: changes decisions only where sample sizes are small — which is where it matters.*

**E5 — Does a stigmergic field beat direct messaging on our work?**
`experiments/02-experiment-matrix.md` already frames this. Given the prior art, the question is not
whether fields work (they do) but whether our organizational signals carry enough information to
beat an explicit dependency graph. *Prediction: loses to an explicit graph on software work, because
our task graph is known, not discovered — stigmergy pays off when the topology is unknown.*

**E6 — Replication check on the load-bearing study.**
Re-run a reduced version of the scaling study's design on our own task distribution before adopting
its thresholds (45% saturation, n^1.724). *Prediction: direction replicates, magnitudes do not.*

**E7 — Does the −3.5% figure survive the Nature revision?**
Purely bibliographic. Obtain the Nature MI version and check whether the aggregate mean and its
interval changed when the study expanded from 180 to 260 configurations. Currently NOT-ACCESSIBLE.

---

## Recommendation

```text
NOW
  · Rename per Deliverable 5 before ANY external publication.
  · Add the prior-art citation to each architecture/ file's header (one line each).
  · Fix the two files that quote −3.5% without its interval (agent-factory
    blueprints/orchestrator_team.yaml and docs/agent-army/CURRENT_STATE.md), and cite
    arXiv:2512.08296 by ID. NOTE: not done by this pass — I was scoped to one file.
  · Adopt PROV-O vocabulary in architecture/09 and Moise+'s three-way split in the Org Specification.
  · Add the four-verdict enum to the ontology.

NEXT
  · Run E1. Nothing organizational should be built before it resolves.
  · Run E2 and E3 — these test the actual novelty claim.
  · Adopt DRRS's (capability, mission class) pairing in architecture/03.

LATER
  · Organization Synthesiser, once E1 says structure helps AND KB-ORG's application-vs-coordination
    knowledge distinction has been read properly (someone must obtain the UMass PDF and read it).
  · Federation — after permissions, provenance, evidence contracts, audit and organization identity.
    This ordering is already in architecture/10 and is validated by the Grid's history.

RESEARCH ONLY
  · Coordination Fields (ex-Stigmergic Fields), Adaptive Team Formation, Organization Design Lab.
    All three have mature prior art to read before any code is written.
  · Temporal/Planning Horizons — the least-precedented concept, therefore the most worth studying,
    and the one where deliberation-scheduling theory could give principled thresholds.

DO NOT BUILD
  · Anything named "Organizational OS", "Executable Doctrine", "Evolution Chamber" or
    "Organizational Digital Twin" as an external-facing artefact.
  · A bespoke federation protocol (use A2A).
  · A bespoke trace format (use OpenTelemetry GenAI conventions).
  · Autopoiesis. It is not a mechanism.
```

### Required closing table (RESEARCH_PROTOCOL)

| IDEA | EVIDENCE | USER VALUE | PERFORMANCE VALUE | COMPLEXITY | RISK | BUILD NOW? | EXPERIMENT? |
|---|---|---|---|---|---|---|---|
| Evidence-gated close + four verdicts | C (our own, in code) | High | Neutral | Low | Low | **Yes — already partly built** | E2, E3 |
| Grader separation | C (our own) | High | Neutral | Medium | Low | **Yes** | E2 |
| Mission Contract (ex-Intent Contract) | B (RFC 9315, e-institutions) | High | Neutral | Medium | Low | Yes, as a schema | E1 |
| Capability readiness w/ sample size | B (DRRS, TRL) + D (our extension) | Medium | Medium | Medium | Low | Next | E4 |
| Organization event log | A (event sourcing) | Medium | Neutral | Medium | Low | Yes | — |
| Staff functions (advisory) | B (PROSA, middle-agents) | Medium | Low | Medium | Medium | Next | E1 |
| Planning horizons (ex-Temporal Echelons) | C (anytime algorithms) | Medium | Medium | Medium | Medium | Later | E1 |
| Organization Synthesiser | A (KB-ORG) as research; D for us | Medium | Unknown | High | High | Later | E1 |
| Organizational Debugger | A (process mining) | High | Neutral | High | Medium | Later | — |
| Context Logistics | B (information logistics, context engineering) | Medium | **High** | Medium | Low | Next | — |
| Organizational Policy (ex-Doctrine) | A (OPA, Rete) | Medium | Neutral | Medium | Low | Later | — |
| Coordination Fields | A (as a mechanism) / D (for our domain) | Low | Unknown | High | High | No | E5 |
| Adaptive Team Formation | A (OSD 1992) / D (governed, at LLM scale) | Low | Unknown | High | **High** | No | E1 first |
| Organization Design Lab | B (MAP-Elites, VDT, ADAS) | Low | Unknown | Very high | **High** | No | — |
| Federated Organizations | B (Grid, A2A) | Low | Neutral | High | High | No | — |

---

## Claims ledger

| Claim | Evidence tier | Primary support | Counterevidence | Confidence |
|---|---|---|---|---|
| Automated organization design for MAS was demonstrated in 2008 | B (DERIVED — abstract + multiple syntheses, full text not read) | KB-ORG, JAAMAS 2008 | None found | High |
| Field-based coordination shipped as middleware in the 2000s | B (DERIVED) | TOTA, ACM TOSEM 2009; Co-Fields | None found | High |
| PROSA contains "staff holons" | B (DERIVED — described consistently across syntheses) | Van Brussel et al. 1998 | I did not read the paper | Medium-High |
| "Morphogenetic Engineering" is a named field | B (DERIVED) | Springer volume 2012 + Natural Computing review | None | High |
| Organizational mining is a named process-mining subfield | B (DERIVED) | van der Aalst et al. 2005; OrgMining 2.0 | None | High |
| The −3.5% figure is real and verbatim | **A (OBSERVED)** | arXiv:2512.08296v1 full text, fetched | None | Very high |
| Its 95% CI is [−18.6%, +25.7%] and is dropped downstream of R2 | **A (OBSERVED)** | Same fetch; `R2-answer-topology.md:15` has it; `orchestrator_team.yaml` and `CURRENT_STATE.md` do not | None | Very high |
| Sequential tasks degrade 39–70% across all tested MAS variants | **A (OBSERVED)** | arXiv:2512.08296v1 abstract | Single study | High |
| The evidence base for "multi-agent underperforms" traces largely to one study | C (DERIVED from search-result convergence) | Repeated citation of 2512.08296 across secondary sources | I cannot prove a negative about the whole literature | Medium |
| Anthropic's 90.2% is `MARKETED` | B | Anthropic's own engineering post; internal eval | It is a real production system | High |
| Cognition has revised its "don't build multi-agents" position | C (DERIVED — title and summary of the 2026 post) | cognition.com/blog/multi-agents-working | Did not read in full | Medium |
| Agent Army terms appear nowhere in agent-factory Python | **A (OBSERVED)** | `CURRENT_STATE.md` with a regenerable grep command | I did not re-run the grep myself | High |
| Four-verdict / grader-separation / evidence-gated-close have no prior art | C | Absence across ~35 searches | Absence of evidence; a targeted search of the SE-testing literature could refute | **Medium** |
| "Echelon" means command level, not time horizon | B | Military usage; ADP 5-0 structure | None | High |
| Nature MI version of the scaling study | NOT-ACCESSIBLE | 303 to idp.nature.com | — | — |

---

## Changed-my-mind section

**Assumption weakened: that Agent Army's risk was "LLM people reinventing 2023 multi-agent
frameworks".** It is not. The dangerous prior art is 1992–2008 organizational MAS, which almost
nobody in the current LLM-agent discourse cites, and which did all of this more rigorously than the
current generation. The exposure is to an academic reviewer, not to a competitor.

**Assumption overturned: that the −3.5% figure was probably a loose summary of something softer.**
The brief told me to treat it as a claim to verify, and I expected to find it unattributable. It is
exact, it is verbatim, and the underlying study matches our description of it configuration for
configuration. `R2-answer-topology.md` is one of the better-cited research documents I have read.
The failure is not in the research — it is in the *summarisation chain*, where a confidence
interval spanning zero was dropped between R2 and the two files people actually read.

**Assumption weakened: that "the LLM era changes everything".** Three things changed. Coordination
overhead, structural opacity, and the difficulty of governing self-modifying organizations did not.
Two of those three unchanged things are exactly what the Evolution Chamber and Morphogenetic Teams
depend on.

**Assumption reversed: that the novelty, if any, would be in the organizational design.** It is not.
Every survivor in the novelty risk map is an epistemic mechanism — evidence independence, sample
size on capability claims, evidence-conditioned breakpoints, the four-verdict contract, grader
separation. The organizational vocabulary is the part with the most prior art and the least defensible
claim, and the epistemic plumbing — which nobody wrote a manifesto about — is the part that is ours.

**Assumption weakened: that "fabric" and "mesh" were harmless flavour words.** We have them backwards
relative to their industry meanings, which is worse than not using them.

---

## Open questions

1. Did KB-ORG's automated organization design ever get deployed outside the distributed-sensor-network
   testbed? If yes, the concept is more thoroughly closed than I have stated. **Requires the UMass PDF.**
2. Why did organization-oriented MAS not reach industry? My "the agents were too expensive"
   explanation is `ASSUMED`. A retrospective by Boissier, Hübner or Zambonelli would settle it, and
   the answer changes whether we are reviving a good idea or repeating a bad one.
3. Does the Nature MI expansion (180→260 configs) change the aggregate mean or its interval?
4. Is there prior art for `UNMEASURABLE` as a first-class verdict in the software-testing or
   scientific-instrumentation literature? I searched the agent and organizational literature, not
   the metrology or SE-testing literature. **This is the single most important remaining search,
   because it is the one that could kill our narrow claim.**
5. Does any LLM-agent memory system track evidence *independence* (our `sourceRootId`)? I found
   none, but I surveyed a small number.
6. Is "Artificial Organization Engineering" genuinely unclaimed as a field name? My check was a
   single search.
7. What is the actual relationship between our Running Estimate schema and TÆMS's quantified task
   interrelations? They may be closer than I have assessed. **Requires the TÆMS papers.**

---

## Proposed architecture changes

1. `architecture/00-target-architecture.md` — add a "Prior art and lineage" section naming, per
   component, the system it descends from. This is cheap and it permanently inoculates the programme.
2. `architecture/02-organizational-staff-mesh.md` — rename to `02-organizational-staff-functions.md`;
   state that staff are **advisory by default** (PROSA); add the control-structure/control-algorithm
   decoupling as an explicit design property.
3. `architecture/05-temporal-echelons.md` — rename to `05-planning-horizons.md`; add deliberation
   scheduling (Dean & Boddy 1988) as the basis for promotion criteria; add a *speculative-work
   information-leakage* guardrail alongside budget/expiry/cancellation.
4. `architecture/08-organization-compiler-pipeline.md` — rename to `08-organization-synthesis-pipeline.md`;
   split pass 5 (candidate topology generation) into application-level and coordination-level
   knowledge, per KB-ORG; add an admission test at pass 1 that measures the single-agent baseline
   and refuses decomposition above ~45%.
5. `architecture/09-organizational-debugger-model.md` — map every causal edge to PROV-O; state that
   the *replay* half is conformance checking and cite process mining; keep the evidence-sufficiency
   breakpoint as the contributed mechanism and say so.
6. `architecture/06-knowledge-evidence-model.md` — promote `independentSourceGroup` from optional to
   required, with Finding 4 as the rationale.
7. `architecture/03-cognitive-logistics.md` — rename to `03-context-logistics.md`; make readiness a
   `(capability, mission class)` pair; keep verification capacity and human attention as supplies
   and flag them as the novel part.
8. **New file** — `architecture/13-verification-and-verdicts.md`, specifying the four-verdict model,
   grader separation and evidence-gated close, ported from `agent-factory`. This is currently the
   programme's strongest asset and it has no home in the research architecture.
9. `ontology/00-core-ontology.md` — add `Verdict` and `Readiness(capability, missionClass)`.

## Proposed ADRs

- **ADR-0008 — Adopt prior-art terminology where it exists.** We use the literature's word unless we
  can state what our thing does that theirs does not. Consequence: the renames in Deliverable 5.
- **ADR-0009 — Every published figure carries its uncertainty in the same string as the estimate.**
  Triggered by the −3.5% interval loss. Consequence: a summarisation rule, enforceable in review.
- **ADR-0010 — `UNMEASURABLE` is a first-class verdict across the whole programme.** Consequence:
  no boolean pass/fail anywhere in the ontology, runtime or UI.
- **ADR-0011 — Federation transport is A2A; observability transport is OpenTelemetry GenAI.** We
  contribute payload semantics, not protocols. Consequence: `architecture/10` becomes a payload spec.
- **ADR-0012 — Structure is gated on E1.** No organizational mechanism is built before a same-budget
  A/B shows structure helps on our own work. Consequence: makes the existing `agent-factory` unlock
  rule ("agent army ← one certified team") binding on the research programme too.

---

## Sources

`‡` = fetched and read directly this session. All others were surfaced by search and are cited at
bibliographic + abstract level; see the research-debt note in the metadata.

**Load-bearing, verified**
- ‡ Kim et al., *Towards a Science of Scaling Agent Systems* — https://arxiv.org/abs/2512.08296 ·
  v1 https://arxiv.org/abs/2512.08296v1 · full text https://arxiv.org/html/2512.08296v1
- Nature Machine Intelligence version — https://www.nature.com/articles/s42256-026-01268-y — **NOT-ACCESSIBLE (paywall)**
- ‡ CrewAI process documentation — https://docs.crewai.com/en/concepts/processes
- ‡ `agent-factory/blueprints/orchestrator_team.yaml`, `docs/agent-army/CURRENT_STATE.md`,
  `docs/research/answers/R2-answer-topology.md`

**Organizational MAS / AOSE**
- KB-ORG — https://link.springer.com/article/10.1007/s10458-007-9023-8 · http://mas.cs.umass.edu/Documents/07-43.pdf
- Organization of Multi-Agent Systems: An Overview — https://arxiv.org/pdf/1506.09032
- Multi-Agent Architectures as Organizational Structures — https://link.springer.com/article/10.1007/s10458-006-5717-6
- Generating and choosing organisations for MAS — https://link.springer.com/article/10.1007/s10458-023-09623-8
- Moise — https://moise-lang.github.io/ · ORA4MAS — https://link.springer.com/chapter/10.1007/978-3-540-79003-7_13
- Gaia — https://www.researchgate.net/publication/2881997_Developing_Multiagent_Systems_The_Gaia_Methodology
- TÆMS/GPGP — https://cdn.aaai.org/ICMAS/1996/ICMAS96-036.pdf · https://dl.acm.org/doi/abs/10.1145/544741.544742
- Contract Net — https://dl.acm.org/doi/10.1109/TC.1980.1675516
- Middle-agents / LARKS — https://www.cs.cmu.edu/~softagents/papers/LARKS.pdf
- Electronic institutions — https://dl.acm.org/doi/10.1145/1082473.1082575
- FIPA Abstract Architecture — http://www.fipa.org/specs/fipa00001/PC00001H.html
- Debugging MAS using design artifacts — https://dl.acm.org/doi/10.1145/544862.544966

**Stigmergy / fields / morphogenesis / holons**
- TOTA — https://dl.acm.org/doi/10.1145/1538942.1538945 · Co-Fields — https://www.tandfonline.com/doi/full/10.1080/08839510500484264
- Digital pheromones — https://dl.acm.org/doi/10.1145/544741.544843 · http://biomimetic.pbworks.com/f/Digital%20pheromone%20mechanisms%20for%20coordinationParunaK.pdf
- Morphogenetic Engineering — https://link.springer.com/book/10.1007/978-3-642-33902-8 · https://link.springer.com/article/10.1007/s11047-013-9398-1
- PROSA — https://www.sciencedirect.com/science/article/abs/pii/S016636159800102X · https://www.mech.kuleuven.be/en/pma/research/MACC/prosapaper

**Organization theory / simulation / process mining**
- Virtual Design Team — https://link.springer.com/article/10.1007/BF00127273 · https://www.jorgdesign.net/article/view/6345 · https://cdn.aaai.org/Symposia/Spring/1994/SS-94-07/SS94-07-015.pdf
- Discovering social networks from event logs — https://dl.acm.org/doi/10.1007/s10606-005-9005-9
- OrgMining 2.0 — https://arxiv.org/pdf/2011.12445
- Process mining from the organizational perspective — https://link.springer.com/chapter/10.1007/978-3-642-54924-3_66

**Autonomic / policy / provenance / readiness**
- Kephart & Chess — https://www.semanticscholar.org/paper/540e7510e92d8f24600eabd2e3ced700e31f1c23
- RFC 9315 — https://www.rfc-editor.org/rfc/rfc9315.html
- Open Policy Agent — https://www.openpolicyagent.org/docs/policy-language
- Kubernetes probes — https://kubernetes.io/docs/concepts/workloads/pods/probes/
- DRRS — https://www.dote.osd.mil/Portals/97/pub/reports/FY2013/dod/2013drrs.pdf · CJCSI 3401.02B — https://www.jcs.mil/Portals/36/Documents/Doctrine/training/cjcsi3401_02b.pdf
- TRL — https://en.wikipedia.org/wiki/Technology_readiness_level
- ADP 5-0 — https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN18126-ADP_5-0-000-WEB-3.pdf

**Federation / grid / interop**
- Anatomy of the Grid — https://journals.sagepub.com/doi/abs/10.1177/109434200101500302 · https://dept-info.labri.fr/~denis/Enseignement/2008-IR/Articles/04-anatomy.pdf
- A2A — https://github.com/a2aproject/A2A · https://en.wikipedia.org/wiki/Agent2Agent
- Governance gaps in MCP/A2A/ACP — https://arxiv.org/pdf/2606.31498

**LLM-era agent systems**
- MAST — https://arxiv.org/abs/2503.13657
- ADAS — https://arxiv.org/abs/2408.08435 · https://github.com/ShengranHu/ADAS
- AFlow — https://arxiv.org/pdf/2410.10762 · AgentSquare — https://arxiv.org/pdf/2410.06153
- Darwin Gödel Machine — https://arxiv.org/abs/2505.22954
- MetaGPT — https://arxiv.org/abs/2308.00352
- MemGPT — https://arxiv.org/pdf/2310.08560
- Anthropic, when to use multi-agent systems — https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
- Cognition — https://cognition.com/blog/dont-build-multi-agents · https://cognition.com/blog/multi-agents-working
- LangGraph supervisor — https://github.com/langchain-ai/langgraph-supervisor-py
- OpenTelemetry GenAI conventions — https://openobserve.ai/blog/opentelemetry-genai-semantic-conventions/

**Terminology collisions**
- EOS® — https://www.eosworldwide.com/what-is-eos
- Doctrine PHP — https://www.doctrine-project.org/
- Evolution Chamber (StarCraft) — https://liquipedia.net/starcraft2/Evolution_Chamber_(Legacy_of_the_Void)
- Gartner DTO — https://www.gartner.com/en/documents/4004172 · https://www.gartner.com/reviews/market/digital-twin-of-an-organization-platforms
- Data mesh / data fabric — https://www.alation.com/blog/data-mesh-vs-data-fabric/
- Information logistics — https://link.springer.com/chapter/10.1007/978-3-642-25370-6_24 · https://en.wikipedia.org/wiki/Information_logistics
- Cognitive logistics (COG-LO, H2020) — https://cordis.europa.eu/project/id/769141
- Swarm cognition — https://link.springer.com/article/10.1007/s11721-010-0050-8
- Context engineering — https://www.langchain.com/blog/context-engineering-for-agents

---

## Narrowest defensible novelty claim for Agent Army

Answering the brief's closing question directly, and deliberately narrowly.

> **An organizational runtime whose unit of organizational truth is an evidence-bound claim rather
> than a status — in which a capability, a readiness state and a completed task each cannot be
> asserted without naming the evidence that supports them and the sample that produced them; in
> which "the instrument could not run" (`UNMEASURABLE`) is a first-class verdict that can never be
> collapsed into pass or fail; in which the refusal to close without evidence lives in the store
> rather than in agent instructions; and in which the evidence graph tracks source independence, so
> that six corroborating records deriving from one root are counted as one.**

That is the whole claim. Note what it does **not** say. It does not claim organizational
compilation, stigmergy, morphogenesis, staff functions, executable policy, readiness, federation,
context logistics, evolutionary organization search, or organizational debugging — every one of
those has implemented, published prior art, and seven of them have prior art that used almost our
exact word.

Three properties make this claim defensible:

1. **It is falsifiable and cheap to test.** E2 and E3 either show it changes outcomes or it does not.
2. **It is already partly built and cited to file and line** — `factory/contract.py:17-21`,
   `factory/evidence.py:48`, `factory/tasks.py:163`, `factory/corpus.py`, `factory/certify.py:15-17`.
   A novelty claim backed by running code beats one backed by an architecture document.
3. **It is the only column in the novelty risk map with no CRITICAL entry.** Everything that
   survived the prior-art sweep is epistemic, and this sentence is what those survivors have in common.

The one thing that could kill it — and it should be searched before this claim is published — is
prior art for `UNMEASURABLE` as a first-class verdict in the software-testing or scientific-
instrumentation literature. I searched the agent, organizational and process-mining literature and
found nothing. I did not search metrology. **Until that search is done, this claim is HIGH
confidence, not established.**

A closing observation the programme should sit with. Agent Army's name, vocabulary and visual
ambition are all about *organization*. Its defensible novelty is about *evidence*. Those point in
different directions, and the gap between them is where a research programme quietly becomes a
branding exercise. The narrow claim above is worth more than the broad one precisely because it
survives contact with sixty years of prior art — and because it happens to be the only part of the
vision that is already running.
