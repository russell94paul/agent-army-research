# Feature Flag Plan

## Principle

Experimental organizational mechanisms must be removable without destabilizing the base Agent Factory.

Suggested flags:

| Flag | Purpose | Initial default | Promotion evidence |
|---|---|---:|---|
| `agent_army_shell` | New visual shell | off | UI task tests |
| `typed_org_events` | Typed event stream | shadow | event parity |
| `org_world_state` | Materialized organization state | shadow | projection parity |
| `artifact_evidence` | Evidence/provenance objects | off | correctness tests |
| `knowledge_objects` | Typed organizational knowledge | off | provenance tests |
| `intent_contracts` | Structured mission intent | off | mission experiments |
| `world_lenses` | Risk/knowledge/etc overlays | off | comprehension tests |
| `field_engine` | Sparse organizational fields | off | routing experiment |
| `adaptive_team_suggestions` | Recommend topology changes | off | offline benchmark |
| `adaptive_team_auto` | Apply topology changes | off | guarded-live evidence |
| `simulation` | Replay/counterfactual engine | off | determinism checks |
| `evolution_chamber` | Search organization variants | off | simulation validity |
| `federation` | Cross-org protocol | off | security review |

## Every flag requires

```text
owner
created date
default
scope
telemetry
rollout stage
kill criteria
removal date/condition
```

## Promotion stages

```text
code only
→ internal shadow
→ internal visible
→ suggestion mode
→ guarded execution
→ production default
```

Do not let flags become permanent undocumented architecture.
