# Claude Code Bootstrap — Create Agent Army Research Repo and Split Agent Factory Safely

You are working in or near the existing `agent-factory` repository.

Your task is to establish a **two-repository operating model**:

```text
<workspace>/
├── agent-factory/
└── agent-army-research/
```

The supplied Agent Army v5 pack is the seed content for `agent-army-research`.

## Objective

1. Inspect the existing Agent Factory repository.
2. Create a sibling `agent-army-research` Git repository.
3. Populate it with the supplied v5 research pack.
4. Locate existing Agent Army/research material in Agent Factory.
5. Move only research/speculative material to the new repository.
6. Keep production/current-state documentation in Agent Factory.
7. Create a small production-facing bridge under `agent-factory/docs/agent-army/`.
8. Preserve history and avoid destructive edits.
9. Produce an audit report of every moved, retained, duplicated or deleted file.
10. Commit the changes separately in each repository.

Do **not** implement Agent Army runtime features in this task.

---

# Non-negotiable safety rules

Before changing files:

```bash
git status --short
git rev-parse --show-toplevel
git branch --show-current
git remote -v
```

Record the starting state.

If there are unrelated uncommitted changes:

- do not discard them,
- do not reset,
- do not checkout over them,
- work around them,
- identify any migration collision in the final report.

Never use:

```bash
git reset --hard
git clean -fd
rm -rf
```

against the existing repository.

Do not delete a file until its destination exists and the migration is verified.

Do not assume a document is speculative based only on its filename. Read it.

Do not claim a feature is implemented without code evidence.

---

# Phase 1 — Inspect Agent Factory

Find:

```text
docs/agent-army/
docs/research/
docs/specs/
CLAUDE.md
README files
architecture docs
research answers/prompts
```

Also search content for:

```text
Agent Army
Artificial Organization
stigmergy
morphogenetic
Evolution Chamber
Mission Command
Intent Contract
Running Estimate
Collective Cognition
Org-IR
doctrine
```

Create a migration inventory before modifying anything:

```text
PATH
TYPE
CURRENT/PRODUCTION?
RESEARCH/SPECULATIVE?
MOVE
KEEP
SPLIT
DUPLICATE TEMPORARILY
RATIONALE
```

Save the inventory as:

```text
agent-army-research/migration/agent-factory-inventory-before.md
```

---

# Phase 2 — Create the research repository

Use the sibling directory:

```text
../agent-army-research
```

unless it already exists.

If it already exists, inspect it; do not overwrite.

Initialize Git if required:

```bash
git init
git branch -M main
```

Copy the **contents** of the v5 pack into the repository root so that the repo contains:

```text
HOME.md
START_HERE.md
CLAUDE.md
foundations/
research/
ontology/
architecture/
design/
experiments/
governance/
implementation/
implementation-handoffs/
repo-boundary/
handoff/
claude-skills/
maps/
```

Do not create an unnecessary nested `agent-army-research-v5/agent-army-research-v5/` directory.

---

# Phase 3 — Migrate existing research

Use the rules in:

```text
repo-boundary/WHAT-MOVES-TO-RESEARCH.md
repo-boundary/WHAT-STAYS-IN-AGENT-FACTORY.md
```

When existing Agent Factory research is not present in v5:

- preserve it,
- move/copy it into a sensible `legacy/`, `research/answers/`, `research/prompts/` or `research/context/` location,
- add provenance indicating its original Agent Factory path.

When both repos contain related but non-identical files:

- do not silently overwrite either;
- retain both initially;
- create a merge note in `migration/content-collisions.md`.

If Git history can be preserved cleanly with `git mv` inside Agent Factory before transferring, do so; otherwise document original path and source commit.

---

# Phase 4 — Clean the product boundary

Agent Factory should end with:

```text
docs/agent-army/
├── README.md
├── RESEARCH_REPO.md
├── CURRENT_STATE.md
├── APPROVED_CONCEPTS.md
└── IMPLEMENTATION_HANDOFFS.md
```

Additional product-specific Agent Army documents may remain if they describe current implemented architecture.

`CURRENT_STATE.md` must be generated from repository evidence.

For each major concept classify:

```text
IMPLEMENTED
PARTIAL
PLANNED
NOT IMPLEMENTED
```

Include code/file references.

Do not mark a concept implemented because it appears in research.

---

# Phase 5 — Obsidian

Treat `agent-army-research` as an Obsidian vault.

Validate:

- `HOME.md` opens as the main map of content;
- internal wiki links resolve where intended;
- no absolute machine-specific paths are required;
- `.obsidian/workspace*.json` remains ignored;
- no personal vault state is committed.

Create missing folders:

```text
assets/
inbox/
research/answers/
research/synthesis/
research/sources/
implementation-handoffs/approved/
implementation-handoffs/proposed/
migration/
templates/
```

---

# Phase 6 — Repository connection

If GitHub CLI is installed and authenticated, check:

```bash
gh auth status
```

If there is no existing remote and authentication is valid, create a **private** repository:

```bash
gh repo create agent-army-research --private --source . --remote origin
```

Do not make it public.

If `gh` is unavailable or unauthenticated:

- keep the local repo complete;
- report the exact command I can run later;
- do not block the rest of the migration.

Do not alter the Agent Factory remote.

---

# Phase 7 — Validation

Research repo:

```bash
git status --short
find . -type f | sort
```

Check:

- all v5 content exists;
- no file depends on content from an earlier research pack;
- all research prompts contain substantive bodies;
- no zero-byte Markdown files;
- the Obsidian home links to core maps;
- no secrets or credentials were copied.

Agent Factory:

- application builds/tests as appropriate;
- no production imports depend on moved docs;
- links affected by moved docs are repaired or intentionally redirected;
- no production source file was deleted.

---

# Phase 8 — Commit strategy

Create **separate commits**.

Research repository:

```text
chore: bootstrap Agent Army research program
docs: migrate Agent Army research from Agent Factory
```

Agent Factory:

```text
docs: separate Agent Army research from product repository
```

If unrelated user changes prevent a clean commit, do not include them.

---

# Phase 9 — Final report

Return:

## Research repository

- path,
- branch,
- remote,
- file count,
- commit hashes.

## Agent Factory

- files moved,
- files retained,
- files split,
- bridge files created,
- tests run and results.

## Collisions

Every document requiring human synthesis.

## Potentially stale research

Identify old research whose assumptions conflict with current code.

## Next action

Recommend the first research wave, but do not run it in this task.

The intended first wave is:

```text
R00 Foundations
R01 Prior Art
R02 Ontology
```

---

# Governing principle

The separation must make this invariant obvious:

> `agent-army-research` is where the organization is imagined, researched, challenged and specified.

> `agent-factory` is where accepted concepts become real, tested software.
