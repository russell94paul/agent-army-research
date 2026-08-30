# Command World Layout

## Default structure

```text
┌─────────────────────────────────────────────────────────────┐
│ AGENT ARMY     Operation: Connector Migration       92%     │
├──────────────┬──────────────────────────────────┬───────────┤
│ Operations   │                                  │ Intel     │
│              │          Command World           │           │
│ Alpha        │                                  │ Risk      │
│ Bravo        │     squads / agents / routes     │ Cost      │
│ Charlie      │                                  │ Intent    │
│              │                                  │ Readiness │
├──────────────┴──────────────────────────────────┴───────────┤
│ Timeline / Events / Alerts / Evidence / Replay              │
└─────────────────────────────────────────────────────────────┘
```

## World entities

```text
Region
District
Facility
Route
Artifact
Agent Unit
Squad
Field Overlay
Alert
Evidence Marker
Knowledge Node
```

## Semantic zoom

```text
Organization
  ↓
Domains / regions
  ↓
Missions / teams
  ↓
Agents / services
  ↓
Artifacts / functions / endpoints
```

## Movement rules

Agents move only when real state changes:

- scope change,
- tool use,
- handoff,
- repository transition,
- team join,
- verification phase,
- escalation.

No random wandering.

## Camera

Controls:

- pan,
- zoom,
- focus selected,
- jump to alert,
- follow agent,
- follow mission,
- replay scrub.

## Minimap

Optional, but useful for:

- agent clusters,
- alerts,
- risk zones,
- traffic,
- active missions.
