# Skill, Capability and Doctrine Model

## Skill

A versioned reusable procedure.

```ts
interface Skill {
  id: string;
  version: string;
  name: string;
  inputs: string[];
  outputs: string[];
  toolRequirements: string[];
  permissionRequirements: string[];
  tests: string[];
  performanceHistoryRef?: string;
  status: "candidate" | "verified" | "deprecated";
}
```

## Capability

Evidence-backed ability.

```ts
interface Capability {
  id: string;
  name: string;
  scope: string;
  evidenceRefs: string[];
  skillRefs: string[];
  historicalSuccessRate?: number;
  sampleSize?: number;
  contextualLimits: string[];
}
```

## Doctrine

Persistent organizational procedure or principle.

```ts
interface Doctrine {
  id: string;
  version: string;
  name: string;
  appliesToMissionClasses: string[];
  rules: string[];
  rationale: string;
  evidenceRefs: string[];
  testRefs: string[];
  status: "candidate" | "shadow" | "active" | "retired";
}
```

## Promotion hardness

```text
experience → easy to record
knowledge  → requires evidence
skill      → requires tests
doctrine   → requires replay/simulation + governance
```
