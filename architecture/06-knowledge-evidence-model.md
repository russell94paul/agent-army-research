# Knowledge and Evidence Model

## Principle

Never merge observation, claim, evidence and knowledge into one generic memory record.

## Draft types

```ts
interface Observation {
  id: string;
  sourceRef: string;
  observerId: string;
  timestamp: string;
  content: string;
}

interface Claim {
  id: string;
  proposition: string;
  status: "hypothesis" | "supported" | "contested" | "refuted" | "verified";
  createdBy: string;
  createdAt: string;
}

interface Evidence {
  id: string;
  claimId: string;
  direction: "supports" | "contradicts";
  sourceRef: string;
  sourceRootId?: string;
  independentSourceGroup?: string;
  strength?: number;
  timestamp: string;
}

interface KnowledgeObject {
  id: string;
  canonicalStatement: string;
  claimRefs: string[];
  evidenceRefs: string[];
  status: "candidate" | "verified" | "stale" | "deprecated";
  validFrom?: string;
  validUntil?: string;
  scope: string[];
}
```

## Key requirement

`sourceRootId` or equivalent provenance is required to detect duplicated evidence chains.

## Promotion

```text
Observation
  ↓
Claim
  ↓
Evidence
  ↓
Knowledge Candidate
  ↓
Independent Verification
  ↓
Knowledge Object
```
