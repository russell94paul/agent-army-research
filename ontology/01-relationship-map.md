# Core Relationship Map

```text
Organization
  ├─ has → Mission
  ├─ owns → Policy
  ├─ owns → Doctrine
  ├─ owns → KnowledgeObject
  ├─ owns → Skill
  ├─ claims → Capability
  └─ versions → OrganizationVersion

Mission
  ├─ governed by → IntentContract
  ├─ executed as → Operation
  ├─ requires → Capability
  ├─ produces → Evidence
  └─ changes → Artifact

Operation
  ├─ contains → Team
  ├─ contains → Agent
  ├─ emits → Event
  └─ maintains → RunningEstimate

Agent
  ├─ fills → Role
  ├─ uses → Skill
  ├─ uses → Tool
  ├─ acts on → Artifact
  ├─ creates → Claim
  ├─ produces → Evidence
  └─ senses → Field

Claim
  ├─ supported by → Evidence
  ├─ contradicted by → Evidence
  ├─ derived from → Claim
  └─ used by → Decision

Doctrine
  ├─ derived from → Lesson
  ├─ tested by → Simulation
  └─ constrains/informs → OrganizationCompiler
```
