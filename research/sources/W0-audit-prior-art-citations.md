# W0 — Evidence Audit: R01's Prior-Art Citations

```yaml
audit_id: W0
audit_date: 2026-08-30
auditor: Claude Opus 5 (claude-opus-5[1m]), local subagent, evidence-auditor skill
target: research/answers/R01-answer-prior-art-and-novelty-boundary.md
scope: >
  The 7 CRITICAL novelty verdicts and the citations that carry them, plus the
  Moise+/ORA4MAS/JaCaMo lineage R00 leans on.
method: >
  Every claim below was checked against a primary artefact or an authoritative
  bibliographic register (Crossref DOI record, DOI handle resolution, publisher
  metadata, or the full text of the paper itself). Two full PDFs were downloaded and
  read via text extraction. Nothing here is assessed on plausibility.
artefacts_read_in_full_or_substantially:
  - Sims, Corkill & Lesser, UMass CS Technical Report 07-43 (42 pp., full text extracted)
  - Van Brussel et al., PROSA, Computers in Industry 37 (1998) 255-274 (full text extracted)
  - Horling, PhD dissertation, UMass Amherst 2006 (3.1 MB, full text extracted, targeted read)
  - Hübner, Sichman & Boissier, Moise+ paper (title page + abstract + intro extracted)
bibliographic_registers_queried:
  - api.crossref.org (8 DOI/bibliographic queries)
  - doi.org/api/handles (1 handle resolution)
  - api.semanticscholar.org/graph/v1 (3 queries; 2 rate-limited, 2 abstracts elided by publisher)
not_accessible:
  - Springer full text of KB-ORG JAAMAS 16(2) — 303 to idp.springer.com. Mitigated: the
    authors' own UMass tech report of the same work WAS read in full.
  - ScienceDirect PROSA page — HTTP 403. Mitigated: the KU Leuven author-hosted PDF of the
    same paper WAS read in full.
  - ORA4MAS full chapter (Springer paywall; abstract elided from both Crossref and
    Semantic Scholar records). See Claim 7c.
```

---

## Executive summary

**Six of the seven citation groups check out. R01's bibliography is, on this sample, materially
more accurate than the audit brief assumed.** Authors, venues, years and — crucially —
*characterisations* are correct in the great majority of cases. PROSA's "staff holons" claim, the
single most quotable line in R01, is not merely correct; the primary text is stronger than R01's
summary of it.

**Three things must nevertheless be corrected**, and one of them is in the audit brief rather than
in R01:

1. **The audit brief's calibration warning is itself wrong.** The brief states that R01's "landed
   in Nature MI 2026" attribution "does not survive checking" because arXiv:2512.08296 carries no
   journal reference. The absent journal-ref is real, but the inference from it is not. DOI
   `10.1038/s42256-026-01268-y` **resolves** (handle responseCode 1, registered 2026-07-24) and
   Crossref returns a complete record: *Capable language models can outgrow the benefits of
   collaboration*, **Nature Machine Intelligence 8(7):1157–1172**, 2026-07-24, with the identical
   20-author list. R01's attribution is **SUPPORTED**. What R01 missed is that the journal version
   was **retitled** — which is both why arXiv shows no journal-ref and why a title search fails.
   The retitle matters on its merits: the journal title asserts a *directional* conclusion the
   preprint title does not.
2. **ODML is not an intermediate representation.** It is a predictive quantitative design model.
   The mapping "ODML = Org-IR" is wrong in kind. The Org-IR CRITICAL verdict survives, but on
   Moise+/OperA/AGR — not on the source R01 names for it.
3. **"Organizational mining" is mis-sourced by three years.** The 2005 CSCW paper discovers social
   networks; the subfield R01 describes (role mining, resource allocation, comprehensive
   organizational perspective) is named and delivered in Song & van der Aalst, *Decision Support
   Systems* 46:300–317, 2008.

**Independence is the finding with the most force against R01's framing.** R01 presents seven
CRITICAL verdicts as if backed by seven independent results. They are not. Two of the three
citations behind the Organizational Compiler and Org-IR verdicts are **back-to-back articles in
the same issue of the same journal from the same laboratory, sharing an author** — and a third
modern precedent R01 offers traces to the Moise circle. Four lineages are genuinely independent.
Seven results are not. See §Independence.

**Disposition of the seven CRITICAL verdicts: five survive at CRITICAL, two drop to HIGH.** See
§Disposition.

---

## Claim-by-claim

### Claim 1 — KB-ORG is a fully automated knowledge-based organization design framework

> R01: "KB-ORG (Sims, Corkill & Lesser, JAAMAS 2008): 'a fully automated, knowledge-based
> organization design framework' that uses situational parameters plus application-level AND
> coordination-level design knowledge to prune and direct a search over candidate organizations …
> which is the Organizational Compiler, including the diagnostics."

