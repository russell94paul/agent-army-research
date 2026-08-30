# Screen Spec — Command World

## Purpose

Primary spatial operating surface.

## Layout

```text
┌────────────────────────────────────────────────────────────┐
│ Mission / Organization / Autonomy / Global Metrics        │
├────────────┬─────────────────────────────────┬─────────────┤
│ Operations │                                 │ Inspector   │
│ Rail       │          World View             │ Dock        │
│            │                                 │             │
├────────────┴─────────────────────────────────┴─────────────┤
│ Timeline / Replay / Events / Breakpoints                  │
└────────────────────────────────────────────────────────────┘
```

## World must show

At appropriate LOD:

- missions,
- squads,
- agents,
- artifacts,
- services,
- dependencies,
- evidence,
- alerts,
- flows,
- fields.

## Stable geography

Existing entities should remain spatially stable across updates.

Avoid force-layout jitter.

## Interaction

- click inspect,
- double click focus,
- shift multi-select,
- lens toggle,
- replay scrub,
- alert jump,
- follow agent,
- follow mission.
