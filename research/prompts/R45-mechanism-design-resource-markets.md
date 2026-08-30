# R45 — Mechanism Design, Internal Markets and Resource Allocation

## Objective

Investigate whether ideas from economics, mechanism design and distributed resource allocation can improve how Agent Army assigns scarce organizational resources.

Resources may include:

```text
agents
specialist skills
expensive models
validator capacity
context budget
tokens
compute
sandboxes
API quota
human attention
research effort
```

Do not assume a literal monetary market is desirable.

## Core questions

Agent Army will repeatedly face allocation decisions:

```text
Which mission gets scarce validator capacity?
Which task deserves the expensive reasoning model?
When is spawning another agent worth its coordination cost?
Which competing hypothesis gets investigation budget?
Which team should receive a specialist skill?
Which low-value work should be abandoned?
```

Research mechanisms that might answer these better than static priority queues.

## Prior art

Study:

- Contract Net Protocol,
- auction-based multi-agent systems,
- matching markets,
- combinatorial auctions,
- operations research,
- constrained scheduling,
- queueing theory,
- admission control,
- budgeted optimization,
- priority systems,
- fair scheduling,
- multi-armed bandits where applicable,
- opportunity-cost models,
- distributed constraint optimization.

## Mechanisms to compare

At minimum compare:

```text
FIFO / static priority
central scheduler
capability-weighted scheduler
budget allocation
bidding/auction
contract-net style assignment
matching optimization
adaptive learned policy
```

## Mechanism requirements

A usable mechanism must be:

- explainable,
- budget bounded,
- resistant to strategic/gaming behavior,
- compatible with constitutional constraints,
- measurable,
- stable under rapidly changing workloads.

## Internal bids

If bids are explored, determine what an agent/team is actually allowed to bid with.

Possible signals:

- estimated success,
- expected cost,
- urgency,
- capability match,
- information value,
- opportunity cost.

Avoid letting self-reported confidence directly determine resource allocation.

## Organizational economics

Investigate whether we need concepts such as:

```text
marginal value of another agent
coordination tax
validator scarcity
information value
context carrying cost
specialist opportunity cost
```

Determine which are useful measurements versus metaphor.

## Experiments

Use mission corpora with deliberately scarce resources.

Compare allocation strategies on:

- verified success,
- deadline success,
- total cost,
- starvation,
- fairness where relevant,
- human intervention,
- allocation churn,
- robustness to bad estimates.

Include cases where a sophisticated market mechanism should lose to a simple scheduler.

## Required deliverables

1. resource ontology;
2. candidate allocation mechanisms;
3. suitability matrix by workload;
4. anti-gaming analysis;
5. simulation design;
6. scheduling API implications;
7. UI/operator controls;
8. performance overhead;
9. MVP recommendation;
10. mechanisms to reject.

Finish with:

> Is there a real "organizational economy" worth implementing, or should Agent Army use conventional resource scheduling with better capability and cost signals?
