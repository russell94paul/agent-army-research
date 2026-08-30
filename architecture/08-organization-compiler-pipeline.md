# Organization Compiler Pipeline

## Input

```text
Mission Intent
Constraints
Required Capabilities
Available Agents
Skills
Knowledge
Resources
Policies
Doctrine
Historical Performance
```

## Passes

```text
1. Intent normalization
2. Constraint validation
3. Capability decomposition
4. Resource feasibility
5. Candidate topology generation
6. Agent/skill assignment
7. Context/logistics plan
8. Verification-plan generation
9. Policy/static checks
10. Org-IR emission
```

## Output

```text
Executable Organization Plan
```

## Diagnostics

Compiler should explain:

```text
why topology chosen
why agent chosen
missing capability
resource bottleneck
policy conflict
unverifiable end state
```

## Future

Candidate topologies may later come from search/evolution, but the compiler should initially be deterministic and explainable.
