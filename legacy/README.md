# Legacy — the research packs that came before v5

This folder holds the Agent Army research material that existed in the **agent-factory**
repository before the v5 pack became the foundation of this repository. It is kept for
provenance and for the handful of ideas the newer pack dropped, not as current specification.

**Nothing here is canonical.** The canonical research specification is [[HOME]] →
`ontology/`, `architecture/`, `governance/`. Read the notes below before quoting anything in
this folder.

---

## What was there, and where it came from

| Pack | Original location in agent-factory | Files | Git provenance |
|---|---|---|---|
| **v2** | `docs/agent-army-research-pack/` | 39 markdown + 1 nested zip | **never committed** — untracked working-tree files |
| **v3** | `docs/agent-army-research-pack-v3/` | 17 markdown | **never committed** — untracked working-tree files |

⚠ **Neither pack was ever tracked by git.** `git log --all -- docs/agent-army-research-pack*`
returns nothing, so there is no commit hash to cite and no way to recover them from agent-factory
history. That is precisely why they are archived here byte-exact.

The directory named `agent-army-research-pack` on disk describes itself internally as
**"Agent Army Research Pack v2"**. This folder uses the pack's own self-description (v2), not the
directory name, so the numbering is continuous: v2 → v3 → v5.

### Recovery note (2026-08-30)

Both directories were deleted from `agent-factory` by a concurrent process while this migration
was in progress, before their contents had been copied out. They were recovered intact from the
Windows Recycle Bin and verified byte-for-byte against the listings taken during the pre-migration
inspection. The archives in `archives/` are those recovered originals.

---

## Layout

```text
legacy/
├── archives/
│   ├── agent-army-research-pack-v2.zip   byte-exact, all 39 files
│   ├── agent-army-research-pack-v3.zip   byte-exact, all 17 files
│   └── SHA256SUMS.txt
├── research-pack-v2/                     the files that DIVERGE from v5, readable
└── research-pack-v3/                     the files that DIVERGE from v5, readable
```

**The archives are complete; the unpacked folders are deliberately partial.**

- 33 of the v2 pack's 39 markdown files are **byte-identical** to their v5 counterparts. Copying
  them here would put two identical documents in one Obsidian vault, which makes search worse and
  teaches nobody anything. They are in the archive and nowhere else.
- The 6 v2 files that genuinely differ are unpacked, so a synthesis pass can read them.
- 14 of the v3 pack's 17 files are **stubs**. Each is one sentence telling the reader to use the
  expanded prompt from the *v2* pack instead — they carry no research content, and
  `scripts/validate_repo.py` rejects that exact sentence because it is a dependency on a pack
  this repository does not contain. They stay in the archive only, where the literal text is
  preserved byte-exact. The 3 substantive v3 files are unpacked.

To read anything that is only in an archive:

```bash
unzip -o legacy/archives/agent-army-research-pack-v3.zip -d /tmp/v3
```

---

## What is still unresolved

Six documents diverge between v2 and v5 in ways that are **not** a simple supersede — v2 carries
material v5 dropped. Every one of them is written up in
[[migration/content-collisions]] with a recommended synthesis action.

The largest of these is not a prompt at all: **v2's `README.md` argues for the opposite repository
topology from the one this repository implements.** See collision C1.
