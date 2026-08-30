# Design Tokens — Draft

This file defines semantic token categories, not final brand colors.

## Color semantics

```text
surface.base
surface.elevated
surface.overlay

text.primary
text.secondary
text.muted

state.healthy
state.warning
state.critical
state.unknown
state.verified
state.human_required

field.risk
field.uncertainty
field.knowledge
field.contention
field.verification
field.readiness
field.intent
field.cost
```

## Spacing scale

Use an 8px-based scale unless the current app already has a strong system.

```text
2 / 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64
```

## Radius

Prefer restrained radii for command surfaces.

```text
sm  4
md  8
lg  12
```

## Elevation

Use elevation to distinguish:

- world,
- persistent chrome,
- temporary inspector,
- modal intervention.

Avoid excessive glass blur.

## Typography roles

```text
display
section
body
label
metric
code
caption
```

Metrics should use tabular numerals.
