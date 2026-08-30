# Agent Army Target Architecture

## Target layers

```text
┌──────────────────────────────────────────────────────────────┐
│ Command World / Artificial Organization IDE                 │
├──────────────────────────────────────────────────────────────┤
│ UI Projections                                               │
│ - world map                                                  │
│ - inspectors                                                 │
│ - debugger                                                   │
│ - profiler                                                   │
│ - knowledge lens                                             │
│ - evolution chamber                                          │
├──────────────────────────────────────────────────────────────┤
│ Materialized Organizational World State                      │
├──────────────────────────────────────────────────────────────┤
│ Durable Event Log                                            │
├──────────────────────────────────────────────────────────────┤
│ Organizational Runtime / OS                                  │
│ - scheduler                                                  │
│ - team manager                                               │
│ - policy engine                                              │
│ - field engine                                               │
│ - cognitive logistics                                        │
│ - staff mesh                                                 │
├──────────────────────────────────────────────────────────────┤
│ Collective Cognition Fabric                                  │
│ - claims                                                     │
│ - evidence                                                   │
│ - knowledge                                                  │
│ - skills                                                     │
│ - capabilities                                               │
│ - doctrine                                                   │
├──────────────────────────────────────────────────────────────┤
│ Organizational Compiler                                      │
│ Mission Intent → Org-IR → Executable Organization            │
├──────────────────────────────────────────────────────────────┤
│ Execution Substrate                                          │
│ - LLMs                                                       │
│ - tools                                                      │
│ - sandboxes                                                  │
│ - repos                                                      │
│ - databases                                                  │
│ - APIs                                                       │
└──────────────────────────────────────────────────────────────┘
```

## Initial target modules

```text
/org
  Organization
  Mission
  Team
  Agent
  Artifact

/events
  Typed events
  Event log
  Projections

/world
  Materialized world state
  LOD projections
  UI transport

/evidence
  Evidence objects
  Claims
  Provenance

/knowledge
  Knowledge objects
  Skills
  Capabilities

/policy
  Intent contracts
  Constitution
  Permissions

/ui
  Command World
  Inspectors
  Timeline
  Lenses
```

## Do first

1. Canonical IDs.
2. Typed events.
3. Materialized world state.
4. Evidence/provenance.
5. Inspectors.
6. Timeline/replay.
7. Basic Command World.
8. Knowledge/capability schemas.

## Do later

1. Stigmergic field engine.
2. Adaptive team formation.
3. Mission compiler.
4. Evolution chamber.
5. Federated organizations.