- **Verdict: SUPPORTED** (with one overreach — see counterevidence)
- **Evidence tier: OBSERVED.** I read the 42-page full text, not an abstract.
- **Strongest source:** Sims, Corkill & Lesser, *Knowledgeable Automated Organization Design for
  Multi-Agent Systems*, UMass CS Technical Report 07-43, 16 Aug 2007 —
  http://mas.cs.umass.edu/Documents/07-43.pdf. Journal of record: *Automated organization design
  for multi-agent systems*, **Autonomous Agents and Multi-Agent Systems 16(2):151–185, 2008**,
  DOI [10.1007/s10458-007-9023-8](https://doi.org/10.1007/s10458-007-9023-8) (Crossref-verified:
  title, three authors, journal, volume, issue, pages, year all exactly as R01 states).

Verbatim from the abstract:

> "we present KB-ORG: a fully automated, knowledge-based organization designer for multi-agent
> systems. Organization design is the process that accepts organizational goals, environmental
> expectations, performance requirements, role characterizations, and agent descriptions and
> assigns responsibilities and roles to each agent."

> "KB-ORG uses both application-level and coordination-level organization design knowledge to
> explore the combinatorial search space of candidate organizations selectively."

Every load-bearing element of R01's sentence is present in the source: *fully automated* (verbatim,
twice — abstract and §1), *knowledge-based organization design framework* (verbatim, §1),
*situational parameters* (verbatim), the application-level/coordination-level split (verbatim), and
selective search over candidate organizations. It is **design, not analysis**: it generates
organizations from inputs. It was **implemented** — §"In the current implementation, the developer
supplies this information to KB-ORG as Java classes."

- **Counterevidence:** R01's "including the diagnostics" is not supported. KB-ORG has an
  *organizational evaluation function* over user-specified criteria, which is scoring, not
  diagnosis. The only diagnostic-shaped element is a closed loop described in the **future tense**
  as future work: "The agents will instantiate the organization and provide feedback to KB-ORG as
  the environment, requirements, tasks, and agent capabilities change." As built, KB-ORG is a
  one-shot designer plus evaluator. The Organizational Compiler's *diagnostic* pass is therefore
  **not** prior-arted by KB-ORG.
- **Missing evidence:** none material. The Springer version is paywalled, but the authors' own
  tech report of the same work is fully accessible and was read.
- **Affect architecture now?** **Yes.** The application-level vs coordination-level design-knowledge
  split is a real, tested structuring idea our 10-pass pipeline lacks, and R01 is right to say we
  should adopt it. Separately, the novelty claim "we built a compiler that turns intent into an
  organization" cannot be made.

---

### Claim 2 — ODML is Org-IR, an organization modelling/design language functioning as an intermediate representation

> R01: "ODML (Horling & Lesser) is the organizational modelling language it searches over — which
> is Org-IR."

- **Verdict: PARTIALLY SUPPORTED.** ODML exists and is exactly the author, kind and role R01 says —
  *except* for the "intermediate representation" framing, which does not fit.
