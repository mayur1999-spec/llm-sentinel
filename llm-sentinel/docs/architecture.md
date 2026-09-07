# Architecture

## v0.1

The system deliberately starts with a deterministic core:

1. **Telemetry** captures model/workload observations.
2. **Evaluation** converts observations into quality and reliability signals.
3. **Drift detection** compares a baseline distribution against the current window.
4. **Health** combines drift and performance into a risk level.
5. **Routing** makes a deterministic fallback decision.

## Why this design?

The goal is to make each layer independently testable. Production AI systems need observability and failure isolation before autonomous remediation.

## Future architecture

```text
LLM / Agent
   │
   ├── traces ───────────────► OpenTelemetry
   │                              │
   ├── evaluations ──────────────┤
   │                              ▼
   │                         Event Store
   │                              │
   │                ┌─────────────┴─────────────┐
   │                ▼                           ▼
   │          Drift Engine                Eval Engine
   │                │                           │
   │                └─────────────┬─────────────┘
   │                              ▼
   │                       Reliability Model
   │                              │
   │                              ▼
   │                       Policy / Router
   │                         │          │
   └─────────────────────────┘          └──► Human review
```
