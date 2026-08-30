#!/usr/bin/env python3
"""Validate the Agent Army research repository without third-party packages."""

from pathlib import Path
import re
import sys
import json

ROOT = Path(__file__).resolve().parents[1]

errors = []
warnings = []

# Required structure
required = [
    "HOME.md", "START_HERE.md", "CLAUDE.md",
    "foundations", "research/prompts", "research/answers",
    "research/synthesis", "ontology", "architecture", "design",
    "experiments", "governance", "implementation-handoffs",
    "repo-boundary", "maps", "templates"
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required path: {rel}")

# Markdown integrity
md_files = list(ROOT.rglob("*.md"))
for p in md_files:
    text = p.read_text(encoding="utf-8")
    if not text.strip():
        errors.append(f"Empty markdown: {p.relative_to(ROOT)}")

# Research prompt substance
prompts = list((ROOT/"research/prompts").glob("R*.md")) + list((ROOT/"foundations").glob("R*.md"))
for p in prompts:
    text = p.read_text(encoding="utf-8")
    if len(text) < 1000:
        warnings.append(f"Short research prompt (<1000 chars): {p.relative_to(ROOT)}")
    if "## Objective" not in text and "# R0" not in text:
        warnings.append(f"No explicit Objective section: {p.relative_to(ROOT)}")

# Disallow dependency on old packs
for p in md_files:
    text = p.read_text(encoding="utf-8").lower()
    suspicious = [
        "use the expanded prompt from the v2 pack",
        "see previous pack",
    ]
    for phrase in suspicious:
        if phrase in text:
            errors.append(f"External-pack dependency in {p.relative_to(ROOT)}: {phrase}")

# Obsidian wikilink validation (best effort).
# Resolve relative links from note directory and vault-root links.
link_re = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
for p in md_files:
    text = p.read_text(encoding="utf-8")
    for raw in link_re.findall(text):
        target = raw.strip()
        candidates = []
        # relative to source
        candidates.append((p.parent / target))
        candidates.append((p.parent / f"{target}.md"))
        # vault root
        candidates.append(ROOT / target)
        candidates.append(ROOT / f"{target}.md")
        if not any(c.exists() for c in candidates):
            warnings.append(f"Unresolved wikilink in {p.relative_to(ROOT)}: [[{target}]]")

summary = {
    "markdown_files": len(md_files),
    "research_prompts": len(prompts),
    "errors": len(errors),
    "warnings": len(warnings),
}

print(json.dumps(summary, indent=2))
if errors:
    print("\nERRORS")
    for e in errors:
        print("-", e)
if warnings:
    print("\nWARNINGS")
    for w in warnings[:100]:
        print("-", w)
    if len(warnings) > 100:
        print(f"... {len(warnings)-100} additional warnings")

sys.exit(1 if errors else 0)