- **Evidence tier: OBSERVED.** Read from Horling's dissertation full text.
- **Strongest source:** Bryan Horling, *Quantitative Organizational Modeling and Design for
  Multi-Agent Systems*, PhD dissertation, University of Massachusetts Amherst, February 2006 (chair:
  Victor Lesser) — http://mas.cs.umass.edu/Documents/bhorling/bhorling-dissertation.pdf. Journal
  version: Horling & Lesser, *Using quantitative models to search for appropriate organizational
  designs*, **JAAMAS 16(2):95–149, 2008**, DOI
  [10.1007/s10458-007-9020-y](https://doi.org/10.1007/s10458-007-9020-y).

Verbatim:

> "I introduce a new representation, the Organizational Design Modeling Language (ODML), designed
> to capture organizational information in a single unified, predictive structure."

> "The Organizational Design Modeling Language (ODML) provides domain-independent mechanisms to
> model, evaluate, and compare a variety of organizational styles … ODML incorporates quantitative
> information in the form of mathematical expressions. These expressions are grouped into
> organizational constructs, connected in a graph of relationships, and ultimately used to represent
> and predict both the localized and global characteristics of an organization."

So: real; Horling & Lesser; a modelling language; and explicitly searched over — the design-search
problem is named **ODML-SAT** and proved NEXP-complete (§4.1.1). R01's "the modelling language whose
search space it prunes" is fair.

- **Counterevidence — this is the substantive finding.** ODML is **not an intermediate
  representation**. An IR, in the sense our "Org-IR" name borrows from LLVM, is a lowered form on the
  path to an executable target. ODML is never lowered into a running organization; it is a
  *predictive equation graph* whose outputs are performance estimates used to rank candidate designs
  (the dissertation's own contrast: "one can embed arbitrary mathematical expressions within the
  model, and use those to produce fast, precise predictions"). Its compilation target is
  **Mathematica**, for optimisation — Appendix A is literally "Translating ODML to Mathematica".
  R01's Deliverable 4 row for Org-IR is therefore justified by the wrong artefact.
  **Moise+ is the correct citation for the executable-specification half** — it is a declarative
  organizational specification that a runtime consumes and enforces (Claim 7). R01 does name Moise+
  and OperA in the same block, so the verdict is recoverable; the *headline sentence in the executive
  conclusion* is not.
- **Missing evidence:** the Horling & Lesser JAAMAS abstract is elided by both Crossref and Semantic
  Scholar and the Springer page is paywalled. Mitigated by the dissertation, which is the same work
  at greater length.
- **Affect architecture now?** **Yes, but differently than R01 says.** If Org-IR is genuinely meant
  to be an IR — lowered, then executed — then ODML is *not* our prior art and the more useful lesson
  is the opposite one: nobody in this lineage built the lowering step, which is a gap rather than a
  collision. Adopt Moise+'s structural/functional/deontic split; do not model Org-IR on ODML.

---

### Claim 3 — Organization Self-Design (Ishida, Gasser & Yokoo, IEEE TKDE 1992) is runtime reorganization

> R01: "Organization Self-Design (Ishida, Gasser & Yokoo, IEEE TKDE 1992) supplies runtime
> composition/decomposition of the agent population — which is Morphogenetic Teams."

- **Verdict: SUPPORTED**
- **Evidence tier: DERIVED.** Bibliographic record verified against Crossref; mechanism verified
  from multiple independent secondary syntheses. **I did not read the paper** — IEEE Xplore is
  paywalled and no author-hosted copy surfaced. Stated plainly per the brief.
- **Strongest source:** Crossref record for DOI
  [10.1109/69.134249](https://doi.org/10.1109/69.134249) — *Organization self-design of distributed
  production systems*, **T. Ishida, L. Gasser, M. Yokoo**, *IEEE Transactions on Knowledge and Data
  Engineering* **4(2):123–134, 1992**. All three authors, venue, volume, issue and year exactly as
  R01 states. 170 citations (Semantic Scholar).

Mechanism, per consistent secondary description: two reorganization primitives, **composition and
decomposition**, which change the *population of agents* and the *distribution of knowledge*; built
on formalised "organizational knowledge"; applied by extending parallel production systems into
distributed production systems with adaptive work allocation.

- **Counterevidence:** one bibliographic wobble worth recording — Semantic Scholar's record for this
  DOI lists only Ishida and Yokoo, dropping Gasser. Crossref (authoritative for the DOI) lists all
  three. R01's three-author attribution is correct. Separately, R01's page range in prose is not
  given, but a secondary source reported 123–184; the Crossref record says **123–134**. Use 123–134.
- **Missing evidence:** the paper itself. The claim "composition/decomposition at runtime" rests on
  secondary description. It is consistently and specifically described across independent sources
  and is consistent with the title, but it is **DERIVED, not OBSERVED**, and should not be quoted as
  if read.
- **Affect architecture now?** **No — not yet.** R01's own recommendation is not to build
  Morphogenetic Teams before there is one certified team. Nothing here changes that ordering.

---

### Claim 4 — Co-Fields / TOTA are stigmergic fields, shipped as middleware (ACM TOSEM 2009)

> R01: "Field-based coordination (Mamei & Zambonelli's Co-Fields, and the TOTA middleware, ACM
> TOSEM 2009) is literally 'computational fields' over a distributed substrate — which is Stigmergic
> Fields, and it shipped as middleware."

- **Verdict: SUPPORTED**, with two corrections of detail (one of which affects a rhetorical claim)
- **Evidence tier: OBSERVED** for the TOTA abstract; **DERIVED** for the Co-Fields papers.
- **Strongest source:** Mamei & Zambonelli, *Programming pervasive and mobile computing
  applications: the TOTA approach*, **ACM Transactions on Software Engineering and Methodology
  18(4), 2009**, DOI [10.1145/1538942.1538945](https://doi.org/10.1145/1538942.1538945)
  (Crossref-verified: title, both authors, journal, volume, issue, year — all exactly as R01
  states). 240 citations.

Verbatim from the abstract:

> "we present TOTA ('Tuples On The Air'), a novel middleware and programming approach for supporting
> adaptive context-aware activities in pervasive and mobile computing scenarios. The key idea in TOTA
> is to rely on spatially distributed tuples, adaptively propagated across a network on the basis of
> application-specific rules"

> "This article includes both application examples to clarify concepts and performance figures to
> show the feasibility of the approach"

That is field-based coordination as a middleware with an implementation and measured results.

- **Counterevidence — two corrections:**
  1. **Co-Fields has a third author.** The canonical papers are **Mamei, Zambonelli & Leonardi** —
     *Cofields: a physically inspired approach to motion coordination*, IEEE Pervasive Computing
     3(2):52–61, 2004, DOI [10.1109/MPRV.2004.1316820](https://doi.org/10.1109/MPRV.2004.1316820);
     and *Co-Fields: Towards a Unifying Approach to the Engineering of Swarm Intelligent Systems*,
     LNCS/ESAW III, 2003, DOI [10.1007/3-540-39173-8_6](https://doi.org/10.1007/3-540-39173-8_6).
     R01 attributes Co-Fields to two authors and cites a Taylor & Francis *Applied Artificial
     Intelligence* URL that is not the primary Co-Fields venue.
  2. **"Shipped as middleware" overstates it.** TOTA is a research middleware with a prototype
     implementation and performance figures in a top journal — which is strong evidence and quite
     enough to defeat a novelty claim. It is not a product that shipped. R01 uses "shipped" twice
     (executive conclusion, Deliverable 6 row 3) in a way that implies industrial deployment. This
     matters because R01's *own* Finding 1 argues this literature "did not reach industry" — the two
     statements are in tension inside the same document.
- **Missing evidence:** the TOTA full text (paywalled; abstract read via Semantic Scholar). The
  Parunak & Brueckner digital-pheromone line, which R01 cites as the *other* direct hit and which
  genuinely did reach defence/manufacturing deployment, was **not audited here** — outside the
  brief's scope.
- **Affect architecture now?** **No.** R01's own assessment is that nothing material transfers and
  that we should not build Stigmergic Fields yet. The corrections are to the write-up, not the plan.

---

### Claim 5 — PROSA (1998) already has staff holons

> R01: "PROSA (Van Brussel et al., 1998), the holonic manufacturing reference architecture, already
> contains 'staff holons' that 'assist the basic holons with expert knowledge' — which is the Staff
> Mesh, under the same word."

- **Verdict: SUPPORTED** — and the primary source is *stronger* than R01's summary of it
- **Evidence tier: OBSERVED.** Full paper text extracted and read.
- **Strongest source:** Van Brussel, Wyns, Valckenaers, Bongaerts & Peeters, *Reference architecture
  for holonic manufacturing systems: PROSA*, **Computers in Industry 37 (1998) 255–274**, KU Leuven
  author-hosted copy — https://www.mech.kuleuven.be/en/pma/research/MACC/prosapaper (ScienceDirect
  DOI page returns 403; the author-hosted PDF is the same paper, header verified).

Verbatim from the abstract — R01's quoted fragment is exact:

> "This architecture, called PROSA, consists of three types of basic holons: order holons, product
> holons, and resource holons. … **Staff holons can be added to assist the basic holons with expert
> knowledge.**"

And the acronym itself settles it (§3.4 heading "Staff holons", and §"The name PROSA stands for
Product-Resource-Order-Staff Architecture, which refers to the composing types of holons"). Four
further passages confirm the role, including the etymology:

> "The name 'staff holon' is inspired by the difference between line functions and staff functions in
> human organisations. Also in a human organisation one of the main goals for the introduction of
> staff functions is to reduce the work load and work complexity of line functions by providing them
> with expert knowledge."

> "The basic holon is still responsible for taking the decision, and the staff holon is considered as
> an external expert that gives advice."

- **Counterevidence: none.** This is the cleanest claim in R01. Two observations that strengthen
  rather than weaken it:
  1. PROSA's staff holons are **explicitly centralised** — "The concept of staff holons allows for
     the presence of centralised elements and functionality in the architecture." R01's Deliverable 3
     argues our name "Staff **Mesh**" asserts decentralisation while the design is centralised.
     PROSA independently confirms that reading from 1998. The naming criticism is better-founded
     than R01 knew.
  2. PROSA staff holons are **advisory-only, and that is load-bearing**, not incidental: "Since staff
     holons are only giving advice to the basic holons, they do not introduce hierarchical rigidity
     into the system." R01 states this correctly and draws the right lesson for our open question on
     staff authority.
- **Missing evidence:** none for this claim.
- **Affect architecture now?** **Yes.** Two directly actionable items, both already identified by
  R01 and both confirmed at source: rename away from "mesh", and settle staff authority as advisory
  by default. Add a third the primary text supplies and R01 under-uses: PROSA's *structure/algorithm
  decoupling* is stated in its own abstract as one of its "significant innovations" — "the system
  structure is decoupled from the control algorithm".

---

### Claim 6 — Organizational mining (van der Aalst, ~2005) is the Organizational Debugger

> R01, Deliverable 6 row 7: "van der Aalst, Reijers & Song (2005), 'Discovering social networks from
> event logs', CSCW … Founds **organizational mining**: structure discovery, SNA, role mining and
> resource allocation from event logs."

- **Verdict: PARTIALLY SUPPORTED** on the citation; **SUPPORTED** on the underlying concept
- **Evidence tier: DERIVED.** Bibliographic records and abstracts verified; neither full text read.
- **Strongest source for what R01 actually describes:** **Song & van der Aalst, *Towards
  comprehensive support for organizational mining*, Decision Support Systems 46:300–317, 2008** —
  https://www.sciencedirect.com/science/article/abs/pii/S0167923608001280. This is the paper that
  names and delivers the subfield, and its abstract states the gap directly: "Lion's share of the
  efforts in this domain has been devoted to control-flow discovery … other aspects have been
  neglected, e.g., the organizational setting and interactions among coworkers."
- **The cited 2005 paper is real and correctly cited, but narrower than described:** van der Aalst,
  Reijers & Song, *Discovering Social Networks from Event Logs*, **Computer Supported Cooperative
  Work (CSCW) 14:549–593, 2005**, DOI
  [10.1007/s10606-005-9005-9](https://doi.org/10.1007/s10606-005-9005-9). Authors, venue, year
  correct. Its scope is social-network mining — handover-of-work metrics, a tool, and one real
  Dutch-organisation event log. **Role mining and resource allocation are not in it**; they arrive
  in the 2008 DSS paper.

- **Counterevidence:** R01 compresses three years and two papers into one citation, and attributes
  to 2005 capabilities published in 2008. The direction of the error is *understating* the prior
  art's age spread, not overstating its existence — the field is real either way.
- **Missing evidence:** neither full text was read. Also unaudited: R01's second pillar for this
  verdict, Poutakidis, Padgham & Winikoff. That citation **does** check out bibliographically —
  *Debugging multi-agent systems using design artifacts: the case of interaction protocols*, AAMAS
  '02, ACM Press, DOI [10.1145/544862.544966](https://doi.org/10.1145/544862.544966), all three
  authors and year exactly as R01 states — but I did not read it, so R01's description of the
  mechanism (AUML → Petri nets → live conformance monitoring) is **DERIVED** and unverified here.
- **Is the mapping fair?** **Mostly, with one asymmetry R01 already states and is right about.**
  Organizational mining is *post-hoc analysis of completed event logs*; the Organizational Debugger
  as posed halts a live organization on an evidence-sufficiency predicate. Those are different
  operations on the same data. R01 concedes exactly this ("Process mining is post-hoc; tracing is
  passive; neither halts the organization on an epistemic condition") and still rates the concept
  CRITICAL. That is defensible for the *retrospective* half and over-strict for the *interventional*
  half.
- **Affect architecture now?** **Yes.** Conformance checking is a real 20-year algorithm base and we
  should use it rather than reinvent it; PROV-O and OTel GenAI spans likewise. The correction here
  is to the citation, not to the recommendation.

---

### Claim 7 — Moise+ / ORA4MAS / JaCaMo / the MIT Press textbook

R00 leans on this lineage to argue AOE is a rename of organisation-oriented MAS. Three sub-claims.

**7a — Moise+ (authors, year, what it models) — Verdict: SUPPORTED. Tier: OBSERVED.**

Hübner, Sichman & Boissier, *A Model for the Structural, Functional, and Deontic Specification of
Organizations in Multiagent Systems*, LNCS 2507 (SBIA 2002), pp. 118–128, DOI
[10.1007/3-540-36127-8_12](https://doi.org/10.1007/3-540-36127-8_12). Also as an AAMAS '02 extended
abstract, DOI [10.1145/544741.544858](https://doi.org/10.1145/544741.544858). Title page and abstract
read directly from the Moise project's own hosted PDF. Verbatim:

> "The MOISE+ model — described here through a soccer team example — intends to be a step in this
> direction since the organization is seen under three points of view: structural, functional, and
> deontic."

The structural/functional/deontic split R01 recommends we adopt is exactly what the source defines.

**7b — JaCaMo is a real runtime that *enforces* an organizational specification — Verdict:
SUPPORTED. Tier: DERIVED.**

JaCaMo integrates Jason (agents) + CArtAgO (environment) + Moise (organisation); the Moise platform
"allows the creation of an organisational specification and the management of organisational
entities", and the specification "is to be used both by the agents to reason about their organisation
and by an organisation platform that **enforces** that the agents follow the specification"
(moise.sourceforge.net; JaCaMo project material). Downloadable, versioned software exists. I did not
run it or read its source, so *that it enforces* is DERIVED from project documentation, not OBSERVED.

**7c — ORA4MAS reifies the organization as first-class runtime artifacts — Verdict: NOT-ACCESSIBLE
for R01's verbatim quote; the citation itself is SUPPORTED.**

Crossref confirms the chapter exists exactly where R01 points: Kitio, Boissier, Hübner & Ricci,
*Organisational Artifacts and Agents for Open Multi-Agent Organisations: "Giving the Power Back to
the Agents"*, in *Coordination, Organizations, Institutions, and Norms in Agent Systems III*, LNCS,
Springer, **2008**, pp. 171–186, DOI
[10.1007/978-3-540-79003-7_13](https://doi.org/10.1007/978-3-540-79003-7_13). R01 gives no authors
for it; they are as listed. **However**, R01 quotes this work directly — "the organisation and the
organisation infrastructure itself … in terms of agents and artifacts, as first-class basic
abstractions" — and I **could not verify that quotation**: the Springer chapter is paywalled and the
abstract is elided from both the Crossref and Semantic Scholar records. Mark it **NOT-ACCESSIBLE**.
Note also that the chapter's own subtitle, "Giving the Power Back to the Agents", points *away* from
regimented enforcement and toward agent autonomy — which is at least worth reading before quoting the
work in support of a runtime-enforcement claim.

**7d — An MIT Press textbook on multi-agent oriented programming exists — Verdict: SUPPORTED. Tier:
DERIVED (publisher and retailer metadata; book not read).**

Boissier, Bordini, Hübner & Ricci, ***Multi-Agent Oriented Programming: Programming Multi-Agent
Systems Using JaCaMo***, **The MIT Press, 15 September 2020**, Intelligent Robotics and Autonomous
Agents series, ISBN 9780262044578, 264 pp. — https://mitpress.mit.edu/9780262044578/multi-agent-oriented-programming/.
Its three-dimension framing (agent / environment / organisation) is the framing R00 says AOE renames.

- **Affect architecture now?** **Yes, and this is the strongest single lever in the audit.** A 2020
  MIT Press textbook plus a maintained platform is a materially harder fact to argue past than a
  1998 or 2008 paper: this lineage is not merely published, it is *taught*. Any external-facing
  claim that AOE is a new field must engage with it by name.

---

## Independence

The audit brief asked whether R01's citations trace back to one group or one survey. **They partly
do, and R01 nowhere discloses it.**

| Lineage | Citations R01 uses | Independent? |
|---|---|---|
| **UMass MAS Lab (Victor Lesser)** | KB-ORG (Sims, Corkill & **Lesser**); ODML (Horling & **Lesser**); TÆMS/GPGP (Decker & **Lesser**) | **No — one lab, one adviser** |
| **Moise circle (Boissier / Hübner / Ricci / Bordini)** | Moise+; ORA4MAS; JaCaMo; MIT Press textbook; *and* the 2023 JAAMAS "Generating and choosing organisations for MAS" (Amaral, **Hübner** & Cranefield) | **No — one circle** |
| Ishida, Gasser & Yokoo (OSD, 1992) | Organization Self-Design | Yes |
| Mamei, Zambonelli & Leonardi (Modena) | Co-Fields, TOTA | Yes |
| KU Leuven PMA (Van Brussel et al.) | PROSA | Yes |
| TU/e (van der Aalst) | organizational mining | Yes |

**The sharpest instance: KB-ORG and ODML are not two independent results.** They are
**JAAMAS 16(2):95–149 and 16(2):151–185** — *consecutive articles in the same 2008 issue*, from the
same laboratory, with **Victor Lesser as a co-author of both**; and Horling's ODML dissertation was
chaired by Lesser. R01's two most damaging CRITICAL verdicts (Organizational Compiler, Org-IR) are
carried by **one research programme publishing a paired special-issue contribution**, presented as
independent corroboration.

Further, R01 offers "Generating and choosing organisations for multi-agent systems" (JAAMAS 37(2),
2023, DOI [10.1007/s10458-023-09623-8](https://doi.org/10.1007/s10458-023-09623-8)) as an
*independent modern* precedent for the Organizational Compiler. Crossref: Amaral, **Hübner** &
Cranefield. That is the Moise circle again.

**What this does and does not do.** It does not rescue novelty — a single lab that implemented
automated organization design still implemented it, and KB-ORG's existence is not made less true by
its neighbour sharing an author. What it does is **falsify the framing that seven independent
research lines converged on our fifteen concepts.** Four did. Two clusters account for the rest. R01
should say so, because the difference between "seven independent results" and "four lineages plus two
lab programmes" is the difference between a settled field and two well-funded groups.

---

## Recency and generalization — does the mechanism transfer to LLM agents?

Every artefact audited here is from **1992–2012**, pre-LLM, and every one was built for
agents that were *hand-constructed, narrow, and expensive per instance*. Per the skill's
generalization dimension, taken one at a time:

| Prior art | Mechanism transfers to LLM agents? | Assessment |
|---|---|---|
| **KB-ORG** | **Partly.** The search-with-design-knowledge mechanism transfers cleanly. The *inputs* do not: KB-ORG requires hand-authored Java role classes, declared agent capability descriptions and TÆMS-style task structures. Our input is natural-language intent over general workers. | **Matched on mechanism.** The verdict is earned. But the input transformation is a real difference and R01 says so. |
| **ODML** | **Weakly.** ODML's value is *precise quantitative prediction* from equations calibrated to a known domain (sensor networks, IR). LLM agent performance is not predictable from such a model — that is the entire content of the Kim et al. finding (cross-validated R²=0.373). An ODML for LLM organizations would be predicting a quantity nobody can currently predict. | **Matched partly on vocabulary.** Both are "organizational modelling languages"; only one claims to compute outcomes, and its central capability is the one that does not transfer. |
| **OSD (1992)** | **Partly.** Composition/decomposition of a population is substrate-neutral. But OSD's primitives redistribute *production-rule knowledge* between agents — an operation with no analogue when every agent shares one general model. | **Mechanism transfers; the thing being redistributed does not.** |
| **Co-Fields / TOTA** | **Yes, mechanically — and that is the problem for us, not for them.** Fields over a distributed substrate are domain-agnostic. Nothing about LLM agents makes them new. | **Matched on mechanism. Verdict fully earned.** |
| **PROSA staff holons** | **Yes.** "A centralised advisory expert that basic units may consult and may ignore" is an organizational pattern with no substrate dependency at all. | **Matched on mechanism *and* word. The strongest verdict in R01.** |
| **Organizational mining** | **Yes for the retrospective half; no for the interventional half.** Conformance checking over event logs transfers directly. Halting a live organization on an epistemic predicate has no counterpart in it. | **Matched on mechanism for what process mining does; R01's own "what does not" paragraph correctly carves out the rest.** |
| **Moise+ / JaCaMo** | **Partly.** The structural/functional/deontic decomposition transfers as a *design vocabulary*. Enforcement does not transfer as-is: JaCaMo enforces over agents whose action repertoire is finite and declared. An LLM agent's action space is open, so "the platform enforces the specification" means something weaker for us. | **Matched on specification; over-matched on enforcement.** |

**Where a CRITICAL verdict is most likely wrong: Org-IR.** It is the one case in this set where the
match is substantially on the *word* ("organizational modelling language") while the mechanism that
made the prior art work — calibrated quantitative prediction of organizational performance — is
precisely the mechanism that does not carry to LLM agents.

---

## Disposition of R01's seven CRITICAL verdicts

| # | Concept | R01 | After audit | Why |
|---|---|---|---|---|
| 1 | Organizational Compiler | CRITICAL | **CRITICAL — survives** | KB-ORG read in full. "Fully automated", implemented, generative, verbatim. Unarguable. Trim only "including the diagnostics". |
| 2 | Org-IR | CRITICAL | **CRITICAL — survives, but re-sourced** | Survives on Moise+/OperA/AGR, which are genuine organizational specification languages consumed by a runtime. **Does not survive on ODML**, which is a predictive design model, not an IR. On ODML alone this would be HIGH. |
| 3 | Organizational OS | CRITICAL | **HIGH — downgrade** | The strongest supporting quote (ORA4MAS) is **NOT-ACCESSIBLE** and unverified; the chapter's own subtitle points away from the enforcement reading. JaCaMo and the MIT Press textbook are solid but are a *platform and a curriculum*, not the durable replayable event log R01 itself identifies as the gap. Restore to CRITICAL only if someone reads the ORA4MAS chapter. |
| 4 | Stigmergic Fields | CRITICAL | **CRITICAL — survives** | TOTA verified at TOSEM 18(4) 2009 with implementation and performance figures. Correct authorship to include Leonardi and drop "shipped". |
| 5 | Morphogenetic Teams | CRITICAL | **CRITICAL on the term; HIGH on the mechanism** | *Morphogenetic Engineering* verified as a real Springer volume (Doursat, Sayama & Michel as **editors**, not authors; Understanding Complex Systems series, 2012) — the term is owned. The mechanism rests on OSD, which is **DERIVED, not read**. Note: this restores R01's own per-concept split, which its Deliverable 4 map flattened to CRITICAL. |
| 6 | Organizational Debugger | CRITICAL | **CRITICAL — survives, citation corrected** | Re-source to Song & van der Aalst, DSS 46:300–317, 2008 for the subfield. Poutakidis et al. 2002 verified bibliographically. The evidence-conditioned breakpoint remains uncontested. |
| 7 | Staff Mesh | CRITICAL | **CRITICAL — survives, and strengthen it** | PROSA read in full. Same word, same advisory role, same human-organisation etymology, and the acronym itself is Product-Resource-Order-**Staff**. R01 understates its own case. |

**Five survive at CRITICAL. One (Organizational OS) drops to HIGH pending an accessible source. One
(Morphogenetic Teams) splits — CRITICAL on the name, HIGH on the mechanism. None is unverifiable in
the sense of the artefact not existing: every work R01 names is real, correctly attributed by author,
venue and year, with one page range and one missing co-author to fix.**

---

## Claims that must be downgraded in the synthesis

1. **"R01 reported this landed in Nature MI 2026 and that does not survive checking."**
   → **This is the audit brief's claim, and it must be withdrawn.** DOI 10.1038/s42256-026-01268-y
   resolves; Crossref returns *Capable language models can outgrow the benefits of collaboration*,
   Nature Machine Intelligence 8(7):1157–1172, 2026-07-24, same 20 authors. R01 was right.
   **Add instead:** R01 must record that the journal version was **retitled**, and must not cite the
   Nature version under the preprint's title. The retitle carries a directional claim the preprint
   title does not, and any use of this study should quote whichever version it actually read.
2. **"ODML … which is Org-IR."** (Executive conclusion; Deliverable 4 row 2)
   → Downgrade. ODML is a predictive quantitative organizational design model whose optimisation
   target is Mathematica, not an intermediate representation lowered into a running organization.
   Re-source the Org-IR verdict to Moise+/OperA/AGR.
3. **"KB-ORG … which is the Organizational Compiler, including the diagnostics."**
   → Strike "including the diagnostics". KB-ORG evaluates and ranks; its feedback loop is future
   work in the authors' own text.
4. **"it shipped as middleware"** (Stigmergic Fields, twice)
   → Downgrade to "was implemented and published as a research middleware with measured
   performance". As written it contradicts R01's own Finding 1 that this literature did not reach
   industry.
5. **"van der Aalst, Reijers & Song (2005) … Founds organizational mining: structure discovery, SNA,
   role mining and resource allocation."**
   → Split the citation. 2005/CSCW = social network discovery. 2008/DSS = the organizational-mining
   subfield including role mining and resource allocation.
6. **"Mamei & Zambonelli's Co-Fields."**
   → Add Leonardi; cite IEEE Pervasive Computing 3(2):52–61 (2004) rather than the Applied
   Artificial Intelligence URL currently listed.
7. **Ishida, Gasser & Yokoo page range.** → 123–134 (Crossref), not 123–184.
8. **"Seven concepts have implemented, published prior art"** — framing, not a citation.
   → Must be qualified with the independence disclosure. The seven verdicts rest on **four
   independent lineages plus two single-lab programmes**; KB-ORG and ODML are consecutive articles in
   one journal issue sharing an author.
9. **The ORA4MAS quotation** → mark **NOT-ACCESSIBLE** until someone reads the chapter. It is
   currently presented as a direct quote supporting the sharpest hit against Organizational OS.
10. **Internal inconsistency, not a source problem:** R01's per-concept blocks and its Deliverable 4
    map disagree in at least two places (Morphogenetic Teams: "CRITICAL on the term; HIGH on the
    mechanism" vs a flat CRITICAL; Evolution Chamber: "MEDIUM on the composition; CRITICAL on the
    NAME" vs a flat MEDIUM). The map is what a reader will quote. Reconcile them.

---

## What this audit did *not* check

Stated so the next reader does not mistake silence for confirmation:

- Parunak & Brueckner's digital pheromone work (R01's *other* Stigmergic Fields hit) — outside brief.
- Poutakidis et al. 2002 beyond its bibliographic record — the AUML→Petri-net mechanism is unverified.
- The eight HIGH and three MEDIUM/LOW verdicts, and every LLM-era citation (ADAS, AFlow, MAST, DGM,
  A2A, MemGPT) — outside brief.
- R01's −3.5% / [−18.6%, +25.7%] summary of Kim et al. — the study's existence and venue are now
  confirmed, but its *numbers as R01 reports them* were not re-derived here.
- arXiv:2606.31498 ("Governance Gaps in Agent Interoperability Protocols") — not checked; the
  identifier's format warrants a look before it is cited.
- Whether `UNMEASURABLE` as a first-class verdict has prior art in metrology or software testing.
  R01 flags this as the one search that could kill its narrowest defensible claim, and it remains
  undone. **It is the highest-value unexecuted search in the programme** — the claim R01 recommends
  building the entire novelty position on rests on a gap nobody has yet looked into.
