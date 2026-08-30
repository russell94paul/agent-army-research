# Claude UI Build Prompt — Agent Army MVP

You are building the first UI slice of Agent Army.

## Goal

Create a usable operational interface, not a decorative game.

## MVP surfaces

Build:

1. Command World shell,
2. operations sidebar,
3. world canvas/graph placeholder,
4. lens selector,
5. agent inspector,
6. team inspector,
7. artifact inspector,
8. timeline/event feed,
9. alert list,
10. basic metrics header.

## MVP data

Use mocked or existing backend data if needed, but structure it around future entities:

```ts
Organization
Mission
Agent
Team
Artifact
Event
Evidence
Claim
FieldSignal
Capability
```

## UI rules

- Technical labels remain visible.
- Agent movement must correspond to real state.
- Lenses can start as simple visual filters.
- Inspectors must answer why/what/waiting/evidence.
- Timeline events must be structured.
- Avoid random animations.

## Build style

- React/TypeScript.
- Componentized.
- Accessible.
- Reduced-motion support.
- Clear empty states.
- Dark premium command aesthetic.

## Components

Suggested:

```text
CommandWorldShell
OperationsRail
WorldViewport
LensSelector
MetricsHeader
AgentUnit
SquadNode
ArtifactNode
RouteLayer
AlertLayer
TimelinePanel
AgentInspector
TeamInspector
ArtifactInspector
KnowledgeInspector
```

## Acceptance criteria

A user can:

- see active missions,
- see agents/teams/artifacts in one operational view,
- select an agent and understand what it is doing,
- select an artifact and see risk/evidence/activity,
- view recent events,
- switch lenses,
- jump from alert to relevant entity.
