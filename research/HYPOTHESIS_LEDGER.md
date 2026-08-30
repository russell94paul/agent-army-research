# Hypothesis Ledger

Use this file to track hypotheses across months.

Status vocabulary: `SUPPORTED` · `WEAKENED` · `FALSIFIED` · `UNCHANGED` · `NEEDS EXPERIMENT` · `open`

| ID | Hypothesis | Evidence | Status | Experiments | Last Updated |
|---|---|---|---|---|---|
| H01 | Intent contracts improve bounded autonomy | R02: not a contract at all — authority/budget are permissions, not falsifiable | NEEDS EXPERIMENT (reframed as `Mandate`) | R39 | 2026-08-30 |
| H02 | Artifact-mediated coordination reduces token overhead | unknown | UNCHANGED | R22/R27 | 2026-08-30 |
| H03 | Capability readiness predicts better routing than idle-agent selection | `Capability` has NO counterpart in code — a claim about an intention | UNCHANGED | R37 | 2026-08-30 |
| H04 | NOW/NEXT/LATER cells reduce critical-path idle time | `Cell` deleted from the ontology in W0 | WEAKENED — restate without `Cell` or drop | R36 | 2026-08-30 |
| H05 | Doctrine improves repeated mission performance | R00 falsified Law 6: *routine as truce* is a political settlement between people with interests; agents have none | WEAKENED | R33 | 2026-08-30 |
| H06 | Organizational world visualization reduces time-to-diagnosis | unknown | UNCHANGED | R25/R41 | 2026-08-30 |
| H07 | Evolution discovers better topologies than manual templates | IMACS (arXiv:2607.25446, verified): winning placement flips across model families, so manual hard-coding cannot be right | SUPPORTED — but every learned result is model-binding-specific and expires with the binding | R24/R30, E3 | 2026-08-30 |
| H08 | Adding a harness-error verdict (TTCN-3 `error`) changes at least one current gate outcome | ITU-T Z.140 §24.2.1 verified against primary text; `contract.py:57` collapses instrument-crash into UNMEASURABLE | NEEDS EXPERIMENT | E1 | 2026-08-30 |
| H09 | Organizational configuration must be re-validated per model binding | IMACS ablation, verified | SUPPORTED | E3 | 2026-08-30 |
| H10 | The nine instrument vocabularies are reconstructible from three orthogonal axes (standing, basis, window) | R02, derived from the vocabulary crawl | NEEDS EXPERIMENT | E2 | 2026-08-30 |

## Retired

| ID | Hypothesis | Why retired |
|---|---|---|
| — | Agent Army's organizational concepts are substantially novel | W0: 5 of 7 CRITICAL prior-art verdicts survive audit; the one surviving novelty claim was refuted on all four components. Reframed as a **synthesis** claim. See `research/synthesis/W0-foundations.md` |
| — | Artificial Organization Engineering is a coherent new discipline | W0/R00: it is organisation-oriented MAS. The name is also occupied twice in 2026 |
