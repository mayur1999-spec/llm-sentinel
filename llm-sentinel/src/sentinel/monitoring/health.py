"""Health and risk scoring."""

from __future__ import annotations

from dataclasses import dataclass
from ..evaluation.metrics import reliability_score


@dataclass(frozen=True)
class HealthReport:
    reliability: float
    risk_level: str


def classify_risk(reliability: float, drift_detected: bool) -> str:
    if reliability < 0.85 or (drift_detected and reliability < 0.92):
        return "CRITICAL"
    if reliability < 0.92 or drift_detected:
        return "WARNING"
    return "LOW"


def build_health_report(
    quality: float,
    tool_success: float,
    error_rate: float,
    latency_ms: float,
    drift_detected: bool,
) -> HealthReport:
    score = reliability_score(
        quality=quality,
        tool_success=tool_success,
        error_rate=error_rate,
        latency_ms=latency_ms,
    )
    return HealthReport(
        reliability=score,
        risk_level=classify_risk(score, drift_detected),
    )
