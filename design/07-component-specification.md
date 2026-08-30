# UI Component Specification

## Shell

```text
AgentArmyShell
CommandHeader
OperationsRail
WorldViewport
InspectorDock
TimelineDock
AlertStack
CommandPalette
```

## World

```text
RegionLayer
FacilityNode
ArtifactNode
AgentUnit
SquadFormation
DependencyRoute
LogisticsRoute
FieldOverlay
EvidenceMarker
KnowledgeMarker
AlertBeacon
MiniMap
```

## Inspectors

```text
AgentInspector
TeamInspector
ArtifactInspector
KnowledgeInspector
CapabilityInspector
MissionInspector
DoctrineInspector
OrganizationVersionInspector
```

## Analysis

```text
LensSelector
CausalTrace
ProfilerFlameView
ReadinessMatrix
KnowledgeCoverage
IntentAlignmentPanel
TimelineReplay
OrganizationDiff
```

## Component contract rule

Every world component must accept:

- stable identity,
- semantic status,
- selected/focused state,
- LOD,
- accessibility label.

No component may derive business state solely from animation state.
