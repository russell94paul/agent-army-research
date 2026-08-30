# ADR-0004 — No Random Agent Animation

## Status

ACCEPTED DESIGN PRINCIPLE

## Context

The Command World can easily become decorative: agents wandering, particles moving and buildings pulsing without corresponding system events. That destroys trust in the visualization.

## Decision

Every meaningful animation must correspond to a real semantic state transition.

Examples:

```text
movement        actual work/scope transition
pulse           new event
route flow      dependency/handoff/logistics flow
formation       team creation
collapse        team dissolution
scan            investigation/retrieval
lock            verification complete
break           verification failure
```

Ambient effects must never imply activity, success or urgency.

## Consequences

The UI may sometimes look quieter than a game. That is desirable if the organization is quiet.

## Accessibility

All motion-coded state must also be available through text/icon/status and reduced-motion mode.
