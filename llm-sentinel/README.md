# LLM Sentinel

**Production-oriented LLM drift, reliability, and adaptive routing starter.**

LLM Sentinel is an AI engineering project for monitoring production LLM workloads. It combines statistical drift detection, reliability scoring, evaluation telemetry, and a policy-based fallback router.

> **Core idea:** don't just ask whether an LLM works — continuously measure whether its behavior is changing, quantify risk, and decide when traffic should be routed differently.

## Architecture

```text
                 ┌─────────────────┐
                 │   LLM / Agent   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Telemetry    │
                 │ tokens/latency  │
                 │ quality/errors  │
                 └────────┬────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
       ┌──────────────┐       ┌──────────────┐
       │ Distribution │       │ Performance  │
       │    Drift     │       │   Metrics    │
       └──────┬───────┘       └──────┬───────┘
              └───────────┬───────────┘
                          ▼
                 ┌─────────────────┐
                 │ Reliability     │
                 │ Risk Engine     │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │ Adaptive Router │
                 └───────┬─────────┘
                         ▼
                 Primary / Fallback
```

## Current MVP

- PSI (Population Stability Index)
- Two-sample KS drift statistic
- Reliability score
- Workload telemetry model
- Risk classification
- Policy-based adaptive routing
- Synthetic drift demo
- Unit tests
- No vendor lock-in: the monitoring layer can sit around any LLM provider

## Quick start

```bash
git clone <your-repository-url>
cd llm-sentinel

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

pip install -r requirements.txt

PYTHONPATH=src python examples/drift_demo.py
pytest
```

## Example output

```text
============================================================
LLM SENTINEL — DRIFT DEMO
============================================================
Baseline requests: 1000
Current requests:  1000

PSI score:          0.4302
KS statistic:       0.4380
Reliability score:  0.8161
Risk level:         CRITICAL

Recommended route: fallback
============================================================
```

## Metrics

### PSI

For bins `i`:

`PSI = Σ (current_i - baseline_i) * ln(current_i / baseline_i)`

The implementation uses small epsilon smoothing to avoid division by zero.

### KS

The two-sample Kolmogorov–Smirnov statistic is:

`D = sup_x |F_baseline(x) - F_current(x)|`

This MVP intentionally reports the statistic rather than treating a single p-value as the entire decision system.

### Reliability

The first version uses a transparent weighted score:

`R = 0.55 * quality + 0.20 * tool_success + 0.15 * (1 - error_rate) + 0.10 * latency_score`

This is a baseline engineering heuristic, not a claim of calibrated probability.

## Important limitation

LLMs do not normally have a literal amount of "intelligence" that gets consumed as they process requests. Sentinel therefore measures **observable workload reliability**, not remaining intelligence.

The next stages should learn a calibrated probability of acceptable output from historical telemetry and controlled evaluation data.

## Roadmap

- [ ] Embedding drift
- [ ] Streaming ADWIN/Page-Hinkley detectors
- [ ] LLM-as-judge evaluation with human calibration
- [ ] OpenTelemetry ingestion
- [ ] Prometheus metrics
- [ ] FastAPI service
- [ ] PostgreSQL event store
- [ ] Reliability forecasting
- [ ] Automatic model routing
- [ ] Canary deployments and rollback
- [ ] RAG retrieval drift
- [ ] Tool/API drift
- [ ] Dashboard
- [ ] Docker + CI/CD
- [ ] Failure-injection benchmark

## Engineering principles

1. **Measure before automating.**
2. **Separate detection from remediation.**
3. **Keep thresholds configurable.**
4. **Use human-calibrated evaluation for high-stakes quality claims.**
5. **Treat drift as evidence of change, not proof of failure.**

## License

MIT
