# Intent Contract Schema

## Purpose

An Intent Contract defines the mission's objective, desired end state, boundaries and escalation rules.

It lets agents act with bounded autonomy while preserving human intent.

## Draft TypeScript

```ts
export interface IntentContract {
  id: string;
  missionId: string;

  objective: string;
  desiredEndState: DesiredEndState[];

  invariants: Invariant[];
  authorityEnvelope: AuthorityEnvelope;
  verificationRequirements: VerificationRequirement[];

  riskTolerance: RiskTolerance;
  budget: BudgetEnvelope;
  escalationConditions: EscalationCondition[];

  createdBy: string;
  createdAt: string;
  version: number;
}

export interface DesiredEndState {
  id: string;
  description: string;
  measurable?: boolean;
  metric?: string;
  target?: string | number | boolean;
}

export interface Invariant {
  id: string;
  description: string;
  severity: "hard" | "soft";
  enforcement: "block" | "warn" | "escalate";
}

export interface AuthorityEnvelope {
  allowedActions: string[];
  forbiddenActions: string[];
  requiresApproval: string[];
  maxAutonomyLevel: "manual" | "suggest" | "guarded_auto" | "autonomous";
}

export interface VerificationRequirement {
  id: string;
  description: string;
  requiredEvidenceTypes: string[];
  passCriteria: string;
}

export interface RiskTolerance {
  productionRisk: "none" | "low" | "medium" | "high";
  dataRisk: "none" | "low" | "medium" | "high";
  costRisk: "low" | "medium" | "high";
}

export interface BudgetEnvelope {
  maxCostUsd?: number;
  maxTokens?: number;
  maxRuntimeSeconds?: number;
  maxAgents?: number;
}

export interface EscalationCondition {
  id: string;
  condition: string;
  reason: string;
  requiredHumanRole?: string;
}
```

## Action alignment score

Every major action can be scored:

```ts
export interface IntentAlignment {
  actionId: string;
  missionAlignment: number;
  policyAlignment: number;
  evidenceSufficiency: number;
  riskScore: number;
  explanation: string;
}
```
