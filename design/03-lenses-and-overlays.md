# Lenses and Overlays

The same world should support multiple lenses.

## Default Lens

Shows mission, teams, agents and artifacts.

## Risk Lens

Highlights high-risk artifacts, services and decisions.

## Knowledge Lens

Shows:

- known areas,
- unknown areas,
- contested claims,
- stale knowledge,
- knowledge propagation,
- expertise clusters.

## Intent Alignment Lens

Shows whether actions and teams are still aligned with mission intent.

## Readiness Lens

Shows capability readiness.

Example:

```text
Schema Migration Capability
  agents      ✓
  skill       ✓
  context     ✓
  sandbox     ✓
  validator   ✗
  readiness   83%
```

## Logistics Lens

Shows context, skills, tools, model capacity and verification capacity as supply lines.

## Contention Lens

Shows competing edits, duplicated research, overlapping ownership.

## Verification Lens

Shows what is verified, unverified, failing or blocked.

## Doctrine Lens

Shows which doctrine/policies are active and which decisions they influenced.

## Evolution Lens

Shows organization versions, variants, mutations and performance history.
