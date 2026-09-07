"""Run a synthetic LLM workload drift demonstration."""

from __future__ import annotations

import numpy as np

from sentinel.drift.detector import detect_drift
from sentinel.evaluation.metrics import reliability_score
from sentinel.routing.router import route_request


def main() -> None:
    rng = np.random.default_rng(42)

    # Simulated quality scores from a healthy production workload.
    baseline_quality = np.clip(rng.normal(0.94, 0.025, 1000), 0, 1)

    # Simulated later workload after a distribution change.
    current_quality = np.clip(rng.normal(0.82, 0.06, 1000), 0, 1)

    drift = detect_drift(baseline_quality, current_quality)

    current_reliability = reliability_score(
        quality=float(current_quality.mean()),
        tool_success=0.86,
        error_rate=0.08,
        latency_ms=2400,
    )

    if current_reliability < 0.85:
        risk = "CRITICAL"
    elif current_reliability < 0.92 or drift.drift_detected:
        risk = "WARNING"
    else:
        risk = "LOW"

    decision = route_request(
        risk_level=risk,
        estimated_quality=float(current_quality.mean()),
    )

    print("=" * 60)
    print("LLM SENTINEL — DRIFT DEMO")
    print("=" * 60)
    print(f"Baseline requests: {len(baseline_quality)}")
    print(f"Current requests:  {len(current_quality)}")
    print()
    print(f"PSI score:          {drift.psi_score:.4f}")
    print(f"KS statistic:       {drift.ks_statistic:.4f}")
    print(f"Reliability score:  {current_reliability:.4f}")
    print(f"Risk level:         {risk}")
    print()
    print(f"Recommended route: {decision.route}")
    print(f"Reason:            {decision.reason}")
    print("=" * 60)


if __name__ == "__main__":
    main()
